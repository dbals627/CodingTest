function solution(id_pw, db) {
  for (let i = 0; i < db.length; i++) {
    if (id_pw[0] === db[i][0] && id_pw[1] === db[i][1]) {
      return 'login';
    } else if (id_pw[0] === db[i][0] && id_pw[1] !== db[i][1]) {
      return 'wrong pw';
    }
  }
  // 어떤 조건도 만족하지 않을 때
  // for문 안에 넣으면 반복문이 일찍 종료되어 버린다.
  return 'fail';
}

//////다른 풀이
function solution(id_pw, db) {
  const [id, pw] = id_pw;
  const map = new Map(db);
  console.log(map);
  console.log(
    map.has(id) ? (map.get(id) === pw ? 'login' : 'wrong pw') : 'fail'
  );
}

solution(
  ['meosseugi', '1234'],
  [
    ['rardss', '123'],
    ['yyoom', '1234'],
    ['meosseugi', '1234'],
  ]
);
