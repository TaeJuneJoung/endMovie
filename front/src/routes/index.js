import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieListPage from '../pages/MovieListPage.vue'
import LoginPage from '../pages/LoginPage.vue'

Vue.use(VueRouter)

export const router = new VueRouter ({
	mode: 'history',
	routes: [
		{
			path: '/',
			redirect: 'movies'
		},
		{
			path: '/movies',
			component: MovieListPage
		},
		{
			path: '/login',
			component: LoginPage
		},
	]
})