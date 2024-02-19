function solution(array, commands) {
  var answer = [];

  for (let i = 0; i < commands.length; i++) {
    let result = array
      .slice(commands[i][0] - 1, commands[i][1])
      .sort((a, b) => a - b)
      .slice(commands[i][2] - 1, commands[i][2]);

    answer.push(...result);
  }

  return answer;
}

solution(
  [1, 5, 2, 6, 3, 7, 4],
  [
    [2, 5, 3],
    [4, 4, 1],
    [1, 7, 3],
  ]
);

///// 다른 풀이
function solution(array, commands) {
  return commands.map((v) => {
    return array
      .slice(v[0] - 1, v[1])
      .sort((a, b) => a - b)
      .slice(v[2] - 1, v[2])[0];
  });

  // map : 새로운 배열 반환
}
