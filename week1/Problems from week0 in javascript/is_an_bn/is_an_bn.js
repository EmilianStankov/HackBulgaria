function is_an_bn(word) {
    new_word = [];
    n = word.length;
    if(n % 2 != 0) {
        return false;
    }
    else {
        while(new_word.length < n / 2) {
            new_word.push('a');
        }
        while(new_word.length < n) {
            new_word.push('b');
        }
        if(word == new_word.join("")) {
            return true;
        }
        else {
            return false;
        }
    }
}


function main() {
    console.log(is_an_bn(""));
    console.log(is_an_bn("rado"));
    console.log(is_an_bn("aaabb"));
    console.log(is_an_bn("aaabbb"));
    console.log(is_an_bn("aabbaabb"));
    console.log(is_an_bn("bbbaaa"));
    console.log(is_an_bn("aaaaabbbbb"));
}

main()