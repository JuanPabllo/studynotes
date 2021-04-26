// try {
//   console.log(naoExisto);
// } catch (err) {
//   console.log("Nao deu bixo");
//   console.log(err);
// }

function somar(x, y) {
  if (typeof x !== "number" || typeof y !== "number") {
    throw new Error("x e y precisam ser numéricos.");
  }
  return x + y;
}

try {
  console.log(somar(1, 4));
  console.log(somar("1", 4));
} catch (err) {
  // console.log(err);
  console.log("Alguma coisa mais amigável para o usuário");
}
