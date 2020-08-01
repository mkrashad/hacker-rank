function getCount(arr) {
  let count = 0
  for (let i in arr) {
    if (arr[i].x == arr[i].y) {
      count++;
    }
  }

  return count
}
