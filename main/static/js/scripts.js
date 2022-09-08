var nav = document.querySelector('#Dropdown_menu')
function nav_dropdown() {

    if(nav.style.display == "block"){
        nav.style.display = "none";
    }
    else {
        nav.style.display = "block";
    }
}

window.onclick = function (event) {
    if (!event.target.matches('.shop')) {
        document.querySelector('#Dropdown_menu').style.display = "none";
    }
} 