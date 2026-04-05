from rest_framework import serializers
from .models import Categoria, Producto, VarianteProducto, Venta, DetalleVenta

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class VarianteSerializer(serializers.ModelSerializer):
    # Esto mostrará el nombre del producto en lugar de solo el ID
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')
    
    class Meta:
        model = VarianteProducto
        fields = ['id', 'producto', 'producto_nombre', 'talla', 'color', 'sku', 'precio_venta', 'stock_actual']