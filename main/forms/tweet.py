from django.forms import Form, ModelForm
from django.forms.fields import CharField
from django.forms.widgets import Textarea
from django.contrib.auth import authenticate

from main.models import User, Tweet
from .base import BootstrapFormMixin


class TweetForm(BootstrapFormMixin, ModelForm):
    content = CharField(
        max_length = 140,
        widget=Textarea(attrs={'placeholder': 'いまどうしてる？'})
    )
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def __init__(self, user, instance=None, *args, **kwargs):
        super().__init__(instance=instance, *args, **kwargs)
        self.user = user
        self.fields["image"].required = False

    def save(self, commit=True):
        self.instance.user = self.user
        tweet = super().save(commit)

        return tweet
