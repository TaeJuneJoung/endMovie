<template>
  <v-app>
    <header-toolbar></header-toolbar>

    <v-content>
      <movieList/>
    </v-content>
  </v-app>
</template>

<script>
import HeaderToolbar from './components/HeaderToolbar';
import MovieList from './pages/MovieList.vue';

export default {
  name: 'App',
  components: {
    HeaderToolbar,
    MovieList,
  },
  data: () => ({
    //
  }),
};
</script>
