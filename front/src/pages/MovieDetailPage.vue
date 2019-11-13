<template>
  <v-container class="mt-10">
    <v-row class="mx-3 mt-5">
      <v-col cols="12">
        <span class="display-2">
          <strong>{{ fetchedMovie.title }}</strong>
          <small class="open-date">| {{fetchedMovie.open_date}}</small>
        </span>
      </v-col>
      <v-col cols="12">
        <span v-for="genre in fetchedMovie.genres" :key="genre.id">
          <v-btn x-small color="info " class="mr-1">{{ genre.genre_type }}</v-btn>
        </span>
      </v-col>
      <v-col cols="12" class="mt-3">
        <v-img :src="fetchedMovie.back_image"></v-img>
      </v-col>
      <v-row class="mt-3">
        <v-col cols="12" sm="6">
          <iframe
            id="player"
            type="text/html"
						class="movie-video"
            :src="`http://www.youtube.com/embed/${fetchedMovie.video}`"
            allowfullscreen="allowfullscreen"
            mozallowfullscreen="mozallowfullscreen"
            msallowfullscreen="msallowfullscreen"
            oallowfullscreen="oallowfullscreen"
            webkitallowfullscreen="webkitallowfullscreen"
            frameborder="0"
          ></iframe>
        </v-col>
        <v-col cols="12" sm="6">
          <v-flex class="content-line">내용</v-flex>
          {{ fetchedMovie.content }}
        </v-col>
      </v-row>
      <comment class="mt-5" :movieId="fetchedMovie.id"></comment>
			<comment-list class="mt-3"></comment-list>
    </v-row>
  </v-container>
</template>

<script>
import CommentList from '../components/CommentList.vue'
import Comment from '../components/Comment.vue'
import { mapGetters } from "vuex"

export default {
	components: {
    CommentList,
    Comment,
	},
  data() {
    return {
      movieId: this.$route.params.id
    };
  },
  mounted() {
    this.$store.dispatch("FetchMovie", this.movieId);
  },
  computed: {
    ...mapGetters(["fetchedMovie"])
  }
};
</script>

<style scoped>
.col {
  padding: 0;
}
.content-line {
  font-weight: bold;
  border-left: 5px solid #8bc34a;
  padding-left: 7px;
  margin-bottom: 10px;
}
.open-date {
  padding-left: 5px;
}
.movie-video {
	height: 360px;
	width: 100%;
}
</style>