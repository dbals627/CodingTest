function solution(t, p) {
  let answer = [];
  for (let i = 0; i <= t.length; i++) {
    let num = t.slice(i, i + p.length);
    // 314, 141, 415, 159, 592, 92, 2
    num.length === p.length ? answer.push(num) : '';
    // 314, 141, 415, 159, 592
  }
  return answer.filter((v) => p >= v).length;
  // 2
}

solution('3141592', '271');

///// 다른 풀이
function solution(t, p) {
  let count = 0;
  // i의 범위 = 0~5 (3자리수만 출력해야히기 때문에)
  for (let i = 0; i <= t.length - p.length; i++) {
    let value = t.slice(i, i + p.length);
    // value가 p보다 작거나 같다면 숫자 1씩 증가
    if (+p >= +value) count++;
  }
  return count;
}
