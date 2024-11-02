import requests
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import RatesSerializer, RatesListSerializer
from .models import Rates
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings

# Create your views here.
API_KEY_KOREAEXIM = settings.API_KEY_KOREAEXIM


def save_rates(request):
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY_KOREAEXIM}&data=AP01'
    response = requests.get(url).json()

    for data in response:
        if '100' in data['cur_unit']:
            cur_unit = data['cur_unit'].partition('(')[0]
            cur_unit = cur_unit.strip()
            cur_nm = data['cur_nm']
            ttb = "{:.2f}".format(float(data['ttb'].replace(',', '')) / 100)
            tts = "{:.2f}".format(float(data['tts'].replace(',', '')) / 100)
        else:
            cur_unit = data['cur_unit']
            cur_nm = data['cur_nm']
            ttb = "{:.2f}".format(float(data['ttb'].replace(',', '')))
            tts = "{:.2f}".format(float(data['tts'].replace(',', '')))

        save_data = {
            'cur_unit': cur_unit,
            'cur_nm': cur_nm,
            'ttb': ttb,
            'tts': tts,
        }

        serializer = RatesSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    return JsonResponse({ 'message': 'save success' })
    

@api_view(['GET'])
def calculate(request):
    rates = Rates.objects.all()
    serializers = RatesListSerializer(rates, many=True)
    return Response(serializers.data)