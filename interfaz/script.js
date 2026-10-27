const formularioLogin = document.getElementById("formulario-login");
const campoUsuario = document.getElementById("usuario");
const campoContrasena = document.getElementById("contrasena");
const seccionLogin = document.getElementById("seccion-login");
const seccionInventario = document.getElementById("seccion-inventario");
const mensajeLogin = document.getElementById("mensaje-login");
const listaEquipos = document.getElementById("lista-equipos");
const formularioEquipo = document.getElementById("formulario-equipo");
const nombre = document.getElementById("nombre");
const tipo = document.getElementById("tipo");
const estado = document.getElementById("estado");
const cerrarSesion = document.getElementById("boton-logout");
const mensajeInventario = document.getElementById("mensaje-inventario")


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
            cargarEquipos();
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




fetch("https://ruta-api-fastapi.onrender.com/sesion", {
    credentials: "include"
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
    }      
})
.catch(function(error){
    console.log(error);
})



function cargarEquipos(){
    fetch("https://ruta-api-fastapi.onrender.com/equipos", {
    credentials: "include"
})
.then(function(respuesta) {
    return respuesta.json();
})
.then(function(resultado) {
    listaEquipos.innerHTML = "";
    if (resultado.length > 0){
            resultado.forEach(function(equipo){
                listaEquipos.innerHTML += `
                <div>
                    <p>Nombre: ${equipo.nombre} </p>
                    <p>Tipo: ${equipo.tipo} </p>
                    <p>Estado: ${equipo.estado} </p>

                    <select id="estado-${equipo.id}">
                    <option value="activo">Activo </option>
                    <option value="en mantenimiento"> En mantenimiento </option>
                    <option value="fuera de servicio"> Fuera de servicio </option>
                    </select>

                    <button type= "button" id="actualizar-${equipo.id}"> Actualizar estado </button>
                </div>`;
            });
            resultado.forEach(function(equipo){
                const actualizarEstado = document.getElementById(`actualizar-${equipo.id}`);

                actualizarEstado.addEventListener("click", function(){
                    const estadoDinamico = document.getElementById(`estado-${equipo.id}`);
                    const nuevoEstado = estadoDinamico.value;
                    console.log(nuevoEstado);
                    
                    fetch(`https://ruta-api-fastapi.onrender.com/equipos/${equipo.id}`, {
                    method: "PATCH",
                    headers: {"Content-Type": "application/json"},
                    credentials: "include",
                    body: JSON.stringify({
                    estado: nuevoEstado
                    })
                })
                .then(function(respuesta) {
                return respuesta.ok;
                })
                .then(function(resultado){
                    if (resultado){
                        cargarEquipos()
                    } else {
                        mensajeInventario.textContent ="Error al actualizar estado"
                    }
                })
                .catch(function(error){
                    console.log(error);
                    mensajeInventario.textContent = "Error de conexión durante la actualización"
                })
            });
            });
    } else {
        listaEquipos.innerHTML += `No hay equipos registrados`
    }
})
.catch(function(error){
    console.log(error);
    mensajeInventario.textContent = "No se pudo conectar con el servidor"
});
}



formularioEquipo.addEventListener("submit", function(event) {
    event.preventDefault()

    const valorNombre = nombre.value
    const valorTipo = tipo.value
    const valorEstado = estado.value

    fetch("https://ruta-api-fastapi.onrender.com/equipos", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        credentials: "include",
        body: JSON.stringify({
        nombre: valorNombre,
        tipo: valorTipo,
        estado: valorEstado
    })
})
    .then(function(respuesta) {
        return respuesta.ok;
    })
    .then(function(resultado) {
        if (resultado) {
            alert("Equipo registrado correctamente");
            cargarEquipos()
            mensajeInventario.textContent = "";
        } else {
            alert("Ocurrió un error al registrar equipo");
        }
    })
    .catch(function(error){
        console.log(error);
        mensajeInventario.textContent= "Error de conexión durante el registro";
    })
});



cerrarSesion.addEventListener("click", function() {

    fetch("https://ruta-api-fastapi.onrender.com/logout", {
    method: "POST",
    credentials: "include"
})

.then(function(respuesta) {
    return respuesta.ok;
})
.then(function(resultado) {
    if (resultado) {
        seccionLogin.style.display = "block";
        seccionInventario.style.display = "none";
        formularioLogin.reset();
        mensajeLogin.textContent ="";
    } else {
        alert("Error al cerrar la sesión")
    }
});
});



