/* eslint-disable camelcase */
import jwt_decode from 'jwt-decode'

export function obtainToken (context, { username, password }) {
  const payload = {
    username: username,
    password: password
  }
  return new Promise((resolve, reject) => {
    this._vm.$axios.post(this.state.auth.endpoints.obtainJWT, payload)
      .then((response) => {
        this.commit('auth/updateToken', response.data)
        resolve(response)
      })
      .catch((error) => {
        reject(error)
      })
  })
}

export function refreshToken () {
  const payload = {
    refresh: this.state.jwt.refresh
  }
  this.$axios.post(this.state.endpoints.refreshJWT, payload)
    .then((response) => {
      const newToken = {
        refresh: this.state.jwt.refresh,
        access: response.data.access
      }
      this.commit('updateToken', newToken)
    })
}

export function inspectToken () {
  const token = this.state.jwt
  if (token) {
    const decoded = jwt_decode(token)
    const exp = decoded.exp
    const orig_iat = decoded.orig_iat

    if (exp - (Date.now() / 1000) < 1800 && (Date.now() / 1000) - orig_iat < 628200) {
      this.dispatch('refreshToken')
    } else if (exp - (Date.now() / 1000) < 1800) {
      // DO NOTHING, DO NOT REFRESH
    } else {
      // TODO: PROMPT USER TO RE-LOGIN, THIS ELSE CLAUSE COVERS THE CONDITION WHERE A TOKEN IS EXPIRED AS WELL
    }
  }
}
