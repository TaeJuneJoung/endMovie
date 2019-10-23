<template>
  <v-app-bar :class="`${toolbarColor} toolbar-px`" dark dense app>
		<v-toolbar-title class="white--text">EndMovie</v-toolbar-title>
		<v-spacer></v-spacer>
		<v-btn text>Login</v-btn>
  </v-app-bar>
</template>

<script>
export default {
	data() {
		return {
			toolbarColor: '',
		}
	},
	mounted() {
		window.addEventListener('scroll', this.updateScroll)
	},
	methods: {
		updateScroll() {
			let scrollPostion = window.scrollY
			if (scrollPostion > 50) {
				this.toolbarColor = "toolbar-transition"
			} else{
				this.toolbarColor = "black--text"
			}
		}
	},
	destroy() {
		window.removeEventListener('scroll', this.updateScroll)
	}
};
</script>

<style scoped>
#app .toolbar-transition {
	background-color: rgba(0, 0, 0, 0.4);
}
@media screen and (min-width: 768px) {
	.toolbar-px {
		padding: 0 150px 0 150px;
	}
}
</style>