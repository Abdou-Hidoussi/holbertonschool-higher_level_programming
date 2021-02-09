#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, url, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    let count = {};
    for (const task of list) {
      if (task.completed === true) {
        if (task.userId in completed) { count[task.userId]++; }
      }
    }
    console.log(count);
  }
});
