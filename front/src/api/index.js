import axios from 'axios'

const config = {
	baseUrl: 'http://127.0.0.1:8000/'
}

function fetchMovieList() {
	return axios.get(`${config.baseUrl}movies/movies`)
}

export {
	fetchMovieList,
}