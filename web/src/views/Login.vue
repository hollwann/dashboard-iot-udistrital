<template>
  <v-container fill-height>
    <v-row align="center" style="height:100%" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="justify-center">
            Ingreso
          </v-card-title>
          <v-card-text class="text-center">
            <v-form
              v-model="validForm"
              @keyup.native.enter="validForm && login()"
            >
              <v-text-field
                label="Correo electronico"
                v-model="email"
                type="email"
                :rules="[required, validEmail]"
              />
              <v-text-field
                label="Contraseña"
                v-model="password"
                type="password"
                :rules="[required, validPassword]"
              />
            </v-form>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn
              width="50%"
              color="primary"
              :loading="loading"
              :disabled="!validForm"
              @click="login"
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
import { mapActions } from 'vuex'
export default {
  data() {
    return {
      validForm: false,
      loading: false,
      email: '',
      password: '',
      required: v => !!v || 'Este campo es requerido.',
      validEmail: v => /.+@.+/.test(v) || 'Digite un email válido.',
      validPassword: v =>
        v.length >= 7 || 'La contraseña debe tener mas de 7 caracteres'
    }
  },
  methods: {
    login() {
      this.loading = true
      const data = {
        name: this.name,
        email: this.email,
        password: this.password
      }

      this.$post('login', data)
        .then(({ data }) => {
          localStorage.setItem('token', data.token)
          this.userLogged()
        })
        .finally(() => (this.loading = false))
    },
    ...mapActions(['userLogged'])
  }
}
</script>

<style lang="scss" scoped></style>
