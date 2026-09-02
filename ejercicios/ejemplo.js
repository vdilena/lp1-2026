// Pedir dos valores y realizar una multiplicacion y mostrar el resultado

const readline = require("readline");

const entrada = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

entrada.question("Ingrese el primer valor: ", (primerValorIngresado) => {
  entrada.question("Ingrese el segundo valor: ", (segundoValorIngresado) => {
    const primerValor = Number(primerValorIngresado);
    const segundoValor = Number(segundoValorIngresado);
    const multiplicacion = primerValor * segundoValor;

    console.log("El resultado de la multiplicacion es:", multiplicacion);
    entrada.close();
  });
});
