<template>
  <v-col cols="12">
	<v-flex class="comment-line">댓글</v-flex>
	<v-col cols="12" v-for="(comment, index) in fetchedComments" :key="index">
		<v-col cols="12" class="font-weight-bold">
			{{ comment.users.username }}
		</v-col>
		<v-col cols="12" class="mb-3">
			{{ comment.content }}
		</v-col>
		<v-col cols="12" class="mb-3">
			<small>{{ comment.update_at }}  | </small>
			<small class="error--text"><v-icon small color="error">mdi-alarm-light</v-icon>신고</small>
			<v-btn text small class="comment-good" @click="commentGood(comment.good_count)">
				<v-icon small>
					mdi-thumb-up-outline
				</v-icon>
				{{ comment.good_count }}
			</v-btn>
		</v-col>
		<v-divider class="my-3"></v-divider>
	</v-col>
</v-col>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
	computed: {
		...mapGetters(['fetchedComments'])
	},
	methods: {
		commentGood(goodCount) {
			console.log(goodCount)
		}
	}
}
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
</style>