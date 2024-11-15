// main.js

document.addEventListener("DOMContentLoaded", () => {
    fetchClientes();
    document.getElementById("clienteSelect").addEventListener("change", mostrarClienteSeleccionado);
});

// Función para obtener los clientes del backend y llenar el <select>
function fetchClientes() {
    fetch('http://127.0.0.1:5000/api/clientes')
        .then(response => response.json())
        .then(data => {
            const clientes = data.clientes;

            // Muestra en consola los nombres de los clientes para verificar que funcione
            clientes.forEach(cliente => {
                console.log("Nombre del Cliente:", cliente.Nombre_Cliente);
            });

            const clienteSelect = document.getElementById("clienteSelect");
            
            // Llenar el <select> con los nombres de los clientes
            clientes.forEach(cliente => {
                const option = document.createElement("option");
                option.value = cliente.ID_Cliente;  // Usamos el ID como valor
                option.textContent = cliente.Nombre_Cliente;
                clienteSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error al obtener los clientes:', error));
}

// Función para mostrar los datos del cliente seleccionado
function mostrarClienteSeleccionado() {
    const clienteId = document.getElementById("clienteSelect").value;
    if (!clienteId) {
        limpiarInfoCliente();
        return;
    }

    fetch('http://127.0.0.1:5000/api/clientes')
        .then(response => response.json())
        .then(data => {
            const cliente = data.clientes.find(c => c.ID_Cliente === clienteId);

            if (cliente) {
                document.getElementById("nombreCliente").textContent = cliente.Nombre_Cliente;
                document.getElementById("deudaCliente").textContent = `$${cliente.Monto_Deuda}`;
            }
        })
        .catch(error => console.error('Error al obtener la información del cliente:', error));
}

// Función para limpiar la información del cliente cuando no se selecciona ninguno
function limpiarInfoCliente() {
    document.getElementById("nombreCliente").textContent = "Seleccione un cliente";
    document.getElementById("deudaCliente").textContent = "";
}
