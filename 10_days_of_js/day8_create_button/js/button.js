addEventListener('click', func)
function func(e) {
  let value = e.target.innerHTML
  value++
  const v = document.getElementById('btn').innerHTML = value
}