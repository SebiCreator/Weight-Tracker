
<script setup>
import {ref, shallowRef, computed, watch, nextTick} from 'vue'
import Chart from 'chart.js/auto'

const weights = ref([])
const weightChartEl = ref(null)
const weightChart = shallowRef(null)

const weightChartEl2 = ref(null)
const weightChart2 = shallowRef(null)

const avg = ref([])

const weightInput = ref(80.0)

const currentWeight = computed(() => {
  return weights.value.sort((a,b) => b.date - a.date)[0] || { weight:0 }
})


const addWeight = () => {
  weights.value.push({
    weight: weightInput.value,
    date: new Date().getTime()
  })
  avg.value.push({
    weight: 10
  })
}

watch(weights, newWeights => {
  const ws = [...newWeights]

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
            backgroundColor: 'rgba(130,220,140,0.7) ',
            borderColor: 'rgba(130,220,140) ',
            borderWidth: 1,
            fill: true,
            order:1
          },
          {
            label: 'moving average',
            type: "line",
            data: avg.value.map(w => w.weight),
            fill: false,
            order: 2
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
            backgroundColor: 'rgba(130,220,140) ',
            borderColor: 'rgba(130,220,140) ',
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
<div id="container">
  <h1>Weight Tracker</h1>
  <div class="current">
    <small>Current weight in kg</small>
    <span>{{ currentWeight.weight }}</span>
  </div>
  <form @submit.prevent="addWeight">
  <input id="weight-input" type="number" step="0.1" v-model="weightInput"/>
  <input id="weight-submit" type="submit" value="Add weight"/>
  </form>
  <div id="databox" v-if="weights && weights.length > 0">
    <h2>Last 30 days</h2>
    <div class="canvas-box">
      <canvas ref="weightChartEl"></canvas>
    </div>
    <h2>Last 7 days</h2>
    <div class="canvas-box">
      <canvas ref="weightChartEl2"></canvas>
    </div>
    <div class="weight-history">
        <h2>Weight History</h2>
        <ul>
          <li v-for="weight in weights">
            <small>{{ new Date(weight.date).toLocaleDateString() }}</small>
            <span>{{ weight.weight }}kg</span>
          </li>
        </ul>
    </div>
  </div>
</div>

</template>
<style>
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@700&display=swap');
* {
  margin: 0;
  padding: 0;
}
body {
  background: rgb(253,253,245);
}
#container {
  font-family: 'Ubuntu', sans-serif;
  border: solid lightgreen 2px;
  border-radius: 1rem;
  display: flex;
  flex-direction: column;
  text-align: center;
  margin: 1rem 2rem;
  padding: 1rem;
  background: white;
}
h1 {
  border: solid gray 0.5px;
  padding: 0.2rem 0.4rem;
  border-radius: 0.3rem;
  margin: 1rem auto;
}
.current {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
}
.current small, .current  span {
  font-size: large;
  margin: 0.4rem;
}
form {
  display: flex;
  flex-direction: column;
  margin: 0 auto;
  margin-top: 2rem;;
  border: solid black 1px;
  padding: 1rem;
  border-radius: 1.3rem;
}

#weight-input {
  text-align: center;
  font-family: 'Ubuntu';
  font-size: large;
  margin: 0 auto;
  border-radius: 4rem;
  padding: 0.4rem;
  width: 50%;
  border: solid rgba(130,220,140) 2px;
}

#weight-submit {
  font-family: 'Ubuntu';
  font-size: large;
  margin: 0 auto;
  margin-top: 2rem;
  padding: 0.7rem;
  border: solid lightgreen 2px;
  border-radius: 1rem;;
  background: white;
}

#weight-submit:hover {
  text-decoration: underline;
  border : solid rgba(130,220,140) 2px;
  cursor: pointer;
}

#databox{
  margin-top: 4rem;
}

.canvas-box {
  width: 95%;
  padding: 1rem;
}

.canvas-box h2 {
  margin-bottom: 2rem;;
}

.weight-history {
  margin-bottom: 2rem;
}

.weight-history h2 {
  margin-top: 3rem;
  margin-bottom: 2rem;
}
.weight-history ul {
  list-style-type: none;
  display: flex;
  flex-direction: column;
}

.weight-history li {
  text-align: center;
  margin: 0 auto;
  padding: 1rem 2rem;
  border-radius: 1rem;
  border: solid lightgreen 1px;
  margin-bottom: 0.1rem;
}

.weight-history small {
  font-size: medium;
  margin-right: 1rem;
}

</style>
