from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='user')

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    email = models.EmailField(unique=True)
    
    def __str__(self) -> str:
        return f"Profile[{self.first_name}]"

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name' )
