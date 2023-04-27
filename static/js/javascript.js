
const btnAddAll = document.querySelectorAll('.btn-add')
const btnMinusAll = document.querySelectorAll('.btn-minus')
const csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
const total_price = document.querySelectorAll('.total')
const total_all = document.querySelector('.total-all')
const total_price_all = ()=>{
  const  totalPrice = Array.from(total_price).reduce((total,element)=>{
        const price = parseFloat(element.textContent);
        return total + price;
    }, 0)
    total_all.textContent = totalPrice + '$'
    
    return totalPrice
}
total_price_all()


btnAddAll.forEach(btn=>{
    btn.addEventListener('click', (e)=>{
        e.preventDefault
        const parent = btn.closest('.d-flex')
        const quantityElement = parent.querySelector('.quantity')
        const totalElement = parent.querySelector('.total')
        const price = btn.dataset.productPrice
        const productId = btn.dataset.productId
        let _price = parseFloat(price)
        let total = parseFloat(totalElement.textContent)
        let count = parseInt(quantityElement.textContent)
        count += 1 
        total = (_price * count)
        totalElement.textContent = total
        quantityElement.textContent = count
        total_price_all()
        fetch(`${productId}/${count}/${total}/`, {
            method:'PUT',
            headers:{
                'X-CSRFToken': csrfToken,
             'Content-Type': 'application/json'
            }
        }).then().catch(err=>console.log(err))
    })
})



btnMinusAll.forEach(btn=>{
    btn.addEventListener('click', (e)=>{
        e.preventDefault
        const parent = btn.closest('.d-flex')
        const quantityElement = parent.querySelector('.quantity')
        const totalElement = parent.querySelector('.total')
        const price = btn.dataset.productPrice
        const productId = btn.dataset.productId
        let _price = parseFloat(price)
        let total = parseFloat(totalElement.textContent)
        let count = parseInt(quantityElement.textContent)
        count -= 1 
        total = (_price * count)
        totalElement.textContent = total
        quantityElement.textContent = count
        total_price_all()
        fetch(`${productId}/${count}/${total}/`, {
            method:'PUT',
            headers:{
                'X-CSRFToken': csrfToken,
             'Content-Type': 'application/json'
            }
        }).then().catch(err=>console.log(err))
    })
})


//delete cart

const btnDelete = document.querySelectorAll('.delete')

btnDelete.forEach(btn=>{
    btn.addEventListener('click', (e)=>{
        const productId = btn.dataset.productId
        fetch(`${productId}/`,{
            method:'DELETE',
            headers:{
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json'
            }
        }).then().catch(err=>console.log(err))

        const parent = btn.parentNode
        parent.remove()
    })
})


