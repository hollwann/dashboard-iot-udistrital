<template>
  <v-container fill-height>
    <v-row align="center" style="height:100%" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="justify-center">
            Ingreso
          </v-card-title>
          <v-card-text class="text-center">
            <v-text-field label="Correo electronico" />
            <v-text-field label="Contraseña" />
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn width="50%" color="primary" :to="{ name: 'dashboard' }"
              >Ingresar</v-btn
            >
          </v-card-actions>
          <v-card-text>
            <a href="">Olvidé la contraseña</a>
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
