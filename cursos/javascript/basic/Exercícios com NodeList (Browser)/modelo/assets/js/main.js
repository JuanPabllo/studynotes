const paragrafos = document.querySelector(".paragrafos");
const ps = paragrafos.querySelectorAll("p");

const stylesBody = getComputedStyle(document.body);
const backgroundColorBody = stylesBody.backgroundColor;

for (p of ps) {
  p.style.backgroundColor = backgroundColorBody;
  p.style.color = "#fff";
}
