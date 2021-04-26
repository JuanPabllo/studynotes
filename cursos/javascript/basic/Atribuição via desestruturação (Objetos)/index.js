const pessoa = {
  nome: "Juan",
  sobrenome: "Pablo",
  idade: 18,
  endereco: {
    rua: "Av. Brasil",
    num: 206,
  },
};

// const { nome: teste = "Não existe", sobrenome } = pessoa;
// const {
//   endereco: { rua: local = 12345, num },
// } = pessoa;

const { nome, ...resto } = pessoa;

console.log(resto);
