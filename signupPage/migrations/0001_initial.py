# Generated by Django 4.2.6 on 2024-10-19 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SignUp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.CharField(max_length=15, verbose_name="사용자 아이디")),
                (
                    "user_password",
                    models.CharField(max_length=20, verbose_name="사용자 비밀번호"),
                ),
                ("username", models.CharField(max_length=20, verbose_name="사용자 이름")),
                ("age", models.IntegerField(verbose_name="사용자 나이")),
                ("email", models.EmailField(max_length=128, verbose_name="사용자 이메일")),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "남성"), ("F", "여성")],
                        max_length=1,
                        verbose_name="성별",
                    ),
                ),
            ],
        ),
    ]
