from django import forms

from .models import Status, StatusComment


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ["content"]


class StatusCommentForm(forms.ModelForm):

    class Meta:
        model = StatusComment
        fields = ["comment", ]
