function nth_fib_lists(listA, listB, n) {
	a = listA;
	b = listB;
	index = 2;

	while(index <= n) {
		next = a.concat(b);
		a = b;
		b = next;
		index += 1;
	}
	return a;
}

function main() {
	console.log(nth_fib_lists([1], [2], 1));
	console.log(nth_fib_lists([1], [2], 2));
	console.log(nth_fib_lists([1, 2], [1, 3], 3));
	console.log(nth_fib_lists([], [1, 2, 3], 4));
	console.log(nth_fib_lists([], [], 100));
}

main();