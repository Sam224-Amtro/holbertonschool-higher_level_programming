#!/usr/bin/node
// Script pour calculer la factorielle d'un entier non négatif

// Fonction factorielle récursive
function factorial (n) {
  // Si n n'est pas un entier ou est négatif, retourne 1
  if (!Number.isInteger(n) || n < 0) return 1;

  // Cas de base : 0! et 1! valent 1
  if (n <= 1) return 1;

  // Cas récursif
  return n * factorial(n - 1);
}

// Récupère le premier argument passé en ligne de commande et
// le convertit en entier
const num = parseInt(process.argv[2], 10);

// Calcule et affiche la factorielle
console.log(factorial(num));
