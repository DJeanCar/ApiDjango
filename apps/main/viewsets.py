from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Notice, Comment
from .serializers import NoticeSerializer, CommentSerializer, NoticeDetailSerializer


class NoticeViewSet(viewsets.ModelViewSet):

	queryset = Notice.objects.all()
	serializer_class = NoticeSerializer

	def list(self, request):
		notices = Notice.objects.all()
		notSer = NoticeSerializer(notices, many=True, context={'request': request})
		return Response(notSer.data)

		
	def retrieve(self, request, pk):
		notice = get_object_or_404(Notice, pk=pk)
		notSer = NoticeDetailSerializer(notice, context={'request': request})
		return Response(notSer.data)

class CommentViewSet(viewsets.ModelViewSet):

	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def create(self, request, noticia_pk):
		notice = Notice.objects.get(pk = noticia_pk)
		Comment.objects.create(user = request.user, comment = request.POST['comment'], notice=notice)
		return Response(status=200)