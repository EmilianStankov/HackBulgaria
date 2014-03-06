function unique_words_count(arr){
    current = "";
    count = 0;
    for(var i = 0; i <= arr.length; i++) {
        current = arr[i];
        for(var j = 0; j <= arr.length; j++) {
            if(current != arr[j]) {
                count += 1;
            }
        }
        break;
        current = "";
    }
    return count;
}

function main(){
    console.log(unique_words_count(["apple", "banana", "apple", "pie"]))
    console.log(unique_words_count(["python", "python", "python", "ruby"]))
    console.log(unique_words_count(["HELLO!", "HELLO!", "HELLO!", "HELLO!", 
        "HELLO!", "HELLO!", "HELLO!", "HELLO!", "HELLO!", "HELLO!"]))
}


main()