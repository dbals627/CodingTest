function solution(A, B) {
  // 각 배열의 원소를 곱해서 더했을 때 최솟값을 만들기 위해서는
  // 가장 작은 수 * 가장 큰 수 를 더하면 된다.
  A.sort((a, b) => a - b);
  B.sort((a, b) => b - a);

  return A.reduce((sum, acc, i) => sum + acc * B[i], 0);
}

solution([1, 4, 2], [5, 4, 4]);
