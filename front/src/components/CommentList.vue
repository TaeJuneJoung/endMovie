<template>
  <v-col cols="12">
    <v-flex class="comment-line">댓글</v-flex>
    <v-col
      cols="12"
      v-for="idx in fetchedComments.length >= limits ? limits : fetchedComments.length "
      :key="idx"
    >
      <v-col
        cols="12"
        class="font-weight-bold"
        :class="fetchedUser.id === fetchedComments[idx-1].users.id ? 'info--text': ''"
      >{{ fetchedComments[idx-1].users.username }}</v-col>
      <v-col cols="12" class="mb-3">{{ fetchedComments[idx-1].content }}</v-col>
      <v-col cols="12" class="mb-3">
        <small>{{ fetchedComments[idx-1].update_at }} |</small>
        <small class="error--text">
          <v-icon small color="error">mdi-alarm-light</v-icon>신고
        </small>
        <v-btn
          text
          small
          class="comment-good"
          @click="commentGood(fetchedComments[idx-1].id)"
          :color="fetchedComments[idx-1].goods.indexOf(fetchedUser.id) == -1 ? '':'info'"
        >
          <v-icon small>mdi-thumb-up-outline</v-icon>
          {{ fetchedComments[idx-1].goods.length }}
        </v-btn>
      </v-col>
      <v-divider class="my-3"></v-divider>
    </v-col>
	<v-col cols="12" class="text-center">
		<v-btn class="w-80" dark @click="more">{{ isMore ? '더보기' : '모두 읽어왔습니다.' }}</v-btn>
	</v-col>
  </v-col>
</template>

<script>
import { mapGetters } from "vuex";
import { commentLikes } from "../api/comment.js";

export default {
  props: {
    movieId: 0
  },
  data() {
    return {
      limits: 10,
      isMore: true
    };
  },
  computed: {
    ...mapGetters(["fetchedUser"]),
    ...mapGetters(["fetchedComments"])
  },
  methods: {
    commentGood(commentId) {
      if (this.fetchedUser.id) {
        const userId = { userId: this.fetchedUser.id };
        commentLikes(commentId, userId)
          .then(({ data }) => {
            this.$store.dispatch("FetchMovieComment", this.movieId);
          })
          .catch(error => {
            console.error(error);
          });
      }
	},
	more() {
		if(this.limits < this.fetchedComments.length) {
			this.limits += 5
    } else {
      this.isMore = false
    }
	}
  }
};
</script>

<style scoped>
.col {
  padding: 0;
}
.comment-line {
  font-weight: bold;
  border-left: 5px solid #8bc34a;
  padding-left: 7px;
  margin-bottom: 10px;
}
.comment-good {
  float: right;
}
.w-80 {
	width: 80%;
}
</style>