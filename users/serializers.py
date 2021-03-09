
# from django.contrib.auth.models import User #default django User implementation
from .models import User # enable more field to be added 
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class UserSerializer(serializers.ModelSerializer):
    """Serilialized User model fields """

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]



# class SetPasswordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SetPasswordModel
#         fields = ('user','new_password1','new_password2')
#         # read_only_fields = ('active', 'is_staff')

