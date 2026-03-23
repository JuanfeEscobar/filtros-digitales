#  Diseño de Filtros Digitales

##  Descripción del proyecto

Este proyecto tiene como objetivo diseñar e implementar filtros digitales pasa bajos, pasa altos y pasa bandas utilizando MATLAB o Python. Se analizan señales compuestas con ruido antes y después de aplicar los filtros para evaluar su efectividad en el dominio del tiempo y la frecuencia.

---

##  Propósito

El propósito principal de este código es:

- Generar señales de prueba con ruido.
- Diseñar filtros digitales utilizando el método Butterworth.
- Aplicar filtros a señales ruidosas.
- Analizar el comportamiento de los filtros mediante gráficas.
- Observar la respuesta en frecuencia de cada filtro.

---

##  Conceptos aplicados

- Filtros digitales (FIR e IIR)
- Filtro pasa bajos
- Filtro pasa altos
- Filtro pasa bandas
- Respuesta en frecuencia
- Procesamiento de señales
- Eliminación de ruido

---

##  Tecnologías utilizadas

- Python / MATLAB
- NumPy (si aplica)
- SciPy (si aplica)
- Matplotlib (si aplica)
- Signal Processing Toolbox (MATLAB)

---

##  Descripción del funcionamiento

1. Se genera una señal compuesta por diferentes frecuencias.
2. Se añade ruido aleatorio a la señal.
3. Se diseñan filtros digitales tipo Butterworth.
4. Se aplican los filtros a la señal ruidosa.
5. Se grafican los resultados para comparar:
   - Señal original con ruido
   - Señal filtrada (pasa bajos)
   - Señal filtrada (pasa altos)
   - Señal filtrada (pasa bandas)
6. Se analiza la respuesta en frecuencia de los filtros.

---

##  Ejecución

### En Python:

Instalar dependencias:

```bash
pip install numpy scipy matplotlib
