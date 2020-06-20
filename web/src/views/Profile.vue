<template>
  <v-container fill-height>
    <v-row align="center" style="height:100%" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="justify-center">
            Perfil
          </v-card-title>
          <v-card-text class="text-center">
            <v-text-field label="Nombre completo" />
            <v-text-field label="Correo electrónico" />
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn width="50%" color="primary" :to="{ name: 'login' }"
              >Actualizar información</v-btn
            >
          </v-card-actions>
          <v-card-text class="text-center">
            <v-text-field label="Nuvea contraseña" />
            <v-text-field label="Confirmar nueva contraseña" />
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn width="50%" color="primary" :to="{ name: 'login' }"
              >Actualizar contraseña</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {}
</script>

<style lang="scss" scoped></style>
