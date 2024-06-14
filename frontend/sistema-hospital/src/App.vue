<script setup>
import { RouterLink, RouterView } from 'vue-router'
import foot from './components/footer.vue';
</script>

<template>

  <RouterView />
  <foot />

</template>

<style>
footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  background: white; /* Ajusta según tu diseño */
  z-index: 1000; /* Ajusta según la necesidad */
}
</style>

