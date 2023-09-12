#!/usr/bin/node

const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

const readStream1 = fs.createReadStream(sourceFile1, 'utf8');
const readStream2 = fs.createReadStream(sourceFile2, 'utf8');

const writeStream = fs.createWriteStream(destinationFile, 'utf8');

// Pipe the contents of the source files to the destination file
readStream1.pipe(writeStream, { end: false });
readStream2.pipe(writeStream, { end: false });

// Handle 'end' event to close the write stream when done
writeStream.on('finish', () => {
  console.log(`Concatenation of ${sourceFile1} and ${sourceFile2} completed. Result saved in ${destinationFile}`);
});

// Handle errors
readStream1.on('error', (err) => {
  console.error(err);
});
readStream2.on('error', (err) => {
  console.error(err);
});
writeStream.on('error', (err) => {
  console.error(err);
});
