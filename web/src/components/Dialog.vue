<template>
  <v-dialog
    :value="dialog.show"
    persistent
    @click:outside="hideDialog()"
    width="400"
  >
    <v-card color="white">
      <v-card-text>
        <p class="black--text text-center title">{{ dialog.text }}</p>
      </v-card-text>
      <v-card-actions>
        <v-btn
          @click="hideDialog"
          color="primary"
          width="100%"
          elevation="0"
          large
        >
          Aceptar
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  computed: {
    ...mapState(['dialog'])
  },
  methods: {
    ...mapActions(['hideDialog'])
  }
}
</script>

<style scoped></style>
