<template>
  <v-hover v-slot:default="{ hover }">
    <v-card :class="`${{ 'on-hover': hover }} mx-auto grey darken-4`" :elevation="hover ? 12 : 2">
      <v-img :src="movie.poster" class="movie-poster">
        <v-expand-transition>
          <v-flex v-if="hover" class="transition-card white--text" @click.self="detail(movie.id)">
            <v-flex class="transition-card-title white--text title-shortly">{{ movie.title }}</v-flex>
            <v-flex class="transition-card-content" v-if="fetchedUser">
              <v-flex @click="createScore(movie.id, movie.score, movie.scoreId)">
              <v-rating
                v-model="rating"
                :value="movie.score"
                background-color="white"
                color="yellow accent-4"
                dense
                half-increments
                hover
                size="18"
              >
              </v-rating>
              </v-flex>
              <v-flex class="transition-card-favorite mt-5"><v-icon class="white--text">mdi-heart</v-icon></v-flex>
            </v-flex>
          </v-flex>
        </v-expand-transition>
      </v-img>
    </v-card>
  </v-hover>
</template>


<script>
import { mapGetters } from 'vuex'
import { postMovieScore, putMovieScore } from '../api/index.js'

export default {
  props: {
    movie: {}
  },
  data() {
    return {
      rating: this.movie.score
    };
  },
  computed: {
    ...mapGetters(['fetchedUser']),
  },
  methods: {
    /** createScore
     * param: 영화id, 현 사용자 평점, 평점id 
     */
    createScore(movieId, movieScore, movieScoreId) {
      if(movieScoreId) {
        /** putMovieScore
         * param: 영화평점id, 사용자id, 영화id, 평점
         */
        putMovieScore(movieScoreId, this.fetchedUser.id, movieId, this.rating)
          .then(({data}) => {
          })
          .catch(error => {
            console.error(error)
          })
      } else {
        /** postMovieScore
         * param: 사용자id, 영화id, 평점
         */
        postMovieScore(this.fetchedUser.id, movieId, this.rating)
          .then(response => {
          })
          .catch(error => {
            console.error(error)
          })
      }
    },
    detail(movieId) {
      this.$router.push(`/movies/${movieId}`)
    }
  }
};
</script>

<style scoped>
.title-shortly {
  font-weight: bold;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}
.movie-poster {
  height: 100%;
  max-height: 400px;
  min-height: 400px;
}
.transition-card {
  background-color: rgba(0, 0, 0, 0.7);
  height: 100%;
}
.transition-card-title {
	font-size: 18px;
	font-weight: bold;
	text-align: center;
	top: 20%;
  position: relative;
}
.transition-card-content {
  text-align: center;
  top: 45%;
  position: relative;
}
.transition-card-favorite {
	text-align: center;
	top: 55%;
  position: relative;
}
</style>
