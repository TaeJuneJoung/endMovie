<template>
  <v-row>
    <v-col cols="12">
			<v-text-field
				v-model="comment"
				type="text"
				:label="fetchedUser ? '댓글을 작성해주세요.' : '댓글을 작성하려면 로그인 해주세요'"
				solo
				flat
				outlined
				counter="100"
				:disabled="!fetchedUser"
				:dark="!fetchedUser"
				@keyup.enter="createComment"
			>
			<v-btn slot="append" v-if="fetchedUser" color="success" @click="createComment">
				등록
			</v-btn>
			</v-text-field>
    </v-col>
  </v-row>
</template>

<script>
import { createComment } from '../api/comment.js'
import { mapGetters } from 'vuex'

export default {
	props: {
		movieId: 0
	},
	data() {
		return {
			comment: '',
		}
	},
	computed: {
		...mapGetters(['fetchedUser'])
	},
	methods: {
		createComment() {
			if(this.comment.length > 0) {
				const commentData = {user: this.fetchedUser.id, movie: this.movieId, content: this.comment}
				this.comment = ''
				createComment(this.movieId, commentData)
					.then(({data}) => {
						this.$store.dispatch('FetchMovieComment', this.movieId)
					})
					.catch(error => {
						console.error(error)
					})
			}
		}
	}
};
</script>

<style scoped>
</style>