<template>
  <v-container fill-height>
    <v-row align="center" style="height:100%" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="justify-center">
            Registro
          </v-card-title>
          <v-card-text class="text-center">
            <v-text-field label="Nombre completo" />
            <v-text-field label="Correo electrónico" />
            <v-text-field label="Contraseña" />
            <v-text-field label="Confirmar contraseña" />
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn width="50%" color="primary" :to="{ name: 'login' }"
              >Registrarme</v-btn
            >
          </v-card-actions>
          <v-card-text>
            <router-link :to="{ name: 'login' }"
              >¿Ya tienes cuenta?, Ingresa aqui</router-link
            >
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped></style>
