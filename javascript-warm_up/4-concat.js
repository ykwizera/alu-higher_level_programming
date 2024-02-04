#!/usr/bin/node

const [, , ...args] = process.argv;

if (args[1]) {
	console.log(args[0], 'is', args[1]);
} else if (args.length === 1) {
	console.log(args[0], 'is  undefined');
} else if (args.length === 0) {
	console.log('undefined is  undefined');
} else {
	console.log(' ');
}
