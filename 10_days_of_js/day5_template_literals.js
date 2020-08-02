function main() {
  let s1 = 10
  let s2 = 14
  const [x, y] = `The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
  return [x, y]

}
function sides(literals, ...expressions) {
  let arr = []
  let P = expressions[1]
  let A = expressions[0]
  let s1 = (P + Math.sqrt((P * P) - 16 * A)) / 4
  let s2 = (P - Math.sqrt((P * P) - 16 * A)) / 4

  arr.push(s1, s2)
  arr.sort()
  return arr
}




