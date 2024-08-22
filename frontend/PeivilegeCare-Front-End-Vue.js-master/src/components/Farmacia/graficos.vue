<template>
    <div class="flex space-x-4">
      <!-- Tarjeta de Medicamentos (Estatus) -->
      <div class="max-w-sm w-full bg-white rounded-lg shadow dark:bg-gray-800 p-4 md:p-6">
        <div class="flex justify-between items-start w-full">
          <div class="flex-col items-center">
            <div class="flex items-center mb-1">
              <h5 class="text-xl font-bold leading-none text-gray-900 dark:text-white me-1">Medicamentos (Estatus)</h5>
            </div>
          </div>
  
          <div v-if="showDropdown" class="z-10 bg-white divide-y divide-gray-100 rounded-lg shadow w-80 lg:w-96 dark:bg-gray-700 dark:divide-gray-600">
            <div class="p-3" aria-labelledby="dateRangeButton">
              <div class="flex items-center">
                <div class="relative">
                  <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>
                    </svg>
                  </div>
                  <input v-model="startDate" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Start date">
                </div>
                <span class="mx-2 text-gray-500 dark:text-gray-400">to</span>
                <div class="relative">
                  <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>
                    </svg>
                  </div>
                  <input v-model="endDate" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="End date">
                </div>
              </div>
            </div>
          </div>
        </div>
    
        <div class="w-full mt-4">
          <canvas id="pieChart" class="w-full h-64"></canvas>
        </div>
      </div>
  
      <!-- Tarjeta de Tipo de Consumible -->
      <div class="max-w-sm w-full bg-white rounded-lg shadow dark:bg-gray-800 p-4 md:p-6">
        <div class="flex justify-between items-start w-full">
          <div class="flex-col items-center">
            <div class="flex items-center mb-1">
              <h5 class="text-xl font-bold leading-none text-gray-900 dark:text-white me-1">Tipo de Consumible</h5>
            </div>
          </div>
        </div>
    
        <div class="w-full mt-4">
          <canvas id="typeChart" class="w-full h-64"></canvas>
        </div>
      </div>
    </div>
  </template>
  
<script>
import { defineComponent, onMounted, ref } from 'vue';
import Chart from 'chart.js/auto';

export default defineComponent({
  name: 'ChartComponent',
  setup() {
    const showPopover = ref(false);
    const showDropdown = ref(false);
    const startDate = ref('');
    const endDate = ref('');
    const medicamentoEstatus = ref([]);
    const consumibleTipos = ref([]);

    const togglePopover = () => {
      showPopover.value = !showPopover.value;
    };

    const toggleDropdown = () => {
      showDropdown.value = !showDropdown.value;
    };

    const fetchMedicamentos = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/medicamentos/');
        const data = await response.json();
        medicamentoEstatus.value = data.map(medicamento => medicamento.Estatus);
      } catch (error) {
        console.error('Error fetching medicamentos:', error);
      }
    };

    const fetchConsumibles = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/consumibles/');
        const data = await response.json();
        consumibleTipos.value = data.map(consumible => consumible.Tipo);
      } catch (error) {
        console.error('Error fetching consumibles:', error);
      }
    };

    const getStatusCounts = () => {
      const activeCount = medicamentoEstatus.value.filter(status => status).length;
      const inactiveCount = medicamentoEstatus.value.length - activeCount;
      return { activeCount, inactiveCount };
    };

    const getTipoCounts = () => {
      const tipoCounts = { Material: 0, Equipo: 0, Instrumento: 0 };
      consumibleTipos.value.forEach(tipo => {
        if (tipo in tipoCounts) {
          tipoCounts[tipo]++;
        }
      });
      return tipoCounts;
    };

    onMounted(async () => {
      await fetchMedicamentos();
      await fetchConsumibles();

      const ctx1 = document.getElementById('pieChart');
      const ctx2 = document.getElementById('typeChart');

      if (ctx1) {
        const { activeCount, inactiveCount } = getStatusCounts();
        new Chart(ctx1, {
          type: 'pie',
          data: {
            labels: ['Activo', 'Inactivo'],
            datasets: [{
              label: 'Medicamentos (Estatus)',
              data: [activeCount, inactiveCount],
              backgroundColor: ['#36A2EB', '#FFCE56'],
              borderColor: ['#fff', '#fff'],
              borderWidth: 1,
            }],
          },
        });
      }

      if (ctx2) {
        const tipoCounts = getTipoCounts();
        new Chart(ctx2, {
          type: 'pie',
          data: {
            labels: ['Material', 'Equipo', 'Instrumento'],
            datasets: [{
              label: 'Consumibles (Tipo)',
              data: [tipoCounts.Material, tipoCounts.Equipo, tipoCounts.Instrumento],
              backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
              borderColor: ['#fff', '#fff', '#fff'],
              borderWidth: 1,
            }],
          },
        });
      }
    });

    return {
      showPopover,
      showDropdown,
      startDate,
      endDate,
      medicamentoEstatus,
      consumibleTipos,
      togglePopover,
      toggleDropdown,
    };
  },
});
</script>
  