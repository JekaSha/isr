from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Token
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def create(self, request, *args, **kwargs):
    
        request.data['user'] = request.user.id
        
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('-created_at')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    
        refresh_token = RefreshToken.for_user(user)
        token = str(refresh_token)
        Token.objects.create(user=user, token=token)

        return Response({'status': 'success', 'token': token}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'fail'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'status': 'success'}, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.create_user(username=username, password=password)

        serializer = self.get_serializer(user)

        user_data = serializer.data
        response_data = {'status': 'success', 'data': user_data}

        return Response(response_data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        response_data = {'status': 'success', 'data': user_data}
        return Response(response_data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class Test1(viewsets.ViewSet):
    
    def list(self, request, *args, **kwargs):
        username = request.GET.get('username')
        print(username)
        return HttpResponse(username)
    
    
