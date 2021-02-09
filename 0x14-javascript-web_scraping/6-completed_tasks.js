#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, url, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    const count = {};
    for (const task of list) {
      if (task.completed === true) {
        if (task.userId in count) { count[task.userId]++; } else { count[task.userId] = 1; }
      }
    }
    console.log(count);
  }
});
