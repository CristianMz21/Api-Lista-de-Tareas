// Script para mejorar la funcionalidad del selector de fecha y hora
document.addEventListener('DOMContentLoaded', function() {
    // Obtener el campo de fecha_vencimiento
    const fechaVencimientoInput = document.querySelector('input[name="fecha_vencimiento"]');
    
    if (fechaVencimientoInput) {
        console.log('Campo fecha_vencimiento encontrado:', fechaVencimientoInput);
        
        // Forzar el tipo a datetime-local y asegurarse de que tenga los atributos correctos
        fechaVencimientoInput.setAttribute('type', 'datetime-local');
        fechaVencimientoInput.classList.add('form-control');
        
        // Asegurarse de que el formato sea correcto
        fechaVencimientoInput.setAttribute('step', '60'); // Paso de 1 minuto
        
        // Verificar si el navegador soporta datetime-local
        const isDateTimeLocalSupported = fechaVencimientoInput.type === 'datetime-local';
        console.log('¿Soporte para datetime-local?', isDateTimeLocalSupported);
        
        if (!isDateTimeLocalSupported) {
            console.log('Este navegador no soporta el tipo datetime-local. Aplicando solución alternativa.');
            // Crear un mensaje de ayuda para el usuario
            const helpText = document.createElement('small');
            helpText.classList.add('form-text', 'text-muted', 'mt-1');
            helpText.textContent = 'Formato: DD/MM/AAAA HH:MM';
            fechaVencimientoInput.parentNode.appendChild(helpText);
        }
        
        // Establecer el valor mínimo como la fecha y hora actual
        const now = new Date();
        const year = now.getFullYear();
        const month = String(now.getMonth() + 1).padStart(2, '0');
        const day = String(now.getDate()).padStart(2, '0');
        const hours = String(now.getHours()).padStart(2, '0');
        const minutes = String(now.getMinutes()).padStart(2, '0');
        
        // Formato: YYYY-MM-DDTHH:MM
        const formattedDateTime = `${year}-${month}-${day}T${hours}:${minutes}`;
        console.log('Fecha y hora formateada:', formattedDateTime);
        
        // Asegurarse de que el valor actual esté en el formato correcto si existe
        if (fechaVencimientoInput.value) {
            try {
                // Intentar convertir el valor actual a un formato compatible con datetime-local
                const currentValue = new Date(fechaVencimientoInput.value);
                if (!isNaN(currentValue.getTime())) {
                    const formattedValue = `${currentValue.getFullYear()}-${String(currentValue.getMonth() + 1).padStart(2, '0')}-${String(currentValue.getDate()).padStart(2, '0')}T${String(currentValue.getHours()).padStart(2, '0')}:${String(currentValue.getMinutes()).padStart(2, '0')}`;
                    fechaVencimientoInput.value = formattedValue;
                    console.log('Valor actual formateado:', formattedValue);
                }
            } catch (e) {
                console.error('Error al formatear el valor actual:', e);
            }
        } else {
            // Solo establecer un valor mínimo si el campo está vacío (creación de nueva tarea)
            fechaVencimientoInput.setAttribute('min', formattedDateTime);
            console.log('Valor mínimo establecido:', formattedDateTime);
            
            // Establecer un valor predeterminado para facilitar la selección
            fechaVencimientoInput.value = formattedDateTime;
        }
        
        // Agregar un evento para asegurarse de que el campo mantenga el tipo correcto
        fechaVencimientoInput.addEventListener('focus', function() {
            if (this.type !== 'datetime-local') {
                this.type = 'datetime-local';
                console.log('Tipo restablecido a datetime-local en focus');
            }
        });
        
        // Asegurarse de que el campo sea visible y accesible
        fechaVencimientoInput.style.display = 'block';
        fechaVencimientoInput.style.width = '100%';
        
        // Agregar un evento para detectar cambios en el campo
        fechaVencimientoInput.addEventListener('change', function() {
            console.log('Valor cambiado a:', this.value);
        });
    } else {
        console.error('No se encontró el campo fecha_vencimiento');
    }
});