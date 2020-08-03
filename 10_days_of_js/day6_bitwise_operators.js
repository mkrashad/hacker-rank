function getMaxLessThanK(n, k) {
  if ((k | (k - 1)) > n) {
    return k - 2
  }

  else {
    return k - 1
  }
}