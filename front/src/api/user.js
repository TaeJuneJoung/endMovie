import axios from 'axios'

const config = {
	baseUrl: 'http://127.0.0.1:8000/accounts/'
}

/**
 * 회원 로그인
 * loginUser
 * @param {*} user 
 */
function loginUser(user) {
	return axios.post(`${config.baseUrl}login`, user)
}

export {
	loginUser
}