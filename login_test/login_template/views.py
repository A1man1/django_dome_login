from django.shortcuts import render, redirect
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from .serializer import RegisterSerializer ,ChangePasswordSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny,  IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

class RegisterView(generics.CreateAPIView):
        queryset = User.objects.all()
        permission_classes = (AllowAny,)
        serializer_class = RegisterSerializer


class ChangePasswordView(generics.UpdateAPIView):
        queryset = User.objects.all()
        permission_classes = (IsAuthenticated,)
        serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):

        queryset = User.objects.all()
        permission_classes = (IsAuthenticated,)
        serializer_class = UpdateUserSerializer


class LogoutView(APIView):
        permission_classes = (IsAuthenticated,)

        def post(self, request):
            try:
                refresh_token = request.data["refresh_token"]
                token = RefreshToken(refresh_token)
                token.blacklist()

                return Response(status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class LogoutAllView(APIView):
        permission_classes = (IsAuthenticated,)

        def post(self, request):
            tokens = OutstandingToken.objects.filter(user_id=request.user.id)
            for token in tokens:
                t, _ = BlacklistedToken.objects.get_or_create(token=token)

            return Response(status=status.HTTP_205_RESET_CONTENT)

'''
def validation(request):
     if request.META.get('HTTP_REFERER')\
        == 'http://127.0.0.1:8000/':
        if request.method == "POST":
            if request.POST.get('pass')[0]\
               == request.POST.get('conform')[0]\
               and request.POST.get('conform') is not ''\
               or request.POST.get('conform') is not None:
                        return redirect('/login/')
            else:
                  return redirect(signup_view)

     else:







def signup_view(request):
     return render(request, 'signup.html')
'''
