from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from ..models import Product
from ..services.products import create_product
from ..selectors.products import get_products
from drf_spectacular.utils import extend_schema


class ProductApi(APIView):
    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = "__all__"

    @extend_schema(request=InputSerializer, responses=OutputSerializer)
    def post(self, request):
        serializer_data = self.InputSerializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        try:
            query = create_product(name=serializer_data.validated_data.get("name"))
        except Exception as ex:
            return Response(status.HTTP_400_BAD_REQUEST)

        return Response(self.OutputSerializer(query, context={"request": request}).data)

    @extend_schema(responses=OutputSerializer)
    def get(self, request):
        query = get_products()
        return Response(self.OutputSerializer(query, context={"request": request}, many=True).data)
