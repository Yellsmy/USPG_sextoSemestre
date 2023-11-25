'''
{
        F"EventId": 1,
        F"Timestamp": "2023-10-29T16:34:05.000Z",
        D"OperatorID": "Operator505146",
        F"MaintenanceSchedule": "2024-04-29T00:00:00.000Z",
        D"Sensor": {
            "SensorID": "P959",
            "SensorType": "Pressure",
            "Location": "TweedTango, Los Angeles, Floor 'A' | 34.0522,-118.2437",
            "Manufacturer": "SensorTech",
            "Model": "Pro 300",
            "Regulations": "EMC2014/30/EU"
        },
        D"SensorReading": {
            "AffectedEquipment": "Pressure Valve",
            F"SampleRate": 62,
            F"Value": 32,
            "Unit": "PSI",
            "Description": "INFO: Pressure has dropped significantly."
        },
        D"Status": {
            "Alert": false,
            "AlarmThreshold": 80,
            "BatteryLevel": 53,
            "Status": "warning",
            "Reliability": "High"
        }
    },

{
        "Id. de evento": 1,
        "Marca de tiempo": "2023-10-29T16:34:05.000Z",
        "OperadorID": "Operador505146",
        "Programación de mantenimiento": "2024-04-29T00:00:00.000Z",
        "Sensor": {
            "ID del sensor": "P959",
            "SensorType": "Presión",
            "Ubicación": "TweedTango, Los Ángeles, Piso 'A' | 34.0522,-118.2437",
            "Fabricante": "SensorTech",
            "Modelo": "Pro 300",
            "Reglamentos": "EMC2014/30/UE"
        },
        "Lectura del sensor": {
            "EquipoAfectado": "Válvula de Presión",
            "Tasa de muestra": 62,
            "Valor": 32,
            "Unidad": "PSI",
            "Description": "INFO: La presión ha bajado significativamente."
        },
        "Estado": {
            "Alerta": falso,
            "Umbral de alarma": 80,
            "Nivel de batería": 53,
            "Estado": "advertencia",
            "Fiabilidad": "Alta"
        }
    }

Campos:
EventId
Timestamp
OperatorID
MaintenanceSchedule
Sensor
SensorID
SensorType
Location
Manufacturer
Model
Regulations
SensorReading
AffectedEquipment
SampleRate
Value
Unit
Description
Status
Alert
AlarmThreshold
BatteryLevel
Status_SKST
Reliability



Claro, aquí tienes las tablas con sus campos listados de forma independiente para una mejor visualización:

### Tabla de Hechos: Eventos de Sensores
- FactID
- EventID
- OperatorDimID
- SensorDimID
- ReadingDimID
- StatusDimID
- Timestamp
- MaintenanceSchedule
- SampleRate
- Value

### Tabla de Dimensiones: Operador
- OperatorDimID
- OperatorID

### Tabla de Dimensiones: Sensor
- SensorDimID
- SensorID
- SensorType
- LocationName (Extraído de Location)
- LocationCoordinates (Extraído de Location)
- Manufacturer
- Model
- Regulations

### Tabla de Dimensiones: Lectura del Sensor
- ReadingDimID
- AffectedEquipment
- Unit
- Description

### Tabla de Dimensiones: Estado
- StatusDimID
- Alert
- AlarmThreshold
- BatteryLevel
- Status
- Reliability

En el caso de la 'Location' en la Tabla de Dimensiones: Sensor, la he dividido en dos campos adicionales: 'LocationName' y 'LocationCoordinates', para facilitar el análisis geográfico y la posible integración con sistemas GIS o consultas por ubicación específica.

Es importante mencionar que, dependiendo de las necesidades de consulta y los requerimientos de rendimiento, estas tablas pueden necesitar índices apropiados, claves foráneas, y quizás políticas de actualización para manejar cambios en los datos a lo largo del tiempo (como mencionado antes, usando estrategias de dimensiones lentamente cambiantes).

Además, es común que las tablas de dimensiones contengan más campos que pueden ser útiles para el análisis, como campos derivados o calculados (por ejemplo, una columna de 'Año' en la tabla de dimensiones de tiempo para facilitar el análisis por año sin tener que extraerlo del timestamp cada vez). Estos campos adicionales dependerán de los requisitos de análisis específicos del negocio.
'''

import requests
import pyodbc

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# Configuración de la conexión a la base de datos SQL Server
server = 'DESKTOP-CSMV2FJ'
database = 'Ecommerce'
username = 'sa'
password = 'secreto123'
driver = '{ODBC Driver 17 for SQL Server}'   # Asegúrate de tener el driver adecuado instalado

# Establecer la conexión a la base de datos
conn = pyodbc.connect('DRIVER=' + driver +
                      ';SERVER=' + server +
                      ';PORT=1433;DATABASE=' + database +
                      ';UID=' + username +
                      ';PWD=' + password)

cursor = conn.cursor()

# URL de la API de donde obtendremos los datos
todoLosDatos = 'https://api-iot-monitoring-production.up.railway.app/event'
totalRegistros = 'https://api-iot-monitoring-production.up.railway.app/event/getTotalRecords' # registros actuales 631289

headers = {
    'accept': 'application/json',
    'Direction': 'ASC',
    'Order': 'SensorID',
}


limit = 120
offset = 110

try:
    while True:
        # Actualizar el offset en los headers
        headers['Offset'] = str(offset)
        headers['Limit'] = str(limit)
        # Obtener los datos de la API
        response = requests.get(todoLosDatos,headers=headers)
        data = response.json() 
       
        # Verificar si hay datos para procesar
        if not data:
            break

        # Procesar y aplanar cada elemento del arreglo JSON
        for item in data:
            flattened_item = flatten_json(item)
        # Insertar datos en la base de datos
            cursor.execute("""
                INSERT INTO stg.Prueba (
                    EventId, Timestamp, OperatorID, MaintenanceSchedule, SensorID, SensorType,
                    Location, Manufacturer, Model, Regulations, AffectedEquipment, SampleRate,
                    Value, Unit, Description, Alert, AlarmThreshold, BatteryLevel, Status, Reliability
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, 
                flattened_item['EventId'],
                flattened_item['Timestamp'],
                flattened_item['OperatorID'],
                flattened_item['MaintenanceSchedule'],
                flattened_item['Sensor_SensorID'],
                flattened_item['Sensor_SensorType'],
                flattened_item['Sensor_Location'],
                flattened_item['Sensor_Manufacturer'],
                flattened_item['Sensor_Model'],
                flattened_item['Sensor_Regulations'],
                flattened_item['SensorReading_AffectedEquipment'],
                flattened_item['SensorReading_SampleRate'],
                flattened_item['SensorReading_Value'],
                flattened_item['SensorReading_Unit'],
                flattened_item['SensorReading_Description'],
                flattened_item['Status_Alert'],
                flattened_item['Status_AlarmThreshold'],
                flattened_item['Status_BatteryLevel'],
                flattened_item['Status_Status'],
                flattened_item['Status_Reliability']
            )
            conn.commit()  # Guardar los cambios en la base de datos

            print("Datos insertados correctamente en la base de datos.")

        # Incrementar el offset para la próxima solicitud
        offset += limit
    # Suponiendo que la API devuelve datos en formato JSON
    #Procesar los datos y insertarlos en la base de datos


except Exception as e:
    print("Ocurrió un error:", e)

finally:
    conn.close()  # Cerrar la conexión a la base de datos