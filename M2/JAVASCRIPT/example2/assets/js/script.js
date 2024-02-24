/**Variables* */
var palabra = "Boot\ncamp";
console.log(palabra);/*Boot
                        camp*/

var booleana = true;//false
console.log(booleana);//

/*operadores aritmeticos(+ - * /) */
var numero1 = 5;
var numero2 = 4;
var total_suma = numero1 + numero2;// var total_suma= 5+4; var total_suma = 9;
console.log(total_suma);//9

console.log(numero1/numero2);//1.25 //solo imprimiendo
console.log(total_suma / 0);//Infinity
console.log(total_suma / "a");//NaN -> No es un numero

var dividendo = 8;
var divisor = 4;
var total_modulo = dividendo % divisor;//var total_modulo = 8 % 4;//var total_modulo =0
console.log(total_modulo);//0

/** operadores de comparacion **/
var variable1 = 5;
var variable2 = "5";
console.log(variable1 == variable2);//true
console.log(variable1 === variable2);//false 

/** prompt() **/
document.write('<h1 class="text-primary"> Hola mundo</h1>');
var nombre = prompt("Ingresa tu nombre", "");
console.log("Tu Nombre es:", nombre);
document.write("Tu Nombre es:", nombre);
var edad;

//document.write("\n");//no funciona en document.write
document.write("<br>");

var apellido = prompt("Ingresa tu apellido", "");
console.log("Tu Apellido es: "+apellido);
document.write("<p> Tu Apellido es: " + apellido + "</p>");
document.write('<h2>Soy un h2</h2>');

/* document.write nos permite escribir dinamicamente el contenido
de las paginas web html*/


