from rest_framework import serializers
from .models import Passport, Qualification, Document


class PassportSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Passport


class QualificationSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Qualification


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Document
