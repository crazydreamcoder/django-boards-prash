'''
Created on Aug 8, 2018

@author: Satavan
'''

from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import resolve

from boards.forms import NewTopicForm

from ..models import Board, Topic, Post
from ..views import new_topic, TopicListView

class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)
        
        
    def test_board_topics_view_contains_link_back_to_homepage(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        homepage_url = reverse('home')
#         print("----------------------------------------||||")
#         print(homepage_url)
#         print(response)
#         print("----------------------------------------||||")
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        
    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('home')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)
#         print("----------------------------------------||||")
#         print('href="{0}"'.format(new_topic_url))
#         print("----------------------------------------||||")
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))