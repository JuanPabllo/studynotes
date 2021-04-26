function mostrarHoraAtual() {
  let data = new Date();
  return data.toLocaleTimeString("pt-BR", {
    hour12: false,
  });
}

const time = setInterval(function () {
  console.log(mostrarHoraAtual());
}, 1000);

setTimeout(() => {
  clearInterval(time);
}, 5000);

setTimeout(function () {
  console.log("oi");
}, 7000);
