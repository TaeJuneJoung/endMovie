<template>
  <v-app>
    <header-toolbar></header-toolbar>
    <transition name="page">
      <router-view></router-view>
    </transition>
  </v-app>
</template>

<script>
import HeaderToolbar from './components/HeaderToolbar';
import MovieListPage from './pages/MovieListPage.vue';

export default {
  name: 'App',
  components: {
    HeaderToolbar,
    MovieListPage,
  },
  data: () => ({
    //
  }),
};
</script>

<style src="./assets/grid.css"></style>