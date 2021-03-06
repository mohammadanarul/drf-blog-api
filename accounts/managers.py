from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AccountManager(BaseUserManager):
    #This is a manager for Account Class
    def create_user(
        self,
        username,
        email,
        phone_number,
        password=None):

        if not username:
            raise ValueError("Users must have an username.")

        if not email:
            raise ValueError("Users must have an email.")

        if not phone_number:
            raise ValueError("Users must have an phone numbe.")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password=None):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user