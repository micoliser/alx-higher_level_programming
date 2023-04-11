#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
  for (let i = 0; i < args.length; i++) args[i] = Number(args[i]);

  let biggest;
  let secBiggest;

  if (args[0] >= args[1]) {
    biggest = args[0];
    secBiggest = args[1];
  } else {
    biggest = args[1];
    secBiggest = args[0];
  }

  for (let i = 2; i < args.length; i++) {
    if (args[i] > biggest) {
      secBiggest = biggest;
      biggest = args[i];
    } else if (args[i] > secBiggest && args[i] < biggest) {
      secBiggest = args[i];
    }
  }

  console.log(secBiggest);
}
