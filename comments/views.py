from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

# custom permission "IsOnlySuperUserAndOwnerAccessComments" only the owner and superusers can do any request on
# cohort's comments
from commons.permissions import IsOnlySuperUserAndOwnerAccessComments

from comments.models import Comment
from comments.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOnlySuperUserAndOwnerAccessComments]
