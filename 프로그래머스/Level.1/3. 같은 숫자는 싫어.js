function solution(arr) {
  var answer = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== arr[i + 1]) {
      answer.push(arr[i]);
    }
  }

  console.log(answer);
}

solution([1, 1, 3, 3, 0, 1, 1]);

///// 다른풀이
function solution(arr) {
  return arr.filter((val, index) => val != arr[index + 1]);
}

// filter = 배열 순회 메서드, 복사 메서드, 얕은 복사본 반환
