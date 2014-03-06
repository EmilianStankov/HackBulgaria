function arrays_dentical(a, b) {
    var i = a.length;
    if (i != b.length) return false;
    while (i--) {
        if (a[i] !== b[i]) return false;
    }
    return true;
}

function member_of_nth_fib_lists(listA, listB, needle) {
	a = listA;
	b = listB;
	index = 2;
	is_member = false;

	while(index <= needle.length) {
		next = a.concat(b);
		a = b;
		b = next;
		index += 1;
		if(arrays_identical(b, needle)) {
			is_member = true;
			break;
		}
		else {
			is_member = false;
		}
	}
	
	return is_member;
}

function main() {
	console.log(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]));
	console.log(member_of_nth_fib_lists([1, 2], [3, 4], [1,2,3,4,3,4,1,2,3,4]));
	console.log(member_of_nth_fib_lists([7,11], [2], [7,11,2,2,7,11,2]));
	console.log(member_of_nth_fib_lists([7,11], [2], [11,7,2,2,7]));
}

main();