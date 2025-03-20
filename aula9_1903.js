/////////////////////////////////////////////////////
//   VETORES/ARRAYS em JavaScript - Aula 9         //
/////////////////////////////////////////////////////

// Arrays em JavaScript são estruturas de dados que permitem armazenar MÚLTIPLOS VALORES em uma única variável.

// Exemplo:
let frutas = ["Maçã", "Banana", "Laranja"];
console.log(frutas);

// Funções/comandos de Array:

// push: Adiciona um ou mais elementos ao final do array.

frutas.push("Laranja");
console.log(frutas);

// count: Em JavaScript, não temos uma função count diretamente, mas podemos utilizar o comando length para contar o número de elementos.

console.log(frutas.length);

// copy: Para copiar um array, podemos usar o método slice().

let copiaFrutas = frutas.slice(); 
console.log(copiaFrutas);

// random: Para selecionar um elemento aleatório de um array.

let randomIndex = Math.floor(Math.random() * frutas.length);
console.log(frutas[randomIndex]);

// range: JavaScript não tem uma função range nativa, mas podemos criar uma.

function range(start, end) {
    return Array.from({ length: end - start + 1 }, (_, i) => start + i);
}

console.log(range(1, 5));

// asort: Em JavaScript, podemos usar sort() para ordenar arrays.

let num = [3, 1, 4, 1, 5, 9];
num.sort((a, b) => a - b);
console.log(num);