from core.models import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField
from .models import User

class RegisterSerializer(serializers.Serializer):
    full_name = serializers.CharField(label="Full Name", max_length=100)
    email = serializers.EmailField(label="Email Address")
    phone_number = serializers.CharField(label="Phone Number", max_length=15)
    password1 = serializers.CharField(label="Password", style={'input_type': 'password'}, max_length=128)
    password2 = serializers.CharField(label="Confirm Password", style={'input_type': 'password'}, max_length=128)
    role = serializers.CharField(label="Role")
    department = serializers.CharField(label="Department")
    office_location = serializers.CharField(label="Office Location")
    security_question = serializers.CharField(label="Security Question")
    two_fa = serializers.BooleanField(label="Enable Two-Factor Authentication", required=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = User(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            role=validated_data['role'],
            department=validated_data['department'],
            office_location=validated_data['office_location'],  
            security_question=validated_data['security_question'],  
            two_fa=validated_data['two_fa'],  
        )
        user.set_password(validated_data['password1'])
        user.save()
        

        return user
    
