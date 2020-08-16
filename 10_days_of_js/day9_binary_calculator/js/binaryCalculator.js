let btn0 = document.getElementById("btn0").innerHTML
let btn1 = document.getElementById("btn1").innerHTML
let btnClr = document.getElementById("btnClr").innerHTML
let btnEql = document.getElementById("btnEql").innerHTML
let btnSum = document.getElementById("btnSum").innerHTML
let btnSub = document.getElementById("btnSub").innerHTML
let btnMul = document.getElementById("btnMul").innerHTML
let btnDiv = document.getElementById("btnDiv").innerHTML

document.getElementById('btns').addEventListener('click', calc);

let str = '';
function calc(e) {
  let value = e.target.innerHTML
  if (value === '1' || value === '0') {
    str += value
    document.getElementById("res").innerHTML = str
  }
  if (value === '+' || value === '-' || value === '*' || value === '/') {
    str += value
    document.getElementById("res").innerHTML = str
  }
  if (value === '=') {
    let result = eval(str)
    document.getElementById("res").innerHTML = result
  }
  if (value === 'C') {
    str = ''
    document.getElementById("res").innerHTML = str
  }
}
