const form = document.getElementById('form')
    form.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form Submitted...')
        document.querySelector('#form-button').classList.add('hidden')
        document.querySelector('#payment-info').classList.remove('hidden')
})

document.querySelector('#make-payment').addEventListener('click',function(e){
    submitFormData()
})

function submitFormData(){
    console.log('Payment button clicked')

    var userFormData = {
        'name':null,
        'email':null,
        'total':total,
    }

    var shippingInfo = {
        'address':null,
        'city':null,  
        'district':null,   
        'zipcode':null,  
        'country':null, 
    }


    shippingInfo.address = form.address.value
    shippingInfo.city = form.city.value
    shippingInfo.district = form.district.value
    shippingInfo.country =  form.country.value
    shippingInfo.zipcode = form.zipcode.value

    var url = '/process_order/'
    fetch( url, {
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body: JSON.stringify({
            'form': userFormData,
            'shipping': shippingInfo
        })
    
    })

    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('Success:',data)
        alert('Transaction completed')
        window.location.href = "http://127.0.0.1:8000"
    })
}