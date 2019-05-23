from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView
from django.contrib.auth import login

from main.models import Tweet
from main.forms import TweetForm

class TweetFormView(FormView):
    template_name = 'main/tweetform.html'
    form_class = TweetForm
    success_url = reverse_lazy('main:index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TweetDeleteView(DeleteView):
    template_name = 'main/tweet_comfirm_delete.html'
    model = Tweet
    form_class = TweetForm
    success_url = reverse_lazy('main:index')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'ツイートを削除しました'.format(self.object))
        return result
    