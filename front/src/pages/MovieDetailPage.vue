<template>
	<v-container class="mt-10" :style="{backgroundImage: `url(${fetchedMovie.back_image})`}" style=" background-size: cover; background-repeat: no-repeat;">
		<v-row class="mx-3 mt-5">
			<!-- <v-col cols="12">
				{{ fetchedMovie }}

			</v-col> -->
			<v-col cols="12">
				<span class="title white--text">
					{{fetchedMovie.title}}
				</span>
			</v-col>
			<v-col cols="12">
				<span v-for="genre in fetchedMovie.genres" :key="genre.id">
					<v-btn x-small color="info " class="mr-1">{{ genre.genre_type }}</v-btn>
				</span>
			</v-col>
			<!-- <v-col cols="6">
				<v-img :src="fetchedMovie.back_image"></v-img>
			</v-col> -->
		</v-row>
	</v-container>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
	data() {
		return {
			movieId: this.$route.params.id
		}
	},
	mounted() {
		console.log(this.movieId)
		this.$store.dispatch('FetchMovie', this.movieId)
	},
	computed: {
		...mapGetters(['fetchedMovie']),
	}
}
</script>

<style scoped>
.col {
	padding: 0;
}
</style>