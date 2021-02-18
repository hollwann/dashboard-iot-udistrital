<template>
  <v-container fluid>
    <div class="px-10 d-flex">
      <draggable
        v-model="charts"
        style="width:100%"
        class="d-flex flex-wrap"
        @end="changeOrderCharts"
      >
        <div
          style="width:50%;padding:10px"
          v-for="chart in charts"
          :key="chart.id_dashboard_chart"
        >
          <v-menu offset-y>
            <template v-slot:activator="{ on, attrs }">
              <v-btn icon v-on="on" v-bind="attrs"
                ><v-icon color="secondary">fa-ellipsis-h</v-icon></v-btn
              >
            </template>
            <v-list>
              <v-list-item>
                <v-list-item-title
                  @click="deleteChart(chart.id_dashboard_chart)"
                  >Eliminar</v-list-item-title
                >
              </v-list-item>
            </v-list>
          </v-menu>

          <ChartLine
            v-if="chart.chart_type == 'line'"
            :id_variable="chart.id_variable"
          />
          <ChartBar
            v-else-if="chart.chart_type == 'bar'"
            :id_variable="chart.id_variable"
          />
          <ChartRadialBar
            v-else-if="chart.chart_type == 'radial'"
            :id_variable="chart.id_variable"
          />
          <ChartMap
            v-else-if="chart.chart_type == 'map'"
            :id_variable="chart.id_variable"
          />
        </div>
        <div style="width:50%; padding:10px">
          <v-card
            height="350"
            class="fill-height d-flex justify-center align-center"
            v-if="!newChart"
          >
            <v-btn fab color="primary" @click="newChart = true"
              ><v-icon x-large>fa-plus</v-icon></v-btn
            >
          </v-card>
          <v-card
            height="350"
            v-else
            class="fill-height d-flex flex-column justify-center align-center py-5"
          >
            <span class="title">Nueva grafica</span>
            <v-select
              :items="devices"
              v-model="device"
              placeholder="Dispositivo"
            ></v-select>
            <v-select
              v-if="device"
              :items="variables"
              placeholder="Variable"
              v-model="variable"
            ></v-select>
            <v-select
              v-if="variable"
              :items="getChartTypes(variable)"
              v-model="chartType"
            ></v-select>
            <v-btn color="secondary" @click="addChart" :loading="loading"
              >Añadir</v-btn
            >
          </v-card>
        </div>
      </draggable>
    </div>
  </v-container>
</template>

<script>
import ChartLine from '@/components/ChartLine.vue'
import ChartBar from '@/components/ChartBar.vue'
import ChartMap from '@/components/ChartMap.vue'
import ChartRadialBar from '@/components/ChartRadialBar.vue'
import draggable from 'vuedraggable'

export default {
  components: { ChartLine, ChartBar, ChartMap, draggable, ChartRadialBar },
  created() {
    setInterval(() => this.fetchCharts(), 5000)
    this.fetchCharts()
    this.fetchDevices()
  },
  data() {
    return {
      newChart: false,
      charts: [],
      devices: [],
      variables: [],
      device: null,
      variable: null,
      chartType: null,
      loading: false
    }
  },
  watch: {
    device(newDevice) {
      this.fetchVariables(newDevice)
    }
  },
  methods: {
    deleteChart(id) {
      this.$post('delete_chart', { id_dashboard_chart: id }).then(
        this.fetchCharts
      )
    },
    changeOrderCharts() {
      const data = {
        charts_order: this.charts.map((chart, i) => {
          return {
            id_dashboard_chart: chart.id_dashboard_chart,
            index_order: i
          }
        })
      }
      this.$post('update_order_charts', data)
    },
    addChart() {
      const data = {
        id_variable: this.variable,
        chart_type: this.chartType
      }
      this.$post('create_chart', data).then(() => {
        this.newChart = false
        this.fetchCharts()
      })
    },
    getChartTypes(variableId) {
      const variableType = this.variables.find(
        variable => variable.value == variableId
      ).id_variable_type

      if (variableType == 1)
        return [
          { text: 'Lineas', value: 'line' },
          { text: 'Barras', value: 'bar' },
          { text: 'Radial', value: 'radial' }
        ]
      else return [{ text: 'Mapa', value: 'map' }]
    },
    fetchCharts() {
      this.$post('get_charts').then(response => {
        this.charts = response.data.charts
      })
    },
    fetchDevices() {
      this.$post('get_devices').then(response => {
        this.devices = response.data.devices.map(device => {
          return {
            value: device.id_device,
            text: device.name
          }
        })
      })
    },
    fetchVariables(id_device) {
      return this.$post('get_variables', { id_device: id_device }).then(
        response => {
          this.variables = response.data.variables.map(variable => {
            return {
              value: variable.id_variable,
              text: variable.name,
              id_variable_type: variable.id_variable_type
            }
          })
        }
      )
    }
  }
}
</script>

<style lang="scss" scoped></style>
