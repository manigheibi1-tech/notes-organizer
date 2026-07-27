from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Course, Note


class CourseTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='password123')
        self.client.login(username='alice', password='password123')

    def test_create_course(self):
        self.client.post(reverse('course_create'), {
            'title': 'algorithms',
            'description': '',
        })
        self.assertTrue(Course.objects.filter(title='algorithms', owner=self.user).exists())

    def test_anonymous_user_redirected_to_login(self):
        self.client.logout()
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, 302)


class NoteTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='password123')
        self.client.login(username='bob', password='password123')
        self.course = Course.objects.create(owner=self.user, title='math')

    def test_create_note_under_course(self):
        self.client.post(reverse('note_create', args=[self.course.pk]), {
            'title': "introduction",
            'description': '',
            'content': 'two plus two equals five!',
        })
        note = Note.objects.get(title="introduction")
        self.assertEqual(note.course, self.course)

    def test_search_returns_only_matching_notes(self):
        Note.objects.create(course=self.course, title='lesson1', content='four times three equals twelve')
        Note.objects.create(course=self.course, title='lesson2', content='ten minus two equals eight')

        response = self.client.get(reverse('note_list', args=[self.course.pk]), {'q': 'times'})

        self.assertContains(response, 'lesson1')
        self.assertNotContains(response, 'lesson2')


class OwnershipTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user(username='owner', password='password123')
        self.intruder = User.objects.create_user(username='intruder', password='password123')
        self.course = Course.objects.create(owner=self.owner, title='private Course')

    def test_user_cannot_view_another_users_course(self):
        self.client.login(username='intruder', password='password123')
        response = self.client.get(reverse('note_list', args=[self.course.pk]))
        self.assertEqual(response.status_code, 404)