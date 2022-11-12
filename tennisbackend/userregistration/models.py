from django.db import models


# Create your models here.
class UserInfo(models.Model):
    class UserSkill(models.IntegerChoices):
        NOVICE = 1
        PRO = 2

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_skill = models.IntegerField(choices=UserSkill.choices)

    def __str__(self):
        return f"{self.first_name} {self.last_name} with skill {self.user_skill}"
