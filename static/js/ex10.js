const entrada = require('readline').createInterface({

input: process.stdin,
output: process.stdout
});

entrada.question("Digite um número para eu verificar se é positivo:", (nInput) => {
    const n = parseFloat(nInput);
    if (n > 0) {
        console.log("O número é positivo.");
    } else if (n === 0) {
        console.log("Número igual a zero.");
    } else {
        console.log("O número é negativo.");
    }
    entrada.close();
})
console.log(n)