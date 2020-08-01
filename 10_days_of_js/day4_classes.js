class Polygon {
  constructor(length) {
    this.length = length
  }
  perimeter() {
    let total = 0
    let arr = this.length
    for (let i in arr) {
      total += arr[i]
    }
    return total
  }
}
