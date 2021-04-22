export function updateToken (state, newToken) {
  localStorage.setItem('t', JSON.stringify(newToken))
  state.jwt = newToken
}

export function removeToken (state) {
  localStorage.removeItem('t')
  state.jwt = null
}
