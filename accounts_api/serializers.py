from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id','username','email','password','password2','first_name','last_name')
        extra_kwargs = {'email': {'required': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name',''),
            last_name=validated_data.get('last_name',''),
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name')
