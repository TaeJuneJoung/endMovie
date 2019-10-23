<template>
  <v-container>
    <v-row>
      <v-col v-for="movie in fetchedMovieList" :key="movie.id" cols="12" lg="3" sm="4" xs="12">
        <movie :movie="movie"></movie>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mapGetters} from 'vuex'
import Movie from '../components/Movie.vue'

export default {
  components: {
    Movie
  },
  data() {
    return {
      show: false,
    }
  },
  created() {
		this.$store.dispatch('FetchMovies')
  },
  computed: {
    ...mapGetters(['fetchedMovieList'])
  }
}
</script>

<style>

</style>