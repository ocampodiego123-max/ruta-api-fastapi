const formularioLogin = document.getElementById("formulario-login");
const campoUsuario = document.getElementById("usuario");
const campoContrasena = document.getElementById("contrasena");
const seccionLogin = document.getElementById("seccion-login");
const seccionInventario = document.getElementById("seccion-inventario");
const mensajeLogin = document.getElementById("mensaje-login");


seccionLogin.style.display = "block"
seccionInventario.style.display = "none"

formularioLogin.addEventListener("submit", function(event) {
    event.preventDefault()

    const usuario = campoUsuario.value
    const contrasena = campoContrasena.value

    fetch("https://ruta-api-fastapi.onrender.com/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        credentials: "include",
        body: JSON.stringify({
        usuario: usuario,
        contrasena: contrasena
    })
})
    .then(function(respuesta) {
        return respuesta.ok;
    })
    .then(function(resultado) {
        if (resultado) {
            seccionLogin.style.display = "none";
            seccionInventario.style.display = "block";
        } else {
            seccionLogin.style.display = "block";
            seccionInventario.style.display = "none";
            mensajeLogin.textContent = "Credenciales incorrectas"
        }      
    })
    .catch(function(error){
        console.log(error);
    })
});