from rest_framework import serializers
from .models import User,Profile,Storesong,Storefile

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =User
#         # field = [
#         #     "id",
#         # ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class storesongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storesong
        fields ='__all__'

#new
class StorefileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storefile
        fields ='__all__'