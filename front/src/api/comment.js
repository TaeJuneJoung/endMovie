import axios from 'axios'

const config = {
    baseUrl: 'http://127.0.0.1:8000/movies/comments/'
}

function fetchMovieComment(movieId) {
    return axios.get(`${config.baseUrl}${movieId}`)
}

function createComment(movieId, commentData) {
    return axios.post(`${config.baseUrl}${movieId}`, commentData)
}

export {
    fetchMovieComment,
    createComment,
}