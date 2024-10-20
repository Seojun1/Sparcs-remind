from django.db import models

class SignUp(models.Model):
    GENDER_CHOICES = [
        ('M', '남성'),
        ('F', '여성'),
    ]

    user_id = models.CharField(max_length=15, verbose_name='사용자 아이디')
    user_password = models.CharField(max_length=20, verbose_name='사용자 비밀번호')
    username = models.CharField(max_length=20, verbose_name='사용자 이름')
    age = models.IntegerField(verbose_name='사용자 나이')
    email = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='성별')

    def __str__(self):
        return self.username
