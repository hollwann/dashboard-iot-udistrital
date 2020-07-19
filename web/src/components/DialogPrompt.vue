<template>
  <v-dialog width="400" v-model="showDialog">
    <v-card>
      <v-card-title>
        {{ title }}
      </v-card-title>
      <v-card-actions class="justify-center">
        <v-btn color="secondary" @click="showDialog = false">No</v-btn>
        <v-btn color="primary" @click="$emit('confirm'), (showDialog = false)"
          >Si</v-btn
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
    title: {
      type: String,
      required: true
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
  }
}
</script>

<style lang="scss" scoped></style>
