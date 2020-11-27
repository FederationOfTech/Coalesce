/* eslint-disable camelcase */

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
