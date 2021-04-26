// (condicao) ? 'valor para verdadeiro' : 'valor para falso'
const pontuacaoUsuario = 876;

const nivelUsuario =
  pontuacaoUsuario >= 1000 ? "Usuário VIP" : "Usuário normal";

const corUsuario = null;
const corPadrao = corUsuario || "preta";

console.log(nivelUsuario, corPadrao);
// if (pontuacaoUsuario >= 1000) {
//   console.log("Usuário VIP");
// } else {
//   console.log("Usuário normal");
// }
