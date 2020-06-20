<template>
  <v-speed-dial v-model="showDial" top left direction="bottom" absolute>
    <template v-slot:activator>
      <v-btn v-model="showDial" color="blue darken-2" dark fab>
        <v-icon v-if="showDial">fa-times</v-icon>
        <v-icon v-else>fa-pencil-alt</v-icon>
      </v-btn>
    </template>
    <v-btn fab dark small color="green">
      <v-icon>fa-pencil-alt</v-icon>
    </v-btn>
    <v-btn fab dark small color="indigo">
      <v-icon>fa-trash</v-icon>
    </v-btn>
  </v-speed-dial>
</template>

<script>
export default {
  data() {
    return {
      showDial: false
    }
  }
}
</script>

<style lang="scss" scoped></style>
