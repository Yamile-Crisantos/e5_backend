from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Categoria, Producto, VarianteProducto
from .serializers import CategoriaSerializer, ProductoSerializer, VarianteSerializer
from .services import InventarioService, VentaService # Importación relativa correcta

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def create(self, request):
        try:
            nombre = request.data.get('nombre')
            nueva_cat = InventarioService.crear_categoria(nombre)
            return Response(CategoriaSerializer(nueva_cat).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def create(self, request):
        try:
            producto = InventarioService.crear_producto_con_categoria(
                nombre=request.data.get('nombre'),
                marca=request.data.get('marca'),
                categoria_id=request.data.get('categoria'),
                descripcion=request.data.get('descripcion', '')
            )
            return Response(ProductoSerializer(producto).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class VarianteViewSet(viewsets.ModelViewSet):
    queryset = VarianteProducto.objects.all()
    serializer_class = VarianteSerializer