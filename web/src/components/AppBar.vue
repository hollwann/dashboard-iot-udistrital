<template>
  <v-app-bar app color="primary" dark>
    <v-app-bar-nav-icon
      @click="$emit('show-side-bar')"
      v-if="user"
    ></v-app-bar-nav-icon>
    <v-toolbar-title>Dashboard IOT Udistrital</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn
      color="secondary"
      :to="{ name: 'sign-up' }"
      v-if="$route.name == 'login'"
      >Registrarse</v-btn
    >
  </v-app-bar>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: {
    ...mapState(['user'])
  }
}
</script>

<style lang="scss" scoped></style>
