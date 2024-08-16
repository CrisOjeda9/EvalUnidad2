<template>
    <div class="min-h-screen bg-gray-200 bg-opacity-100 flex-col justify-center py-5 sm:px-6 lg:px-8 px-6"
        style="background-repeat: repeat;">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
            <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
                Consumibles
            </h2>
        </div>
        
        <!-- Formulario de búsqueda -->
        <form @submit.prevent="search" class="flex items-center max-w-sm mx-auto mb-6">
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

        <div class="mt-6">
            <a href="/consumibles"
                class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
                Agregar +
            </a>
        </div>

        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">ID</th>
                        <th scope="col" class="px-6 py-3">Nombre</th>
                        <th scope="col" class="px-6 py-3">Descripción</th>
                        <th scope="col" class="px-6 py-3">Cantidad</th>
                        <th scope="col" class="px-6 py-3">Tipo</th>
                        <th scope="col" class="px-6 py-3">Departamento ID</th>
                        <th scope="col" class="px-6 py-3">Estatus</th>
                        <th scope="col" class="px-6 py-3">Fecha Registro</th>
                        <th scope="col" class="px-6 py-3">Fecha Actualización</th>
                        <th scope="col" class="px-6 py-3">Observaciones</th>
                        <th scope="col" class="px-6 py-3">Espacio Médico</th>
                        <th scope="col" class="px-6 py-3">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in filteredConsumibles" :key="item.ID" :class="getRowClass(item)">
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.ID }}</span>
                            <input v-else v-model="item.ID" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Nombre }}</span>
                            <input v-else v-model="item.Nombre" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Descripcion }}</span>
                            <input v-else v-model="item.Descripcion" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Cantidad }}</span>
                            <div v-else class="flex items-center">
                                <button @click="changeValue(item, 'Cantidad', -1)"
                                    class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                                <input v-model.number="item.Cantidad" type="number" min="0"
                                    class="w-20 px-2 py-1 border-t border-b text-center" />
                                <button @click="changeValue(item, 'Cantidad', 1)"
                                    class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
                            </div>
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Tipo }}</span>
                            <input v-else v-model="item.Tipo" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Departamento_ID }}</span>
                            <input v-else v-model="item.Departamento_ID" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Estatus }}</span>
                            <input v-else v-model="item.Estatus" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Fecha_Registro }}</span>
                            <input v-else v-model="item.Fecha_Registro" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Fecha_Actualizacion }}</span>
                            <input v-else v-model="item.Fecha_Actualizacion" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Observaciones }}</span>
                            <input v-else v-model="item.Observaciones" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.Espacio_Medico }}</span>
                            <input v-else v-model="item.Espacio_Medico" type="text" class="w-full border p-1 rounded" />
                        </td>
                        <td class="px-6 py-4 text-center">
                            <a href="#" v-if="!item.editing" @click.prevent="editItem(item)"
                                class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                            <a href="#" v-if="!item.editing" @click.prevent="deleteItem(item.ID)"
                                class="font-medium text-red-600 dark:text-red-500 hover:underline ml-2">Eliminar</a>
                            <a href="#" v-if="item.editing" @click.prevent="saveItem(item)"
                                class="font-medium text-green-600 dark:text-green-500 hover:underline ml-2">Guardar</a>
                            <a href="#" v-if="item.editing" @click.prevent="cancelEdit(item)"
                                class="font-medium text-gray-600 dark:text-gray-500 hover:underline ml-2">Cancelar</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            searchQuery: '',
            consumibles: [
                { ID: 1, Nombre: 'Mascarillas', Descripcion: 'Mascarillas quirúrgicas', Cantidad: 100, Tipo: 'Protección', Departamento_ID: 2, Estatus: 'Activo', Fecha_Registro: '2024-01-01 10:00:00', Fecha_Actualizacion: '2024-01-01 10:00:00', Observaciones: 'Stock alto', Espacio_Medico: 'Área de emergencia', editing: false },
                { ID: 2, Nombre: 'Guantes', Descripcion: 'Guantes de nitrilo', Cantidad: 200, Tipo: 'Protección', Departamento_ID: 7, Estatus:'Activo',   Fecha_Registro: '2024-01-01 10:00:00', Fecha_Actualizacion: '2024-01-01 10:00:00', Observaciones: 'Stock alto', Espacio_Medico: 'Área de emergencia', editing: false },
                { ID: 3, Nombre: 'Desinfectante', Descripcion: 'Desinfectante de manos', Cantidad: 50, Tipo: 'Higiene', Departamento_ID: 4, Estatus: 'Inactivo', Fecha_Registro: '2024-03-01 12:00:00', Fecha_Actualizacion: '2024-03-01 12:00:00', Observaciones: 'Agotado', Espacio_Medico: 'Recepción', editing: false }
            ]
        };
    },
    computed: {
        filteredConsumibles() {
            const query = this.searchQuery.toLowerCase();
            return this.consumibles.filter(item => 
                item.Nombre.toLowerCase().includes(query) ||
                item.Descripcion.toLowerCase().includes(query) ||
                item.Tipo.toLowerCase().includes(query) ||
                item.Estatus.toLowerCase().includes(query) ||
                item.Fecha_Registro.toLowerCase().includes(query) ||
                item.Fecha_Actualizacion.toLowerCase().includes(query) ||
                item.Observaciones.toLowerCase().includes(query) ||
                item.Espacio_Medico.toLowerCase().includes(query)
            );
        }
    },
    methods: {
        getRowClass(item) {
            return {
                'odd:bg-white odd:dark:bg-gray-900': true,
                'even:bg-gray-50 even:dark:bg-gray-800': true,
                'border-b dark:border-gray-700': true,
                'bg-gray-200': item.editing // Highlight the row being edited
            };
        },
        editItem(item) {
            item.editing = true;
        },
        saveItem(item) {
            item.editing = false;
            // Aquí podrías añadir lógica para guardar los cambios si es necesario
        },
        cancelEdit(item) {
            item.editing = false;
            // Opcional: Restaurar el valor original si es necesario
        },
        deleteItem(id) {
            this.consumibles = this.consumibles.filter(item => item.ID !== id);
        },
        changeValue(item, field, delta) {
            if (item.editing) {
                // Actualiza el valor del campo especificado con el incremento o decremento dado
                item[field] = Math.max(0, parseFloat((item[field] + delta).toFixed(2))); // Prevent negative values
            }
        },
        search() {
            // No es necesario hacer nada especial aquí, ya que `filteredConsumibles` se actualiza automáticamente
        },
        clearSearch() {
            this.searchQuery = '';
        }
    }
};
</script>
