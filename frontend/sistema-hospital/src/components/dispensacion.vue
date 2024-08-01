<template>
  <div class="bg-gray-200 w-full h-full min-h-screen relative">
    <form>
      <div class="mx-auto w-full lg:w-8/12 dark:bg-gray-700 p-8 lg:rounded-l-none">
        <!-- Campos de selección en la esquina superior derecha -->
        <div class="absolute top-4 right-4 space-y-4">
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="receta_id">
              Receta ID
            </label>
            <select
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="receta_id" @change="handleRecetaChange" v-model="selectedRecetaId">
              <option value="">Seleccionar</option>
              <option v-for="receta in recetas" :key="receta.id" :value="receta.id">{{ receta.nombre }}</option>
            </select>
          </div>
          <div>
            <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white" for="solicitud_id">
              Solicitud ID
            </label>
            <select
              class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 dark:text-white dark:bg-gray-700 dark:border-gray-600"
              id="solicitud_id" @change="handleSolicitudChange" v-model="selectedSolicitudId">
              <option value="">Seleccionar</option>
              <option v-for="solicitud in solicitudes" :key="solicitud.id" :value="solicitud.id">{{ solicitud.nombre }}
              </option>
            </select>
          </div>

        </div>
        <a href="/tabladis"
          class="text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
          Regresar
        </a>

        <!-- Datos de Receta o Solicitud en la esquina superior izquierda -->
        <div class="absolute top-4 left-4 space-y-4">
          <!-- Mostrar campos basados en la selección de Receta ID -->
          <div v-if="selectedRecetaId && !selectedSolicitudId">
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Paciente Nombre</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="receta.paciente_nombre" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Paciente Edad</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="receta.paciente_edad" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Médico Nombre</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="receta.medico_nombre" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Fecha</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm" :value="receta.fecha"
                readonly />
            </div>
          </div>

          <!-- Mostrar campos basados en la selección de Solicitud ID -->
          <div v-if="selectedSolicitudId && !selectedRecetaId">
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Paciente ID</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="solicitud.Paciente_ID" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Médico ID</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="solicitud.Medico_ID" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Servicio ID</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="solicitud.Servicio_ID" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Prioridad</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="solicitud.Prioridad" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Descripción</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm"
                :value="solicitud.Descripcion" readonly />
            </div>
            <div>
              <label class="block mb-2 text-sm font-semibold text-gray-700 dark:text-white">Estatus</label>
              <input type="text" class="w-full px-4 py-2 text-sm border rounded-lg shadow-sm" :value="solicitud.Estatus"
                readonly />
            </div>
          </div>
        </div>

        <h3 class="py-4 text-3xl font-semibold text-center text-gray-800 dark:text-white">Dispensación</h3>

        <!-- Tabla editable en el centro -->
        <div class="panel panel-default mt-8 overflow-x-auto">
          <table class="table-auto w-full border-collapse">
            <thead>
              <tr class="bg-gray-300 text-gray-700">
                <th class="px-3 py-2">Elemento</th>
                <th class="px-3 py-2">Costo</th>
                <th class="px-3 py-2">Cantidad Solicitada</th>
                <th class="px-3 py-2">Entregado</th>
                <th class="px-3 py-2">Importe</th>
                <th class="px-3 py-2">Estatus</th>
                <th class="px-3 py-2">Tipo</th>
                <th class="px-3 py-2">Eliminar</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in items" :key="index">
                <td class="px-3 py-2">{{ item.nombre }}</td>
                <td class="px-3 py-2">{{ item.costo }}</td>
                <td class="px-3 py-2">{{ item.cantidad }}</td>
                <td class="px-3 py-2">
                  <input type="number" v-model.number="item.entregado" @input="updateEstatus(item)" min="0"
                    class="w-full px-2 py-1 border rounded-lg shadow-sm" />
                </td>
                <td class="px-3 py-2">{{ item.entregado * item.costo }}</td>
                <td class="px-3 py-2">{{ item.estatus }}</td>
                <td class="w-40">
                  <select v-model="item.tipo" @change="updateTipo(item)"
                    class="w-full px-2 py-1 border rounded-lg shadow-sm">
                    <option value="Pública">Pública</option>
                    <option value="Privada">Privada</option>
                    <option value="Mixta">Mixta</option>
                  </select>
                </td>
                <td class="px-3 py-2 text-center">
                  <button type="button" class="bg-red-600 text-white px-2 py-1 rounded-lg" @click="eliminarFila(index)">
                    <i class="fa fa-trash-o"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Total Costo -->
        <div class="mt-6 text-center bg-gray-100 p-4 border-t border-gray-300">
          <p class="text-lg font-semibold">Total Costo: {{ totalCosto }}</p>
        </div>

        <!-- Botón de registrar -->
        <div class="mt-6 text-center">
          <button
            class="bg-indigo-600 text-white font-semibold py-2 px-4 w-full rounded-lg hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            type="button">
            Registrar
          </button>
        </div>
      </div>
    </form>
  </div>
</template>



