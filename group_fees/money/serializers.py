from rest_framework import serializers
from .models import Payment,Collect,Contribution

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CollectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collect
        fields = '__all__'

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'
