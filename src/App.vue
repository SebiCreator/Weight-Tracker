
<script setup>
import {ref, shallowRef, computed, watch, nextTick} from 'vue'
import Chart from 'chart.js/auto'

const weights = ref([])
const weightChartEl = ref(null)
const weightChart = shallowRef(null)

const weightChartEl2 = ref(null)
const weightChart2 = shallowRef(null)

const weightInput = ref(0)

const currentWeight = computed(() => {
  return weights.value.sort((a,b) => b.date - a.date)[0] || { weight:0 }
})

const movingAverage =  (points,window) => {
  if (!points){
    return []
  }
  if (points.length == 1){
    return points[0].weight
  }
  let index = window - 1
  const len = points.length + 1
  const output = []
  while (++index < len){
    const windowSlice = points.slice(index-window,index)
    const sum = windowSlice.reduce((prev,curr) => prev + curr.weight, 0)
    output.push(sum / window)
  }
  if (output.length == 0){
    return points.reduce((prev,curr) => prev+curr.weight,0) / points.length
  }
  return output 
}

const addWeight = () => {
  weights.value.push({
    weight: weightInput.value,
    date: new Date().getTime()
  })
}

watch(weights, newWeights => {
  const ws = [...newWeights]
  console.log(movingAverage(ws,3))

  if (weightChart.value) {
    weightChart.value.data.labels = ws
      .sort((a,b) => a.date - b.date)
      .map(w => new Date(w.date).toLocaleDateString())
      .slice(-30)

    weightChart.value.data.datasets[0].data = ws
      .sort((a,b) => a.date - b.date)
      .map(w => w.weight)
      .slice(-30)

    weightChart.value.update()

  }

  if (weightChart2.value) {
    weightChart2.value.data.labels = ws
      .sort((a,b) => a.date - b.date)
      .map(w => new Date(w.date).toLocaleDateString())
      .slice(-7)

    weightChart2.value.data.datasets[0].data = ws
      .sort((a,b) => a.date - b.date)
      .map(w => w.weight)
      .slice(-7)
    
    weightChart2.value.update()

      return 
  }

  nextTick(() => {
    weightChart.value = new Chart(weightChartEl.value.getContext('2d'),{
      type: 'line',
      data: {
        labels: ws
        .sort((a,b) => a.date - b.date)
        .map(w => new Date(
          w.date
        ).toLocaleDateString()),
        datasets: [
          {
            label: 'weight1',
            data: ws
              .sort((a,b) => a.date - b.date)
              .map(w => w.weight),
            backgroundColor: 'rgba(55,255,255,0.4',
            borderColor: 'rgba(120,120,120,1)',
            borderWidth: 1,
            fill: true
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    })

  weightChart2.value = new Chart(weightChartEl2.value.getContext('2d'),{
      type: 'line',
      data: {
        labels: ws
        .sort((a,b) => a.date - b.date)
        .map(w => new Date(
          w.date
        ).toLocaleDateString()),
        datasets: [
          {
            label: 'weight',
            data: ws
              .sort((a,b) => a.date - b.date)
              .map(w => w.weight),
            backgroundColor: 'rgba(55,255,255,0.4',
            borderColor: 'rgba(120,120,120,1)',
            borderWidth: 1,
            fill: true
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    })
  })
},{deep:true})
</script>
<template>
<div>
  <h1>Weight Tracker</h1>
  <div class="current">
    <span>{{ currentWeight.weight }}</span>
    <small>Current weight in kg</small>
  </div>
  <form @submit.prevent="addWeight">
  <input type="number" step="0.1" v-model="weightInput"/>
  <input type="submit" value="Add weight"/>
  </form>
  <div v-if="weights && weights.length > 0">
    <h2>Last 30 days</h2>
    <div class="canvas-box">
      <canvas ref="weightChartEl"></canvas>
    </div>
    <h2>Last 7 days</h2>
    <div class="canvas-box2">
      <canvas ref="weightChartEl2"></canvas>
    </div>
    <div class="weight-history">
        <h2>Weight History</h2>
        <ul>
          <li v-for="weight in weights">
            <span>{{ weight.weight }}kg</span>
            <small>{{ new Date(weight.date).toLocaleDateString() }}</small>
          </li>
        </ul>
    </div>
  </div>
</div>

</template>
<style>
</style>
