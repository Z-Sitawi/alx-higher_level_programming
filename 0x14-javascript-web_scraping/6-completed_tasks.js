#!/usr/bin/node
/*  computes the number of tasks completed by user id. */
if (process.argv.length > 2) {
  const url = process.argv[2];
  const request = require('request');
  request(url, function (error, response) {
    if (error) {
      console.log(error);
    } else {
      const body = JSON.parse(response.body);
      const completedUid = [];
      for (const user of body) {
        if (user.completed) {
          completedUid.push(user.userId);
        }
      }
      const result = completedUid.reduce((acc, currentValue) => {
        acc[currentValue] = (acc[currentValue] || 0) + 1;
        return acc;
      }, {});

      console.log(result);
    }
  });
}
