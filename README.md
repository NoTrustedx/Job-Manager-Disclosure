# CV Filename Disclosure Scanner – CVE-2015-6668

Este script automatiza la búsqueda de archivos de CV (como `.jpg`, `.png`, `.jpeg`) expuestos públicamente mediante la vulnerabilidad [CVE-2015-6668](https://nvd.nist.gov/vuln/detail/CVE-2015-6668), relacionada con el plugin **WP Job Manager** para WordPress (versiones ≤ 0.7.25).

## 🧠 Descripción

La vulnerabilidad permite conocer el nombre exacto de un archivo subido por los usuarios (por ejemplo, currículums) accediendo directamente a rutas de carga predecibles en el servidor web.

Este script:

- Construye rutas basadas en nombre, año, mes y extensiones.
- Realiza requests HTTP a cada URL posible.
- Muestra una barra de progreso interactiva con `tqdm`.
- Resalta en color verde las URLs encontradas.
- Guarda los resultados en `found_cv_urls.txt`.

## 🛠️ Requisitos

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
