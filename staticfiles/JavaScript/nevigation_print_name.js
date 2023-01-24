function textContentprint(clicked){
    console.log(clicked)
}
function menu_after_responsive(){
    var clikc = document.getElementsByClassName('yuptup')[0]
    if (clikc.style.display === "none"){
        clikc.style.display = "block"
    }
    else{
        clikc.style.display = "none"   
    }
}

function fluid_data(){
    var login_detail = document.getElementById("login_file_details")
    let cons = document.getElementById('icon_tag')
    if (tett == 1){
        login_detail.style.display = "none"
        cons.style.color = 'white'
        cons.style.borderBottom='none'
        cons.style.textShadow='none' 
    }

}

