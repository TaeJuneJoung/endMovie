import { fetchMovieList, fetchMovieScore, fetchMovie } from '../api/index.js'
import { loginUser } from '../api/user.js'
import { fetchMovieComment } from '../api/comment.js'

export default {
	login({commit}, user) {
		loginUser(user)
			.then(({data}) => {
				commit('setUser', data)
			})
			.catch(error => {
				console.error(error)
			})
	},
	logout({commit}) {
		commit('setUser', '')
	},
	FetchMovies({commit}, username) {
		fetchMovieList()
			.then(({data}) => {
				if (username) {
					let movies = data
					fetchMovieScore(username)
						.then(({data}) => {
							let count = data.length
							for (let movie of movies) {
								for (let score of data) {
									if (movie.id === score.movie) {
										count = count - 1
										movie['score'] = score.star
										movie['scoreId'] = score.id
									}
									if (count == false) break
								}
							}
							commit('setMovieList', movies)
						})
						.catch(error => {
							console.error(error)
						})
				} else {
					commit('setMovieList', data)
				}
			})
			.catch(error => {
				console.error(error)
			})
	},
	FetchMovie({commit}, movieId) {
		fetchMovie(movieId)
			.then(({data}) => {
				commit('setMovie', data)
			})
			.catch(error => {
				console.error(error)
			})
	},
	FetchMovieComment({commit}, movieId) {
		fetchMovieComment(movieId)
			.then(({data}) => {
				commit('setComments', data)
			})
			.catch(error => {
				console.error(error)
			})
	}
}