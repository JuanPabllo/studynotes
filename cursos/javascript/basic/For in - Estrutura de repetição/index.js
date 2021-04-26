//  for in lê os indices ou chaves do objeto

const pessoa = {
  nome: "Juan",
  sobrenome: "Pablo",
  idade: 18,
};
// console.log(pessoa.nome);
// console.log(pessoa["nome"]);

for (let chave in pessoa) {
  console.log(`${chave}: ${pessoa[chave]}`);
}

//               1       2       3      4          5
// const frutas = ["maça", "Pera", "uva", "laranja", "manga"];

// for (let indice in frutas) {
//   console.log(frutas[indice]);
// }
// for (let i = 0; i < frutas.length; i++) {
//   console.log(frutas[i]);
// }
