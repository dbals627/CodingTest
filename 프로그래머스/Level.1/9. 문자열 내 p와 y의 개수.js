function solution(s) {
  const countP = s.replace(/[^pP]/g, '').toLowerCase().split('').length;
  const countY = s.replace(/[^yY]/g, '').toLowerCase().split('').length;

  return countP === countY ? true : false;
}

solution('Pyy');

////////다른 풀이
function solution(s) {
  console.log(
    s.toUpperCase().split('P').length === s.toUpperCase().split('Y').length
  );
}
