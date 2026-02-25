let nome = prompt("Digite seu nome");
let idade = Number(prompt("Digite sua idade: "));

if (idade >= 18 && nome != "") {
    alert("Acesso Aprovado!! Bem vindo(a) " + nome);
} else {
    alert("Acesso Negado!! Verifique sua idade ou se digitou o nome.");
}