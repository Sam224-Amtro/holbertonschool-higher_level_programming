#!/usr/bin/node

// Récupère les arguments après "node script.js"
const args = process.argv.slice(2);

// Déterminer le message en fonction du nombre d'arguments
if (args.length === 0) {
  console.log("No argument");
} else if (args.length === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
