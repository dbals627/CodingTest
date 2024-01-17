function solution(numbers) {
  // 반복문 돌려서 가장 큰 값 출력하기
  var answer = [];
  for (let i = 0; i < numbers.length; i++) {
    for (let j = 0; j < numbers.length; j++) {
      // 만약에 i와 j값이 같으면 계산하지 않는다.
      if (i !== j) {
        const multiple = numbers[i] * numbers[j];
        answer.push(multiple);
      }
    }
  }
  const max = Math.max(...answer);
  console.log(max);
}

solution([1, 2, -3, 4, -5]);

// 빅오 : O(N^2)
// 반복문을 두개 쓰는게 찝찝했는데 다른 풀이를 보니 sort를 사용했다.

/////////////// 다른 풀이 ////////////////
function solution(numbers) {
  // 배열 오름차순으로 정렬
  numbers.sort((a, b) => a - b); // [-5, -3, 1, 2, 4]
  // 가장 작은 두 수를 곱하고, 가장 큰 두 수를 곱해서 최댓값을 찾는다.
  return Math.max(
    numbers[0] * numbers[1],
    numbers[numbers.length - 1] * numbers[numbers.length - 2]
  );
}

// 빅오 : O(n log n)
// 정렬 알고리즘의 시간 복잡도는 일반적으로 O(n log n)
