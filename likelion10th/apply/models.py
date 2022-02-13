from django.db import models
from account.models import User


#이는 아래 category 필드에서 사용되는 초이스 입니다. 우리가 흔히 웹사이트에서 무언가를 선택할 때 사용되는 select 안에 들어간다고 생각하시면 됩니다.
CATEGORY_CHOICES = (
    ("P/D","기획/디자인"),
    ("FE","프론트엔드"),
    ("BE","벡엔드")
)

#공통적으로 등장하는 verbose_name 은 db에서 보다 간편하게 필드가 무엇을 의미하는지 알 수 있도록 해주는 역할이라고 생각하시면 될 것 같습니다.
class Apply(models.Model):
    """"Model definition for Apply"""
    
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        #related_name은 유저 모델에서 apply라는 모델이 어떻게 표시될지(?) 어떤 이름으로 나타날지 설정해줍니다.\
        related_name="apply",
        verbose_name="지원자",
        null=False,
    )
    category = models.CharField(
        max_length=10,
        choices = CATEGORY_CHOICES,
        null=False,
        #choice의 기본값을 설정해줍니다.
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
    second_q = models.TextField(
        null=False,
        verbose_name="질문 2",
    )
    third_q = models.TextField(
        null=False,
        verbose_name="질문 3",
    )
    fourth_q = models.TextField(
        null=False,
        verbose_name="질문 4"
    )
    is_submitted= models.BooleanField(
        null=False,
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


