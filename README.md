Detector de rostros con OpenCV y Haar Cascades
Este proyecto detecta rostros en tiempo real utilizando una cámara web. Está desarrollado en Python y utiliza la librería OpenCV junto con el clasificador preentrenado Haar Cascades para la detección de rostros.

Características principales
Detección de rostros en tiempo real.

Fácil de usar y configurar.

Utiliza un clasificador preentrenado para una detección rápida y precisa.

Requisitos
Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

Python 3.9.2

OpenCV (opencv-python)

Instalación
Clona este repositorio en tu máquina local:

bash
Copy
git clone https://github.com/emdraw/PythonFaceRecognition.git

cd detector-rostros-opencv

Instala las dependencias necesarias:

bash

Copy

pip install -r requirements.txt

Si no tienes un archivo requirements.txt, puedes instalar las dependencias manualmente:


bash

Copy

pip install opencv-python

Uso

Ejecuta el script principal:


bash

Copy

python detector_rostros.py

La cámara web se encenderá y comenzará a detectar rostros en tiempo real.

Presiona la tecla d para salir del programa.

Estructura del proyecto

Copy

detector-rostros-opencv/

├── detector_rostros.py   # Script principal

├── haarcascade_frontalface_default.xml  # Clasificador Haar Cascade

├── README.md             # Este archivo

└── requirements.txt      # Dependencias del proyecto

Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

Haz un fork del repositorio.

Crea una rama con tu nueva característica (git checkout -b feature/nueva-caracteristica).

Realiza tus cambios y haz commit (git commit -am 'Añade nueva característica').

Haz push a la rama (git push origin feature/nueva-caracteristica).

Abre un Pull Request.

Licencia

Este proyecto está bajo la licencia MIT.
