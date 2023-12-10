from rest_framework import serializers,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from . import signals
# Create your views here.
"""amader kono Ekjon user er data database e ache ki na seta checking er process ta hocche authentication ...
   checking process hote  pare email,and password diye check kortechi j database e ache ki na ..jodi database e thake 
   taile email and password diye login koray dibo  etake bole authentication process then se amake kon kon page access dibe
   setake boltechi authorization 

"""
""" #  Without Token created and database e save kora chara
class RegistrationView(APIView):
    def post(self,request): # ekahne amader func er name oi dite hoi post diye 
        serializer=RegistrationSerializer(data=request.data)  # form e j kaj ta kortam ekhaneo same kaj oi kortechi  
        if serializer.is_valid(): # age likhtam form.is_valid ekhon serializer er khetre eka likhte hoi 
            serializer.save() # age form save kortam ekhon serializer save kortechi 
            return Response(serializer.data,status=status.HTTP_201_CREATED) # jodi sob kisu thik thake taile create kore dibe
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) # otherwise jodi se if condition e dhuke jai taile Http_400 bad request dibe 
 """

# Token created and database e save kora soho
class RegistrationView(APIView):
    queryset=User.objects.all()
    serializer_class=RegistrationSerializer
    def post(self,request):
        data= {}
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account=serializer.save()
            data['response'] = 'Registration Successful'
            data['username'] = account.username
            data['email'] = account.email
            token=Token.objects.get(user=account).key
            data['token'] = token
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            data=serializer.errors
        return Response(data)
    
    
class LogoutView(APIView):
     def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)