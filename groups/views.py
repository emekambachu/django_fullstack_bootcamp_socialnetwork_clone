from django.shortcuts import render
from django.contrib import messages

# authentication mixins
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.urls import reverse
from django.views import generic
from django.shortcuts import get_object_or_404

from groups import models
from . models import Group, GroupMember


# Create your views here.
class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group


class SingleGroup(generic.DetailView):
    model = Group


class ListGroups(generic.ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    # redirect to group detail page after joining group
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:detail', kwargs={'slug': self.kwargs.get('slug')})

    # give an error if they are already in the group
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            # get object from group member where user is equal to logged in or current user and group is equal to group
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning! Already a member')
        else:
            messages.success(self.request, 'You are now a member')

        return super().get(request, *args, **kwargs)


class LeaveGroup(LoginRequiredMixin, generic.RedirectView):

    # redirect to group detail page after joining group
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:detail', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = models.GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry!! You are not in this group')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group')
        return super().get(request, *args, **kwargs)
