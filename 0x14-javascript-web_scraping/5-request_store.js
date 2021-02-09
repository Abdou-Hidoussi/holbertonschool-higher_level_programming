#!/usr/bin/node
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (error, url, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (error) => {
        if (error) {
          console.log(error);
        }
  })
}
