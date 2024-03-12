from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, email , username, password, first_name, last_name , **extra_fields):
        if not email:
            raise ValueError("Email must be Provided")

        if not password:
            raise ValueError("Password must be Provided")

        if not username:
            raise ValueError("Username must be Provided")

        user= self.model(
            email  = self.normalize_email(email), 
            first_name = first_name,
            last_name = last_name,
            username = username,
            **extra_fields

        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_user(self, email , username, password, first_name, last_name , **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_student", True)
        extra_fields.setdefault("is_banned", False)
        extra_fields.setdefault("is_Superuser", False)

        return self._create_user(self, email , username, password, first_name, last_name , **extra_fields)
    def create_superuser(self, email , username, password, first_name, last_name , **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_student", True)
        extra_fields.setdefault("is_banned", False)
        extra_fields.setdefault("is_Superuser", True)

        return self._create_user(self, email , username, password, first_name, last_name , **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True, max_length=254)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    is_banned = models.BooleanField(default = False)
    is_student = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = True)
    is_student = models.BooleanField(default = True)
    username = models.CharField(max_length=100, unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    

    