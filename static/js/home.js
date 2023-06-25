const menuo = document.querySelector(".imgnavbarmenuo");
const visib = document.querySelector(".menuo");
var c = false
function visiblemenuo(){
    if (c == false){
        visib.style.visibility="visible";
    }
    if (c == true){
        visib.style.visibility="hidden";
    }
    switch (c){
        case false: c = true;
             break;
        case true: c = false;
             break;        
    }

}
menuo.addEventListener("click",visiblemenuo);

var slideIndex = 0;

showSlides();

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
     }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
     }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 4000); // Change image every 2 seconds
}


function menuooo() {
  console.log("kkkkkkkkkkklllllllllll");
}
