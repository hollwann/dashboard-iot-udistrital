<template>
  <v-navigation-drawer app v-if="user" v-model="showSideBar">
    <v-list-item two-line class="px-1">
      <v-list-item-avatar>
        <v-img v-html="getImage(user.email)"></v-img>
      </v-list-item-avatar>

      <v-list-item-content>
        <v-list-item-title>{{ user.name }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-divider></v-divider>

    <v-list dense nav>
      <v-list-item
        v-for="item in items"
        :key="item.title"
        exact
        :to="{ name: item.route }"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <template v-slot:append>
      <div class="pa-2">
        <v-btn width="100%" color="secondary" @click="logout"
          >Cerrar sesión</v-btn
        >
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import Avatars from '@dicebear/avatars'
import sprites from '@dicebear/avatars-identicon-sprites'

export default {
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      items: [
        {
          title: 'Dashboard',
          icon: 'fa-tachometer-alt',
          route: 'dashboard'
        },
        {
          title: 'Dispositivos',
          icon: 'fa-tablet',
          route: 'devices'
        },
        {
          title: 'Perfil',
          icon: 'fa-user',
          route: 'profile'
        },
        {
          title: 'Ayuda',
          icon: 'fa-question-circle',
          route: 'help'
        }
      ]
    }
  },
  computed: {
    showSideBar: {
      get() {
        return this.value
      },
      set(v) {
        this.$emit('input', v)
      }
    },
    ...mapState(['user'])
  },
  methods: {
    getImage(email) {
      let options = {}
      let avatars = new Avatars(sprites, options)
      return avatars.create(email)
    },
    logout() {
      this.userLogout()
    },
    ...mapActions(['userLogout'])
  }
}
</script>

<style lang="scss" scoped></style>
