let alt_centimetros = 179;
let alt_metros = 1.79;
let peso_kg= 89.5;
let alt_redondeo_arriba = Math.ceil(alt_metros);
let peso_redondeo_abajo = Math.floor(peso_kg);
let valor_max = Number.MAX_VALUE + 1;

//OUTPUTS:

console.log("La altura en centimetros es:", alt_centimetros);
console.log("La altura en metros es:", alt_metros);
console.log("El peso es:", peso_kg , "Kg." );
console.log("Altura redondeada es:" , alt_redondeo_arriba);
console.log("El peso redondeado hacia abajo es: ", peso_redondeo_abajo);
console.log("el máximo valor que se puede obtener en Javascript + 1 es: ", valor_max)
