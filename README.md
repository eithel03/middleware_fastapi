# Middleware CORS con FastAPI

<!-- local-development:start -->
## Desarrollo local

Consulta [RUNNING.md](RUNNING.md) para ubicar cada componente, abrirlo en su IDE, compilarlo y conocer las comprobaciones realizadas y los requisitos pendientes.
<!-- local-development:end -->

## Descripción del proyecto
Este proyecto demuestra la implementación del **middleware CORS (Cross-Origin Resource Sharing)** utilizando **FastAPI**.  
El objetivo es permitir la comunicación segura entre el *frontend* y el *backend* cuando ambos están alojados en diferentes dominios, controlando qué orígenes pueden acceder a los recursos del servidor.

---

## Archivos del proyecto
- **main.py** → Contiene el código principal del servidor con la configuración del middleware CORS.  
- **TAREA CORS Eithel.docx** → Documento de investigación sobre el middleware CORS.  
- **myenv/** → Entorno virtual de Python.  
- **\_\_pycache\_\_/** → Archivos generados automáticamente por Python.

---

## Ejecución del proyecto
1. Activa el entorno virtual:
   ```bash
   .\myenv\Scripts\actívate

Ejecución del servidor:
uvicorn main:app --reload

Abrir el navegador con: http://127.0.0.1:8000

Middleware CORS implementado:
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensaje": "Middleware CORS activo correctamente"}

Conclusión:

El uso del middleware CORS en FastAPI permite controlar el acceso entre diferentes orígenes, garantizando la seguridad de la comunicación y evitando errores del tipo CORS Policy Error.
Gracias a su implementación sencilla y flexible, se convierte en una herramienta clave en el desarrollo de APIs REST seguras y modernas.
