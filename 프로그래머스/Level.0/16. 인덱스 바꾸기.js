function solution(my_string, num1, num2) {
  // split은 문자열을 배열로 변환 (인덱스를 바꾸기 위해서)
  let array = my_string.split('');

  // 배열 비구조화 할당을 사용해서 요소 교환
  // ex. [a,b]=[1,2] 1을 a에, 2를 b에 할당
  [array[num1], array[num2]] = [array[num2], array[num1]];
  // 바뀐 배열을 다시 문자열로 바꿈
  // join은 배열을 문자열로 합침
  let result = array.join('');
  console.log(result);
}
solution('hello', 1, 2);
