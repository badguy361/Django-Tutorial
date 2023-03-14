from django.test import TestCase
from django.test import client
from zoo import models

class AnimalTestCase(TestCase):
    def test_dog_says(self):
        dog = models.Dog(name="Snoopy")
        self.assertEqual(dog.says(), 'woof')

    def test_cat_says(self):
        cat = models.Cat(name="Garfield")
        self.assertEqual(cat.says(), 'meow')

class IndexWebpageTestCase(TestCase):

    def setUp(self):
        self.c = client.Client()

    def test_add_visiting(self):
        resp = self.c.get('/1/plus/2/')
        self.assertEqual(resp.status_code, 200)
        # self.assertContains(resp, '<p>歡迎來到餐廳王</p>')
        self.assertTemplateUsed(resp, 'main.html')