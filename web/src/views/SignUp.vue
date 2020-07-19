<template>
  <v-container fill-height>
    <v-row align="center" style="height:100%" justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="justify-center">
            Registro
          </v-card-title>
          <v-card-text class="text-center">
            <v-form
              v-model="validForm"
              @keyup.native.enter="validForm && signUp()"
            >
              <v-text-field
                label="Nombre completo"
                v-model="name"
                :rules="[required]"
              />
              <v-text-field
                label="Correo electrónico"
                v-model="email"
                :rules="[required, validEmail]"
              />
              <v-text-field
                label="Contraseña"
                v-model="password"
                :rules="[required, validPassword]"
                type="password"
              />
              <v-text-field
                label="Confirmar contraseña"
                v-model="confirmPassowrd"
                type="password"
                :rules="[required, matchPassword, validPassword]"
              />
            </v-form>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn
              width="50%"
              color="primary"
              @click="signUp"
              :disabled="!validForm"
              :loading="loading"
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
import { mapActions } from 'vuex'
export default {
  data() {
    return {
      loading: false,
      validForm: false,
      name: '',
      email: '',
      password: '',
      confirmPassowrd: '',
      required: v => !!v || 'Este campo es requerido.',
      validEmail: v => /.+@.+/.test(v) || 'Digite un email válido.',
      validPassword: v =>
        v.length >= 7 || 'La contraseña debe tener mas de 7 caracteres',
      matchPassword: v =>
        v == this.password || 'Las contraseñas deben coincidir'
    }
  },
  methods: {
    async signUp() {
      this.loading = true
      const data = {
        name: this.name,
        email: this.email,
        password: this.password
      }
      const login = () =>
        this.$post('login', data)
          .then(({ data }) => {
            localStorage.setItem('token', data.token)
            this.userLogged()
          })
          .finally(() => (this.loading = false))

      this.$post('sign-up', data)
        .then(login)
        .catch(() => (this.loading = false))
    },
    ...mapActions(['userLogged'])
  }
}
</script>

<style lang="scss" scoped></style>
