async function fetchData(offset, limit) {
    const url = 'https://api-iot-monitoring-production.up.railway.app/'; // Reemplaza con la URL de tu API
    const headers = {
        'Direction': '1', // O '-1' para orden descendente
        'Order': 'SensorID', // Campo por el cual ordenar
        'Offset': offset.toString(), // Inicio del registro
        'Limit': limit.toString() // Número de registros a devolver
    };

    try {
        const response = await fetch(url, { method: 'GET', headers: headers });
        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }
        return await response.json(); // O el formato adecuado de la respuesta
    } catch (error) {
        console.error('Error al obtener datos:', error);
    }
}

// Usar la función para obtener 100 registros
fetchData(0, 100).then(data => {
    if (data) {
        console.log('Datos obtenidos:', data);
    }
});
