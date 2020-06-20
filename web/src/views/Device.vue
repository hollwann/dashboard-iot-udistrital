<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="8" offset-sm="2">
        <v-card>
          <v-card-title class="justify-center display-2">
            Información del dispositvo
          </v-card-title>
          <v-card-text>
            <p><b>Id:</b> {{ device.id }}</p>
            <p><b>Nombre:</b> {{ device.name }}</p>
            <p><b>Descripción:</b> {{ device.description }}</p>
            <p><b>Fecha de creación:</b> {{ device.creation }}</p>
            <p><b>API KEY:</b> {{ device.apiKey }}</p>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="12" style="position:relative" sm="8" offset-sm="2">
        <v-btn absolute fab bottom right color="primary" class="mt-5"
          ><v-icon>fa-plus</v-icon></v-btn
        >
        <p class="display-1 text-center">Variables del dispositivo</p>
        <v-data-table :headers="headers" :items="variables" class="elevation-2">
          <template v-slot:item.data="{ item }">
            <v-btn color="secondary" :to="{ name: 'variable-data' }">
              Datos
            </v-btn>
          </template>
          <template v-slot:item.options="{ item }">
            <v-icon class="mr-5">fa-trash</v-icon>
            <v-icon>fa-edit</v-icon>
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
          text: 'Tipo',
          value: 'type'
        },
        {
          text: 'Datos',
          value: 'data',
          sortable: false
        },
        {
          text: 'Fecha de ultimo dato',
          value: 'lastData'
        },
        {
          text: 'Opciones',
          value: 'options'
        }
      ],
      variables: [
        {
          id: 20303,
          name: 'Temperatura',
          type: 'numerico', //numero, texto, geo
          lastData: 'Hace una hora'
        },
        {
          id: 20304,
          name: 'Ubicación',
          type: 'geolocation', //numero, texto, geo
          lastData: 'Hace 3 minutos'
        }
      ],
      device: {
        id: '234',
        name: 'Dispositivo UD',
        creation: new Date(),
        description: 'Esta es la descripción de prueba para el dispositivo UD.',
        apiKey: 'iu435kjb534bl34lkbkl34bkl4nknkl'
      }
    }
  }
}
</script>

<style lang="scss" scoped></style>
