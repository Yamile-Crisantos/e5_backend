import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/'
});

// axios interceptors
// dividir por eiponds los servicio crear por ejemplo archivo products_services

export default {
    // GET: Obtener datos
    getProductos() { return api.get('productos/'); },
    getCategorias() { return api.get('categorias/'); },
    
    // POST: Enviar datos al Controller de Django
    crearProducto(data) {
        return api.post('productos/', data);
    }
}