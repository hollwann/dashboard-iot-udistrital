<template>
  <v-container>
    <v-row>
      <v-col cols="12" style="position:relative">
        <v-btn absolute bottom right color="primary" fab>
          <v-icon>fa-plus</v-icon>
        </v-btn>
        <p class="text-center display-3">Dispositivos</p>
        <v-data-table :headers="headers" :items="devices" class="elevation-2">
          <template v-slot:item.details="{ item }">
            <v-btn color="secondary" :to="{ name: 'device' }">
              Detalles del dispositivo
            </v-btn>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        {
          text: 'ID',
          value: 'id'
        },
        {
          text: 'Nombre',
          value: 'name'
        },
        {
          text: 'Variables',
          value: 'variables'
        },
        {
          text: 'Detalles',
          value: 'details',
          sortable: false
        }
      ],
      devices: [
        { id: '234', name: 'Dispositivo UD', variables: 2 },
        { id: '256', name: 'Dispositivo Soacha', variables: 3 }
      ]
    }
  }
}
</script>

<style lang="scss" scoped></style>
