export default function () {
  return {
    //
    jwt: localStorage.getItem('t'),
    endpoints: {
      obtainJWT: '/api/token/',
      refreshJWT: '/api/token/refresh/'
    }
  }
}
