#!/usr/bin/node
/**
 * Write a string to a file
 */

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

// Write the provided string to the file
fs.writeFile(filePath, content, 'utf8', (error) => {
  if (error) return console.error(error);
});
