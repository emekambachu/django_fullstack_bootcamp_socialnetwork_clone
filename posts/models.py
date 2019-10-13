from django.db import models

#import revers
from django.urls import reverse

#import settings
from django.conf import settings

#import misaka for pretty url
import misaka

#import groups model from groups app
from groups.models import Group

#import current user model
from django.contrib.auth import get_user_model

#posts.py
# Create your models here.

# connect current post to whichever user is logged in
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=False)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single', kwargs={'username': self.user.username, 'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'message']