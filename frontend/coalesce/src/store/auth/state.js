export default function () {
  return {
    //
    jwt: JSON.parse(localStorage.getItem('t') || '{}'),
    endpoints: {
      obtainJWT: '/api/token/',
      refreshJWT: '/api/token/refresh/'
    }
  }
}
