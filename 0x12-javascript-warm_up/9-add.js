#!/usr/bin/node

// script that prints the addition of 2 integers

add(parseInt(process.argv[2]), parseInt(process.argv[3]));

function add(a, b) {
  console.log(a + b);
}
