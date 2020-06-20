<template>
  <v-app-bar app color="primary" dark>
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
export default {}
</script>

<style lang="scss" scoped></style>
