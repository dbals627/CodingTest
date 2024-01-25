function solution(num_list, n) {
  let arr = [];

  // for, slice 사용
  // 반복문을 돌려 i,i+n의 인덱스 만큼 잘라준 후,
  // 반환된 새 배열을 빈 배열에 추가해준다.

  // slice : 얕은 복사본으로 새 배열 반환
  for (let i = 0; i < num_list.length; i += n) {
    let sli = num_list.slice(i, i + n);
    arr.push(sli);
  }
  // console.log(arr);
}

////// 다른 풀이
// while, splice 사용
// splice : 원본 배열 복사
function solution(num_list, n) {
  let answer = [];
  // num_list의 길이가 0이 될떄까지 반복
  // 원본배열이 변경되기 때문에
  while (num_list.length) {
    answer.push(num_list.splice(0, n));
  }
  console.log(answer);
}

solution([1, 2, 3, 4, 5, 6, 7, 8], 2);
