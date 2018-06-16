var path = require('path');
module.exports = {
  entry: './index.jsx',
  mode:'development',
  module: {
    rules: [{
      loader: 'babel-loader',
      query: {
        presets: ['env']
      },
      test: /\.js$/
    }, 
    {
      test: /\.css$/,
      use: [ 'style-loader', 'css-loader' ]
    },{
      exclude: /node_modules/,
      loader: 'eslint-loader',
      test: /\.js$/
    }, {
      exclude: /node_modules/,
      loader: 'babel-loader',
      query: {
        presets: ['env', 'react']
      },
      test: /\.jsx$/
    }, {
      exclude: /node_modules/,
      loader: 'eslint-loader',
      test: /\.jsx$/
    }]
  },
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist')
  }
};




