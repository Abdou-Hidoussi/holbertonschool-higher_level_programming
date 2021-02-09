#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, url, body) {
  if (error) {
    console.log(error);
  } else {
    const list = JSON.parse(body);
    let count = 0;
    for (const task of list) {
      if (task.completed === true) {
        if (task.userId in completed) { completed[task.userId]++; }
      }
    }
    console.log(count);
  }
});
