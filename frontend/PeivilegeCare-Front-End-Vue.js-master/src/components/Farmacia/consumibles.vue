<template>
  <div class="bg-gray-200 w-full h-full min-h-screen">
    <div class="mx-auto w-full lg:w-7/12 dark:bg-gray-700 p-8 lg:rounded-l-none">
      <!-- Formulario de registro -->
      <h3 class="py-4 text-3xl font-semibold text-center text-gray-800 dark:text-white">Consumibles</h3>
      <form @submit.prevent="submitForm" class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
        <a href="/tablacon"
          class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
          Regresar
        </a>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <!-- Nombre -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="nombre">
              Nombre
            </label>
            <input v-model="form.Nombre" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="nombre" type="text" placeholder="" required />
          </div>

          <!-- Descripción -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="descripcion">
              Descripción
            </label>
            <textarea v-model="form.Descripcion" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="descripcion" placeholder=""></textarea>
          </div>

          <!-- Cantidad -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="cantidad">
              Cantidad
            </label>
            <input v-model.number="form.Cantidad" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="cantidad" type="number" placeholder="" required />
          </div>

          <!-- Tipo -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="tipo">
              Tipo
            </label>
            <select v-model="form.Tipo" id="tipo" required
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="" disabled>Selecciona tipo</option>
              <option value="Material">Material</option>
              <option value="Equipo">Equipo</option>
              <option value="Instrumento">Instrumento</option>
            </select>
          </div>

          <!-- Departamento -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="departamento">
              Departamento
            </label>
            <input v-model.number="form.Departamento_ID" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="departamento" type="number" placeholder="" min="0" required />
          </div>

          <!-- Estatus -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="estatus">
              Estatus
            </label>
            <select v-model="form.Estatus" id="estatus" required
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="" disabled>Selecciona estatus</option>
              <option value="Activo">Activo</option>
              <option value="Inactivo">Inactivo</option>
              <option value="En Revisión">En Revisión</option>
            </select>
          </div>

          <!-- Espacio Médico -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="espacioMedico">
              Espacio Médico
            </label>
            <input v-model="form.Espacio_Medico" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="espacioMedico" type="text" placeholder="" required />
          </div>
        </div>

        <div class="mt-6 text-center">
          <button type="submit"
            class="bg-indigo-600 text-white font-semibold py-2 px-4 w-full rounded-lg hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500">
            Registrar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        Nombre: '',
        Descripcion: '',
        Cantidad: null,
        Tipo: '',
        Departamento_ID: null,
        Estatus: '',
        Espacio_Medico: '',
      },
      searchQuery: ''
    };
  },
  methods: {
    async submitForm() {
      try {
        // Envía los datos del formulario al backend
        await axios.post('http://127.0.0.1:8000/consumibles/', this.form);

        // Muestra una alerta de éxito
        alert('Consumible registrado con éxito');

        // Limpia los campos del formulario
        this.resetForm();
      } catch (error) {
        // Muestra un mensaje de error
        console.error('Error al registrar consumible:', error.response ? error.response.data : error.message);
        alert('Error al registrar consumible');
      }
    },
    resetForm() {
      // Reinicia los campos del formulario a sus valores iniciales
      this.form = {
        Nombre: '',
        Descripcion: '',
        Cantidad: null,
        Tipo: '',
        Departamento_ID: null,
        Estatus: '',
        Espacio_Medico: '',
      };
    },
    search() {
      // Aquí puedes implementar la lógica para manejar la búsqueda
      console.log('Buscar:', this.searchQuery);
    },
    clearSearch() {
      // Limpia el campo de búsqueda
      this.searchQuery = '';
    }
  }
}
</script>
