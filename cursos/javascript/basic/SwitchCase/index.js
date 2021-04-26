const data = new Date("2002-03-31 00:00:00");
let diaDaSemana = data.getDay();
// diaDaSemana = 7;
let diaDaSemanaTexto;

switch (diaDaSemana) {
  case 0:
    diaDaSemanaTexto = "Domingo";
    break;
  case 1:
    diaDaSemanaTexto = "Segunda";
    break;
  case 2:
    diaDaSemanaTexto = "Terça";
    break;
  case 3:
    diaDaSemanaTexto = "Quarta";
    break;
  case 4:
    diaDaSemanaTexto = "Quinta";
    break;
  case 5:
    diaDaSemanaTexto = "Sexta";
    break;
  case 6:
    diaDaSemanaTexto = "Sábado";
    break;
  default:
    diaDaSemanaTexto = "";
}

// if (diaDaSemana === 0) {
//   diaDaSemanaTexto = "Domingo";
// } else if (diaDaSemana === 1) {
//   diaDaSemanaTexto = "Segunda";
// } else if (diaDaSemana === 2) {
//   diaDaSemanaTexto = "Terça";
// } else if (diaDaSemana === 3) {
//   diaDaSemanaTexto = "Quarta";
// } else if (diaDaSemana === 4) {
//   diaDaSemanaTexto = "Quinta";
// } else if (diaDaSemana === 5) {
//   diaDaSemanaTexto = "Sexta";
// } else if (diaDaSemana === 6) {
//   diaDaSemanaTexto = "Sábado";
// } else {
//   diaDaSemanaTexto = "aa";
// }

console.log(diaDaSemana, diaDaSemanaTexto);
