//count procuts
const btn_left = document.querySelector('.btn-left')
const btn_right= document.querySelector('.btn-right')
const count_detail = document.querySelector('.count')

let count = parseInt(count_detail.textContent)

btn_left.addEventListener('click', (e) => {
    e.preventDefault()
  if (count > 1) {
    count -= 1
    count_detail.textContent = count
  }
})

btn_right.addEventListener('click', (e) => {
    e.preventDefault()
  count += 1
  count_detail.textContent = count
})

// add to cart

btn_addToCart = document.querySelector('.btn-add-to-cart')

