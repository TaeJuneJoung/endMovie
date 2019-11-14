<template>
  <v-container>
    <v-row>
      <v-col
        v-for="i in fetchedMovieList.length >= limits ? limits : fetchedMovieList.length"
        :key="i"
        cols="12"
        lg="3"
        sm="4"
        xs="12"
      >
        <movie :movie="fetchedMovieList[i-1]"></movie>
      </v-col>
      <v-col cols="12" class="text-center">
        <v-btn class="w-60" dark @click="more">
          {{ isMore ? '더보기' : '모두 읽어왔습니다.' }}
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import Movie from "../components/Movie.vue";

export default {
  components: {
    Movie
  },
  data() {
    return {
      user: this.fetchedUser,
      limits: 28,
      isMore: true
    };
  },
  created() {
    this.$store.dispatch("FetchMovies", this.fetchedUser.username);
  },
  computed: {
    ...mapGetters(["fetchedUser"]),
    ...mapGetters(["fetchedMovieList"])
  },
  methods: {
    more() {
      if(this.limits > this.fetchedMovieList.length) {
        this.isMore = false
      } else {
        this.limits += 12;
      }
    }
  }
};
</script>

<style scoped>
.w-60 {
  width: 60%;
}
</style>