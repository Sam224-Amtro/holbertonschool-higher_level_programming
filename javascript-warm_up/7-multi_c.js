#!/usr/bin/node

// Récupère le premier argument de la ligne de commande
const count = parseInt(process.argv[2], 10);

// Valider l'argument
if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < count) {
    console.log('C is fun');
    i++;
  }
}
