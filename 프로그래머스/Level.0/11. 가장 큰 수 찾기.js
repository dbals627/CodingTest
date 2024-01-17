function solution(array) {
  const max = Math.max(...array);
  const idx = array.indexOf(max);
  console.log([max, idx]);
}
solution([9, 10, 11, 8]);

// 빅오 : O(n)
// 배열에서 최대값을 찾기 위해 Math.max를 사용하고
// 배열에서 최대값의 인덱스를 찾기 위해 indexOf를 사용한다.
// 배열의 길이에 비례하여 두 가지 작업을 수행한다.
// 최댓값을 찾는 작업 자체가 배열의 선형 검색을 필요로 한다.
