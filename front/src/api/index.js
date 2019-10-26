import axios from 'axios'

const config = {
	baseUrl: 'http://127.0.0.1:8000/'
}

function fetchMovieList() {
	return axios.get(`${config.baseUrl}movies/movies`)
}

function fetchMovieScore(username) {
	return axios.get(`${config.baseUrl}movies/scores/${username}`)
}

function postMovieScore(userId, movieId, score) {
	let data = {'user': userId, 'movie': movieId, 'star': score}
	return axios.post(`${config.baseUrl}movies/scores/${userId}/${movieId}`, data)
}

function putMovieScore(scoreId, userId, movieId, score) {
	let data = {'user': userId, 'movie': movieId, 'star': score}
	return axios.put(`${config.baseUrl}movies/score/${scoreId}`, data)
}

export {
	fetchMovieList,
	fetchMovieScore,
	postMovieScore,
	putMovieScore,
}