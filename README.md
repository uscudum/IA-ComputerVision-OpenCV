# OpenCV Projects
Este repositorio contiene cuatro proyectos desarrollados con OpenCV en Python, los cuales abordan diferentes técnicas de procesamiento de imágenes y video. A continuación se describe cada uno de los proyectos:

## 1. Detección de Color Verde en una Imagen
Este script permite cargar una imagen y detectar áreas que contienen el color verde dentro de un rango específico de valores RGB. El resultado es una máscara binaria que resalta las regiones verdes de la imagen original.

### Características:
* Carga una imagen RGB desde un archivo.
* Aplica un umbral para detectar el color verde.
* Genera y guarda una imagen que muestra solo las áreas verdes detectadas.

## 2. Detección en Tiempo Real de Color Verde en Video
Este script realiza la detección de color verde en tiempo real usando la cámara web. Se detectan las áreas verdes en cada fotograma del video, y se muestra tanto la imagen original como la imagen con las áreas verdes resaltadas.

### Características:
* Captura video en tiempo real desde la cámara web.
* Aplica un umbral para detectar el color verde en cada fotograma.
* Muestra el video original y la detección de áreas verdes en tiempo real.


## 3. Detección de Rostros en Tiempo Real
Este script utiliza un clasificador en cascada preentrenado (haarcascade_frontalface_default.xml) para detectar rostros en tiempo real a través de la cámara web. Los rostros detectados son resaltados con un rectángulo verde.

### Características:
* Captura video en tiempo real desde la cámara web.
* Convierte la imagen a escala de grises para mejorar la detección.
* Utiliza un clasificador Haar para detectar rostros.
* Dibuja un rectángulo verde alrededor de los rostros detectados.

## 4. Conteo de Vehículos en Video
Este script implementa un contador de vehículos utilizando técnicas de sustracción de fondo y procesamiento de contornos en un video pregrabado. El contador se incrementa cada vez que un vehículo cruza una línea específica en el video.

### Características:
* Carga y analiza un video para detectar movimiento.
* Utiliza sustracción de fondo para identificar objetos en movimiento.
* Cuenta el número de vehículos que cruzan una línea específica.
* Muestra el video con el conteo de vehículos en tiempo real.
