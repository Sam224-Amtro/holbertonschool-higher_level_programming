#!/usr/bin/node
// Script pour calculer la factorielle d'un entier non négatif

// Fonction factorielle récursive
function factorial (n) {
  // Traite les valeurs non entières ou négatives
  if (!Number.isInteger(n) || n < 0) return 1;
  return n <= 1 ? 1 : n * factorial(n - 1); // Cas de base et cas récursif
}

// Récupère le premier argument passé en ligne de commande et
// le convertit en entier
const num = parseInt(process.argv[2], 10);

// Calcule et affiche la factorielle
console.log(factorial(num));
