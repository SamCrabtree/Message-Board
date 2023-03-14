from django.test import TestCase
from .models import Post
# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.Objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.Post.text, "This is a test!")