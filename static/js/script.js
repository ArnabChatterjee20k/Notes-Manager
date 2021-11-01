// getting the important==yes elements
let yes=document.querySelectorAll(".ye");
yes.forEach(function(e){e.style.background="#f29c95"})

// Making darkmode
let darkBtn = document.getElementById("darkmode");
darkBtn.addEventListener("click", function () {
    let dark_check = document.getElementById("darkmode").innerHTML;
    if (dark_check == "Dark") {
        toggle_color("black", "white")
        color_list = ["#f44336", "#009688", "#3f51b5", "#00bcd4", "#ffeb3b", "#03a9f4"]
        let card_color = document.querySelectorAll(".dynamicCard ");
        card_color.forEach(function (element) {
            // element.style="border:4px solid #009688;width:18rem"
            card_color.forEach(function (element) {
                if (element.classList.contains("no")) {
                    element.classList.add("bg-dark", "text-white");//adding bootstrap class to change the style without modifing the whole content;
                }
            })
        })

        let dark_text = document.getElementById("darkmode");
        dark_text.innerHTML = "Light";

    }
    else {
        // to switch normal white theme
        toggle_color("white", "black");
        let dark_text = document.getElementById("darkmode");
        dark_text.innerHTML = "Dark";
        let card_color = document.querySelectorAll(".dynamicCard");
        card_color.forEach(function (element) {
            if (element.style.background != "red") {
                element.classList.remove("bg-dark", "text-white");
            }
        })

    }


})

function toggle_color(bg, headings) {
    /** to toggle between dark and light theme */
    document.body.style = `background:${bg};`;
    let dark_bg = document.querySelectorAll(".dark_color");
    // console.log(dark_bg);
    dark_bg.forEach(function (element) {
        element.style = `background:${bg};`;
    })

    let head_hr = document.querySelectorAll(".white_dark")
    head_hr.forEach(function (element) {
        element.style = `color:${headings};`;
    })
}

// search function
let field=document.querySelector("#searchTxt")
field.addEventListener("input",function(){
    let search=field.value
    let card=document.getElementsByClassName("dynamicCard")
    Array.from(card).forEach(function(e){
        let cardTxt=e.getElementsByTagName("h5")[0].innerText
        if (cardTxt.includes(search)){
            e.style.display="block"
        }
        else{
            e.style.display="none"
        }
    })
})