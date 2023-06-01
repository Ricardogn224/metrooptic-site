function showFTTH() {
    document.getElementById("id_fibre_FTTO").classList.toggle("hide");



}

function showFTTO() {
    document.getElementById("id_fibre_FTTH").classList.toggle("hide");
}

function show_internet_option() {
    document.getElementById("id_internet_option").classList.toggle("hide");

}


const carousel = document.querySelector('.carousel');
const slides = carousel.querySelector('.zone-carousel');
const slideWidth = carousel.querySelector('.slide').offsetWidth;
let currentSlide = 0;

function nextSlide() {
  currentSlide++;
  if (currentSlide > slides.children.length - 1) {
    currentSlide = 0;
  }
  slides.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
}

setInterval(nextSlide, 5000);

