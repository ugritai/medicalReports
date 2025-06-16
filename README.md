# Trabajo Fin de Grado: Aplicación de Ayuda para la Generación de Informes Clínicos

**Autor: Raúl Martínez Alonso**

**Curso: 2024/2025**

**Grado en Ingeniería Informática**

**Escuela Técnica Superior de Ingenierías Informática y de Telecomunicación**

**Universidad de Granada**


## Descripción general

Código de la implementación del TFG Aplicación de Ayuda para la Generación de Informes Clínicos. Este proyecto desarrolla una aplicación capaz de generar automáticamente informes clínicos a partir de textos o diagnósticos médicos, utilizando modelos de Inteligencia Artificial (IA) generativa. Se utiliza el conjunto de datos MIMIC-IV, una colección de información clínica de pacientes de acceso público. El procedimiento metodológico comienza con el procesado y la limpieza de los datos, eliminando redundancias y conservando los informes clínicos más relevantes. Posteriormente, los datos preparados se utilizan como contexto para que los modelos generativos puedan producir informes clínicos más concisos pero completos a partir de determinados parámetros de entrada.

La principal funcionalidad de la aplicación consiste en resumir textos clínicos extensos y generar así informes más ágiles y estructurados. Los modelos se han evaluado utilizando métricas automáticas, como BLEU, que mide el solapamiento y la similitud entre el informe original y el texto resumido. Además, se han realizado diferentes pruebas para determinar la influencia de añadir un rol especializado al prompt y de modificar la temperatura en el procedimiento de generación.

## Estructura del proyecto
El código está organizado en los siguientes notebooks:

1. **preprocessing_demo.ipynb:** Prueba inicial de preprocesamiento realizado con los datos de la demo.
2. **preprocessing.ipynb:** Preprocesamiento general de todos los módulos del dataset MIMIC-IV.
3. **preprocessing_notes.ipynb:** Preprocesamiento del módulo note del dataset.
4. **data_analysis.ipynb:** Código con las gráficas extraídas para el análisis exploratorio del conjunto de datos.
5. **pruebas_modelos.ipynb:** Pruebas realizadas con los modelos de generación de texto.
6. **metricas_modelos.ipynb:** Resultados obtenidos en las métricas aplicadas a las respuestas de los modelos de lenguaje.


## Resultados
El el fichero **tfg.pdf** se encuentra la memoria realizada para el proyecto.
