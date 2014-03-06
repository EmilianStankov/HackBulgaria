function prepare_meal(number) {
    answer = [];
    if(number % 5 != 0) {
        for(var i = number; i > 0; i--) {
            if(number % Math.pow(3, i) == 0) {
                var j = 0;
                while(j < i) {
                    answer.push('spam ');
                    j++;
                }
                break;
            }
        }
    }
    else {
        for(var i = number; i > 0; i--) {
            if(number % Math.pow(3, i) == 0) {
                var j = 0;
                while(j < i) {
                    answer.push('spam ');
                    j++;
                }
                answer.push('and eggs');
                break;
            }
            else if(number % 3 != 0) {
                answer.push('eggs');
                break;
            }
        }
    }
    return '\'' + answer.join("") +'\'';
}

function main() {
    console.log(prepare_meal(3));
    console.log(prepare_meal(27));
    console.log(prepare_meal(7));
    console.log(prepare_meal(5));
    console.log(prepare_meal(15));
    console.log(prepare_meal(45));
}


main();