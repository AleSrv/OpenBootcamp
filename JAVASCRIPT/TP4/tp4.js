let nombre="Alejandro";
let ape="Fernandez";
let estudiante = `${nombre} ${ape}`;
let estudianteMayus = estudiante.toUpperCase();
let estudianteMinus = estudiante.toLowerCase();
let num_letras = estudiante.length;
let letraNombre= nombre[0];
let letraApellido= ape[ape.length -1];
// Todas válidas
// const estudianteSinEspacios = estudiante.replace(" ", "")
const estudianteSinEspacios = estudiante.replace(/ /g, "")
let estaNombre = estudiante.includes(nombre);




