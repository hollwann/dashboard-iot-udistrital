export const trace = a =>
  process.env.NODE_ENV == 'development' && console.log(a)
