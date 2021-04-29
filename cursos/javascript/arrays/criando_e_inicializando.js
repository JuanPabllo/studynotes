let daysOfWeek = new Array();
daysOfWeek = new Array(7); // especificando o tamanho
daysOfWeek = new Array(
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday'
);
console.table(daysOfWeek);

let daysOfWeek2 = [];
let daysOfWeek3 = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
];

console.log(daysOfWeek.length);

// acessando elementos e fazendo uma iteração em um Array

for (let i = 0; i < daysOfWeek.length; i++) {
  console.log(daysOfWeek[i]);
}

console.log('---------------------------');
// Fibonacci

const fibonacci = [];
fibonacci[1] = 1;
fibonacci[2] = 1;
for (let i = 3; i < 20; i++) {
  fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
}
for (let i = 1; i < fibonacci.length; i++) {
  console.log(fibonacci[i]);
}

console.log('-----------------------------');

// Acrescentando elementos

let numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
numbers[numbers.length] = 10; //ultima posicao
console.table(numbers);
