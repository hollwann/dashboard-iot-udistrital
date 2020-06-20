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
        <v-data-table :headers="headers" :items="data"> </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      startDate: '',
      endDate: '',
      headers: [
        {
          text: 'Valor',
          value: 'value'
        },
        {
          text: 'Fecha y hora',
          value: 'timestamp'
        },
        {
          text: 'IP',
          value: 'ip'
        }
      ],
      data: [...Array(100)].map(() => ({
        value: Math.random(),
        timestamp: new Date(),
        ip: '127.0.0.1'
      }))
    }
  }
}
</script>

<style lang="scss" scoped></style>
