let n1 = Number(prompt("Digite a primeira nota: "));
let n2 = Number(prompt("Digite a seguda nota: "));
let M = ((n1 + n2)/2);

if (M > 7 && n1 == 10 || n2 == 10) {
   alert("Uauuuuuu!!! Você é extraordinário. Aprovadissimo, sua média é "+ M);
} else if (M >= 7) {
   alert("Aprovado!! Com média "+ M);
} else if (M >= 5 && M < 7) {
    alert("Recuperção!! Com média "+ M);
} else {
    alert("Reprovado!! Sinto muito.");
}