from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# User serializers
class UserSerializer(serializers.Serializer):
    password= serializers.CharField(write_only=True)

    class Meta:
        model = User
        filed = ('id', 'username', 'email', 'password')
        
        def create(self, validate_data):
            user = User.objects.create(
                username= validate_data['username'],
                email = validate_data['email']
            )
            user.set_password(validate_data['password'])
            user.save()
            return user

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password',
         'email')
    # extra_kwargs = {
    #   'first_name': {'required': True},
    #   'last_name': {'required': True}
    # }
  def create(self, validated_data):
    user = User.objects.create(
      username=validated_data['username'],
      email=validated_data['email'],
    )
    user.set_password(validated_data['password'])
    user.save()
    return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user is None or not user.is_active:
            raise serializers.ValidationError("Incorrect Credentials")

        token, created = Token.objects.get_or_create(user=user)
        data['token'] = token.key
        return data



