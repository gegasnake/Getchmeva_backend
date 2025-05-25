from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# View for single product lookup by barcode
class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get(self, request, barcode):
        try:
            product = Product.objects.get(barcode=barcode)
            serializer = self.serializer_class(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


# View for listing all products
class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)
