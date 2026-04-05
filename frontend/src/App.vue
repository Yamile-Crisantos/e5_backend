<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">📦 Registro de Inventario</h1>

    <div class="card shadow mb-5">
      <div class="card-header bg-success text-white">
        <h4 class="mb-0">Agregar Nuevo Producto</h4>
      </div>
      <div class="card-body">
        <form @submit.prevent="guardarProducto">
          <div class="row">
            <div class="col-md-6 mb-3">
              <label class="form-label">Nombre del Producto</label>
              <input v-model="nuevoProducto.nombre" type="text" class="form-control" placeholder="Ej: Camisa Slim Fit" required>
            </div>
            <div class="col-md-6 mb-3">
              <label class="form-label">Marca</label>
              <input v-model="nuevoProducto.marca" type="text" class="form-control" placeholder="Ej: Levi's" required>
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label class="form-label">Categoría</label>
              <select v-model="nuevoProducto.categoria" class="form-select" required>
                <option value="" disabled>Seleccione una categoría</option>
                <option v-for="cat in categorias" :key="cat.id" :value="cat.id">
                  {{ cat.nombre }}
                </option>
              </select>
            </div>
            <div class="col-md-6 mb-3">
              <label class="form-label">Descripción</label>
              <textarea v-model="nuevoProducto.descripcion" class="form-control" rows="1"></textarea>
            </div>
          </div>
          
          <button type="submit" class="btn btn-primary w-100">Guardar en Base de Datos</button>
        </form>
      </div>
    </div>

    <div class="card shadow">
      <div class="card-header bg-dark text-white">
        <h4 class="mb-0">Productos en MySQL</h4>
      </div>
      <div class="card-body px-0">
        <table class="table table-hover mb-0">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Marca</th>
              <th>Categoría</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="p in productos" :key="p.id">
              <td>{{ p.id }}</td>
              <td>{{ p.nombre }}</td>
              <td>{{ p.marca }}</td>
              <td>{{ p.categoria }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from './services/api';

const productos = ref([]);
const categorias = ref([]);
const nuevoProducto = ref({ nombre: '', marca: '', categoria: '', descripcion: '' });

// Cargar datos iniciales
const cargarDatos = async () => {
  const [resProd, resCat] = await Promise.all([
    api.getProductos(),
    api.getCategorias()
  ]);
  productos.value = resProd.data;
  categorias.value = resCat.data;
};

// Enviar al Controller -> Service
const guardarProducto = async () => {
  try {
    await api.crearProducto(nuevoProducto.value);
    alert("¡Producto guardado exitosamente!");
    // Limpiar formulario y recargar tabla
    nuevoProducto.value = { nombre: '', marca: '', categoria: '', descripcion: '' };
    cargarDatos();
  } catch (error) {
    console.error("Error al guardar:", error);
    alert("Hubo un error al procesar la petición.");
  }
};

onMounted(cargarDatos);
</script>