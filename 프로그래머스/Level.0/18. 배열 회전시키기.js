function solution(numbers, direction) {
  var answer = [];
  if (direction == 'right') {
    answer.push(numbers.pop());
    numbers.unshift(answer[0]);
  } else if (direction == 'left') {
    answer.push(numbers.shift());
    numbers.push(answer[0]);
  }
}

solution([1, 2, 3], 'right');
solution([4, 455, 6, 4, -1, 45, 6], 'left');

///// 다른풀이
function solution(numbers, direction) {
  if (direction === 'right') {
    numbers.unshift(numbers.pop());
  } else {
    numbers.push(numbers.shift());
  }
  return numbers;
}
