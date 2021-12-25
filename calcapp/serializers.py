from rest_framework import serializers

from calcapp.models import Calculator

class CalculatorSerializer(serializers.ModelSerializer):
    model = Calculator
    fields = ('id',
              'result')