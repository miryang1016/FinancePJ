from dj_rest_auth.registration.views import RegisterView
from rest_framework.decorators import api_view, permission_classes
from .serializers import CustomRegisterSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer
    
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def add_product(request):
#     user = request.user
    
#     if not user.financial_products:
#         products = []
#     else:
#         products = user.financial_products.split(',')
    # print(products)

    # if product_cd in products:
    #     products.remove(product_cd)
    # else:
    #     products.append(product_cd)
    
    # user.financial_products = ','.join(products)
    # print(user.financial_products)
    # user.save()
    # print(user.financial_products)

    # return Response({'message': 'Product added to favorites'}, status=status.HTTP_201_CREATED)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request):
    print(request.data)
    serializer = UserSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)