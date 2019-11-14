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

/**
 * 이메일 인증
 * emailCheck
 * @param {*} email 
 */
function emailCheck(email) {
	return axios.get(`${config.baseUrl}emailcheck/${email}`)
}

/**
 * 회원가입
 * joinUser
 * @param {*} user 
 */
function joinUser(user) {
	return axios.post(`${config.baseUrl}users`, user)
}

/**
 * 아이디 중복확인
 * idCheck
 * @param {*} username 
 */
function idCheck(username) {
	return axios.post(`${config.baseUrl}idcheck`, username)
}

export {
	loginUser,
	emailCheck,
	joinUser,
	idCheck,
}