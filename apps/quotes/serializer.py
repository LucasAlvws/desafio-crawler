from rest_framework import serializers
from .models import Quote, Log

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['quote','author','tags','link']

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'

        


