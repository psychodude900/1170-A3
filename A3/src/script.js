function notifOnSubmit(){
    const message = document.getElementById("text-area").value;
    if(message.length < 1){
        alert("You submitted an empty message!");
    } else {
        alert("Thank you for submitting feedback");
    }
}

function colScheme(bgCol, textCol, secCol){
    var elements = document.querySelectorAll("*");
    
    for (var i = 0, len = elements.length; i < len; i++) {
        var element = elements[i];
        var elemId = element.getAttribute("id")
        if(elemId !== "white-scheme" && elemId !== "red-scheme" && elemId !== "navy-scheme"){
            element.style.background = bgCol;
            element.style.color = textCol;
        }
        var navbuttons = document.getElementsByClassName("nav-button");
        for(var x = 0; x < navbuttons.length; x++){
            var navbutton = navbuttons[x];
            if(element == navbutton){
                navbutton.style.backgroundColor = secCol;
                break;
            }
        }
        if(element.getAttribute('class') === "audio-button"){
            element.style.background = secCol;
        }
    }
}
