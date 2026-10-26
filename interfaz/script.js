const campoNombre = document.getElementById("nombre");
const campoTipo = document.getElementById("tipo");
const campoEstado = document.getElementById("estado");

const formulario = document.getElementById("formulario-equipo");
const resultado = document.getElementById("resultado");
const listaEquipos = document.getElementById("lista-equipos");


formulario.addEventListener("submit", function(event){
    event.preventDefault();

    const nombre = campoNombre.value;
    const tipo = campoTipo.value;
    const estado = campoEstado.value;

    resultado.textContent = `Nombre: ${nombre} | Tipo: ${tipo} | Estado: ${estado}`;


    const equipo = document.createElement("div");
    equipo.className = "equipo-item";

    const titulo = document.createElement("h3");
    titulo.textContent = nombre;

    const textoTipo = document.createElement("p");
    textoTipo.textContent = `Tipo: ${tipo}`;

    const textoEstado = document.createElement("p");
    textoEstado.textContent = `Estado: ${estado}`;

    equipo.appendChild(titulo);
    equipo.appendChild(textoTipo);
    equipo.appendChild(textoEstado);

    listaEquipos.appendChild(equipo);


});


fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(function(respuesta) {
        return respuesta.json();
    })
    .then(function(datos) {
        const titulo = document.getElementById("titulo-publicacion");
        titulo.textContent = datos.title;
    })
    .catch(function(error) {
        console.log("Ocurrió un error:", error);
    });





function mostrarEquipos(equipos) {
    // 1. Limpiar las tarjetas anteriores
    listaEquipos.innerHTML = "";

    // 2. Recorrer la lista de equipos
    equipos.forEach(function(equipo) {
        // 3. Crear la tarjeta
        const tarjeta = document.createElement("div");
        tarjeta.className = "equipo-item";

        // 4. Crear el título con el nombre
        const titulo = document.createElement("h3");
        titulo.textContent = equipo.nombre;

        // 5. Crear el párrafo con el tipo
        const textoTipo = document.createElement("p");
        textoTipo.textContent = `Tipo: ${equipo.tipo}`;

        // 6. Crear el párrafo con el estado
        const textoEstado = document.createElement("p");
        textoEstado.textContent = `Estado: ${equipo.estado}`;

        // 7. Añadir la información a la tarjeta
        tarjeta.appendChild(titulo);
        tarjeta.appendChild(textoTipo);
        tarjeta.appendChild(textoEstado);

        // 8. Añadir la tarjeta al inventario
        listaEquipos.appendChild(tarjeta);
    });
}


const equiposPrueba = [
    {
        id: 1,
        nombre: "Router Cisco",
        tipo: "Redes",
        estado: "activo"
    },
    {
        id: 2,
        nombre: "Cámara",
        tipo: "CCTV",
        estado: "en mantenimiento"
    }
];

mostrarEquipos(equiposPrueba);

