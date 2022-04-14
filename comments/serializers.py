from django.contrib.auth.models import User
from rest_framework import serializers

from comments.models import Comment
from patients.models import Patient
from patients.serializers import PatientSerializer


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Comment
        fields = (
            'id', 'comment', 'owner', 'patient', 'created_at', 'updated_at',
        )
