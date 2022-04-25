from django.test import TestCase
from category.models import Category

class TestCategoryModel(TestCase):

    def test_category_create(self):
        category = Category.objects.create(name='django', slug='django')
        perent = category.parent
        self.assertIsInstance(category, Category)
        self.assertEqual(str(category), 'django')
        
