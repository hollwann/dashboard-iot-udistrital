<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <p class="display-3 text-center">Datos de la variable</p>
      </v-col>
      <v-col cols="6">
        <v-datetime-picker
          label="Fecha de inicio"
          v-model="startDate"
          clearText="Borrar"
          ><template slot="dateIcon">
            <v-icon>fas fa-calendar</v-icon>
          </template>
          <template slot="timeIcon">
            <v-icon>fas fa-clock</v-icon>
          </template></v-datetime-picker
        >
      </v-col>
      <v-col cols="6">
        <v-datetime-picker
          label="Fecha de inicio"
          v-model="endDate"
          clearText="Borrar"
          ><template slot="dateIcon">
            <v-icon>fas fa-calendar</v-icon>
          </template>
          <template slot="timeIcon">
            <v-icon>fas fa-clock</v-icon>
          </template></v-datetime-picker
        >
      </v-col>
      <v-col cols="12">
        <v-data-table
          single-expand
          :expanded.sync="expanded"
          :headers="headers"
          :items="data"
          :loading="loading"
          show-expand
        >
          <template v-slot:item.options="{ item }">
            {{ new Date(item.timestamp) }}
          </template>
          <template v-slot:expanded-item="{ item }">
            <pre :id="item.id_variable_data">{{ beautifier(item) }}</pre>
          </template>
          <template v-slot:item.map="{ item }">
            <a
              :href="
                `https://www.google.com/maps/search/?api=1&query=${item.value[0]},${item.value[1]}`
              "
              target="__blank"
              >Ver</a
            >
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: {
    id: {
      required: true
    }
  },
  created() {
    this.getVariable()
    this.updateData()
  },
  data() {
    return {
      expanded: [],
      loading: true,
      startDate: new Date('2020/01/01'),
      endDate: new Date('2021/01/01'),
      data: [],
      variable: null
    }
  },
  computed: {
    headers() {
      return this.variable && this.variable.id_variable_type == 1
        ? [
            {
              text: 'Valor',
              value: 'value'
            },
            {
              text: 'Fecha y hora',
              value: 'timestamp_data'
            },
            { text: '', value: 'data-table-expand' }
          ]
        : [
            {
              text: 'Valor',
              value: 'value'
            },
            {
              text: 'Fecha y hora',
              value: 'timestamp_data'
            },
            {
              text: 'Ver en mapa',
              value: 'map'
            },
            { text: '', value: 'data-table-expand' }
          ]
    }
  },
  methods: {
    beautifier(i) {
      const item = {
        ...i,
        meta_info: JSON.parse(i.meta_info.replace(/'/g, '"'))
      }
      return JSON.stringify(item, null, 4)
    },
    updateData() {
      const data = {
        id_variable: this.id,
        start: this.startDate,
        end: this.endDate,
        type: 'date',
        results: 100
      }
      this.$post('get_variable_data', data)
        .then(({ data }) => {
          this.data = data.map(item => ({
            ...item,
            value: JSON.parse(item.value),
            id: item.id_variable_data
          }))
        })
        .finally(() => (this.loading = false))
    },
    getVariable() {
      const data = {
        id_variable: this.id
      }
      this.$post('get_variable', data)
        .then(({ data }) => {
          this.variable = data
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="scss" scoped></style>
