from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField
from users.models import User
from .models import Transaction

class CoreModelSerializer(serializers.ModelSerializer):
    created_by = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )
    updated_by = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = models.CoreModel  # The concrete model that extends CoreModel
        fields = ['created_at', 'updated_at', 'is_active', 'created_by', 'updated_by']
        read_only_fields = ['created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Automatically set the updated_by field if present in the data
        user = self.context['request'].user if 'request' in self.context else None
        if user and user.is_authenticated:
            validated_data['updated_by'] = user
        return super().update(instance, validated_data)
    
    def create(self, validated_data):
        # Automatically set the created_by field if present in the data
        user = self.context['request'].user if 'request' in self.context else None
        if user and user.is_authenticated:
            validated_data['created_by'] = user
        return super().create(validated_data)
    
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction  # Specify the model to serialize
        fields = '__all__' 