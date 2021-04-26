// Escreva uma funcao que receba dois numeros e retorne o maior deles

function max(num1, num2) {
  if (num1 > num2) {
    console.log(`O maior numero é ${num1}`);
  } else {
    console.log(`O maior numero é ${num2}`);
  }
}

max(10, 8);

const max2 = (num1, num2) => (num1 > num2 ? num1 : num2);
console.log(max2(10, 50));
