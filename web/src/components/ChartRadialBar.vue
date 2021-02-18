<template>
  <div id="chart">
    <apexchart
      type="radialBar"
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
          type: 'radialBar',
          offsetY: -20,
          sparkline: {
            enabled: true
          }
        },
        plotOptions: {
          radialBar: {
            startAngle: -90,
            endAngle: 90,
            track: {
              background: '#e7e7e7',
              strokeWidth: '97%',
              margin: 5, // margin is in pixels
              dropShadow: {
                enabled: true,
                top: 2,
                left: 0,
                color: '#999',
                opacity: 1,
                blur: 2
              }
            },
            dataLabels: {
              name: {
                show: false
              },
              value: {
                offsetY: -2,
                fontSize: '22px'
              }
            }
          }
        },
        grid: {
          padding: {
            top: -10
          }
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'light',
            shadeIntensity: 0.4,
            inverseColors: false,
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 50, 53, 91]
          }
        },
        labels: ['Average Results']
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
          this.series = [dataSeries[dataSeries.length - 1].y]
            
          
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="scss" scoped></style>
