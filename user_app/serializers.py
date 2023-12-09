""" from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":'password'},write_only='True')
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):    # amra save ei function ta tkhone use korbo jkhn dekhbo field ke validation use korte hoi tkhn 
        username=self.validated_data['username']
        email=self.validated_data['email']
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password!=password2:
            raise serializers.ValidationError({'error':'password doesnot match'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'email already exists'})
        
        account=User(username=username,email=email)
        account.set_password(password)
        account.save()
        return account """
    
    
    
    
from django.contrib.auth.models import User
from rest_framework import serializers
# amader form er moddhe j field gulo chilo same to same ekhaneo ache ...rest framework amader form support kore na eta amra html diye generate korte parbo
# rest framework amader form support kore na sobsomoy serializer niye kaj korbo 

""" User login korar somoy username and password dibe sei username and password er upor base kore ekta password create kore dibe 
    Amra registration er khetre sob kaj postman e kortechi kono frontend e kaj kortechi na ...
    Amader target username always unique rakhbo ...email 2 jon user(rahim,karim) er same hote parbe na jodio django seta support kore 
    Django amader password dekhte dibe na login korar por jokhon onno kono user e login korbo ...password and confirm_password same ki na 
    eta amra validation korbo j 2 ta same ki na ...amra read only type e kore nibo 
    """
class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":'password'},write_only='True') 
    # amra age widget use kortam ekhon serializer er khetre style use korbo ..ar bole dicchi j input type hobe password and write only true kore dichi karon eta amra sudhu write korte parbo
    class Meta:
        model=User # by default user model 
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True} # amra password2 k write only true kore dichi upore ekhane amra password k write only true kore dilam 
        }
    def save(self): # save amra tokhonoi use kori jokhon amra uporer j datagulo pacchi segulor moddhe kono type er validation check korte hoi jemonta amra email check korbo j 2 jon user er email same hobe na
        # normally ei kaj ta form e kora hoi ekhane amra serializer e kore thakbo  
        username=self.validated_data['username'] # username nicchi age form er khetre clean data nicchilam ekhon validation data 
        email=self.validated_data['email'] # amra email,password,password2 nilam
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        # ekhane self bolte oi class er instance er j data seta niye kaj kortechi amra ..self er moddhe validated data ache and self bolte object ta k bujhay  
        
        # ekhon amra validation kortechi j jodi amader password and password2 match na hoi taile serializers.validationerror e bole ekta message bole dibo
        if password!=password2:
            raise serializers.ValidationError({'error':'password doesnot match'})# error message ta evabe dite hoi
        if User.objects.filter(email=email).exists(): # j user instance ekhon create holo setar email ta j asteche upor theke seta ami amra object er moddhe pass kore dekhalm j ei email ta exist kre ki na
            # jodi exist kore sekhetre validation error diye bolbe email already exist kore 
            raise serializers.ValidationError({'error':'email already exists'})
        
        # uporer validation howar por jodi tara beche jai or if condition e na dhuke taile nicher line gulo kaj korbe
        account=User(username=username,email=email) # ekhon amra username er moddhe username and email er moddhe email pass kortechi ....ekhane first j username ta ache seta djangor by default username ar pore j username seta user j data pass kore seta suppose rahim karim etc 
        account.set_password(password) # set password dile amader password ta save hoye jabe and finally save kore ami account ta return kore dicchi  
        account.save()
        return account
    
    # user jokhon kono data pass korbe data pass korar pore ei validation gulo korbe 