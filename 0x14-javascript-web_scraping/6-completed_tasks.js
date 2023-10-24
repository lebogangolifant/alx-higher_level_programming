#!/usr/bin/node
/**
 * Computes the number of tasks completed by user ID
 */

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = JSON.parse(body);
    const completedTasksByUser = {};
    for (const todo of jsonBody) {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId] += 1;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    }
    console.log(completedTasksByUser);
  }
});
