from .models import Categoria, Producto, VarianteProducto, Venta, DetalleVenta
from django.shortcuts import get_object_or_404
from django.db import transaction

class InventarioService:
    @staticmethod
    def crear_categoria(nombre):
        return Categoria.objects.create(nombre=nombre)

    @staticmethod
    def crear_producto_con_categoria(nombre, marca, categoria_id, descripcion=""):
        categoria = get_object_or_404(Categoria, id=categoria_id)
        return Producto.objects.create(
            nombre=nombre, marca=marca, categoria=categoria, descripcion=descripcion
        )

class VentaService:
    @staticmethod
    @transaction.atomic
    def registrar_venta(variante_id, cantidad, metodo_pago):
        variante = get_object_or_404(VarianteProducto, id=variante_id)
        if variante.stock_actual < cantidad:
            raise Exception("No hay suficiente stock")
        
        total_venta = variante.precio_venta * cantidad
        nueva_venta = Venta.objects.create(total=total_venta, metodo_pago=metodo_pago)
        
        DetalleVenta.objects.create(
            venta=nueva_venta,
            variante=variante,
            cantidad=cantidad,
            precio_unitario_aplicado=variante.precio_venta,
            subtotal=total_venta
        )
        variante.stock_actual -= cantidad
        variante.save()
        return nueva_venta