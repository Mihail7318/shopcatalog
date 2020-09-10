from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase

from catalog.models import Category, Attribute, Value

class TestAttributeListAPIView(APITestCase):
    def test_missing_attr(self):
        self.attr = Attribute.objects.create(
            name='Мощность',
            position=1
        )

        self.attr.category.create(id=1, name='blender', position=4)
        self.attr.value.create(value='1400', position=1)


        self.exp_attribute = [
            {
                "name": "Мощность",
                "value": [
                    {
                        "value": "1400",
                        "position": 1
                    }
                ]
            }
        ]
        resp = self.client.get('/catalog/category/1/attrs/')
        self.assertEqual(self.exp_attribute, resp.json())

