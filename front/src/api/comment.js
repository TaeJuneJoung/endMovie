import axios from 'axios'

const config = {
    baseUrl: 'http://127.0.0.1:8000/movies/'
}

function fetchMovieComment(movieId) {
    return axios.get(`${config.baseUrl}comments/${movieId}`)
}

function createComment(movieId, commentData) {
    return axios.post(`${config.baseUrl}comments/${movieId}`, commentData)
}

function commentLikes(commentId, userId) {
    return axios.patch(`${config.baseUrl}comment/${commentId}`, userId)
}

export {
    fetchMovieComment,
    createComment,
    commentLikes,
}