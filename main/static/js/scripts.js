var nav = document.querySelector('#Dropdown_menu')
function nav_dropdown() {

    if(nav.style.display == "block"){
        nav.style.display = "none";
    }
    else {
        nav.style.display = "block";
    }
}

// Cart Function to remove item
$('a.remove').click(function(){
    event.preventDefault();
    $( this ).parent().parent().parent().hide( 400 );
   
})
  
