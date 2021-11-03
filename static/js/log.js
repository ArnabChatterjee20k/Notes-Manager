// for alerting modal class text which is containing the flashed message from the server
let message=document.getElementById("modal").innerText;
console.log(message)
if (message!='\n        \n        \n        \n    '){
    alert(message);
}
// dynamically changing login page to registration page
let links = Array.from (document.getElementsByClassName("link"))
let form=document.getElementById("form")
let title=document.getElementById("title")
let previoustitle = title.innerText

links.forEach(function(e){
    e.addEventListener("click",function(){
        let current_active=document.querySelector(".active");
        current_active.classList.remove("active")
        e.classList.toggle("active")
        if(e.innerText=="Login"){
            title.innerText=previoustitle
            form.action="/login"
        }
        else{
            title.innerText="Register"
            form.action="/register"
        }
    })
})



