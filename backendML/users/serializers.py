from ..core import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField

class RegisteSerialize(serializers.ModelSerializer):
    full_name = serializers.CharField(label="Full Name", max_length=100)
    email = serializers.EmailField(label="Email Address")
    phone_number = serializers.CharField(label="Phone Number", max_length=15)
    password1 = serializers.CharField(label="Password", widget=serializers.PasswordInput())
    password2 = serializers.CharField(label="Confirm Password", widget=serializers.PasswordInput())
    role = serializers.CharField(label="Role")
    department = serializers.CharField(label="Department")
    office_location = serializers.CharField(label="Office Location")
    security_question = serializers.CharField(label="Security Question")
    two_fa = serializers.BooleanField(label="Enable Two-Factor Authentication", required=True)

    class Meta:
        model = models.User
        fields = ['email', 'full_name', 'phone_number', 'password1', 'password2', 'role', 'department', 'office_location', 'security_question', 'two_fa']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        user = models.User(
            fullname=validated_data['full_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password1'])
        user.save()
        
        # Handle additional fields in a separate model or extend the User model
        return user
