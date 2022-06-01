from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Account


class AccountSerializerId(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountRegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # country = CountryField()

    class Meta:
        model = Account
        fields = ('username', 'email', 'phone_number',
                  'password1', 'password2', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = Account.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
        )
        password1 = validated_data['password1']
        password2 = validated_data['password2']

        if password1 != password2:
            raise serializers.ValidationError(
                {"password": "Password didn't match."})
        user.set_password(password1)
        user.is_active = False
        user.save()

        return user
