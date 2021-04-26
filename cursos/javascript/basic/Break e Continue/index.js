const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// continue  continua para a próxima interação
// break sai do laço

for (numero of numeros) {
  if (numero === 2) {
    console.log("Pulei o numero 2");
    continue;
  }
  console.log(numero);

  if (numero === 7) {
    console.log("Encontrei o 7, saindo....");

    break;
  }
}
