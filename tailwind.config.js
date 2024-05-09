/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ 
      './main/templates/main/parts/*.html',
      './main/templates/main/views/*.html'
    ],
  theme: {
    extend: {
      colors : {
        'button' : '#E9AB10',
      }
    },
  },
  plugins: [],
}

