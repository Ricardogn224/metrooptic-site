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

/* gestion du menu telephone */

const menuElement = document.getElementById('menu');
const section = document.querySelector('section.menu-nav-phone');

// Ajouter un écouteur d'événement au clic sur l'élément du menu
menuElement.addEventListener('click', () => {
  // Changer la classe de la section
  section.classList.toggle('hide');
  console.log("hide")
});