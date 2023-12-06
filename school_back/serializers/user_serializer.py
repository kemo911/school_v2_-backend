from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', None)
        permissions_data = validated_data.pop('user_permissions', None)

        user = get_user_model().objects.create_user(**validated_data)

        if groups_data:
            user.groups.set(groups_data)
        if permissions_data:
            user.user_permissions.set(permissions_data)

        return user
