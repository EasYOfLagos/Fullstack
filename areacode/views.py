from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import FoodSerializer, UserSerializer, LoginSerializer
from .models import Food
from rest_framework import status 
# Create your views here.

@api_view(['POST'])
def login(request):
    
    try:

        serializer = LoginSerializer(request.data)

        user = serializer.checkuser(serializer.data)
        
        if user is None:
            return Response(data="invalid credentials", status=400)
        else:
            return Response(data=user, status=200)

    except BaseException as e :
        return Response(data=str(e), status=400)



@api_view(['POST'])
def signup(request):
   

    try: 

        serializer = UserSerializer(data=request.data)

        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except BaseException as e:
        
         return Response(data=str(e), status=400)
   



@api_view(['GET'])
def allsauce(request):

    foods = Food.objects.all()

    converted = FoodSerializer(foods, many=True)

    return Response(data=converted.data, status=201)

 