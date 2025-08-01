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

---


## 🛠️ Requisitos

Instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
````
---

### 📦 `requirements.txt`
```txt
requests
tqdm
colorama
````

## 🚀 Uso

```bash
python jobmanagerdisclosure.py
```

### Ejemplo de ejecución:

```bash
Enter a vulnerable website (e.g. https://example.com): https://example.com
Enter the CV file name (e.g. John Doe): HackerAccessGranted
Enter start year (e.g. 2017): 2017
Enter end year (e.g. 2019): 2019
```

### Resultado:

```text
[+] Found CV: https://example.com/wp-content/uploads/2018/04/HackerAccessGranted.png
[+] Results saved to found_cv_urls.txt
```

## 📂 Archivos

* `jobmanagerdisclosure.py`: Script principal.
* `requirements.txt`: Librerías necesarias.
* `found_cv_urls.txt`: Archivo generado con URLs encontradas.
* `README.md`: Documentación del proyecto.

## 🛡️ CVE Referencia

* [https://nvd.nist.gov/vuln/detail/CVE-2015-6668](https://nvd.nist.gov/vuln/detail/CVE-2015-6668)

## ⚠️ Disclaimer

Este script se proporciona **solo con fines educativos**. No está destinado a ser utilizado en sistemas sin autorización explícita. El uso no autorizado de este script puede ser ilegal.

````



