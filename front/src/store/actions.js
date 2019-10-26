import { fetchMovieList, fetchMovieScore } from '../api/index.js'

export default {
	FetchMovies({commit}) {
		fetchMovieList()
			.then(({data}) => {
				let username = 'admin'
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
}