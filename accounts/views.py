from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import UserLoginSerializer
from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
#from django.http import HttpResponse,JsonResponse
from rest_framework.authtoken.models import Token

from .serializers import UserCreateSerializer
from .models import User
#from django.shortcuts import render


@api_view(['POST'])
@permission_classes([AllowAny])
@method_decorator(csrf_exempt)
#@ensure_csrf_cookie
def createUser(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        #user = authenticate(UserCreateSerializer.password)
        #user = UserCreateSerializer.user
        #token, _ = Token.objects.get_or_create(user=user)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            user = serializer.save()
            token = Token.objects.create(user=user) # 유저가 있으면 가져오고, 없으면 토큰을 생성한다.
            return Response({
                            "message": "ok",
                            "Token": token.key
                            },
                            status=status.HTTP_201_CREATED)
        return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([AllowAny])
@method_decorator(csrf_exempt)
#@ensure_csrf_cookie
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_409_CONFLICT)
        token = serializer.data['token']
        #token = Token.objects.create()
        response = {
            'success': 'True',
            'token':serializer.data['token'],
            
        }
        #res = render(request, 'users/logins')
        #res = HttpResponse({'success':True})
        #res.set_cookie('accesstoken',token)
        #HttpResponse.set_cookie('acdsdftoken',token)

        #response.set_cookie('csrf',serializer.data['token'])
        return Response(response, status=status.HTTP_200_OK)
        #return res
        
