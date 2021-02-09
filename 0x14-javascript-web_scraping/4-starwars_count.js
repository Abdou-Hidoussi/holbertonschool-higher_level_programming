#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, url, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body).results;
    let count = 0;
    for (const film of list) {
      for (const ch of film.characters) {
        if (ch.search('/18/') > 0) { count++; }
      }
    }
    console.log(count);
  }
});
