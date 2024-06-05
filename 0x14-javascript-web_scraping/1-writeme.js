#!/usr/bin/node

const fsw = require('fs');

fsw.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) console.log(err);
});
