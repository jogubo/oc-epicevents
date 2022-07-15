from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_staff = False
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        user = self.create_user(email, password=password, **other_fields)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    first_name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    email = models.CharField(max_length=128, blank=False, unique=True)
    password = models.CharField(max_length=128, blank=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def is_sales_contact(self, obj):
        return True if self == obj.sales_contact else False

    def is_support_contact(self, obj):
        return True if self == obj.support_contact else False

    def has_perm(self, perm, obj=None):
        if self.is_admin:
            return True
        elif perm in self.get_all_permissions(obj=obj):
            return True
        else:
            return False

    def has_module_perms(self, app_label):
        return True
