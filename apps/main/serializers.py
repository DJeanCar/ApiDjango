from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notice, Comment, Category, Author

class UserSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = User
		fields = ('username',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Category
		fields = ('name',)

class AuthorSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Author
		fields = ('name',)

		
class NoticeSerializer(serializers.ModelSerializer):

	class Meta:
		model = Notice
		fields = ('id', 'title', 'resumen', 'main', 'image')

class NoticeDetailSerializer(serializers.ModelSerializer):

	category = CategorySerializer()
	author = AuthorSerializer()

	class Meta:
		model = Notice

class CommentSerializer(serializers.ModelSerializer):

	user = UserSerializer()

	class Meta:
		model = Comment