#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2].toString();
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  for (const url of data.characters) {
    request(url, (err, resp, body) => {
      if (err) { console.log(err); }
      if (resp && resp.statusCode === 200) {
        console.log(JSON.parse(body).name);
      }
    });
  }
});
