<template>
  <div id="chart">
    <apexchart
      type="area"
      height="350"
      :options="chartOptions"
      :series="series"
    ></apexchart>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'

export default {
  props: {
    id_variable: {
      type: Number,
      required: true
    }
  },
  created() {
    this.fetchData()
  },
  components: {
    apexchart: VueApexCharts
  },
  data() {
    return {
      series: [],
      chartOptions: {
        chart: {
          type: 'area',
          stacked: false,
          height: 350,
          zoom: {
            type: 'x',
            enabled: true,
            autoScaleYaxis: true
          },
          toolbar: {
            autoSelected: 'zoom'
          }
        },
        dataLabels: {
          enabled: false
        },
        markers: {
          size: 0
        },
        title: {
          text: 'Prueba',
          align: 'left'
        },
        fill: {
          type: 'gradient',
          gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100]
          }
        },
        yaxis: {
          labels: {},
          title: {
            text: 'Valor'
          }
        },
        xaxis: {
          type: 'datetime'
        },
        tooltip: {
          shared: false,
          y: {
            formatter: function(val) {
              return (val / 1000000).toFixed(0)
            }
          }
        }
      }
    }
  },
  methods: {
    fetchData() {
      const data = {
        id_variable: this.id_variable,
        start: new Date('2020/01/01'),
        end: new Date('2021/01/01'),
        type: 'date',
        results: 100
      }
      this.$post('get_variable_data', data)
        .then(({ data }) => {
          const dataSeries = data.map(item => ({
            x: item.timestamp_data,
            y: item.value
          }))
          console.log(dataSeries)
          this.series = [
            {
              name: 'Prueba',
              data: dataSeries
            }
          ]
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="scss" scoped></style>
