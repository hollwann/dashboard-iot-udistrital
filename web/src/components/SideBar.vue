<template>
  <v-navigation-drawer
    app
    mini-variant
    expand-on-hover
    v-if="!invalidRoutes.includes($route.name)"
  >
    <v-list-item two-line class="px-1">
      <v-list-item-avatar>
        <img :src="require('@/assets/profile.jpeg')" />
      </v-list-item-avatar>

      <v-list-item-content>
        <v-list-item-title>Victor Angulo</v-list-item-title>
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
        <v-btn width="100%" color="secondary" :to="{ name: 'login' }"
          >Cerrar sesión</v-btn
        >
      </div>
    </template>
  </v-navigation-drawer>
</template>

<script>
export default {
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
      ],
      invalidRoutes: ['login', 'sign-up']
    }
  }
}
</script>

<style lang="scss" scoped></style>
