<template>
  <v-app-bar :class="`${toolbarColor} toolbar-px`" dark dense app>
		<v-toolbar-title>
			<router-link to="/" class="white--text">EndMovie</router-link>
		</v-toolbar-title>
		<v-spacer></v-spacer>
		<v-btn text @click="logout" v-if="fetchedUser">로그아웃</v-btn>
		<template v-else>
			<v-btn text @click="join">회원가입</v-btn>
			<v-btn text @click="login">로그인</v-btn>
		</template>
  </v-app-bar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
	data() {
		return {
			toolbarColor: '',
			user: '',
		}
	},
	computed: {
		...mapGetters(['fetchedUser'])
	},
	mounted() {
		this.user = this.$store.state.user
		window.addEventListener('scroll', this.updateScroll)
	},
	methods: {
		updateScroll() {
			let scrollPostion = window.scrollY
			if (scrollPostion > 50) {
				this.toolbarColor = "toolbar-transition"
			} else {
				this.toolbarColor = "black--text"
			}
		},
		login() {
			this.$router.push('/login')
		},
		join() {
			this.$router.push('/join')
		},
		logout() {
			this.$store.dispatch('logout')
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
		padding: 0 75px 0 75px;
	}
}
@media screen and (min-width: 1024px) and (max-width: 1440px) {
	.toolbar-px {
		padding: 0 120px 0 120px;
	}
}
a {
	text-decoration: none;
}
</style>