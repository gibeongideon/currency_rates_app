from django.test import TestCase  #, Client
from django.urls import reverse
from .models import User
from django.http import HttpRequest
from django.template.loader import render_to_string
from .template_views import register

class UserTestCase(TestCase):
    def setUp(self):
        self.usera = User.objects.create(
            username="test_usera", email="testa@gmail.com",)
        self.userb = User.objects.create(
            username="test_userb", email="testb@gmail.com",)
        self.userc = User.objects.create(
            username="test_userc", email="testc@gmail.com",)
        self.userd = User.objects.create(
            username="test_userd", email="testd@gmail.com",)
    def test_user_creation(self):
        user = User.objects.get(username="test_usera")
        self.assertEqual(user.username, 'test_usera')

    def test_user_count(self):
        self.assertEqual(User.objects.count(), 4)

    def test_correct_saved_pone_number(self):

        self.assertEqual(self.usera.username, "test_usera")
        self.assertEqual(self.userb.username, "test_userb")
        self.assertEqual(self.userc.username, "test_userc")
        self.assertEqual(self.userd.username, "test_userd")# pone verification later
       

# class UserCorrecTemplate(TestCase):
#     def test_omepage_returns_correct_html(self):
#         response = self.client.get('/')
#         print('RES',response)
#         self.assertTemplateUsed(response, 'exchanges.html')
           
