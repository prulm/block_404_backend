from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class UserAccountManager(BaseUserManager):
    def create_user(self, firstName, lastName, phone, email, password=None):
        if not phone:
            raise ValueError('Users must have a phone number')
        
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
    
        user = self.model(firstName=firstName, lastName=lastName, email=email, phone=phone)

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, firstName, lastName, phone, email, password=None):
        user = self.create_user(firstName, lastName, phone, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

class UserAccount (AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    profilePicture = models.ImageField(upload_to="profile_pics", default="profile_pics/default_profile.png")

    objects = UserAccountManager()
    
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'email']

    def get_full_name(self):
        return self.firstName + self.lastName

    def get_short_name(self):
        return self.firstName

    def __str__(self):
        return self.phone