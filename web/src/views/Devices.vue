<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <p class="display-1">Dispositivos</p>
      </v-col>
      <v-col cols="12" sm="6">
        <v-text-field
          v-model="search"
          append-icon="fa-magnify"
          label="Buscar"
        ></v-text-field>
      </v-col>
      <v-col cols="12" sm="6" class="text-center">
        <v-btn color="primary" @click="showDialog = true">
          Nuevo <v-icon x-small="">fa-plus</v-icon>
        </v-btn>
      </v-col>
      <v-col cols="12" style="position:relative">
        <v-data-table
          :headers="headers"
          :search="search"
          :items="devices"
          class="elevation-2"
          :loading="loading"
        >
          <template v-slot:item.details="{ item }">
            <v-btn
              color="secondary"
              :to="{ name: 'device', params: { id: item.id_device } }"
            >
              Detalles del dispositivo
            </v-btn>
          </template>
          <template v-slot:item.options="{ item }">
            <v-icon
              class="mr-5"
              @click=";(showDialogDelete = true), (selectedDevice = item)"
              >fa-trash</v-icon
            >
            <v-icon @click=";(showDialogEdit = true), (selectedDevice = item)"
              >fa-edit</v-icon
            >
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <DialogDevice v-model="showDialog" />
    <DialogEditDevice
      v-model="showDialogEdit"
      :device="selectedDevice"
      v-if="showDialogEdit"
      @update-devices="updateDevices"
    />
    <DialogPrompt
      v-model="showDialogDelete"
      @confirm="deleteDevice"
      title="¿Seguro que deseas eliminar este dispositivo?"
    />
  </v-container>
</template>

<script>
import DialogDevice from '@/components/DialogDevice.vue'
import DialogEditDevice from '@/components/DialogEditDevice.vue'
import DialogPrompt from '@/components/DialogPrompt.vue'
export default {
  components: {
    DialogDevice,
    DialogEditDevice,
    DialogPrompt
  },
  created() {
    this.updateDevices()
  },
  data() {
    return {
      headers: [
        {
          text: 'ID',
          value: 'id_device'
        },
        {
          text: 'Nombre',
          value: 'name'
        },
        {
          text: 'Detalles',
          value: 'details',
          sortable: false
        },
        {
          text: 'Opciones',
          value: 'options'
        }
      ],
      devices: [],
      loading: true,
      showDialog: false,
      showDialogEdit: false,
      showDialogDelete: false,
      search: '',
      selectedDevice: {}
    }
  },
  methods: {
    updateDevices() {
      this.loading = true
      this.$post('get_devices')
        .then(response => {
          this.devices = response.data.devices
        })
        .finally(() => (this.loading = false))
    },
    async deleteDevice() {
      this.loading = true
      const data = {
        id_device: this.selectedDevice.id_device
      }
      this.$post('delete_device', data)
        .then(() => {
          this.updateDevices()
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="scss" scoped></style>
