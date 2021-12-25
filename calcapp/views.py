from django.shortcuts import render
from calcapp.models import Calculator
from calcapp.serializers import CalculatorSerializer
from Calculate.calculate import Calculate
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['POST'])
def calculate(request):
    if request.method == "POST":
        try:
            request_data = JSONParser().parse(request)
            calc_ob = Calculate()
            result = calc_ob.calculate()

            return JsonResponse({'result': result}, status=status.HTTP_200_Success)
        except Exception:
            return JsonResponse({'error': "Internal Server Error"}, status=status.HTTP_500_error)
        