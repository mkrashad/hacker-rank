function getSecondLargest(nums) {
  let first = nums[0]
  let second = nums[0]
  for (let i = 0; i < nums.length; i++) {
    if (first < nums[i]) {
      second = first
      first = nums[i]
    }
    if (nums[i] > second && nums[i] < first) {
      second = nums[i]
    }
  }
  nums = second
  return nums
}