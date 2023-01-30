<template>
    <div>
        <canvas id="myChart"></canvas>
    </div>
</template>

<style scoped>
div{
    width: 600px;
    height: 600px;
}
</style>
  
<script>
import Chart from 'chart.js/auto';
export default {
    props: {
        labels: Array,
        datasets: Array,

    },
    mounted(){
        const ctx = document.getElementById('myChart');
        const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: this.labels,
            datasets: this.datasets
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    myChart;
    }
}
  </script>