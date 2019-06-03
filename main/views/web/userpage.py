from django.views.generic import TemplateView
from main.models import User, Tweet


class UserView(TemplateView):
    template_name = "main/userpage.html"

    def get_context_data(self, **kwargs):
        user_id = User.id
        context = super().get_context_data(**kwargs)
        context['latest_tweet_list'] = Tweet.objects.filter(user_id=self.kwargs.get('id')).order_by('-created_at')[:23]
        print('id: ', id)
        print('self: ', self.kwargs.get('id'))
        # print('user: ', Tweet.tweet_id)
        # context['og_type'] = 'website'
        return context
