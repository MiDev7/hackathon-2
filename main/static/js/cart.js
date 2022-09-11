let updateBtn = document.querySelectorAll('.chg-quantity')

for(let i = 0 ; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click',function() {

        let productId = this.dataset.product
        let action = this.dataset.action
        console.log('productId: ', productId ,', action: ' , action)
        updateUserOrder(productId,action)
    })
}


function updateUserOrder(productId, action){
    var url = '/updateCart/'
    fetch( url, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body: JSON.stringify({
            'productId': productId,
            'action': action
        })
    
    })

    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:',data)
        location.reload()
    })
}
