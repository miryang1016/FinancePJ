from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
    mainbank = serializers.CharField(max_length=225)
    register = serializers.CharField(max_length=100)
    work = serializers.CharField(max_length=100)
    salary = serializers.CharField(max_length=100)
    money = serializers.IntegerField()
    financial_products = serializers.CharField(required=False, max_length=10000, allow_blank=True, allow_null=True)

    def get_cleaned_data(self):        
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'mainbank' : self.validated_data.get('mainbank', ''),
            'register' : self.validated_data.get('register', ''),
            'work' : self.validated_data.get('work', ''),
            'salary' : self.validated_data.get('salary', ''),
            'money' : self.validated_data.get('money', ''),
            'financial_products' : self.validated_data.get('financial_products', '')
        }
        

    # def save(self, request):
    #     user = super().save(request)
    #     user.mainbank = self.validated_data.get('mainbank', '')
    #     user.register = self.validated_data.get('register', '')
    #     user.work = self.validated_data.get('work', '')
    #     user.salary = self.validated_data.get('salary', '')
    #     user.money = self.validated_data.get('money', 0)
    #     print(user.money)
    #     print('-------------')
    #     user.financial_products = self.validated_data.get('financial_products', '')
    #     user.save()
    #     return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'