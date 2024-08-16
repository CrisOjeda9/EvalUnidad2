<template>
  <div class="min-h-screen bg-gray-200 flex-col justify-center py-5 sm:px-6 lg:px-8 px-6 bg-repeat">
    <div class="sm:mx-auto sm:w-full sm:max-w-md">
      <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
      <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
        Lotes Medicamentos
      </h2>
    </div>
    <div class="mt-6">
      <a href="/lotes"
         class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
        Agregar +
      </a>
    </div>
    <form class="flex items-center max-w-sm mx-auto mb-6">
      <label for="simple-search" class="sr-only">Buscar</label>
      <div class="relative w-full">
        <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
          <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm12 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm0 0V6a3 3 0 0 0-3-3H9m1.5-2-2 2 2 2" />
          </svg>
        </div>
        <input type="text" id="simple-search" v-model="searchQuery"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="Buscar..." required />
      </div>
      <button type="button" @click="clearSearch"
          class="p-2.5 ms-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
          <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z" />
        </svg>
        <span class="sr-only">Limpiar búsqueda</span>
      </button>
    </form>
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
      <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 bg-white">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">

          <tr>
            <th scope="col" class="px-6 py-3">Medicamento</th>
            <th scope="col" class="px-6 py-3">Personal Médico</th>
            <th scope="col" class="px-6 py-3">Clave</th>
            <th scope="col" class="px-6 py-3">Estatus</th>
            <th scope="col" class="px-6 py-3">Costo Total</th>
            <th scope="col" class="px-6 py-3">Cantidad</th>
            <th scope="col" class="px-6 py-3">Ubicación</th>
            <th scope="col" class="px-6 py-3">Fecha de Registro</th>
            <th scope="col" class="px-6 py-3">Fecha de Actualización</th>
            <th scope="col" class="px-6 py-3 text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in lotes" :key="item.ID" :class="getRowClass(item)">
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ getMedicamentoName(item.Medicamento_ID) }}</span>
              <input v-else v-model="item.Medicamento_ID" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Personal_Medico_ID }}</span>
              <input v-else v-model="item.Personal_Medico_ID" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Clave }}</span>
              <input v-else v-model="item.Clave" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Estatus }}</span>
              <select v-else v-model="item.Estatus" class="w-full border p-1 rounded">
                <option value="Reservado">Reservado</option>
                <option value="En_transito">En transito</option>
                <option value="Recibido">Recibido</option>
                <option value="Rechazado">Rechazado</option>
              </select>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">${{ item.Costo_Total }}</span>
              <div v-else class="flex items-center">
                <button @click="changeValue(item, 'Costo_Total', -1)" class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                <input v-model.number="item.Costo_Total" type="number" step="0.01" min="0" class="w-20 px-2 py-1 border-t border-b text-center" />
                <button @click="changeValue(item, 'Costo_Total', 1)" class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
              </div>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Cantidad }}</span>
              <div v-else class="flex items-center">
                <button @click="changeValue(item, 'Cantidad', -1)" class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                <input v-model.number="item.Cantidad" type="number" min="0" class="w-20 px-2 py-1 border-t border-b text-center" />
                <button @click="changeValue(item, 'Cantidad', 1)" class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
              </div>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ item.Ubicacion }}</span>
              <input v-else v-model="item.Ubicacion" type="text" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4">
              <span>{{ new Date(item.Fecha_Registro).toLocaleString() }}</span>
            </td>
            <td class="px-6 py-4">
              <span v-if="!item.editing">{{ new Date(item.Fecha_Actualizacion).toLocaleString() }}</span>
              <input v-else v-model="item.Fecha_Actualizacion" type="datetime-local" class="w-full border p-1 rounded" />
            </td>
            <td class="px-6 py-4 text-center">
              <button @click="editItem(item)" class="text-blue-500 hover:underline">Editar</button>
              <button v-if="item.editing" @click="saveItem(item)" class="text-green-500 hover:underline">Guardar</button>
              <button v-if="item.editing" @click="cancelEdit(item)" class="text-red-500 hover:underline">Cancelar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      searchQuery: '',
      lotes: [],
      medicamentos: [],
      medicamentoIdMap: {}
    };
  },
  created() {
    this.fetchLotes();
    this.fetchMedicamentos();
  },
  methods: {
    async fetchLotes() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/lotes/');
        this.lotes = response.data;
      } catch (error) {
        console.error('Error al obtener los lotes:', error);
      }
    },
    async fetchMedicamentos() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/medicamentos/');
        this.medicamentos = response.data.map(medicamento => ({
          id: medicamento.ID,
          nombreGenerico: medicamento.Nombre_generico
        }));
        this.medicamentoIdMap = this.medicamentos.reduce((map, medicamento) => {
          map[medicamento.nombreGenerico] = medicamento.id;
          return map;
        }, {});
      } catch (error) {
        console.error('Error al obtener los medicamentos:', error);
      }
    },
    getMedicamentoName(ID) {
      const medicamento = this.medicamentos.find(m => m.id === ID);
      return medicamento ? medicamento.nombreGenerico : 'Desconocido';
    },
    editItem(item) {
      item.editing = !item.editing;
    },
    async saveItem(item) {
      try {
        await axios.put(`http://127.0.0.1:8000/lotes/${item.ID}/`, item);
        item.editing = false;
        this.fetchLotes();
      } catch (error) {
        console.error('Error al guardar el lote:', error);
      }
    },
    cancelEdit(item) {
      item.editing = false;
      this.fetchLotes();
    },
    clearSearch() {
      this.searchQuery = '';
    },
    getRowClass(item) {
      return item.editing ? 'bg-gray-100' : '';
    },
    changeValue(item, field, delta) {
      if (item[field] !== undefined) {
        item[field] = Math.max(0, (item[field] || 0) + delta);
      }
    }
  },
  computed: {
    filteredLotes() {
      const query = this.searchQuery.toLowerCase();
      return this.lotes.filter(lote =>
        lote.Medicamento_ID.toLowerCase().includes(query) ||
        lote.Personal_Medico_ID.toLowerCase().includes(query) ||
        lote.Clave.toLowerCase().includes(query) ||
        lote.Estatus.toLowerCase().includes(query) ||
        lote.Ubicacion.toLowerCase().includes(query)
      );
    }
  }
};
</script>

<style scoped>
/* Agrega tus estilos aquí si es necesario */
</style>
