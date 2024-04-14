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
