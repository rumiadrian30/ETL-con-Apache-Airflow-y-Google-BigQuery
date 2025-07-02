📊 ETL SRI Vehículos
Bienvenido al repositorio del proyecto ETL para el dataset de vehículos del Servicio de Rentas Internas (SRI) del Ecuador. Aquí se integra un proceso completo de extracción, transformación y carga de datos utilizando Apache Airflow para la orquestación y Google BigQuery como almacén de datos.

📂 Contenido del Repositorio
📁 dags/: Contiene el archivo principal del DAG (etl_sri_dag.py) para Airflow y utilidades necesarias.

📄 data/: Archivo CSV original con los datos del SRI.

🛠️ scripts/: Scripts auxiliares para subir archivos a Google Cloud Storage y otras tareas relacionadas.

📚 docs/: Informe técnico completo, diagramas del modelo dimensional y capturas de pantalla que muestran la ejecución.

✅ tests/: Pruebas unitarias para validar funciones clave (opcional).

⚙️ Archivos de configuración para Docker y dependencias.

📋 Requisitos Previos
Para ejecutar o explorar el proyecto es necesario contar con:

🌐 Cuenta activa en Google Cloud Platform con permisos para BigQuery y Storage.

🔐 Archivo JSON con credenciales para autenticación (ubicado en dags/keys/).

🐳 Docker y Docker Compose instalados para levantar Apache Airflow en un entorno local.

🔧 Variables de entorno configuradas correctamente en .env (no subido al repositorio por seguridad).

🚀 Guía Rápida para Ejecutar el Proyecto
🔽 Clonar el repositorio a tu entorno local.

🔐 Colocar el archivo de credenciales JSON dentro de la carpeta dags/keys/.

⚙️ Configurar el archivo .env con los parámetros necesarios como el nombre del bucket, ID de proyecto, etc.

🐳 Levantar Apache Airflow ejecutando:

bash
Copiar
Editar
docker-compose up -d
🌐 Acceder a la interfaz web de Airflow en http://localhost:8080.

▶️ Activar y ejecutar el DAG llamado etl_sri_vehiculos.

📊 Monitorizar la ejecución a través de los logs y verificar que todas las tareas finalicen correctamente.

🔍 Validar los datos cargados en BigQuery mediante consultas SQL para confirmar la integridad y consistencia.

📖 Documentación Adicional
En la carpeta docs/ encontrarás:

📄 Informe técnico completo en PDF que explica el desarrollo, el modelado dimensional, la configuración y las pruebas realizadas.

📊 Diagramas visuales del esquema estrella (modelo dimensional).

📸 Capturas de pantalla de la interfaz de Airflow, el bucket en Cloud Storage y las tablas en BigQuery.

⚠️ Buenas Prácticas
🔒 Nunca subir archivos con credenciales sensibles como el JSON de la cuenta de servicio a repositorios públicos.

🚫 Mantener actualizado el archivo .env y asegurarse de incluirlo en .gitignore.

📝 Documentar cada cambio relevante para facilitar el mantenimiento y futuras ampliaciones.

🔍 Revisar los logs periódicamente para detectar posibles errores en la ejecución del DAG.

📞 Contacto
Para dudas o sugerencias, contactar a:

Rumi Adrian Grefa Rivadeneyra
✉️ Correo: rumi.grefa@espoch.edu.ec
