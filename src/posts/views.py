from django.contrib import messages
from django.contrib.auth import(authenticate, login, logout)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, RedirectView

from .forms import StatusForm, StatusCommentForm
from .models import Status, StatusComment
from plans.models import UserPlan, Plan


def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                userplan = UserPlan.objects.get(user=user)
                form_plan = Plan.objects.get(plan='Plan1')
                userplan.plan = form_plan
                userplan.save()
                messages.success(request, 'Your account successfully created')
                return redirect(('plans:plans'))
        else:
            form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    else:
        return redirect(reverse('posts:list'))


class CreateStatusView(LoginRequiredMixin, CreateView):
    """Basic CreateView implementation to create new status."""
    model = Status
    fields = ['content']
    message = ("Your status has been Created.")
    template_name = 'posts/status_create.html'

    def form_valid(self, form):
        status = form.save(commit=False)
        status.user = self.request.user
        status.save()
        messages.success(self.request, self.message)
        return redirect(status.get_absolute_url())


class StatusListView(LoginRequiredMixin, ListView):
    """Basic ListView implementation to call the published articles list."""
    model = Status
    paginate_by = 5
    context_object_name = "status"

    def get_context_data(self, **kwargs):
        context = super(StatusListView, self).get_context_data(**kwargs)
        user = self.request.user
        user_plan = user.userplan.plan
        if user.statuscomment_set.count() < user_plan.status:
            context['form'] = StatusForm()
        else:
            message = ("Your status creation limit for this plan has been finished.")
            messages.warning(self.request, message)
        if user.statuscomment_set.count() < user_plan.comments:
            context['comment_form'] = StatusCommentForm()
        else:
            message = ("Your comment creation limit for this plan has been finished.")
            messages.warning(self.request, message)
        return context

    def get_queryset(self):
        return Status.objects.order_by('-timestamp')


class StatusLikeView(LoginRequiredMixin, RedirectView):
    model = Status

    def get_redirect_url(self, *args, **kwargs):
        status = get_object_or_404(Status, pk=self.request.POST.get('status_id'))
        is_liked = True
        user = self.request.user
        user_plan = user.userplan.plan
        if status.like.filter(id=self.request.user.id).exists():
            status.like.remove(self.request.user)
            message = ("You unliked this status successfully.")
            messages.success(self.request, message)
            return status.get_absolute_url()
        elif user.status_like.count() >= user_plan.likes:
            message = ("Your like limit for this plan has finished.")
            messages.warning(self.request, message)
            return status.get_absolute_url()
        else:
            message = ("You liked this status successfully.")
            messages.success(self.request, message)
            status.like.add(self.request.user)
            return status.get_absolute_url()


@login_required
def comment(request):
    if request.method == 'POST':
        form = StatusCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.status_id = request.POST.get('status_id')
            comment.user = request.user
            comment.save()
            message = ("You commented on this status successfully.")
            messages.success(request, message)
            return redirect(comment.status.get_absolute_url())
        else:
            status = get_object_or_404(Status, pk=request.POST.get('status_id'))
            message = ("There is an error while postin this comment.")
            messages.warning(request, message)
            return redirect(status.get_absolute_url())
