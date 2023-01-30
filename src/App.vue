<template>
  <FirstChart :labels="this.weekdays" :datasets="this.datasetWeekly"/>
</template>

<script>
import FirstChart from './components/FirstChart';
import MainDs from './components/Datasets.js'
export default {
  components: {
    FirstChart
  },
  data(){
    return {
      weekdays : MainDs.labels,
      datasetWeekly :  [{
                label: 'Gewicht',
                data: WeeklyDS.values
            }]
    }
  }
}
</script>
<style>
</style>
