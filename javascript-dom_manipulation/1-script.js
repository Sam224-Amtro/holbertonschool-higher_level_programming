#!/usr/bin/node

// Sélectionne le div cliquable
const redHeader = document.getElementById('red_header');

// Sélectionne le header dont on va changer la couleur
const header = document.querySelector('header');

// Quand on clique sur le div, on appelle la fonction makethingsred
redHeader.addEventListener('click', () => makethingsred(header));

// Fonction qui change la couleur du texte en rouge
function makethingsred(element) {
  element.style.color = '#FF0000';
}
