<script setup>
import MyChart from "./components/MyChart.vue"
</script>

<template>
<Suspense>
  <template #default>
    <MyChart />  
  </template>
  <template #fallback>
    <h1>Loading</h1>
  </template>
</Suspense>
</template>


