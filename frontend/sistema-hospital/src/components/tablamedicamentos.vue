<template>
    <div class="min-h-screen bg-gray-200 bg-opacity-100  flex-col justify-center py-5 sm:px-6 lg:px-8 px-6 bg-repeat  "
        style="background-image: url(https://img.freepik.com/vector-premium/medicamentos-medicamentos-pildoras-botellas-elementos-medicos-cuidado-salud-patron-transparente-color-ilustracion-estilo-doodle-sobre-fondo-blanco_192280-30.jpg);">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
            <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
                Medicamentos
            </h2>
        </div>
        <div class="mt-6">




            <a href="/medicament"
                class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
                Agregar +
            </a>

        </div>

        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="px-6 py-3">
                            Cdigo
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Nombre Comercial
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Nombre Generico
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Via de Administracion
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Presentacion
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Tipo
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Volumen
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Cantidad
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Estatus
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Acciones
                        </th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="item in medicamentos" :key="item.id" :class="getRowClass(item)">
                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.codigo }}</span>
                            <input v-else v-model="item.codigo" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.nombreComercial }}</span>
                            <input v-else v-model="item.nombreComercial" type="text"
                                class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.nombreGenerico }}</span>
                            <input v-else v-model="item.nombreGenerico" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.viaAdministracion }}</span>
                            <input v-else v-model="item.viaAdministracion" type="text"
                                class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.presentacion }}</span>
                            <input v-else v-model="item.presentacion" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.tipo }}</span>
                            <input v-else v-model="item.tipo" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.volumen }}</span>
                            <input v-else v-model="item.volumen" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.cantidad }}</span>
                            <div v-else class="flex items-center">
                                <button @click="changeValue(item, 'cantidad', -1)"
                                    class="px-2 py-1 border rounded-l bg-gray-200 hover:bg-gray-300">-</button>
                                <input v-model.number="item.cantidad" type="number" min="0"
                                    class="w-20 px-2 py-1 border-t border-b text-center" />
                                <button @click="changeValue(item, 'cantidad', 1)"
                                    class="px-2 py-1 border rounded-r bg-gray-200 hover:bg-gray-300">+</button>
                            </div>
                        </td>

                        <td class="px-6 py-4" :class="{ 'w-1/8': item.editing }">
                            <span v-if="!item.editing">{{ item.estatus }}</span>
                            <input v-else v-model="item.estatus" type="text" class="w-full border p-1 rounded" />
                        </td>

                        <td class="px-6 py-4 text-center">
                            <a href="#" v-if="!item.editing" @click.prevent="editItem(item)"
                                class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                            <a href="#" v-if="!item.editing" @click.prevent="deleteItem(item.id)"
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
            medicamentos: [
                { id: 1, codigo: '001', nombreComercial: 'Ibuprofeno', nombreGenerico: 'Ibuprofeno', viaAdministracion: 'Oral', presentacion: 'Comprimidos', tipo: 'Antiinflamatorios', volumen: '200 mg', cantidad: 30, estatus: 'Activo', editing: false },
                { id: 2, codigo: '002', nombreComercial: 'Paracetamol', nombreGenerico: 'Paracetamol', viaAdministracion: 'Oral', presentacion: 'Grageas', tipo: 'Analgésicos', volumen: '500 mg', cantidad: 50, estatus: 'Activo', editing: false },
                { id: 3, codigo: '003', nombreComercial: 'Amoxicilina', nombreGenerico: 'Amoxicilina', viaAdministracion: 'Oral', presentacion: 'Cápsulas', tipo: 'Antibióticos', volumen: '250 mg', cantidad: 20, estatus: 'Inactivo', editing: false }
            ]
        };
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
            this.medicamentos = this.medicamentos.filter(item => item.id !== id);
        },
        changeValue(item, field, delta) {
            if (item.editing) {
                // Actualiza el valor del campo especificado con el incremento o decremento dado
                item[field] = Math.max(0, parseFloat((item[field] + delta).toFixed(2))); // Prevent negative values
            }
        }
    }
};
</script>
