<template>
    <div class="min-h-screen bg-gray-200 flex-col justify-center py-5 sm:px-6 lg:px-8 px-6 bg-repeat">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
            <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
                Medicamentos
            </h2>
        </div>
        
        <!-- Formulario de búsqueda -->
        <form class="flex items-center max-w-sm mx-auto mb-6">
            <label for="simple-search" class="sr-only">Search</label>
            <div class="relative w-full">
                <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 20">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5v10M3 5a2 2 0 1 0 0-4 2 2 0 0 0 0 4Zm0 10a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm12 0a2 2 0 1 0 0 4 2 2 0 0 0 0-4Zm0 0V6a3 3 0 0 0-3-3H9m1.5-2-2 2 2 2"/>
                    </svg>
                </div>
                <input type="text" id="simple-search" v-model="searchQuery" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Buscar..." required />
            </div>
            <button type="button" @click="clearSearch" class="p-2.5 ms-2 text-sm font-medium text-white bg-blue-700 rounded-lg border border-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                <svg class="w-4 h-4" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"/>
                </svg>
                <span class="sr-only">Clear Search</span>
            </button>
        </form>

        <div class="mt-6">
            <a href="/medicament"
                class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
                Agregar +
            </a>
        </div>

        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6 bg-white">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">Código</th>
                        <th scope="col" class="px-6 py-3">Nombre Comercial</th>
                        <th scope="col" class="px-6 py-3">Nombre Genérico</th>
                        <th scope="col" class="px-6 py-3">Vía de Administración</th>
                        <th scope="col" class="px-6 py-3">Presentación</th>
                        <th scope="col" class="px-6 py-3">Tipo</th>
                        <th scope="col" class="px-6 py-3">Volumen</th>
                        <th scope="col" class="px-6 py-3">Cantidad</th>
                        <th scope="col" class="px-6 py-3">Estatus</th>
                        <th scope="col" class="px-6 py-3">Acciones</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="item in filteredMedicamentos" :key="item.ID" :class="getRowClass(item)">
                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.ID }}</span>
                            <input v-else v-model="item.ID" type="text" class="w-full border p-1 rounded" readonly />
                        </td>

                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.Nombre_comercial }}</span>
                            <input v-else v-model="item.Nombre_comercial" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.Nombre_generico }}</span>
                            <input v-else v-model="item.Nombre_generico" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.Via_administracion }}</span>
                            <select v-else v-model="item.Via_administracion" class="w-full px-2 py-1 border rounded">
                                <option value="" disabled>Selecciona vía</option>
                                <option value="Oral">Oral</option>
                                <option value="Intravenoso">Intravenoso</option>
                                <option value="Rectal">Rectal</option>
                                <option value="Cutáneo">Cutáneo</option>
                                <option value="Subcutáneo">Subcutáneo</option>
                                <option value="Oftálmica">Oftálmica</option>
                                <option value="Ótica">Ótica</option>
                                <option value="Nasal">Nasal</option>
                                <option value="Tópica">Tópica</option>
                                <option value="Parenteral">Parenteral</option>
                            </select>
                        </td>

                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.Presentacion }}</span>
                            <select v-else v-model="item.Presentacion" class="w-full px-2 py-1 border rounded">
                                <option value="" disabled>Selecciona presentación</option>
                                <option value="Comprimidos">Comprimidos</option>
                                <option value="Grageas">Grageas</option>
                                <option value="Cápsulas">Cápsulas</option>
                                <option value="Jarabes">Jarabes</option>
                                <option value="Gotas">Gotas</option>
                                <option value="Solución">Solución</option>
                                <option value="Pomada">Pomada</option>
                                <option value="Jabón">Jabón</option>
                                <option value="Supositorios">Supositorios</option>
                                <option value="Viales">Viales</option>
                            </select>
                        </td>

                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.Tipo }}</span>
                            <select v-else v-model="item.Tipo" class="w-full px-2 py-1 border rounded">
                                <option value="" disabled>Selecciona tipo</option>
                                <option value="Analgésicos">Analgésicos</option>
                                <option value="Antibióticos">Antibióticos</option>
                                <option value="Antidepresivos">Antidepresivos</option>
                                <option value="Antihistamínicos">Antihistamínicos</option>
                                <option value="Antiinflamatorios">Antiinflamatorios</option>
                                <option value="Antipsicóticos">Antipsicóticos</option>
                            </select>
                        </td>

                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.Volumen }}</span>
                            <input v-else v-model.number="item.Volumen" type="number" step="0.01" min="0"
                                class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4">
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

                        <td class="px-6 py-4">
                            <span v-if="!item.editing">{{ item.Estatus ? 'Activo' : 'Inactivo' }}</span>
                            <select v-else v-model="item.Estatus" class="w-full px-2 py-1 border rounded">
                                <option :value="true" selected>Activo</option>
                                <option :value="false">Inactivo</option>
                            </select>
                        </td>

                        <td class="px-6 py-4 text-center">
                            <a href="#" v-if="!item.editing" @click.prevent="editItem(item)"
                                class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                            <a href="#" v-if="!item.editing" @click.prevent="deleteItem(item.ID)"
                                class="font-medium text-red-600 dark:text-red-500 hover:underline"> Eliminar</a>
                            <a href="#" v-if="item.editing" @click.prevent="saveItem(item)"
                                class="font-medium text-green-600 dark:text-green-500 hover:underline">Guardar</a>
                            <a href="#" v-if="item.editing" @click.prevent="cancelEdit(item)"
                                class="font-medium text-gray-600 dark:text-gray-500 hover:underline">Cancelar</a>
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
            medicamentos: [],
            originalData: [],
            searchQuery: '', // Modelo para la búsqueda
        };
    },
    computed: {
        filteredMedicamentos() {
            const query = this.searchQuery.toLowerCase();
            return this.medicamentos.filter(item => {
                return (
                    item.Nombre_comercial.toLowerCase().includes(query) ||
                    item.Nombre_generico.toLowerCase().includes(query) ||
                    item.Via_administracion.toLowerCase().includes(query) ||
                    item.Presentacion.toLowerCase().includes(query) ||
                    item.Tipo.toLowerCase().includes(query) ||
                    (item.Estatus ? 'Activo' : 'Inactivo').toLowerCase().includes(query)
                );
            });
        }
    },
    methods: {
        async fetchMedicamentos() {
            try {
                const response = await fetch('http://localhost:8000/medicamentos');
                const data = await response.json();
                this.medicamentos = data;
                this.originalData = JSON.parse(JSON.stringify(data)); // Guardar una copia para cancelar ediciones
            } catch (error) {
                console.error('Error fetching medicamentos:', error);
            }
        },
        async editItem(item) {
            item.editing = true;
        },
        async cancelEdit(item) {
            // Restaurar datos originales para cancelar cambios
            const originalItem = this.originalData.find(i => i.ID === item.ID);
            Object.assign(item, originalItem);
            item.editing = false;
        },
        async saveItem(item) {
            try {
                const response = await fetch(`http://localhost:8000/medicamento/${item.ID}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(item),
                });

                if (response.ok) {
                    item.editing = false;
                    this.fetchMedicamentos(); // Recargar datos para reflejar los cambios
                } else {
                    console.error('Error saving item');
                }
            } catch (error) {
                console.error('Error saving item:', error);
            }
        },
        async deleteItem(id) {
            try {
                const response = await fetch(`http://localhost:8000/medicamentos/${id}`, {
                    method: 'DELETE',
                });

                if (response.ok) {
                    this.fetchMedicamentos(); // Recargar datos después de eliminar
                } else {
                    console.error('Error deleting item');
                }
            } catch (error) {
                console.error('Error deleting item:', error);
            }
        },
        changeValue(item, field, delta) {
            item[field] = Math.max((item[field] || 0) + delta, 0); // Evitar valores negativos
        },
        getRowClass(item) {
            return item.editing ? 'bg-gray-100' : '';
        },
        clearSearch() {
            this.searchQuery = '';
        }
    },
    created() {
        this.fetchMedicamentos();
    },
};
</script>
