from rest_framework import serializers
from tweets.models import Tweet



class TweetSelializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']