from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class UserAccountManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

class UserAccount (AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    profilePicture = models.ImageField(upload_to="profile_pics/")

    objects = UserAccountManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def get_full_name(self):
        return self.firstName + self.lastName

    def get_short_name(self):
        return self.firstName

    def __str__(self):
        return self.phone