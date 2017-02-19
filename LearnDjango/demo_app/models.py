from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    def user_property(self):
        return self.user + ':' + self.pwd
    user_property.short_description = 'user and password'

    information = property(user_property)

    def __str__(self):
        return self.user