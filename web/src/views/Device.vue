<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <v-card>
          <v-card-title class="justify-center display-2">
            Información del dispositvo
          </v-card-title>
          <v-card-text v-if="loading">
            <v-progress-circular
              indeterminate
              color="primary"
            ></v-progress-circular>
          </v-card-text>
          <v-card-text v-else>
            <p><b>Id:</b> {{ device.id_device }}</p>
            <p><b>Nombre:</b> {{ device.name }}</p>
            <p><b>Descripción:</b> {{ device.description }}</p>
            <p>
              <b>Fecha de creación:</b>
              {{ new Date(device.timestamp).toLocaleString() }}
            </p>
            <p><b>APIKEY Escritura:</b> {{ device.api_key_read }}</p>
            <p><b>APIKEY Lectura:</b> {{ device.api_key_write }}</p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" style="position:relative" sm="8" offset-sm="2">
        <v-btn
          absolute
          fab
          top
          right
          color="primary"
          class="mt-5"
          @click="showDialog = true"
          ><v-icon>fa-plus</v-icon></v-btn
        >
        <p class="display-1 text-center">Variables del dispositivo</p>
        <v-data-table
          :headers="headers"
          :items="variables"
          class="elevation-2"
          :loading="loading"
        >
          <template v-slot:item.data="{ item }">
            <v-btn color="secondary" :to="{ name: 'variable-data' }">
              Datos
            </v-btn>
          </template>
          <template v-slot:item.id_variable_type="{ item }">
            {{
              variableTypes.length > 0 &&
                variableTypes.find(v => v.value == item.id_variable_type).text
            }}
          </template>
          <template v-slot:item.options="{ item }">
            <v-icon class="mr-5">fa-trash</v-icon>
            <v-icon>fa-edit</v-icon>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <DialogVariable
      :id_device="id"
      :variableTypes="variableTypes"
      v-model="showDialog"
      @update-variables="updateVariables"
    />
  </v-container>
</template>

<script>
import DialogVariable from '@/components/DialogVariable.vue'
export default {
  components: {
    DialogVariable
  },
  props: {
    id: {
      required: true
    }
  },
  async created() {
    await this.$post('get_device', { id_device: this.id }).then(response => {
      this.device = response.data.device
    })
    await this.updateVariables()
    await this.getVariableTypes()
    this.loading = false
  },
  data() {
    return {
      headers: [
        {
          text: 'ID',
          value: 'id_variable'
        },
        {
          text: 'Nombre',
          value: 'name'
        },
        {
          text: 'Tipo',
          value: 'id_variable_type'
        },
        {
          text: 'Datos',
          value: 'data',
          sortable: false
        },
        {
          text: 'Opciones',
          value: 'options'
        }
      ],
      variables: [],
      device: {
        id_device: '',
        variables_number: '',
        name: '',
        timestamp: '',
        description: '',
        api_key_read: '',
        api_key_write: ''
      },
      loading: true,
      showDialog: false,
      variableTypes: []
    }
  },
  methods: {
    updateVariables() {
      return this.$post('get_variables', { id_device: this.id }).then(
        response => {
          this.variables = response.data.variables
        }
      )
    },
    getVariableTypes() {
      this.$post('get_variable_types', {}).then(response => {
        this.variableTypes = response.data.variable_types.map(variable => ({
          text: variable.name,
          value: variable.id_variable_type
        }))
      })
    }
  }
}
</script>

<style lang="scss" scoped></style>
