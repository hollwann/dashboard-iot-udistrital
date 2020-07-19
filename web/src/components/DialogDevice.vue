<template>
  <v-dialog width="400" v-model="showDialog">
    <v-card>
      <v-card-title class="justify-center">
        <p class="display-1">Nuevo dispositivo</p>
      </v-card-title>
      <v-card-text>
        <v-form v-model="validForm">
          <v-text-field
            label="Nombre del dispositivo"
            v-model="name"
            :rules="[required]"
          />
          <v-textarea
            label="Descripción"
            v-model="description"
            :rules="[required]"
          />
        </v-form>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn
          width="50%"
          color="primary"
          :loading="loading"
          :disabled="!validForm"
          @click="addDevice"
          >Añadir</v-btn
        >
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      validForm: false,
      loading: false,
      name: '',
      description: '',
      required: v => !!v || 'Este campo es requerido.'
    }
  },
  computed: {
    showDialog: {
      get() {
        return this.value
      },
      set(v) {
        this.$emit('input', v)
      }
    }
  },
  methods: {
    addDevice() {
      this.loading = true
      const data = {
        name: this.name,
        description: this.description
      }
      this.$post('create_device', data)
        .then(response => {
          this.showDialog = false
          this.$router.push({
            name: 'device',
            params: { id: response.data.id }
          })
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="scss" scoped></style>
