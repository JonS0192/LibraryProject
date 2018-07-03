import datetime

from django.utils import timezone
from django.test import TestCase
from .models import *


class QuestionMethodTests(TestCase):

    def test_models_books(self):
        b = Books(isbn='1111111', title='The Grapes of Wrath', author='John Steinbeck')

    def test_models_library_card(self):
        card = LibraryCards(id='1111111', name='Iris Omlout', phone_number='123-123-1234', email='123@gmail.com')