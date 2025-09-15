function solution(my_string) {
    let answer = '';
    my_string.split('').reverse().forEach((v)=> answer += v )
    return answer;
}