let c = document.getElementById('canvas');
let $ = c.getContext('2d');

// Función para aplicar el color a un pixel
let col = function(x, y, r, g, b) {
    $.fillStyle = `rgb(${r},${g},${b})`;
    $.fillRect(x, y, 1, 1);
};

// Paleta personalizada
const colors = {
    color1: { r: 5, g: 15, b: 18 },   // #050f12
    color2: { r: 4, g: 40, b: 54 },   // #042836
    color3: { r: 4, g: 57, b: 70 },   // #043946
    color4: { r: 4, g: 77, b: 90 }    // #044d5a
};

// Funciones para generar los colores dinámicos
let R = function(x, y, t) {
    return Math.floor(
        colors.color1.r + (colors.color2.r - colors.color1.r) * (Math.sin(t + x / 10) + 1) / 2 +
        (colors.color3.r - colors.color2.r) * (Math.cos(t + y / 20) + 1) / 2 +
        (colors.color4.r - colors.color3.r) * (Math.sin(t + (x - y) / 15) + 1) / 2
    );
};

let G = function(x, y, t) {
    let g = Math.floor(
        colors.color1.g + (colors.color2.g - colors.color1.g) * (Math.sin(t + y / 10) + 1) / 2 +
        (colors.color3.g - colors.color2.g) * (Math.cos(t + x / 20) + 1) / 2 +
        (colors.color4.g - colors.color3.g) * (Math.sin(t + (x + y) / 15) + 1) / 2
    );
    return Math.min(g, 70); // límite para evitar verde brillante
};

let B = function(x, y, t) {
    return Math.floor(
        colors.color1.b + (colors.color2.b - colors.color1.b) * (Math.sin(t + (x + y) / 20) + 1) / 2 +
        (colors.color3.b - colors.color2.b) * (Math.cos(t + (x - y) / 20) + 1) / 2 +
        (colors.color4.b - colors.color3.b) * (Math.sin(t + x / 15) + 1) / 2
    );
};

let t = 0;

// Animación
let run = function() {
    for (let x = 0; x <= 35; x++) {
        for (let y = 0; y <= 35; y++) {
            col(x, y, R(x, y, t), G(x, y, t), B(x, y, t));
        }
    }
    t += 0.025;
    window.requestAnimationFrame(run);
};

run();
