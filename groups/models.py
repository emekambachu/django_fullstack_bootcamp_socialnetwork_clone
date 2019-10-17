from django.db import models

# for reverse and redirection
from django.urls import reverse

# for url slugs and pretty urls
from django.utils.text import slugify


# must install visual studio c++ 14 for it to work
import misaka

# get user model that is currently active in project
from django.contrib.auth import get_user_model


from django import template

User = get_user_model()

register = template.Library()

# Groups app
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    # redirect after creating group
    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = {'name'}


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')