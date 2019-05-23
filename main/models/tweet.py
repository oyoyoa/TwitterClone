import uuid

from django.db import models
from django.utils import timezone
from main.models import User
from main.decorators import delete_previous_file

class Tweet(models.Model):
    tweet_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=140, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')

    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_content(self):
        print('self: ', self.content.all())
        # print('tweet: ', Tweet.objects.all())
        return self.content.all()