<script>
export default {
  data() {
    return {
      selectedRecetaId: '',
      selectedSolicitudId: '',
      receta: {
        paciente_nombre: '',
        paciente_edad: '',
        medico_nombre: '',
        fecha: ''
      },
      solicitud: {
        Paciente_ID: '',
        Medico_ID: '',
        Servicio_ID: '',
        Prioridad: '',
        Descripcion: '',
        Estatus: ''
      },
      items: [], // Array para almacenar medicamentos o utensilios
      recetas: [
        { id: '1', nombre: 'Receta 1' },
        { id: '2', nombre: 'Receta 2' }
        // Añadir más recetas según sea necesario
      ],
      solicitudes: [
        { id: '1', nombre: 'Solicitud 1' },
        { id: '2', nombre: 'Solicitud 2' }
        // Añadir más solicitudes según sea necesario
      ]
    };
  },
  computed: {
    // Computar el total costo sumando los importes de cada fila
    totalCosto() {
      return this.items.reduce((total, item) => total + (item.entregado * item.costo), 0).toFixed(2);
    }
  },
  methods: {
    handleRecetaChange() {
      if (this.selectedRecetaId) {
        this.selectedSolicitudId = ''; // Limpiar la selección de solicitud
        if (this.selectedRecetaId === '2') {
          this.receta = {
            paciente_nombre: 'Jane Doe',
            paciente_edad: 34,
            medico_nombre: 'Dr. Jones',
            fecha: '2024-07-31'
          };
          this.items = [
            { nombre: 'Medicamento X', costo: 10, cantidad: 15, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Mixta' },
            { nombre: 'Medicamento Y', costo: 12, cantidad: 8, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Pública' }
          ];
        } else {
          this.receta = {
            paciente_nombre: 'John Doe',
            paciente_edad: 45,
            medico_nombre: 'Dr. Smith',
            fecha: '2024-07-31'
          };
          this.items = [
            { nombre: 'Medicamento A', costo: 15, cantidad: 10, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Pública' },
            { nombre: 'Medicamento B', costo: 20, cantidad: 5, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Privada' }
          ];
        }
      }
    },
    handleSolicitudChange() {
      if (this.selectedSolicitudId) {
        this.selectedRecetaId = ''; // Limpiar la selección de receta
        if (this.selectedSolicitudId === '2') {
          this.solicitud = {
            Paciente_ID: '2',
            Medico_ID: 'M2',
            Servicio_ID: 'S2',
            Prioridad: 'Alta',
            Descripcion: 'Descripción de la solicitud 2',
            Estatus: 'En Proceso'
          };
          this.items = [
            { nombre: 'Utensilio X', costo: 20, cantidad: 15, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Mixta' },
            { nombre: 'Utensilio Y', costo: 15, cantidad: 8, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Pública' }
          ];
        } else {
          this.solicitud = {
            Paciente_ID: '1',
            Medico_ID: 'M1',
            Servicio_ID: 'S1',
            Prioridad: 'Normal',
            Descripcion: 'Descripción de la solicitud 1',
            Estatus: 'Registrada'
          };
          this.items = [
            { nombre: 'Utensilio A', costo: 25, cantidad: 10, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Pública' },
            { nombre: 'Utensilio B', costo: 30, cantidad: 5, entregado: 0, estatus: 'Parcialmente abastecida', tipo: 'Privada' }
          ];
        }
      }
    },
    updateEstatus(item) {
      item.estatus = item.entregado >= item.cantidad ? 'Abastecida' : 'Parcialmente abastecida';
    },
    updateTipo(item) {
      // Implementar lógica para actualizar tipo si es necesario
    },
    eliminarFila(index) {
      this.items.splice(index, 1);
    }
  }
};
</script>

<style>
.table-container {
  width: 100%;
  overflow: hidden;
  /* Elimina cualquier posible barra de desplazamiento */
}

.table-container table {
  width: 100%;
  border-collapse: collapse;
  table-layout: fixed;
  /* Ajusta el ancho de las columnas para evitar el desbordamiento */
}

.table-container th,
.table-container td {
  padding: 8px;
  text-align: left;
  overflow: hidden;
  /* Evita que el contenido de las celdas se desborde */
  text-overflow: ellipsis;
  /* Muestra "..." si el contenido es demasiado largo */
  white-space: nowrap;
  /* Previene el ajuste de línea */
}

.table-container th {
  background-color: #f3f4f6;
  /* Fondo claro para los encabezados */
  font-weight: bold;
}

.table-container td {
  background-color: #ffffff;
  /* Fondo blanco para las celdas */
}

.table-container td input {
  width: 100%;
  /* Hace que los campos de entrada se ajusten al tamaño de la celda */
  box-sizing: border-box;
  /* Asegura que el padding y el border se incluyan en el tamaño total del elemento */
}

.table-container td select {
  width: 100%;
  /* Hace que los campos de selección se ajusten al tamaño de la celda */
  box-sizing: border-box;
  /* Asegura que el padding y el border se incluyan en el tamaño total del elemento */
}

.total-cost {
  margin-top: 1.5rem;
  /* Espacio superior */
  text-align: center;
  background-color: #f3f4f6;
  /* Fondo claro */
  padding: 1rem;
  /* Espaciado interno */
  border-top: 1px solid #e5e7eb;
  /* Borde superior */
  font-weight: bold;
}

.delete-button {
  background-color: #ef4444;
  /* Color de fondo rojo */
  color: #ffffff;
  /* Color de texto blanco */
  border: none;
  padding: 0.5rem 1rem;
  /* Espaciado interno */
  border-radius: 0.375rem;
  /* Bordes redondeados */
  cursor: pointer;
}
</style>
