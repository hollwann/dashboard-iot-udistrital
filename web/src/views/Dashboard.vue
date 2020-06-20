<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6" style="position:relative">
        <DialChart />
        <Chart :height="300" :data="data" />
      </v-col>
      <v-col cols="12" md="6" style="position:relative">
        <DialChart />
        <Chart :height="300" :data="data" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Chart from '@/components/Chart.vue'
import DialChart from '@/components/DialChart.vue'
export default {
  components: { Chart, DialChart },
  data() {
    return {
      data: {
        labels: [...Array(10)].map((v, i) => i),
        datasets: [
          {
            label: 'Grafica test',
            data: [...Array(10)].map(() => Math.random()),
            borderWidth: 1
          }
        ]
      }
    }
  }
}
</script>

<style lang="scss" scoped></style>
