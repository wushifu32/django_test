import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice

class QeustionModelTests(TestCase):
    def test_was_published_recently_this_day(self):
        time = timezone.now() - datetime.timedelta(hours=12)
        future_q = Question(publish_date=time)
        self.assertIs(future_q.was_published_recently(), True)
    def test_was_published_recently_with_2days(self):
        time = timezone.now() - datetime.timedelta(days=2)
        future_q = Question(publish_date=time)
        self.assertIs(future_q.was_published_recently(), False)
    def test_was_published_recently_with_future_date(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_q = Question(publish_date=time)
        self.assertIs(future_q.was_published_recently(), False)

def create_question(name, days):
    date = timezone.now() + datetime.timedelta(days)
    return Question.objects.create(q_text=name, publish_date=date)

class IndexViewTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        create_question('Past question', -2)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ['<Question: Past question>'])

    def test_future_question(self):
        create_question('Future question', 2)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_and_past_question(self):
        create_question('Future question', 2)
        create_question('Past question', -2)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ['<Question: Past question>'])

    def test_two_past_question(self):
        create_question('Past question 1', -2)
        create_question('Past question 2', -20)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'],
                                 ['<Question: Past question 1>',
                                  '<Question: Past question 2>'])
