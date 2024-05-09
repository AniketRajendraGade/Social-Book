from django.shortcuts import render
from rest_framework.views import APIView
from myapp.models import CustomUser
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.core.mail import send_mail
from django.conf import settings
import jwt,datetime
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        user=CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("user not found!")
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
                'user_id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat':datetime.datetime.utcnow()
            }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256') 

        response=Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)   

        response.data={
            'jwt':token
        }

        sendEmail(email)
        
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')
        

        user = CustomUser.objects.filter(id=payload['user_id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self,request):
        response=Response()
        response.delete_cookie('jwt')
        response.data={
            'message':'success'
        }
        return response
    

def sendEmail(email):
    subject = "About login"
    message = f"You have loged in "
    email_from = settings.EMAIL_HOST
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


class BookUploadAPIView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token!')
        
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)