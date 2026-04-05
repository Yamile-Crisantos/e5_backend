from django.db import models

# Tabla Independiente de Categorías 
class Categoria(models.Model):
    nombre = models.CharField(max_length=100) 

    def __str__(self):
        return self.nombre

# Tabla de Productos (Hereda la PK de Categoria) 
class Producto(models.Model):
    nombre = models.CharField(max_length=150) 
    descripcion = models.TextField(blank=True, null=True) 
    # Relación: Un producto pertenece a una categoría (FK) 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.CharField(max_length=100) 

    def __str__(self):
        return self.nombre

# Tabla de Variantes (Para Tallas y Colores específicos) 
class VarianteProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    talla = models.CharField(max_length=50) 
    color = models.CharField(max_length=50) 
    sku = models.CharField(max_length=100, unique=True) 
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2) 
    stock_actual = models.IntegerField(default=0) 

# Registro principal de la venta 
class Venta(models.Model):
    fecha_venta = models.DateTimeField(auto_now_add=True) 
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    metodo_pago = models.CharField(max_length=50) 

    def __str__(self):
        return f"Venta #{self.id}"

# Lo que contiene cada venta 
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE) 
    variante = models.ForeignKey(VarianteProducto, on_delete=models.PROTECT) 
    cantidad = models.IntegerField() 
    precio_unitario_aplicado = models.DecimalField(max_digits=10, decimal_places=2) 
    subtotal = models.DecimalField(max_digits=10, decimal_places=2) 