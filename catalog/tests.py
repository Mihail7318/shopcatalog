from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase

from catalog.models import Attribute, Category, Value


class TestAttributeListAPIView(APITestCase):
    def test_missing_attr(self):
        self.attr = Attribute.objects.create(
            name='Мощность',
        )
        self.attr.category.create(id=1, name='blender', position=4)
        self.attr.values.create(value="1400")
        self.exp_attribute = [
            {
                "name": "Мощность",
                "values": [
                    {
                        "value": "1400"
                    }
                ]
            }
        ]
        resp = self.client.get('/catalog/category/1')
        self.assertEqual(self.exp_attribute, resp.json())
