import axios from 'axios'

const config = {
	baseUrl: 'http://127.0.0.1:8000/movies/'
}

function fetchMovieList() {
	return axios.get(`${config.baseUrl}movies`)
}

function fetchMovie(movieId) {
	return axios.get(`${config.baseUrl}movie/${movieId}`)
}

function fetchMovieScore(username) {
	return axios.get(`${config.baseUrl}scores/${username}`)
}

function postMovieScore(userId, movieId, score) {
	let data = {'user': userId, 'movie': movieId, 'star': score}
	return axios.post(`${config.baseUrl}scores/${userId}/${movieId}`, data)
}

function putMovieScore(scoreId, userId, movieId, score) {
	let data = {'user': userId, 'movie': movieId, 'star': score}
	return axios.put(`${config.baseUrl}score/${scoreId}`, data)
}

export {
	fetchMovieList,
	fetchMovie,
	fetchMovieScore,
	postMovieScore,
	putMovieScore,
}