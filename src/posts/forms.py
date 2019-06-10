from django import forms

from .models import Status, StatusComment


class StatusForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'What\'s your status'}), label='Status')

    class Meta:
        model = Status
        fields = ["content"]


class StatusCommentForm(forms.ModelForm):

    class Meta:
        model = StatusComment
        fields = ["comment", ]
