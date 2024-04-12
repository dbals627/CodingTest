// function solution(arr) {
//   // for (let i = 0; i < arr.length; i++) {
//   //   if (arr[i] >= 50 && arr[i] % 2 === 0) {
//   //     arr[i] = arr[i] / 2;
//   //   } else if (arr[i] < 50 && arr[i] % 2 === 1) {
//   //     arr[i] = arr[i] * 2 + 1;
//   //   }
//   // }
//   // console.log(arr);

//   const newArray = arr.map((v) => {
//     if (v >= 50 && v % 2 === 0) {
//       v = v / 2;
//     } else if (v < 50 && v % 2 === 1) {
//       v = v * 2 + 1;
//     }
//   });

//   console.log(newArray);
// }

// solution([1, 2, 3, 100, 99, 98]);

// 배열을 몇번 바뀔 수 있나? 제일 오래가는 애가 몇번 살아남는가

const isOdd = (num) => num % 2 !== 0;

const getConvertStep = (num, count = 0) => {
  if (num >= 50 && !isOdd(num)) {
    return getConvertStep(num / 2, count + 1);
  }

  if (num < 50 && isOdd(num)) {
    return getConvertStep(num * 2 + 1, count + 1);
  }

  return count;
};

const max = (arr) => arr.reduce((acc, cur) => (acc > cur ? acc : cur));
const solution = (arr) => max(arr.map((num) => getConvertStep(num)));
