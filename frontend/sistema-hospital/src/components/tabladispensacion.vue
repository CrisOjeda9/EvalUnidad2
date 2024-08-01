<template>
    <div class="min-h-screen bg-gray-200 bg-opacity-100 flex-col justify-center py-5 sm:px-6 lg:px-8 px-6 bg-repeat">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <img class="mx-auto h-10 w-auto" src="https://www.svgrepo.com/show/301692/login.svg" alt="Workflow">
            <h2 class="mt-6 text-center text-3xl leading-9 font-extrabold text-gray-900">
                Dispensación de Medicamentos - Recetas
            </h2>
        </div>
        <a href="/dispensation"
            class="text-white bg-gradient-to-r from-cyan-400 via-cyan-500 to-cyan-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-cyan-300 dark:focus:ring-cyan-800 shadow-lg shadow-cyan-500/50 dark:shadow-lg dark:shadow-cyan-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
            Agregar +
        </a>

        <div class="relative overflow-x-auto shadow-md sm:rounded-lg mt-6">
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
                    <tr v-for="item in items" :key="item.id" class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="px-6 py-4">{{ item.id }}</td>
                        <td class="px-6 py-4">{{ item.recetaMedicaId || 'No Aplica' }}</td>
                        <td class="px-6 py-4">{{ item.personalMedicoId || 'No Aplica' }}</td>
                        <td class="px-6 py-4">{{ item.solicitudId || 'No Aplica' }}</td>
                        <td class="px-6 py-4">{{ item.estatus }}</td>
                        <td class="px-6 py-4">{{ item.tipo }}</td>
                        <td class="px-6 py-4">{{ item.totalMedicamentosEntregados }}</td>
                        <td class="px-6 py-4">{{ item.totalCosto.toFixed(2) }}</td>
                        <td class="px-6 py-4">{{ item.fechaRegistro }}</td>
                        <td class="px-6 py-4">{{ item.fechaActualizacion }}</td>
                        <td class="px-6 py-4 text-right">
                            <a href="#" @click.prevent="handleDelete(item.id)" class="font-medium text-red-600 hover:underline">Eliminar</a>
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
            items: [
                {
                    id: 1,
                    recetaMedicaId: 1001,
                    personalMedicoId: 2001,
                    solicitudId: null,
                    estatus: 'Abastecida',
                    tipo: 'Pública',
                    totalMedicamentosEntregados: 10,
                    totalCosto: 500.00,
                    fechaRegistro: '2024-07-30 10:00:00',
                    fechaActualizacion: '2024-07-31 14:00:00',
                },
                {
                    id: 2,
                    recetaMedicaId: 1002,
                    personalMedicoId: 2002,
                    solicitudId: null,
                    estatus: 'Parcialmente abastecida',
                    tipo: 'Privada',
                    totalMedicamentosEntregados: 5,
                    totalCosto: 250.00,
                    fechaRegistro: '2024-07-31 11:00:00',
                    fechaActualizacion: '2024-08-01 15:00:00',
                },
                {
                    id: 3,
                    recetaMedicaId: 1003,
                    personalMedicoId: 2003,
                    solicitudId: null,
                    estatus: 'Abastecida',
                    tipo: 'Mixta',
                    totalMedicamentosEntregados: 8,
                    totalCosto: 400.00,
                    fechaRegistro: '2024-08-01 09:00:00',
                    fechaActualizacion: '2024-08-02 16:00:00',
                },
            ]
        };
    },
    methods: {
        handleDelete(id) {
            // Aquí puedes hacer una solicitud al servidor para eliminar el registro.
            // Por ejemplo: axios.delete(`/api/dispensation/${id}`)
            // Para la simulación, eliminamos el elemento del array local.
            this.items = this.items.filter(item => item.id !== id);
        }
    }
};
</script>
