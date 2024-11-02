import requests
from django.http import JsonResponse
from .serializers import DepositProductSerializer, SavingProductSerializer, DepositOptionSerializer, SavingOptionSerializer
from .models import SavingProduct, DepositProduct, SavingOption, DepositOption
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import DepositProduct

API_KEY_FINLIFE=settings.API_KEY_FINLIFE

def get_deposit(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY_FINLIFE}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    for dic in response['result']['baseList']:
        fin_prdt_cd = dic['fin_prdt_cd']

        if DepositProduct.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue
        
        dcls_month = dic['dcls_month']
        kor_co_nm = dic['kor_co_nm']
        fin_prdt_nm = dic['fin_prdt_nm']
        join_way = dic['join_way']
    
        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'dcls_month': dcls_month,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'join_way': join_way,
        }

        serializer = DepositProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()

            for option_dic in response['result']['optionList']:
                if option_dic['fin_prdt_cd'] == fin_prdt_cd:
                    option_data = {
                        'intr_rate_type_nm': option_dic['intr_rate_type_nm'],
                        'intr_rate': option_dic['intr_rate'],
                        'save_trm': option_dic['save_trm'],
                        'product': product.id
                    }
                    option_serializer = DepositOptionSerializer(data=option_data)
                    if option_serializer.is_valid(raise_exception=True):
                        option_serializer.save()

    return JsonResponse({ 'message': 'save success' })

def get_saving(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY_FINLIFE}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()

    for dic in response['result']['baseList']:
        fin_prdt_cd = dic['fin_prdt_cd']
        
        if SavingProduct.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            continue
        
        dcls_month = dic['dcls_month']
        kor_co_nm = dic['kor_co_nm']
        fin_prdt_nm = dic['fin_prdt_nm']
        join_way = dic['join_way']
    
        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'dcls_month': dcls_month,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'join_way': join_way,
        }

        serializer = SavingProductSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            product = serializer.save()

            for option_dic in response['result']['optionList']:
                if option_dic['fin_prdt_cd'] == fin_prdt_cd:
                    option_data = {
                        'intr_rate_type_nm': option_dic['intr_rate_type_nm'],
                        'intr_rate': option_dic['intr_rate'],
                        'save_trm': option_dic['save_trm'],
                        'product': product.id
                    }
                    option_serializer = SavingOptionSerializer(data=option_data)
                    if option_serializer.is_valid(raise_exception=True):
                        option_serializer.save()

    return JsonResponse({ 'message': 'save success' })

@api_view(['GET'])
def deposit_list(request):
    deposits = DepositProduct.objects.prefetch_related('depositoption_set').all()
    serializer = DepositProductSerializer(deposits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def saving_list(request):
    savings = SavingProduct.objects.prefetch_related('savingoption_set').all()
    serializer = SavingProductSerializer(savings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def deposit_detail(request, pk):
    deposit = DepositProduct.objects.prefetch_related('depositoption_set').get(pk=pk)
    serializer = DepositProductSerializer(deposit)
    return Response(serializer.data)

@api_view(['GET'])
def saving_detail(request, pk):
    saving = SavingProduct.objects.prefetch_related('savingoption_set').get(pk=pk)
    serializer = SavingProductSerializer(saving)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_click_deposit(request, pk):
    product = DepositProduct.objects.get(pk=pk)
    product.click_deposit += 1  # click_deposit 값을 1 증가
    product.save()
    
    serializer = DepositProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_click_saving(request, pk):
    product = SavingProduct.objects.get(pk=pk)
    product.click_saving += 1  # click_deposit 값을 1 증가
    product.save()

    print(product.click_saving)
    
    serializer = SavingProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)