<template>
  <v-col cols="12" sm="6">
		<iframe
			id="player"
			type="text/html"
			class="movie-video"
			:src="`http://www.youtube.com/embed/${video}`"
			allowfullscreen="allowfullscreen"
			mozallowfullscreen="mozallowfullscreen"
			msallowfullscreen="msallowfullscreen"
			oallowfullscreen="oallowfullscreen"
			webkitallowfullscreen="webkitallowfullscreen"
			frameborder="0"
		></iframe>
	</v-col>
</template>

<script>
export default {
	props: {
		video: ''
	}
}
</script>

<style>
.movie-video {
	height: 360px;
	width: 100%;
}
</style>