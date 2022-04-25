# from django.test import TestCase
# from posts.models import Post

# class TestPostModel(TestCase):
#     def test_post_create(self):
#         post = Post.objects.create()


# from faker import Faker
import faker

fake = faker.Faker()

for n in range(1, 7):
    print(fake.phone_number().slice("-"))
    print('--------------------')
