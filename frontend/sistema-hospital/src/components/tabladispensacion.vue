<template>
    <div class="min-h-screen bg-gray-200 bg-opacity-100 flex-col justify-center py-5 sm:px-6 lg:px-8 px-6 bg-repeat">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
            <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
                Dispensación de Medicamentos
            </h2>
        </div>
        <a href="/dispensation"
            class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
            Agregar +
        </a>

        <!-- Formulario de búsqueda -->
        <form @submit.prevent class="flex items-center max-w-sm mx-auto mb-4">
            <label for="simple-search" class="sr-only">Search</label>
            <div class="relative w-full">
                <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm12 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm0 0V6a3 3 0 0 0-3-3H9m1.5-2-2 2 2 2"/>
                    </svg>
                </div>
                <input v-model="searchQuery" type="text" id="simple-search" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Search..." required />
            </div>
            <button type="submit" class="p-2.5 ms-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
                <span class="sr-only">Search</span>
            </button>
        </form>

        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">ID</th>
                        <th scope="col" class="px-6 py-3">Receta Médica ID</th>
                        <th scope="col" class="px-6 py-3">Personal Médico ID</th>
                        <th scope="col" class="px-6 py-3">Solicitud ID</th>
                        <th scope="col" class="px-6 py-3">Estatus</th>
                        <th scope="col" class="px-6 py-3">Tipo</th>
                        <th scope="col" class="px-6 py-3">Total Medicamentos Entregados</th>
                        <th scope="col" class="px-6 py-3">Total Costo</th>
                        <th scope="col" class="px-6 py-3">Fecha Registro</th>
                        <th scope="col" class="px-6 py-3">Fecha Actualización</th>
                        <th scope="col" class="px-6 py-3"><span class="sr-only">Eliminar</span></th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in filteredDispensaciones" :key="item.ID" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="px-6 py-4">{{ item.ID || 'No Aplica' }}</td>
                        <td class="px-6 py-4">{{ item.RecetaMedica_id || 'No Aplica' }}</td>
                        <td class="px-6 py-4">{{ item.PersonalMedico_id || 'No Aplica' }}</td>
                        <td class="px-6 py-4">{{ item.Solicitud_id || 'No Aplica' }}</td>
                        <td class="px-6 py-4">{{ item.Estatus || '' }}</td>
                        <td class="px-6 py-4">{{ item.Tipo || '' }}</td>
                        <td class="px-6 py-4">{{ item.TotalMedicamentosEntregados || 0 }}</td>
                        <td class="px-6 py-4">{{ (item.Total_costo || 0).toFixed(2) }}</td>
                        <td class="px-6 py-4">{{ formatDate(item.Fecha_registro) }}</td>
                        <td class="px-6 py-4">{{ formatDate(item.Fecha_actualizacion) }}</td>
                        <td class="px-6 py-4 text-right">
                            <a href="#" @click.prevent="handleDelete(item.ID)" class="font-medium text-red-600 hover:underline">Eliminar</a>
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
            dispensaciones: [],  // Lista de dispensaciones
            searchQuery: '',     // Modelo para la búsqueda
        };
    },
    computed: {
        filteredDispensaciones() {
            const query = this.searchQuery.toLowerCase();
            return this.dispensaciones.filter(item => {
                return (
                    (item.RecetaMedica_id || '').toString().toLowerCase().includes(query) ||
                    (item.PersonalMedico_id || '').toString().toLowerCase().includes(query) ||
                    (item.Solicitud_id || '').toString().toLowerCase().includes(query) ||
                    (item.Estatus || '').toLowerCase().includes(query) ||
                    (item.Tipo || '').toLowerCase().includes(query)
                );
            });
        }
    },
    methods: {
        async fetchDispensaciones() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/dispensaciones/');
                if (response.status === 200) {
                    this.dispensaciones = response.data;
                } else {
                    console.error('Error fetching dispensaciones: Unexpected response status', response.status);
                }
            } catch (error) {
                console.error('Error fetching dispensaciones:', error);
            }
        },
        async handleDelete(id) {
            try {
                const response = await axios.delete(`http://127.0.0.1:8000/dispensaciones/${id}`);
                if (response.status === 204) {
                    this.dispensaciones = this.dispensaciones.filter(item => item.ID !== id);
                } else {
                    console.error('Error deleting dispensacion: Unexpected response status', response.status);
                }
            } catch (error) {
                console.error('Error deleting dispensacion:', error);
            }
        },
        formatDate(dateString) {
            if (!dateString) return 'Invalid Date';
            const date = new Date(dateString);
            if (isNaN(date.getTime())) return 'Invalid Date';
            return date.toLocaleString(); // Puedes ajustar el formato si es necesario
        }
    },
    created() {
        this.fetchDispensaciones();  // Recuperar los datos al crear el componente
    }
};
</script>

<style scoped>
/* Puedes añadir estilos personalizados aquí */
</style>
