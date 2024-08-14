<template>
  <div class="bg-gray-200 w-full h-full min-h-screen">
    <div class="mx-auto w-full lg:w-7/12 dark:bg-gray-700 p-8 lg:rounded-l-none">
      <h3 class="py-4 text-3xl font-semibold text-center text-gray-800 dark:text-white">Medicamentos</h3>
      <form @submit.prevent="submitForm" class="px-8 pt-6 pb-8 mb-4 bg-white dark:bg-gray-800 rounded">
        <a href="/tablamedic"
          class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
          Regresar
        </a>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <!-- Nombre Comercial -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="nombreCom">
              Nombre Comercial
            </label>
            <input v-model="form.Nombre_comercial"
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="nombreCom" type="text" placeholder="" required />
          </div>

          <!-- Nombre Generico -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="nombreGen">
              Nombre Generico
            </label>
            <input v-model="form.Nombre_generico"
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="nombreGen" type="text" placeholder="" required />
          </div>

          <!-- Via de Administracion -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="via">
              Via de Administracion
            </label>
            <select v-model="form.Via_administracion" id="via" name="via" required
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="" disabled>Selecciona via</option>
              <option value="Oral">Oral</option>
              <option value="Intravenoso">Intravenoso</option>
              <option value="Rectal">Rectal</option>
              <option value="Cutaneo">Cutáneo</option>
              <option value="Subcutaneo">Subcutáneo</option>
              <option value="Oftalmica">Oftálmica</option>
              <option value="Otica">Ótica</option>
              <option value="Nasal">Nasal</option>
              <option value="Topica">Tópica</option>
              <option value="Parenteral">Parenteral</option>
            </select>
          </div>

          <!-- Presentacion -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="presentacion">
              Presentacion
            </label>
            <select v-model="form.Presentacion" id="presentacion" name="presentacion" required
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="" disabled>Selecciona tipo</option>
              <option value="Comprimidos">Comprimidos</option>
              <option value="Grageas">Grageas</option>
              <option value="Capsulas">Cápsulas</option>
              <option value="Jarabes">Jarabes</option>
              <option value="Gotas">Gotas</option>
              <option value="Solucion">Solución</option>
              <option value="Pomada">Pomada</option>
              <option value="Jabon">Jabón</option>
              <option value="Supositorios">Supositorios</option>
              <option value="Viales">Viales</option>
            </select>
          </div>

          <!-- Tipo -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="tipo">
              Tipo
            </label>
            <select v-model="form.Tipo" id="tipo" name="tipo" required
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="" disabled>Selecciona tipo</option>
              <option value="Analgésicos">Analgésicos</option>
              <option value="Antibióticos">Antibióticos</option>
              <option value="Antidepresivos">Antidepresivos</option>
              <option value="Antihistamínicos">Antihistamínicos</option>
              <option value="Antiinflamatorios">Antiinflamatorios</option>
              <option value="Antipsicóticos">Antipsicóticos</option>
            </select>
          </div>

          <!-- Volumen -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="volumen">
              Volumen
            </label>
            <input v-model.number="form.Volumen"
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="volumen" type="number" step="0.01" min="0" placeholder="" />
          </div>

          <!-- Cantidad -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="cantidad">
              Cantidad
            </label>
            <input v-model.number="form.Cantidad"
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="cantidad" type="number" placeholder="" min="0" required />
          </div>

          <!-- Estatus -->
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="estatus">
              Estatus
            </label>
            <select v-model="form.Estatus" id="estatus" required
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600">
              <option value="" disabled>Selecciona estatus</option>
              <option value="true">Activo</option>
              <option value="false">Inactivo</option>
            </select>
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
        Nombre_comercial: '',
        Nombre_generico: '',
        Via_administracion: '',
        Presentacion: '',
        Tipo: '',
        Cantidad: null,
        Volumen: null,
        Estatus: null,
        Fecha_registro: new Date().toISOString(),
        Fecha_actualizacion: new Date().toISOString(),
      }
    };
  },
  methods: {
    async submitForm() {
      try {
        await axios.post('http://127.0.0.1:8000/medicamentos/', this.form);
        alert('Medicamento registrado con éxito');
        // Reiniciar el formulario
        this.resetForm();
      } catch (error) {
        console.error('Error al registrar medicamento:', error.response ? error.response.data : error.message);
        alert('Error al registrar medicamento');
      }
    },
    resetForm() {
      // Reiniciar los campos del formulario a sus valores iniciales
      this.form = {
        Nombre_comercial: '',
        Nombre_generico: '',
        Via_administracion: '',
        Presentacion: '',
        Tipo: '',
        Cantidad: null,
        Volumen: null,
        Estatus: null,
        Fecha_registro: new Date().toISOString(),
        Fecha_actualizacion: new Date().toISOString(),
      };
    }
  }
}
</script>
