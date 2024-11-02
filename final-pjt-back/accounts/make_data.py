import os
import django
from collections import OrderedDict
import json
import random
import requests

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pjt_back.settings")
# django.setup()

first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'

def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result + str(random.randint(1, 100))

# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
financial_deposit = []
financial_saving = []
financial_products = []
api_key = ''

# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = f''
SP_URL = f''

financial_products = []

# 정기예금 목록 저장
response = requests.get(DP_URL).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_deposit.append(product['fin_prdt_nm'])

# 적금 목록 저장
response = requests.get(SP_URL).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_saving.append(product['fin_prdt_nm'])

dict_keys = [
    'username',
    'financial_products',
    # 'money',
    'salary',
]

# json 파일 만들기
file = OrderedDict()

username_list = []
N = 10000
i = 0

while i < N:
    rn = random_name()
    if rn in username_list:
        continue

    username_list.append(rn)
    i += 1

# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = ''
save_path = os.path.dirname(save_dir)
os.makedirs(save_path, exist_ok=True)

with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')

    for i in range(N):
        # 랜덤한 데이터를 삽입
        file['model'] = 'accounts.User'
        file['pk'] = i + 1
        file['fields'] = {
            'username': username_list[i],  # 유저 이름 랜덤 생성
            # 랜덤한 0~5개의 상품을 가입하도록 삽입됨
            'financial_products': ','.join(
                [
                    random.choice(financial_deposit)
                    for _ in range(random.randint(0, 2))
                ]
            )  + ','.join(
                [
                    random.choice(financial_saving)
                    for _ in range(random.randint(0, 3))
                ]
            ),  # 금융 상품 리스트
            # 'money': random.randrange(0, 100000000, 100000),  # 현재 가진 금액
            'salary': random.randrange(0, 1500000000, 1000000),  # 연봉
            'password': '1234',
        }

        json.dump(file, f, ensure_ascii=False, indent='\t')
        if i != N - 1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
