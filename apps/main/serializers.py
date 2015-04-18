from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notice, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('username',)

class NoticeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Notice

class CommentSerializer(serializers.ModelSerializer):

	user = UserSerializer()

	class Meta:
		model = Comment