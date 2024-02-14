function solution(arr) {
  //   return arr.length === 1 ? [-1] : arr.splice(arr.indexOf(Math.min(...arr)), 1);
  const result = arr.filter((num) => num !== Math.min(...arr));
  return result.length === 0 ? [-1] : result;
}

solution([4, 2, 1, 3]);
solution([10]);

//////다른 풀이
function solution(arr) {
  arr.splice(arr.indexOf(Math.min(...arr)), 1);
  if (arr.length < 1) return [-1];
  return arr;
}
