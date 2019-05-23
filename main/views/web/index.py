from django.views.generic import TemplateView
from main.models import User, Tweet


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_tweet_list'] = Tweet.objects.all().order_by('-created_at')[:23]
        print('self: ', Tweet.pk)
        # print('tweet: ', Tweet.objects.filter(id=))
        return context