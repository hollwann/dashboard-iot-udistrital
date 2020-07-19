<template>
  <v-app>
    <AppBar @show-side-bar="showSideBar = !showSideBar" />
    <SideBar v-model="showSideBar" />
    <v-content>
      <router-view />
      <Dialog />
    </v-content>
  </v-app>
</template>

<script>
import AppBar from '@/components/AppBar.vue'
import SideBar from '@/components/SideBar.vue'
import Dialog from '@/components/Dialog.vue'

export default {
  name: 'App',
  components: {
    AppBar,
    SideBar,
    Dialog
  },
  data() {
    return {
      showSideBar: false
    }
  }
}
</script>
