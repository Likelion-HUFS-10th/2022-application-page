from django.db import models
from account.models import User

CATEGORY_CHOICES = (
    ("P/D","기획/디자인"),
    ("FE","프론트엔드"),
    ("BE","벡엔드")
)

class Apply(models.Model):
    """"Model definition for Apply"""
    
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name="apply",
        verbose_name="지원자",
        null=False,
    )
    category = models.CharField(
        max_length=10,
        choices = CATEGORY_CHOICES,
        null=False,
        default="P/D",
    )
    study_url = models.CharField(
        max_length=2100,
        null=True,
        verbose_name="깃헙/블로그 링크",
    )
    first_q = models.TextField(
        null=False,
        verbose_name="질문 1",
    )
    second_first_q = models.TextField(
        null=False,
        verbose_name="질문 2-1",
    )
    second_second_q = models.TextField(
        null=False,
        verbose_name="질문 2-2",
    )
    third_q = models.TextField(
        null=False,
        verbose_name="질문 3",
    )
    fourth_q = models.TextField(
        null=False,
        verbose_name="질문 4"
    )
    is_completed = models.BooleanField(
        null=False,
        default=False,
    )

