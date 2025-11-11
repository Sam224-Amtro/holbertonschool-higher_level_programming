#!/usr/bin/node

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json()) // Convertir la réponse en JSON
  .then(data => {
    const moviesList = document.getElementById('list_movies'); // Récupérer l’élément <ul>
    data.results.forEach(movie => {
      const listItem = document.createElement('li'); // Créer un nouvel élément <li> pour chaque film
      listItem.textContent = movie.title; // Définir le titre du film comme contenu texte
      moviesList.appendChild(listItem); // Ajouter le <li> à la liste <ul>
    });
  })
  .catch(error => {
    console.error('Erreur lors du chargement des films :', error); // Gérer les erreurs
  });
