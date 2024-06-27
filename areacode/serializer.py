from rest_framework import serializers
from .models import Food, User, Cart
from django.contrib.auth import authenticate 



class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, data):

     User.objects.create_user(
        first_name = data['first_name'],
        last_name = data['last_name'],
        email = data['email'],
        password = data['password'],
        profile = data['profile']
    )
     return data
    

class LoginSerializer(serializers.Serializer):
   email = serializers.EmailField()
   password = serializers.CharField()
  
   def checkuser(self, data):
      
      user = authenticate(email = data['email'], password = data['password'])

      if user is None:
         return None
      else:
         id = getattr(user, "id")

         return id
                            

class cartSerilizer(serializers.ModelSerializer):
   class Meta:
      model = Cart
      fields = '__all__'
    

