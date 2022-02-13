from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

GRADE_CHOICES = (
    ("1","1학년"),
    ("2","2학년"),
    ("3","3학년"),
    ("4","4학년"),
)

class UserManager(BaseUserManager):
    def create_user(self, email, password, username=""):
        if not email:
            raise ValueError(("Users must have an email address"))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, email, password, username):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )

        user.is_superuser = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    objects = UserManager()

    email = models.EmailField(
        verbose_name=("email"),
        max_length=200,
        unique=True,
    )  
    username = models.CharField(
        verbose_name=("username"),
        max_length=50,
        unique=True,
    ) 
    is_active = models.BooleanField(
        verbose_name=("Is active"),
        default=True,
    )
    name = models.CharField(
        max_length=20,
        verbose_name="이름",
    )
    student_num = models.CharField(
        verbose_name="학번",
        max_length=30,
        null=True,
    )
    grade = models.CharField(
        max_length=10,
        choices = GRADE_CHOICES,
        default="1",
        verbose_name="학년",
    )
    phone_num = models.CharField(
        max_length=20,
        verbose_name="휴대폰 번호",
    )
    first_major = models.CharField(
        max_length=30,
        verbose_name="본전공",
    )
    second_major = models.CharField(
        max_length=30,
        verbose_name="이중전공",
    )
    is_accepted = models.BooleanField(
        default = False,
        verbose_name="합격 여부",
    )
    
    @property
    def is_staff(self):
        return self.is_superuser
