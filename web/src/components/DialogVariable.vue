<template>
  <v-dialog width="400" v-model="showDialog">
    <v-card>
      <v-card-title class="justify-center">
        <p class="display-1">Nueva variable</p>
      </v-card-title>
      <v-card-text>
        <v-form v-model="validForm">
          <v-text-field
            label="Nombre de la variable"
            v-model="name"
            :rules="[required]"
          />
          <v-combobox
            auto-select-first
            :rules="[required]"
            :items="variableTypes"
            v-model="variableType"
          />
        </v-form>
      </v-card-text>
      <v-card-actions class="justify-center">
        <v-btn
          width="50%"
          color="primary"
          :loading="loading"
          :disabled="!validForm"
          @click="addVariable"
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
    },
    id_device: {
      required: true
    },
    variableTypes: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      validForm: false,
      loading: false,
      name: '',
      variableType: null,
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
    addVariable() {
      this.loading = true
      const data = {
        name: this.name,
        id_variable_type: this.variableType.value,
        id_device: this.id_device
      }
      console.log(data)
      this.$post('create_variable', data)
        .then(() => {
          this.showDialog = false
          this.$emit('update-variables')
        })
        .finally(() => (this.loading = false))
    }
  }
}
</script>

<style lang="scss" scoped></style>
