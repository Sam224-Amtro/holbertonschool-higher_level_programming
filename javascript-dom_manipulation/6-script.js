#!/usr/bin/node

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Convertir la réponse en JSON
  .then(data => {
    document.getElementById('character').textContent = data.name; // Afficher le nom du personnage
  })
  .catch(error => {
    console.error('Error fetching data:', error); // Gérer les erreurs
  });
