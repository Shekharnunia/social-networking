from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, RedirectView

from .forms import StatusForm, StatusCommentForm
from .models import Status, StatusComment


class CreateStatusView(CreateView):
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


class StatusListView(ListView):
    """Basic ListView implementation to call the published articles list."""
    model = Status
    paginate_by = 5
    context_object_name = "status"

    def get_context_data(self, **kwargs):
        context = super(StatusListView, self).get_context_data(**kwargs)
        context['form'] = StatusForm()
        context['comment_form'] = StatusCommentForm()
        return context

    def get_queryset(self):
        return Status.objects.order_by('-timestamp')


class StatusLikeView(RedirectView):
    model = Status

    def get_redirect_url(self, *args, **kwargs):
        status = get_object_or_404(Status, pk=self.request.POST.get('status_id'))
        is_liked = True
        if status.like.filter(id=self.request.user.id).exists():
            print('in')
            status.like.remove(self.request.user)
            message = ("You unliked this status successfully.")
            messages.success(self.request, message)
            return status.get_absolute_url()
        else:
            message = ("You liked this status successfully.")
            messages.success(self.request, message)
            status.like.add(self.request.user)
            return status.get_absolute_url()


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
