from rest_framework import serializers
from users.models import CustomUser, Pref
from django.contrib.auth.hashers import make_password


def validate_tel(value):
    if not value.isnumeric():
        raise serializers.ValidationError("Tel must be numeric")
    return value


class UserSerializer(serializers.ModelSerializer):
    pref_id = serializers.PrimaryKeyRelatedField(
        source="pref", queryset=Pref.objects.all(), required=False
    )
    tel = serializers.CharField(validators=[validate_tel])

    class Meta:
        model = CustomUser
        fields = ["id", "username", "tel", "pref_id", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = ["id"]

    def validate_password(self, value):
        """Hash the password before saving"""
        return make_password(value)


class PrefectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pref
        fields = ["id", "name"]
