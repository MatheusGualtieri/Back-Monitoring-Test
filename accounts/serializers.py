from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "name", "email", "password", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"required": False, "default": False},
        }

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(), message="This field must be unique."
            )
        ],
    )

    def create(self, validated_data: dict) -> User:
        if validated_data["is_superuser"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(raw_password=instance.password)

        instance.save()

        return instance


User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = User.objects.filter(email=email).first()

            if user and user.check_password(password):
                refresh = self.get_token(user)
                data = {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user_id": user.id,
                }
                return data

        raise serializers.ValidationError("Credenciais inválidas.")
