
function saludar(){
    let nombre = prompt('Cuál es tu nombre');
    let edad = parseInt(prompt('Cual es tu edad'));
    let result = `Hola ${nombre} que genial que tengas ${edad} `;
    console.log(result, `Longitud del saludo de ${result.length}`);
};

saludar()


/*Programas ramificados*/ 
alert('Bienvenido comparador de edades');
let persona_1 = {
    nombre: prompt('Nombre de la persona 1'),
    edad: parseInt(prompt('Edad de la persona 1'))
};

let persona_2 = {
    nombre: prompt('Nombre de la persona 2'),
    edad: parseInt(prompt('Edad de la persona 2'))
};


function compararEdades(){
    if(persona_1.edad > persona_2.edad){
        alert(`${persona_1.nombre} es mayor que ${persona_2.nombre}`)
    }
    else if(persona_1.edad < persona_2.edad){
        alert(`${persona_2.nombre} es mayor que ${persona_1.nombre}`)
    }
    else{
        alert(`${persona_1.nombre} tiene la misma edad que ${persona_2.nombre}`)
    }
};

compararEdades();