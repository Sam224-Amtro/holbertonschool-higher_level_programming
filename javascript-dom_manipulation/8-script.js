#!/usr/bin/node

window.onload = function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json()) // Convertir la réponse en JSON
    .then(data => {
      document.getElementById('hello').textContent = data.hello; // Afficher la traduction de "hello" dans l’élément
    })
    .catch(error => {
      console.error('Erreur lors de la récupération des données :', error); // Gérer les erreurs
    });
};
