function solution(my_string) {
  const lower = my_string.toLowerCase(); // 'hello'
  return [...lower].sort().join('');
  // [ 'e', 'h', 'l', 'l', 'o' ] sort()
  // 'ehllo' join('')
}

solution('heLLo');
