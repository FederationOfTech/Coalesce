// No console.log() / setTimeout
// console.log = jest.fn(() => { throw new Error('Do not use console.log() in production') })
jest.setTimeout(1000)

global.Promise = require('promise')

// do this to make sure we don't get multiple hits from both webpacks when running SSR
setTimeout(()=>{
  // do nothing
}, 1)
