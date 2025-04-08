// Función para marcar una tarea como completada o no completada
document.addEventListener('DOMContentLoaded', function() {
    // Seleccionar todos los checkboxes de tareas
    const checkboxes = document.querySelectorAll('.tarea-completada');
    
    // Añadir evento a cada checkbox
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const tareaId = this.getAttribute('data-id');
            const completada = this.checked;
            
            // Enviar solicitud AJAX para actualizar el estado
            fetch(`/toggle-completada/${tareaId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({
                    'completada': completada
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Actualizar la apariencia de la tarea
                    const tareaTitle = document.querySelector(`#tarea-${tareaId} .tarea-titulo`);
                    if (completada) {
                        tareaTitle.classList.add('text-muted', 'text-decoration-line-through');
                    } else {
                        tareaTitle.classList.remove('text-muted', 'text-decoration-line-through');
                    }
                    
                    // Mostrar mensaje de éxito
                    const alertContainer = document.getElementById('alert-container');
                    const alertElement = document.createElement('div');
                    alertElement.className = 'alert alert-success alert-dismissible fade show';
                    alertElement.role = 'alert';
                    alertElement.innerHTML = `
                        Tarea ${completada ? 'completada' : 'marcada como pendiente'} exitosamente
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                    `;
                    alertContainer.appendChild(alertElement);
                    
                    // Eliminar la alerta después de 3 segundos
                    setTimeout(() => {
                        alertElement.remove();
                    }, 3000);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

// Función para obtener el token CSRF de las cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}