function solution(my_string) {
  const arr = my_string.split('');
  const filter = arr.filter((word) => my_string.includes(word));
  console.log(filter);
}
solution('We are the world');
