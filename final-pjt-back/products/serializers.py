from rest_framework import serializers
from .models import DepositOption, DepositProduct, SavingOption, SavingProduct

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'

class DepositProductSerializer(serializers.ModelSerializer):
    options = DepositOptionSerializer(many=True, read_only=True, source='depositoption_set')
    
    class Meta:
        model = DepositProduct
        fields = '__all__'

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'

class SavingProductSerializer(serializers.ModelSerializer):
    options = SavingOptionSerializer(many=True, read_only=True, source='savingoption_set')
    
    class Meta:
        model = SavingProduct
        fields = '__all__'