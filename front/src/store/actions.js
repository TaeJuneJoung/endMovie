import { fetchMovieList } from '../api/index.js'

export default {
	FetchMovies({commit}) {
		fetchMovieList()
			.then(({data}) => {
				commit('setMovieList', data)
			})
			.catch(error => {
				console.error(error)
			})
	}
}