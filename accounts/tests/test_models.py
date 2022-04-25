from rest_framework.test import APITestCase
from accounts.models import Account


class TestModel(APITestCase):

    def test_create_user(self):
        user = Account.objects.create_user('anarul', 'anarul@exampl.com', '01831183333')
        self.assertIsInstance(user, Account)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'anarul@exampl.com')
        self.assertEqual(str(user), 'anarul')
    
    def test_has_perm(self):
        user = Account.has_perm(self, True)
        self.assertTrue(user, Account)

    def test_has_module_perms(self):
        user = Account.has_module_perms(self, True)
        self.assertTrue(user, Account)
    
    def test_raises_error_with_message_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Users must have an username.'):
            Account.objects.create_user(username='', email='anarul@exampl.com', phone_number='01831183333')


    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Users must have an email.'):
            Account.objects.create_user(username='anarul', email='', phone_number='01831183333')

    def test_raises_error_with_message_when_no_phone_number_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Users must have an phone numbe.'):
            Account.objects.create_user(username='anarul', email='anarul@exampl.com', phone_number='')

            

    def test_creates_super_user(self):
        user = Account.objects.create_superuser('anarul', 'anarul@exampl.com', '01831183333')
        self.assertIsInstance(user, Account)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'anarul@exampl.com')