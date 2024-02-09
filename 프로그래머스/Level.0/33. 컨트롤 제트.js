function solution(s) {
  let arr = s.split(' ');
  let answer = 0;

  s.split(' ').forEach((v, i) => {
    if (v === 'Z') answer -= Number(arr[i - 1]);
    else answer += Number(v);
  });

  console.log(answer);
}

solution('10 Z 20 Z 1');

///////다른 풀이
function solution(s) {
  const stack = [];

  s.split(' ').forEach((target) => {
    if (target === 'Z') stack.pop();
    else stack.push(+target);
  });

  console.log(stack.length ? stack.reduce((pre, cur) => pre + cur) : 0);
}
