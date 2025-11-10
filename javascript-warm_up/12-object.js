#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject); // Affiche { type: 'object', value: 12 }

myObject.value = 89; // Modifie la propriété "value" de l'objet

console.log(myObject); // Affiche { type: 'object', value: 89 }
