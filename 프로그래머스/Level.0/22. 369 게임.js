// function solution(order) {
//   var count = 0;
//   var string = order.toString();

//   for (let i = 0; i < string.length; i++) {
//     if (string[i] === '3' || string[i] === '6' || string[i] === '9') {
//       count++;
//     }
//   }
//   return count;
// }

////// 다른풀이
function solution(order) {
  var answer = [...order.toString().matchAll(/[3|6|9]/g)].length;
  return answer;
}
solution(29423);
