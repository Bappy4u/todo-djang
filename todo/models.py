from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class TodoList(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.CharField(max_length=300)
    due_date = models.DateField()
    is_completed = models.BooleanField(default=0)


class Profile(models.Model):
    # required to associate Author model with User model (Important)
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(
        upload_to='static/profilepicture', null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
