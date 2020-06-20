<template>
  <v-app>
    <AppBar />
    <SideBar />
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import AppBar from '@/components/AppBar.vue'
import SideBar from '@/components/SideBar.vue'
export default {
  name: 'App',
  components: {
    AppBar,
    SideBar
  }
}
</script>
