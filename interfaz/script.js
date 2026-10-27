const formularioLogin = document.getElementById("formulario-login");
const campoUsuario = document.getElementById("usuario");
const campoContrasena = document.getElementById("contrasena");
const seccionLogin = document.getElementById("seccion-login");
const seccionInventario = document.getElementById("seccion-inventario");


seccionLogin.style.display = "block"
seccionInventario.style.display = "none"





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
