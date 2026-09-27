<!--
  Este archivo lo genera scripts/build_readme.py a partir de README.template.es.md, data/*.json y data/i18n/es.json.
  Edita la plantilla o los datos y luego ejecuta: python3 scripts/build_readme.py
  Palabras clave: prompts nsfw, prompts de video ia nsfw, ejemplos de prompts wan 2.2 nsfw, guía de prompts wan 2.2 imagen a video,
  prompts de imagen a video nsfw, prompts para video ia sin censura, prompts seedance spicy, prompts de imagen ia nsfw,
  prompts negativos, ia para adultos, nsfw ai video prompts, nsfw prompts, wan 2.2 nsfw prompt example,
  wan 2.2 image to video prompt guide, nsfw image to video prompts, uncensored ai video prompts, seedance spicy prompts
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <b>Español</b></p>

<h1 align="center">NSFW AI Video Prompts</h1>

<p align="center">
  <b>116 prompts de video con IA NSFW para copiar y pegar, 24 prompts de imagen para el primer fotograma y 130 ejemplos con resultados reales, para Wan 2.2 Spicy, Seedance Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy y otros modelos de imagen a video sin censura.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/video%20prompts-116-ff4d6d" alt="116 prompts de video">
  <img src="https://img.shields.io/badge/first--frame%20prompts-24-8b5cf6" alt="24 prompts de imagen">
  <img src="https://img.shields.io/badge/showcase-130-10b981" alt="130 ejemplos reales">
  <img src="https://img.shields.io/badge/updated-2026-09-27-blue" alt="Actualizado: 2026-09-27">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#ejemplos-reales-resultados-y-sus-prompts">Ejemplos</a> ·
  <a href="#los-prompts">Prompts</a> ·
  <a href="#prompts-de-imagen-para-el-primer-fotograma">Primeros fotogramas</a> ·
  <a href="#prompts-negativos">Prompts negativos</a> ·
  <a href="#guía-rápida-de-cámara-iluminación-y-movimiento">Guía rápida</a> ·
  <a href="#ejecuta-un-prompt-en-60-segundos">Ejecutar</a> ·
  <a href="#preguntas-frecuentes">Preguntas frecuentes</a>
</p>

> **Solo para mayores de 18 años. Todos los personajes de este repositorio son adultos.** Los prompts indican una edad adulta y evitan a propósito las descripciones que sugieran juventud. Nunca uses estos prompts con imágenes de personas reales que no hayan dado su consentimiento documentado, y nunca "desvistas" la foto de una persona real. Consulta las [Reglas](#reglas).

> Lo mantiene el equipo de [SpicyAPI](https://spicyapi.ai/es?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=disclosure-es), donde puedes ejecutar todos los prompts de aquí. Los prompts son texto plano y funcionan con cualquier modelo de imagen a video que los acepte.

---

## Por qué existe este repositorio

La mayoría de las listas de "prompts NSFW" son montones de palabras clave pensados para imágenes fijas de Stable Diffusion. Los modelos de video necesitan otra cosa: **un único movimiento claro, un movimiento de cámara con nombre y un primer fotograma que ya defina el aspecto**. Todos los prompts de aquí están escritos así e incluyen:

- el **modelo** para el que se escribió, con un enlace directo a la página del modelo,
- **resolución, duración y relación de aspecto**,
- el **costo de una ejecución** con los precios actuales del catálogo,
- una **descripción del primer fotograma** para que sepas de qué imagen partir,
- un **consejo** que explica por qué funciona o qué suele fallar.

Los consejos son recomendaciones prácticas basadas en uso real, no resultados de benchmarks. Los [ejemplos reales](#ejemplos-reales-resultados-y-sus-prompts) son la parte de este repositorio con resultados reales.

Los datos de los modelos y los precios proceden del catálogo público de SpicyAPI, consultado el 2026-09-27.

## Contenido

- [Modelos incluidos](#modelos-incluidos)
- [Ejemplos reales: resultados y sus prompts](#ejemplos-reales-resultados-y-sus-prompts)
- [Cómo escribir un prompt de video NSFW que funcione](#cómo-escribir-un-prompt-de-video-nsfw-que-funcione)
- [Los prompts](#los-prompts)
  - [Boudoir y lencería](#boudoir-y-lencería) (16)
  - [Desnudo artístico y bellas artes](#desnudo-artístico-y-bellas-artes) (14)
  - [Parejas y romance](#parejas-y-romance) (14)
  - [Actuación en solitario y baile](#actuación-en-solitario-y-baile) (14)
  - [Baño, ducha y agua](#baño-ducha-y-agua) (10)
  - [Fantasía, ciencia ficción y cosplay](#fantasía-ciencia-ficción-y-cosplay) (12)
  - [Estilo anime y hentai](#estilo-anime-y-hentai) (10)
  - [Sensualidad comercial apta para marcas](#sensualidad-comercial-apta-para-marcas) (10)
  - [Plantillas reutilizables de movimiento y cámara](#plantillas-reutilizables-de-movimiento-y-cámara) (10)
  - [Prompts de estilo con LoRA (Wan 2.2 Spicy LoRA)](#prompts-de-estilo-con-lora-wan-22-spicy-lora) (6)
- [Prompts de imagen para el primer fotograma](#prompts-de-imagen-para-el-primer-fotograma)
- [Prompts negativos](#prompts-negativos)
- [Guía rápida de cámara, iluminación y movimiento](#guía-rápida-de-cámara-iluminación-y-movimiento)
- [Consejos por modelo](#consejos-por-modelo)
- [El flujo de imagen a video](#el-flujo-de-imagen-a-video)
- [Ejecuta un prompt en 60 segundos](#ejecuta-un-prompt-en-60-segundos)
- [Deja que un LLM escriba tus prompts](#deja-que-un-llm-escriba-tus-prompts)
- [Preguntas frecuentes](#preguntas-frecuentes)
- [Reglas](#reglas)

---

## Modelos incluidos

**Modelos de video**

| Modelo | Tipo | Tareas | Duración | Desde |
|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/es/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s |
| [Seedance 2.5](https://spicyapi.ai/es/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–30 s | $0.1234/s |
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s |
| [Seedance 2.0](https://spicyapi.ai/es/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.07/s |
| [Wan 3.0 Prime](https://spicyapi.ai/es/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.0612/s |
| [Wan 3.0](https://spicyapi.ai/es/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.045/s |
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s |
| [MiniMax H3](https://spicyapi.ai/es/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.025/s |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/es/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V | 3–15 s | $0.06/s |
| [LTX 2.5](https://spicyapi.ai/es/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, T2V | 5–20 s | $0.09/s |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/es/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.234/s |
| [Wan 3.0 Pro](https://spicyapi.ai/es/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 2–30 s | $0.144/s |
| [MiniMax H3 LoRA](https://spicyapi.ai/es/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 3–15 s | $0.05/s |
| [HappyHorse 1.1](https://spicyapi.ai/es/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 3–15 s | $0.14/s |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s |
| [Seedance 2.0 Mini](https://spicyapi.ai/es/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.01097/s |
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s |
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/es/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s |
| [Seedance 2.0 Fast](https://spicyapi.ai/es/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 4–15 s | $0.02254/s |
| [Vidu Q3 Turbo](https://spicyapi.ai/es/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V | 1–16 s | $0.042/s |
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s |
| [Vidu Q3](https://spicyapi.ai/es/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V | 1–16 s | $0.07/s |
| [Vidu Q3 Pro](https://spicyapi.ai/es/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V | 1–16 s | $0.054/s |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/es/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s |
| [Seedance 1.5 Pro](https://spicyapi.ai/es/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, T2V | 4–12 s | $0.0112/s |
| [Wan 2.6 Flash](https://spicyapi.ai/es/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V | 5, 10, 15 s | $0.0225/s |
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s |
| [Wan 2.6](https://spicyapi.ai/es/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s |
| [Wan 2.5](https://spicyapi.ai/es/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V, T2V | 5, 10 s | $0.045/s |
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s |
| [Wan 2.2 LoRA](https://spicyapi.ai/es/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | I2V | 5, 8 s | $0.024/s |

**Modelos de imagen** (primeros fotogramas e imágenes fijas)

| Modelo | Tipo | Tareas | Desde |
|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.024/image |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/es/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.042/image |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.04/image |
| [Qwen Image 3.0](https://spicyapi.ai/es/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image |
| [Seedream 5.0 Pro](https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.036/image |
| [Qwen Image Edit Spicy](https://spicyapi.ai/es/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | Edit | $0.038/image |
| [Seedream 5.0 Lite](https://spicyapi.ai/es/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.0345/image |
| [Qwen Image 2](https://spicyapi.ai/es/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.035/image |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/es/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image |
| [Z-Image Spicy Pro](https://spicyapi.ai/es/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | T2I | $0.019/image |
| [Z-Image Spicy](https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | 🌶️ Spicy | T2I | $0.01235/image |
| [Z-Image](https://spicyapi.ai/es/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | T2I | $0.01/image |
| [Z-Image Turbo LoRA](https://spicyapi.ai/es/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.012/image |
| [Seedream 4.0](https://spicyapi.ai/es/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | Edit, T2I | $0.03/image |
| [Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | T2I | $0.015/image |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/es/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-es) | Estándar | T2I | $0.018/image |


El orden sigue el catálogo de SpicyAPI: primero los más populares y la versión más reciente. Las ediciones 🌶️ Spicy están ajustadas para contenido adulto; los modelos estándar de esta lista tienen el nivel `unrestricted` en el catálogo (el proveedor no los filtra), así que también sirven para prompts para adultos y añaden texto a video y referencia a video. Los precios corresponden al nivel más barato; la página del modelo es siempre la referencia. Las ejecuciones fallidas se reembolsan automáticamente.

---

## Ejemplos reales: resultados y sus prompts

130 casos reales sacados de las páginas de los modelos y de la [biblioteca de prompts](https://spicyapi.ai/es/prompts?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es) de SpicyAPI. Cada caso muestra un resultado junto al prompt exacto que lo generó. Los modelos aparecen de más a menos popular y con la versión más reciente primero: ediciones Spicy y modelos estándar con nivel `unrestricted` en el catálogo. Haz clic en una vista previa para ver el clip en calidad completa.

### Seedance 2.5 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/561b3b36ee1cdc88.mp4"><img src="assets/showcase/seedance-2-5-spicy--onsen-rise-embrace.gif" alt="Onsen rise embrace" width="230"></a></td><td valign="top"><b>Onsen rise embrace</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/561b3b36ee1cdc88.mp4">▶ clip completo</a></sub><br><br>The two women rise toward camera only as far as the collarbone, water sheeting off their shoulders, and the steam banks thick across the surface in front of them. One slides behind the other and wraps both arms around her from behind, her forearm crossing high over the chest; they settle cheek to cheek and hold the look into the lens while the water swells and slaps the rocks. Slow push in on their faces and shoulders, framed from the collarbone up the whole time. Dusk light on wet skin, drifting snow beyond. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.5-spicy/0510366bd110c007.mp4"><img src="assets/showcase/seedance-2-5-spicy--onsen-two-rise.gif" alt="Two women in a steaming outdoor hot spring at dusk, first facing the camera with the water at their shoulders, then seen from behind with bare backs above the waterline" width="230"></a></td><td valign="top"><b>Two women rising from a misty outdoor hot spring</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.5-spicy/0510366bd110c007.mp4">▶ clip completo</a></sub><br><br>Cast: two women. The camera stays on their backs as they rise, and stops there. In the mist of an outdoor hot spring at dusk, first one and then the other rises only until the waterline reaches the small of the back and no further; they hold there, steam closing over the surface behind them. Nothing below the waterline ever leaves the water. Locked framing. Cinematic, heavy film grain, steam white and rock grey, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/8ae0a0222aa9f90f.mp4"><img src="assets/showcase/seedance-2-5-spicy--steam-glass-handprint.gif" alt="Behind fogged shower glass in a dark bathroom, a woman drags her palm down the pane and leans in until her face comes into focus through the clear streak" width="230"></a></td><td valign="top"><b>Face pressed close behind steamed shower glass</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/8ae0a0222aa9f90f.mp4">▶ clip completo</a></sub><br><br>Her palm drags straight down the fogged glass, carving one long clear streak from the wiped patch to the bottom edge, and her fingertips lift away. She immediately steps forward and leans into that clear streak: her face arrives close to the glass and comes into sharp focus through it, wet skin and lashes clearly visible, water beading and running around her cheek. She holds there, eyes level with the lens, and breathes out against the glass so a small bloom of fog spreads and fades. The framing stays tight on the glass panel the entire time. Do not pull back, do not widen the shot, do not change the camera angle. Running water, muffled room tone, one slow breath.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/fec77dab61baeb3a.mp4"><img src="assets/showcase/seedance-2-5-spicy--hotel-window-turn.gif" alt="A woman in an ivory silk slip turning from a floor-to-ceiling hotel window at night, city lights behind her" width="230"></a></td><td valign="top"><b>Silk slip turn at a night hotel window</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/fec77dab61baeb3a.mp4">▶ clip completo</a></sub><br><br>She turns slowly from the window toward camera, the silk slip catching the city light as it moves, one hand trailing along the glass, then she tilts her head and holds the look. Subtle handheld drift, warm lamp against cool skyline, quiet room tone.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/c5f2690c42576a26.mp4"><img src="assets/showcase/seedance-2-5-spicy--pov-hand-pull.gif" alt="A first-person shot of a woman in black satin taking the viewer&#x27;s hand and running through a neon night market, laughing back over her shoulder" width="230"></a></td><td valign="top"><b>First-person: pulled by the hand through a night market</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/c5f2690c42576a26.mp4">▶ clip completo</a></sub><br><br>She closes her hand around the viewer&#x27;s and pulls, breaking into a run and towing the camera after her through the neon stalls, laughing back over her shoulder once. Handheld first-person motion, neon streaking past, crowd noise and sizzling griddles.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/b8be819fa36bd881.mp4"><img src="assets/showcase/seedance-2-5-spicy--opera-stair-train.gif" alt="A woman in a backless black velvet gown and long gloves climbs a marble opera house staircase, glancing back over her shoulder as the train drags behind her" width="230"></a></td><td valign="top"><b>Backless gown gliding up an opera house staircase</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/b8be819fa36bd881.mp4">▶ clip completo</a></sub><br><br>She holds the look back over her bare shoulder, then turns and continues up two more steps, the velvet train dragging heavily behind her across the marble, her gloved hand sliding along the brass banister. The chandelier flares a little brighter and the gilt catches, deep shadows swinging across the wall. Slow dolly following her up the stairs, hushed hall reverb, no music.</td></tr>
</table>

### Seedance 2.5

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5/7ceb81a8701180d6.mp4"><img src="assets/showcase/seedance-2-5--night-train-press.gif" alt="In a dim night train carriage, a woman in a long dark coat with bare legs stands at the door; a man steps in behind her and they end up face to face as tunnel lights strobe" width="230"></a></td><td valign="top"><b>Night train crowd presses two strangers together</b><br><sub><code>bytedance/seedance-2.5/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5/7ceb81a8701180d6.mp4">▶ clip completo</a></sub><br><br>A woman alone in a night train carriage, coat falling open over bare legs, stands as the train lurches and catches the overhead rail; a man steps in behind her at the stop and the crowd presses them chest to back against the door. Her head tips onto his shoulder, his hand finds her hip, neither looks at the other. Tunnel lights strobe across their faces. Slow push in through the carriage, warm light against black glass. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Fantasy trailer: two leads close the distance</b><br><sub><code>bytedance/seedance-2.5/reference-to-video</code></sub><br><br>Cast: a mixed crowd of men and women of different ages and skin tones. Cut a fantasy trailer from the thirty supplied boards: the distance between the two leads closes board by board until the last is face to face. Bodies come closer board by board until the last is skin to skin. Cinematic, heavy film grain.</td></tr>
</table>

### Seedance 2.0 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/showcase/seedance-2-0-spicy--velvet-spiral-turn.gif" alt="A backlit silhouette turns inside a red velvet stage curtain, the fabric wound across her front and her bare shoulders catching a rim of light" width="230"></a></td><td valign="top"><b>Velvet curtain spiral turn in red backlight</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4">▶ clip completo</a></sub><br><br>The velvet curtain sweeps across her as she turns inside it, wrapping her body in one continuous spiral of fabric, then billows out behind her as she steps toward the light. Her bare shoulders and the line of her back come into the glow; the curtain stays wound across her front as she moves. Backlight flares through the gap and dims. Slow push toward the silhouette, velvet rippling the whole time. Cinematic, heavy film grain, deep red and black, glowing rim light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-spicy/d65d988b0c120dd8.mp4"><img src="assets/showcase/seedance-2-0-spicy--velvet-curtain-turn-4k.gif" alt="Velvet curtain turn 4k" width="230"></a></td><td valign="top"><b>Velvet curtain turn 4k</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-spicy/d65d988b0c120dd8.mp4">▶ clip completo</a></sub><br><br>Cast: one woman. The camera stays on her silhouette as the curtain shifts around it. A silhouette turns behind a velvet curtain and the fabric sweeps across and catches there. Pure backlight, no detail beyond outline. Cinematic, heavy film grain, deep red-black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/00246b5b1923cf62.mp4"><img src="assets/showcase/seedance-2-0-spicy--fogged-mirror-lean.gif" alt="A woman in a loosely tied waffle robe wiping a streak through a fogged bathroom mirror and leaning toward her reflection" width="230"></a></td><td valign="top"><b>Wiping a fogged bathroom mirror in a waffle robe</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/00246b5b1923cf62.mp4">▶ clip completo</a></sub><br><br>She wipes a wider streak through the fogged mirror, steam curling back across the glass, then leans in closer to her reflection and exhales, the robe slipping a little further off her shoulder. Slow push toward the mirror, warm vanity bulbs, water dripping.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/31eeaff5e2446da8.mp4"><img src="assets/showcase/seedance-2-0-spicy--darkroom-safelight.gif" alt="Under a red darkroom safelight, a woman in an open shirt rocks a developer tray, then lifts a dripping print into the light and glances at the camera" width="230"></a></td><td valign="top"><b>Red-safelight darkroom with a dripping print</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/31eeaff5e2446da8.mp4">▶ clip completo</a></sub><br><br>She rocks the developer tray with the tongs, then lifts the dripping print up into the red safelight and turns it to look at it, glancing sideways at the camera. The open shirt slides further off one shoulder. Slow dolly in, safelight steady, chemical ripples reflecting on the ceiling.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/0842ecee1511d6d9.mp4"><img src="assets/showcase/seedance-2-0-spicy--library-ladder-dust.gif" alt="A woman in a cream blouse and dark skirt on a rolling library ladder pulls a heavy book from a high shelf, dust drifting through the window light as she turns and smiles" width="230"></a></td><td valign="top"><b>Library ladder, a pulled book and a plume of dust</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/0842ecee1511d6d9.mp4">▶ clip completo</a></sub><br><br>She pulls a heavy book from the top shelf, releasing a plume of dust that ignites in the window shaft, and looks down over her shoulder toward the lens as the ladder rolls a few inches along its rail. Camera cranes slowly up to meet her.</td></tr>
</table>

### Seedance 2.0

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0/2142f319602eb377.mp4"><img src="assets/showcase/seedance-2-0--same-suit-three-cities.gif" alt="A dark-haired male model in an unbuttoned charcoal suit with no shirt walks toward the camera on a night street as the wind blows the jacket open, traffic lights blurred behind him" width="230"></a></td><td valign="top"><b>Same model, same open suit, a third city at night</b><br><sub><code>bytedance/seedance-2.0/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0/2142f319602eb377.mp4">▶ clip completo</a></sub><br><br>The camera stays on him as the wind takes the jacket fully open. The same model, the same unbuttoned suit, a third city corner at night: the wind takes the jacket open as he walks toward camera, traffic streaking behind. The wind takes the jacket fully open over a bare chest as he walks in; medium close. Cinematic, shallow depth of field, heavy film grain, cold street blue.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0/b22ec0154e2e4b0d.mp4"><img src="assets/showcase/seedance-2-0--character-into-location.gif" alt="A woman in a sheer black robe over black lace walks between white sheets drying on a rooftop at sunset and glances back over her shoulder" width="230"></a></td><td valign="top"><b>Put your character on a new rooftop at sunset</b><br><sub><code>bytedance/seedance-2.0/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0/b22ec0154e2e4b0d.mp4">▶ clip completo</a></sub><br><br>The woman from @Image1, in the same sheer black robe, steps out onto the rooftop from @Image2 at sunset. She walks slowly between the drying white sheets; the wind lifts one sheet across her body and lets it fall away. She stops at the parapet, the robe sliding off one shoulder, and glances back over her shoulder into camera. Warm golden backlight, slow tracking shot, no cuts.</td></tr>
</table>

### Wan 3.0 Prime

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-prime/00cef285db666750.mp4"><img src="assets/showcase/wan-3-0-prime--balcony-robe-wind.gif" alt="At golden hour on a high hotel balcony, a man embraces a woman as the wind blows her champagne silk robe sideways over a city skyline" width="230"></a></td><td valign="top"><b>Hotel balcony embrace as the wind lifts a silk robe</b><br><sub><code>alibaba/wan-3.0-prime/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-prime/00cef285db666750.mp4">▶ clip completo</a></sub><br><br>Golden hour on a hotel balcony: she stands at the rail in a champagne silk robe that lifts and falls in the wind, and he comes up behind her and closes both arms around her waist. She leans back into him and turns her face up to his. The robe streams sideways, the city hazes gold below. Slow orbit around the pair at the rail. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-prime/e2f09083882d90e4.mp4"><img src="assets/showcase/wan-3-0-prime--lighthouse-one-night.gif" alt="A bearded keeper in a wool sweater and a woman in a rain-soaked white blouse stand at a lighthouse rail in a storm as the sweeping beam lights them and passes" width="230"></a></td><td valign="top"><b>Storm at a lighthouse, two strangers in the beam</b><br><sub><code>alibaba/wan-3.0-prime/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-prime/e2f09083882d90e4.mp4">▶ clip completo</a></sub><br><br>Cast: one man and one woman. Thirty seconds at a lighthouse through one night: the keeper and the visitor who came up out of the fog, the revolving beam sweeping across the two of them once every few seconds and leaving them in dark between passes. The visitor&#x27;s soaked shirt clings to the chest; the beam finds a bare throat, then leaves them dark; close two-shot. Foghorn and sea. Cinematic, heavy film grain, beam white in fog green.</td></tr>
</table>

### Wan 3.0

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0/067c4e121975b1cc.mp4"><img src="assets/showcase/wan-3-0--ten-boards-travel-cut.gif" alt="Two climbers in red and blue down jackets stand before a snowy peak, then a couple wrapped in one blanket outside a tent at dawn" width="230"></a></td><td valign="top"><b>Travel short cut from storyboards and an ambience track</b><br><sub><code>alibaba/wan-3.0/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0/067c4e121975b1cc.mp4">▶ clip completo</a></sub><br><br>Cast: a mixed crowd of men and women of different ages and skin tones. Cut a travel short from the ten supplied boards and the supplied ambience track: the distance between the two travellers is the thread that runs through every shot. The two travellers keep ending up shoulder to shoulder, sun-flushed skin and open collars. Cinematic, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3-0/5f28d071ae584a56.mp4"><img src="assets/showcase/wan-3-0--lingerie-window-turn.gif" alt="A woman in a short ivory silk chemise stands at a window with sheer curtains, turns slowly toward the lens and lifts her eyes to the camera" width="230"></a></td><td valign="top"><b>Dawn window turn in a silk chemise</b><br><sub><code>alibaba/wan-3.0/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3-0/5f28d071ae584a56.mp4">▶ clip completo</a></sub><br><br>She turns from the window toward the lens in one slow movement, the silk chemise settling against her as she comes round, and lifts her eyes to camera. The sheer curtain drifts across the light behind her. Slow push in, no cut, dawn light strengthening.</td></tr>
</table>

### MiniMax H3 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Sauna shoulder turn</b><br><sub><code>minimax/h3-spicy/image-to-video</code></sub><br><br>She rolls her shoulders back and stretches upward in the cedar heat, the towel at her hips sliding loose and dropping away out of frame, water running the length of her bare spine. She turns her head to look back over one shoulder into the lens, then steps forward into the billowing steam. The vapour boils up around her and swallows the far wall. Slow handheld drift following her, warm cedar light, condensation crawling down the glass. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Steam room turn</b><br><sub><code>minimax/h3-spicy/image-to-video</code></sub><br><br>She turns in the steam room, water beading down the shoulder blades, the steam swirling where she moves and closing again behind her. Water beads and runs the length of her spine as she turns, the towel slipping at the hip; close. Slow, single turn. Cinematic, shallow depth of field, heavy film grain, warm cedar and white vapour.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/3ab0c4145b288d90.mp4"><img src="assets/showcase/minimax-h3-spicy--neon-window.gif" alt="Night interior: a woman on an apartment windowsill exhaling smoke against rain-streaked glass while a red neon sign pulses across her face" width="230"></a></td><td valign="top"><b>Red neon cigarette smoke by the window blinds</b><br><sub><code>minimax/h3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/3ab0c4145b288d90.mp4">▶ clip completo</a></sub><br><br>She exhales a slow plume of smoke against the rain-streaked glass, the neon sign outside pulses red across her face, and she turns her head toward camera without changing expression. Blind shadows creep, rain runs down the window, distant traffic.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/5b1f11a28c987479.mp4"><img src="assets/showcase/minimax-h3-spicy--pov-glove-tap.gif" alt="Pov glove tap" width="230"></a></td><td valign="top"><b>Pov glove tap</b><br><sub><code>minimax/h3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/5b1f11a28c987479.mp4">▶ clip completo</a></sub><br><br>First person point of view, the camera never moves. She leans in toward the lens until her face and shoulders fill the frame, reaches out and presses one gloved fingertip against the lens, holds eye contact, then tilts her head and smiles. She keeps the black leather harness, satin camisole, long opera gloves and choker on the whole time. The hard overhead light rakes her collarbone and the background stays pure black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/c581dd66c32e8f29.mp4"><img src="assets/showcase/minimax-h3-spicy--greenhouse-mist.gif" alt="In a humid glasshouse full of banana leaves and ferns, a woman in a white cotton sundress sprays a brass mister, then wipes her brow and turns her face up to the light" width="230"></a></td><td valign="top"><b>Misting plants in a sunlit greenhouse</b><br><sub><code>minimax/h3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/c581dd66c32e8f29.mp4">▶ clip completo</a></sub><br><br>She squeezes the brass mister twice and a fine haze drifts through the green light; the big banana leaves nod under the water. She wipes the back of her wrist across her forehead, pushes a damp strand of hair off her neck and turns her face up into the sunlight coming through the glass roof, breathing out. Slow push in, humid air, droplets falling from the ferns, birdsong outside.</td></tr>
</table>

### MiniMax H3

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/e7e1d9d42f04a009.mp4"><img src="assets/showcase/minimax-h3--cup-then-two-in-one-shirt.gif" alt="A woman in an oversized white shirt holds a coffee cup at a kitchen counter while a shirtless man stands in the dim room behind her" width="230"></a></td><td valign="top"><b>Tilt up from a coffee cup to a morning-after kitchen</b><br><sub><code>minimax/h3/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/e7e1d9d42f04a009.mp4">▶ clip completo</a></sub><br><br>The cup is lifted out of frame by a hand, then the camera tilts up: she is wearing an oversized men&#x27;s shirt, and further back in the dim room a man is just getting up. Slow tilt and rack focus. Cinematic, shallow depth of field, heavy film grain, morning grey-gold.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/7efb827ad33aabfc.mp4"><img src="assets/showcase/minimax-h3--red-dress-theatre-three-angles.gif" alt="A woman in a long-sleeved red dress with a high slit and a low back walks through an ornate empty theatre onto the stage, followed from behind" width="230"></a></td><td valign="top"><b>Red slit dress crossing a theatre stage, a third angle</b><br><sub><code>minimax/h3/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/7efb827ad33aabfc.mp4">▶ clip completo</a></sub><br><br>The camera stays on her, the slit opening with every step. The same actress in the same high-slit red dress on the same theatre stage, shot from a third angle: she crosses to the proscenium and turns, the slit opening and closing with the walk, follow-spot tracking her. The slit opens over the thigh with every step, the bodice cut low at the back; medium close tracking. Cinematic, shallow depth of field, heavy film grain, crimson and gold.</td></tr>
</table>

### LTX 2.5

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/ef31b81ab1470620.mp4"><img src="assets/showcase/ltx-2-5--surf-lift-embrace.gif" alt="Surf lift embrace" width="230"></a></td><td valign="top"><b>Surf lift embrace</b><br><sub><code>lightricks/ltx-2.5/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/ef31b81ab1470620.mp4">▶ clip completo</a></sub><br><br>She turns into him in the shallows and hooks a wet arm around his neck; he takes her waist and lifts her against him, and she wraps a leg around his hip as the swell breaks around them both. Water sheets off their skin into the low sun. She leans back in his arms, throat to the light, and laughs. Handheld, camera drifting closer through the surf, gold backlight, spray in the air. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/5c83fe7b1b557753.mp4"><img src="assets/showcase/ltx-2-5--copper-tub-candlelight.gif" alt="Copper tub candlelight" width="230"></a></td><td valign="top"><b>Copper tub candlelight</b><br><sub><code>lightricks/ltx-2.5/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/5c83fe7b1b557753.mp4">▶ clip completo</a></sub><br><br>A woman lowers herself into a candlelit copper tub, water rising to her shoulders as she sinks back and tips her head against the rim, one wet arm draped over the edge. Steam climbs through the candlelight, water laps and settles, a drop falls from her fingertips to the stone floor. Slow push in along the length of the tub, warm flame light on wet skin, deep shadow. Cinematic, very shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 3.0 Pro Prime

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Shirt drawn aside</b><br><sub><code>alibaba/wan-3.0-pro-prime/image-to-video</code></sub><br><br>Her hand comes into frame and touches the folds of the shirt, then lets them fall back. The bud between the folds opens a little in the warm air. Slow push in along the shirt, low gold light raking across the fabric, very shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro-prime/5143df366cca3f75.mp4"><img src="assets/showcase/wan-3-0-pro-prime--dancer-three-stages-4k.gif" alt="A dancer in layered grey-white chiffon spins on a dark stage as a follow spot from behind turns the skirt translucent and glowing" width="230"></a></td><td valign="top"><b>Backlit dancer spinning in translucent chiffon</b><br><sub><code>alibaba/wan-3.0-pro-prime/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro-prime/5143df366cca3f75.mp4">▶ clip completo</a></sub><br><br>The same dancer, the same layered chiffon, a third stage: the follow spot comes from behind this time and the fabric goes translucent as she turns through it. The chiffon glows as the backlight comes up; close. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 3.0 Pro

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro/57c86b075f9fadb0.mp4"><img src="assets/showcase/wan-3-0-pro--same-two-three-times.gif" alt="White sheets in morning light, then the same couple on a sofa at night by a city window as he lights her cigarette" width="230"></a></td><td valign="top"><b>Same couple, same apartment, different times of day</b><br><sub><code>alibaba/wan-3.0-pro/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro/57c86b075f9fadb0.mp4">▶ clip completo</a></sub><br><br>The camera stays on the same two people in all three. The same two people, the same apartment, three times of day: morning light across the bed, dusk with the two of them in the kitchen, night with the two of them on the balcony sharing one cigarette. Same faces, same room, rendered at 4K. Cinematic, shallow depth of field, heavy film grain, warm interior against cold window light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-pro/115148ffd12fa417.mp4"><img src="assets/showcase/wan-3-0-pro--silk-shoulder-turn.gif" alt="A woman in a champagne satin slip dress by a rain-streaked window at night turns to face the camera" width="230"></a></td><td valign="top"><b>Rainy-window turn as a silk strap slips</b><br><sub><code>alibaba/wan-3.0-pro/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-pro/115148ffd12fa417.mp4">▶ clip completo</a></sub><br><br>She turns her shoulders slowly toward camera, the silk catching the light, her breath settling as she stops. Slow push-in, one hard key from the left, rain on the window behind her.</td></tr>
</table>

### MiniMax H3 LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/8df03dd8cf5dbff7.mp4"><img src="assets/showcase/minimax-h3-lora--hotel-window-dawn.gif" alt="Hotel window dawn" width="230"></a></td><td valign="top"><b>Hotel window dawn</b><br><sub><code>minimax/h3-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/8df03dd8cf5dbff7.mp4">▶ clip completo</a></sub><br><br>From this exact frame: he turns away from the window, walks toward the camera tying the belt of his robe, and stops with a half smile. Slow handheld push-in. Audio: morning city hum through the glass, bare feet on carpet.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/12d5eb4bbb9c2d0d.mp4"><img src="assets/showcase/minimax-h3-lora--character-lora-plus-references.gif" alt="Character lora plus references" width="230"></a></td><td valign="top"><b>Character lora plus references</b><br><sub><code>minimax/h3-lora/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/12d5eb4bbb9c2d0d.mp4">▶ clip completo</a></sub><br><br>Picture 1 is the woman, Picture 2 is the hotel room. She walks into the room at night, drops her coat on the bed and turns to the mirror, pushing her hair back. Slow dolly. Audio: door closing, heels on carpet, a low bass line from the next room.</td></tr>
</table>

### HappyHorse 1.1

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/happyhorse-1-1/4d22782ccf7d7385.mp4"><img src="assets/showcase/happyhorse-1-1--sea-walk-wet-slip.gif" alt="Sea walk wet slip" width="230"></a></td><td valign="top"><b>Sea walk wet slip</b><br><sub><code>alibaba/happyhorse-1.1/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/happyhorse-1-1/4d22782ccf7d7385.mp4">▶ clip completo</a></sub><br><br>A woman walks out of the sea at dusk in a soaked slip that clings to every line of her, wringing her hair out over one shoulder as she comes. She stops ankle deep, plants her feet, and looks straight down the lens while the swell breaks white behind her and drags back. Wind takes the wet fabric against her. Slow push in from the waterline, low gold light through spray. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Seedance 2.0 Mini Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini-spicy/0e9a1972d379e9f6.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--robe-tie-pulled.gif" alt="Robe tie pulled" width="230"></a></td><td valign="top"><b>Robe tie pulled</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini-spicy/0e9a1972d379e9f6.mp4">▶ clip completo</a></sub><br><br>Cast: two women. The camera stays on her waist and the hand at the belt, nothing above the ribs. Close on the waist only: another hand rests on the knotted belt of the bathrobe and stays there. The frame never goes above the ribs or below the hip. Cinematic, very shallow depth of field, heavy film grain, low warm light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/a5cd491837869375.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--fridge-glow-exit.gif" alt="A woman in an oversized white shirt in the blue glow of an open refrigerator at night, closing the door with her hip as the room goes dark" width="230"></a></td><td valign="top"><b>Late-night fridge glow, then lights out</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/a5cd491837869375.mp4">▶ clip completo</a></sub><br><br>She lowers the bottle, shuts the refrigerator door with her hip and the room drops to darkness except for a thin sliver of street light, then she pads barefoot out of frame. Static camera, cold blue to warm black, fridge hum and bare feet on tile.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/c839b6bc8eb47b74.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--fogged-shower-streak.gif" alt="Behind fogged shower glass, a woman in a black bikini drags her palm down the steamed pane, backlit by a bright window as steam rolls across the frame" width="230"></a></td><td valign="top"><b>Hand streak on a fogged shower glass</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/c839b6bc8eb47b74.mp4">▶ clip completo</a></sub><br><br>Locked-off camera, no move. Steam keeps rolling across the frame and the glass fogs further. She presses her palm flat on the glass and drags it slowly downward, leaving one clear streak that immediately re-fogs, then turns her head and sweeps her wet hair across to the other shoulder. She keeps the black bikini on the whole time. Water runs down the outside of the glass, the backlight stays blown out and cold, and her body stays only a soft outline through the fog. No camera move, no cut.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/e03de02a8cc1d691.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--van-door-sunrise.gif" alt="A woman sits in the open side door of a white van in a red crop top and flannel shirt, sipping from a mug as the sun rises over a desert of mesas" width="230"></a></td><td valign="top"><b>Desert sunrise coffee from an open van door</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/e03de02a8cc1d691.mp4">▶ clip completo</a></sub><br><br>She pulls the flannel closed against the cold, sips from the mug and lets her head tip back into the sunrise with her eyes closed. Steam off the mug catches the rim light; the sun climbs and the orange rim strengthens. Camera drifts slowly in from outside the van.</td></tr>
</table>

### Seedance 2.0 Mini

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/3968a086dd25eadf.mp4"><img src="assets/showcase/seedance-2-0-mini--latte-then-robe.gif" alt="A latte on a sunlit white kitchen counter is lifted out of frame as the camera tilts up to a woman in a loose white bathrobe who smiles softly at the viewer" width="230"></a></td><td valign="top"><b>Tilt up from a latte to a morning bathrobe</b><br><sub><code>bytedance/seedance-2.0-mini/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/3968a086dd25eadf.mp4">▶ clip completo</a></sub><br><br>Cast: one woman. The latte is lifted away and the camera tilts up to a woman in a white terry bathrobe tied closed, leaning on the counter with a sleepy half-smile toward the lens, morning light coming in hard from the side. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/8cc520660c695a11.mp4"><img src="assets/showcase/seedance-2-0-mini--same-couple-three-angles.gif" alt="A backlit couple in white shirts sit close on a park bench under trees, foreheads together, then settle back as she drapes her legs across his lap" width="230"></a></td><td valign="top"><b>Same couple on a park bench from a new angle</b><br><sub><code>bytedance/seedance-2.0-mini/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/8cc520660c695a11.mp4">▶ clip completo</a></sub><br><br>The same couple on the same park bench from a third angle: they settle back into each other against a low backlight that fuses the two outlines into one. Her bare legs come across his lap as they settle back; medium close. Cinematic, shallow depth of field, heavy film grain, late-gold palette.</td></tr>
</table>

### Wan 2.7 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/showcase/wan-2-7-spicy--silk-draught-pull.gif" alt="A gust drags cream silk off a woman’s bare shoulder and back on a beach at dusk, then blows it back across her as she turns her head toward the light." width="230"></a></td><td valign="top"><b>A gust pulls silk off the shoulder, the camera follows the fabric</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4">▶ clip completo</a></sub><br><br>The draught drags the silk off her in one continuous pull, baring the whole slope of the shoulder and the line of the spine as the fabric slips away, then a second gust throws it back across her hip. She turns her head toward the light as the silk settles against her arm. The camera slides slowly along the body following the silk. Low gold light, dust turning in the beam, very shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.7-spicy/287f6caf66e84d8c.mp4"><img src="assets/showcase/wan-2-7-spicy--silk-drifts-own-track.gif" alt="Close-up of a woman’s bare back and shoulder on a dim beach as a length of cream silk drifts across it in the wind." width="230"></a></td><td valign="top"><b>Close-up: silk drifting across a bare back in low gold light</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.7-spicy/287f6caf66e84d8c.mp4">▶ clip completo</a></sub><br><br>Cast: one woman. The camera stays on her as the silk crosses her. Silk is drawn slowly across the body by the draught; cut to the supplied slow music track. The silk drags across a bare shoulder, the waist and the whole line of the spine in turn; very close. Cinematic, very shallow depth of field, heavy film grain, low gold light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/c1dab148533285b8.mp4"><img src="assets/showcase/wan-2-7-spicy--backstage-mirror-turn.gif" alt="A showgirl in a fringed emerald sequin leotard finishes adjusting a shoulder strap at a bulb-lit backstage mirror, then turns her head to camera and raises an eyebrow before stepping out of frame." width="230"></a></td><td valign="top"><b>Showgirl checks the mirror backstage, then turns to camera</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/c1dab148533285b8.mp4">▶ clip completo</a></sub><br><br>She finishes adjusting the sequin strap, checks herself in the bulb-lit mirror, then turns her head to camera and raises one eyebrow before stepping out of frame toward the stage. Bulbs flicker, feathers stir in the draft, smoke drifts, muffled orchestra and applause building behind the wall.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/09b29059d5b8b826.mp4"><img src="assets/showcase/wan-2-7-spicy--dune-silk-throw.gif" alt="A woman in a dark slip dress throws a huge sheet of indigo silk overhead on a desert dune at night, a lantern at her feet and the Milky Way above." width="230"></a></td><td valign="top"><b>Night dune: a sheet of indigo silk thrown into the wind</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/09b29059d5b8b826.mp4">▶ clip completo</a></sub><br><br>She sweeps the huge sheet of indigo silk down and across in front of her, then throws it back up so it billows overhead and fills the sky, turning under it with her head tipped back. Sand streams off the crest of the dune in the wind and the lantern flame gutters, throwing her shadow long across the ripples. Slow arc around her, starfield steady above, wind and snapping fabric.</td></tr>
</table>

### LTX 2.3 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Steam mirror towel</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code></sub><br><br>She presses both palms to the fogged glass and drags them slowly down, carving two clear streaks, then steps in and leans her forehead against the mirror, rolling her shoulders back and letting the wet hair fall away from her neck. Her reflection sharpens through the streaks and her eyes open toward the lens. The towel stays knotted above the chest throughout. Steam rolls across the ceiling, water beads and runs down the glass, the bulbs flicker. Slow push toward the mirror. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/6d4795df0ff9089b.mp4"><img src="assets/showcase/ltx-2-3-spicy--rain-car.gif" alt="Rain car" width="230"></a></td><td valign="top"><b>Rain car</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/6d4795df0ff9089b.mp4">▶ clip completo</a></sub><br><br>She turns further toward the driver&#x27;s seat, wet shirt clinging as she moves, pushes a soaked strand of hair back and mouths something with a tired smile. Rain streams down the windscreen, neon reflections crawl across the glass, wipers sweep once.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/f719693ce2b6ad2b.mp4"><img src="assets/showcase/ltx-2-3-spicy--hearth-chaise-heels.gif" alt="Hearth chaise heels" width="230"></a></td><td valign="top"><b>Hearth chaise heels</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/f719693ce2b6ad2b.mp4">▶ clip completo</a></sub><br><br>The fire surges and the orange light flickers across her bare legs and the green velvet. She uncrosses her ankles and re-crosses them the other way, the pointed heels tipping, then slides her free hand slowly up the black silk robe and draws the hem a little higher on her thigh before letting it settle. She tips her head back against the chaise, keeps her eyes on the camera and one corner of her mouth lifts. Locked-off camera, no camera move, logs cracking and popping.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/0eccc200eb648e68.mp4"><img src="assets/showcase/ltx-2-3-spicy--drive-in-bonnet.gif" alt="Drive in bonnet" width="230"></a></td><td valign="top"><b>Drive in bonnet</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/0eccc200eb648e68.mp4">▶ clip completo</a></sub><br><br>The projector beam flickers and the blank screen pulses brighter then dimmer, washing her face in shifting blue light. She uncrosses her ankles on the warm bonnet, pushes herself up on one elbow, tips the paper cup back and grins toward the camera, then pulls the striped blanket up over one knee. Headlights sweep past behind her and the dusk sky deepens. Locked-off wide shot, no camera move, crickets and a distant tinny speaker.</td></tr>
</table>

### LTX 2.3 Spicy LoRA

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Vhs grain two on bed</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code></sub><br><br>Cast: one man and one woman. The camera stays on the two of them from the shoulders up, and never tilts below the collarbone. Push the whole frame to 1990s VHS: two people sitting at the edge of an unmade bed in low lamplight, one bare shoulder and a sheet held at the chest, her head tipping onto his shoulder; scan lines, chroma bleed and tape wobble crawl across the image. Handheld, low light, heavy analogue grain, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/673813a5c0f4f554.mp4"><img src="assets/showcase/ltx-2-3-spicy-lora--neon-rooftop.gif" alt="Neon rooftop" width="230"></a></td><td valign="top"><b>Neon rooftop</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/673813a5c0f4f554.mp4">▶ clip completo</a></sub><br><br>The glowing cyan circuits along her arms and spine pulse in sequence as she completes the turn, holographic billboards flickering behind her, rain hissing on the rooftop. Slow arc around her silhouette, volumetric neon fog, synth bass swell.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/6470b2a1b89cbe1c.mp4"><img src="assets/showcase/ltx-2-3-spicy-lora--gouache-poster-pier.gif" alt="Gouache poster pier" width="230"></a></td><td valign="top"><b>Gouache poster pier</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/6470b2a1b89cbe1c.mp4">▶ clip completo</a></sub><br><br>The painted illustration comes alive without losing its flat printed look: the striped umbrella canopy ripples in the sea breeze, her hair lifts and the gulls glide across the turquoise sky. She lowers her sunglasses with one finger, glances over the top of them at the camera and smiles, then swings the dangling sandal off her toe. The sea sparkles behind the bathing huts. Gentle slow push in, gouache brush texture and screen-print grain held stable throughout.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/e151f11d0696350f.mp4"><img src="assets/showcase/ltx-2-3-spicy-lora--strength-sweep.gif" alt="Strength sweep" width="230"></a></td><td valign="top"><b>Strength sweep</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/e151f11d0696350f.mp4">▶ clip completo</a></sub><br><br>She drives up out of the squat, the bar flexing on her shoulders, chalk dust bursting off her hands into the lamp beam, and racks the bar with a heavy metallic clang before straightening and exhaling at the lens. Handheld, slight shake on the rack, haze rolling through the light.</td></tr>
</table>

### Seedance 2.0 Fast Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-fast-spicy/518ad024b9b8a2dc.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--pool-cannonball-crowd.gif" alt="At a floodlit outdoor pool at night, swimmers in competition suits crouch on the edge and dive in one after another, spray bursting white" width="230"></a></td><td valign="top"><b>Floodlit night pool, swimmers diving one after another</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-fast-spicy/518ad024b9b8a2dc.mp4">▶ clip completo</a></sub><br><br>Cast: a mixed crowd of men and women of different ages and skin tones. A night pool: one after another they hit the water, the splashes blowing up white in the floodlights, the surface never settling; someone hauls themselves out at the near edge, soaked. Wet swimwear clinging as one of them hauls out at the near edge, water running off the shoulders; close at the lip of the pool. Cinematic, heavy film grain, chlorine cyan and floodlight white.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/1461db51e6ecc0b1.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--balcony-laundry-turn.gif" alt="A woman in a bikini top and denim cutoffs pinning a sheet to a washing line on a sunlit balcony, turning to camera with a grin" width="230"></a></td><td valign="top"><b>Sunny balcony laundry turn with a grin</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/1461db51e6ecc0b1.mp4">▶ clip completo</a></sub><br><br>The sheet billows and drops as she pins it to the line, then she turns fully toward camera, pushes windblown hair off her face and grins. Bright midday sun, fabric snapping in the breeze, cicadas and distant sea.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/7eaa3a9aae761e79.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--pillow-pov-lean.gif" alt="Pillow pov lean" width="230"></a></td><td valign="top"><b>Pillow pov lean</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/7eaa3a9aae761e79.mp4">▶ clip completo</a></sub><br><br>First person point of view, the camera stays where it is on the pillow and does not move. She lowers herself closer toward the lens, her long hair falling forward around the edges of the frame, holds eye contact and smiles. She keeps the black lace top and the black satin robe on the whole time and stays fully dressed. Candlelight flickers behind her; the background stays black. Only her movement, no camera move, no cut.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/09bed565d0700cae.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--pool-hall-break.gif" alt="A woman in a black satin slip dress leans over a green pool table under hanging lamps, breaks the rack, then straightens up and looks toward the camera through drifting smoke" width="230"></a></td><td valign="top"><b>Pool hall break shot in a black satin slip dress</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/09bed565d0700cae.mp4">▶ clip completo</a></sub><br><br>She strikes the break — the cue drives forward, the rack scatters across the felt, and she straightens up and looks at the lens as the balls settle. Smoke rolls through the lamp beam from the impact. Camera holds low at table height.</td></tr>
</table>

### Vidu Q3 Turbo

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>One still push in</b><br><sub><code>vidu/q3-turbo/image-to-video</code></sub><br><br>The camera stays on her the whole way in. Slow push in on the same still, and nothing else: the frame tightens by degrees. The frame tightens until it holds only a bare shoulder and the sheet at her hip. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Vidu Q3 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/334a9b5ae943a9b6.mp4"><img src="assets/showcase/vidu-q3-spicy--wet-hair-lift-gaze.gif" alt="Wet hair lift gaze" width="230"></a></td><td valign="top"><b>Wet hair lift gaze</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/334a9b5ae943a9b6.mp4">▶ clip completo</a></sub><br><br>She lifts her face slowly out of the fall of wet hair, water running off her chin and throat, and opens her eyes straight into the lens. Her lips part on an exhale and she tilts her head, hair peeling away from her cheek in wet strands, one bare shoulder rolling forward into frame. Slow push in, water still dripping, cold blue light, condensation in the air. Cinematic, very shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/2d08be3cd91a6d59.mp4"><img src="assets/showcase/vidu-q3-spicy--ryokan-pour.gif" alt="Ryokan pour" width="230"></a></td><td valign="top"><b>Ryokan pour</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/2d08be3cd91a6d59.mp4">▶ clip completo</a></sub><br><br>She finishes pouring, sets the flask down and lifts her eyes to camera with a small smile, steam rising from the cup, the yukata sliding a fraction lower on her shoulder. Paper shoji glow, evening cicadas, very slow push-in.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/7b5a55df8a3bffec.mp4"><img src="assets/showcase/vidu-q3-spicy--booth-heel-drop.gif" alt="Booth heel drop" width="230"></a></td><td valign="top"><b>Booth heel drop</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/7b5a55df8a3bffec.mp4">▶ clip completo</a></sub><br><br>She rolls the black stiletto off her pointed toes and it drops onto the velvet, then draws that leg down along the back of the booth and crosses it over the other. Her other hand pulls the fallen strap back up onto her bare shoulder and she holds the look into the lens, lifting her chin. The red neon on the right breathes brighter and the amber sconce flickers. Slow low tracking dolly moving in past the edge of the table, quiet bar room tone.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/3a5edfd4e36921ff.mp4"><img src="assets/showcase/vidu-q3-spicy--wheel-and-hands.gif" alt="Wheel and hands" width="230"></a></td><td valign="top"><b>Wheel and hands</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/3a5edfd4e36921ff.mp4">▶ clip completo</a></sub><br><br>The wheel keeps spinning and the clay wall rises under her hands, then she opens the rim with her thumbs and it flares outward. She lifts one wet hand off, wipes her forearm across her cheek leaving a grey streak, and glances up at the camera with a small smile before going back to the pot. Slip water runs down the wheel head. Slow push in, wheel hum and wet clay.</td></tr>
</table>

### Vidu Q3

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Blind light reach</b><br><sub><code>vidu/q3/image-to-video</code></sub><br><br>The blind slats of light slide up their bare backs as one of them shifts and reaches across the sheets for the other. The far one turns their face into the pillow. Slow push along the bed, dust turning in the light bars, curtain breathing at the window. Cinematic, shallow depth of field, heavy film grain, warm morning light.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Blinds light two bodies</b><br><sub><code>vidu/q3/image-to-video</code></sub><br><br>Cast: one man and one woman. Locked-off camera, tight on two bare shoulders and upper backs with a white sheet drawn up over both of them from the waist down, so the sheet fills the lower third of the frame. Nothing moves but the light: hard blind stripes travel slowly across their shoulders and across the sheet as the sun drops. Cinematic, heavy film grain, amber stripes on shadow, restrained and tasteful.</td></tr>
</table>

### Seedance 1.5 Pro Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro-spicy/da11e751bcf25dd0.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--silk-breathing-locked.gif" alt="Silk breathing locked" width="230"></a></td><td valign="top"><b>Silk breathing locked</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro-spicy/da11e751bcf25dd0.mp4">▶ clip completo</a></sub><br><br>Cast: one man and one woman. Locked-off camera, absolutely no movement: the silk sheet over the two of them rises and falls with their breathing, a bare shoulder and one arm outside it, nothing else in the frame moves. Cinematic, shallow depth of field, heavy film grain, low warm lamp light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/c16f53eee15a669f.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--locked-hotel-sheets.gif" alt="Locked hotel sheets" width="230"></a></td><td valign="top"><b>Locked hotel sheets</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/c16f53eee15a669f.mp4">▶ clip completo</a></sub><br><br>Camera stays locked off. Her crossed ankles rock slowly and one foot flexes. She slides one hand out from behind her head and rests it on her stomach, her fingers tracing a slow circle on the camisole, while her other hand stays tucked behind her head. Her chest rises with a long breath. Nothing else in frame moves except the light shifting on the sheets.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/f22c2b64fc387ebf.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--stocking-and-heel.gif" alt="Stocking and heel" width="230"></a></td><td valign="top"><b>Stocking and heel</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/f22c2b64fc387ebf.mp4">▶ clip completo</a></sub><br><br>Slow push-in along the floor from the dangling stiletto heel up toward her hands. She rolls the black stocking the rest of the way down to her ankle and slips it off over her toes, flexes her bare foot, then lets the patent heel swing twice on the toes of her other foot and drops it to the floor. She stays in the black lace outfit the whole time. Hard overhead key light, everything else stays black, extremely shallow focus. Continuous dolly, no cut.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/45a9fa4e438db221.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--tail-sweep-arc.gif" alt="Tail sweep arc" width="230"></a></td><td valign="top"><b>Tail sweep arc</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/45a9fa4e438db221.mp4">▶ clip completo</a></sub><br><br>The fluffy tail sweeps slowly across the rug behind her. She shifts her weight on her knees, tucks a strand of hair behind her ear and holds the camera&#x27;s gaze over her shoulder, then breaks into a small laugh and looks away. Warm bedside lamp light, soft shadows moving on the rug. Slow arc around to her left.</td></tr>
</table>

### Seedance 1.5 Pro

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro/251525c66c0fb58a.mp4"><img src="assets/showcase/seedance-1-5-pro--seance-candle-bare-feet.gif" alt="Seance candle bare feet" width="230"></a></td><td valign="top"><b>Seance candle bare feet</b><br><sub><code>bytedance/seedance-1.5-pro/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro/251525c66c0fb58a.mp4">▶ clip completo</a></sub><br><br>Cast: one woman. Locked-off camera, absolutely no movement: a woman lies back across a chaise in a candlelit parlour, one bare foot hooked over the arm of it, the other knee drawn up, her robe fallen open at the knee. The candle flames lean and recover and their shadows sway up her calf and thigh; nothing else in the frame moves. Cinematic, heavy film grain, candle gold in near black.</td></tr>
</table>

### Wan 2.6 Flash

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-flash/6b7cd6d830945dc6.mp4"><img src="assets/showcase/wan-2-6-flash--three-angles-one-scene.gif" alt="A man and a woman lean across a bar table in conversation, covered from three angles that end on their two faces almost touching." width="230"></a></td><td valign="top"><b>One bar conversation covered from three ever-closer angles</b><br><sub><code>alibaba/wan-2.6-flash/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-flash/6b7cd6d830945dc6.mp4">▶ clip completo</a></sub><br><br>Cast: one man and one woman. The camera stays on the two of them, closer with every angle. The same quiet conversation covered from three angles, each one closer than the last, ending on the two faces almost touching. Each angle closer: shoulders, then throats, then only the space between two mouths. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 2.6 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Green tub turn in</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code></sub><br><br>One turns in the water and moves behind the other. The front one tips her head back onto the other&#x27;s shoulder and they turn their faces together. Framed from behind and above the shoulder line, the water surface holding steady at chest height the whole time. The bath swells against the green enamel, steam tearing and closing between their faces. Slow push in over the rim. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-spicy/3271dbc80ff97d8d.mp4"><img src="assets/showcase/wan-2-6-spicy--bathtub-knees-steam.gif" alt="Two pairs of knees rise above the waterline of a green enamel bathtub as steam curls off the water." width="230"></a></td><td valign="top"><b>Steam and knees above the waterline of a green bathtub</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-spicy/3271dbc80ff97d8d.mp4">▶ clip completo</a></sub><br><br>Cast: two women. The camera stays on the knees and the waterline. Two pairs of knees cross above the bathtub waterline, steam curling off, the water&#x27;s reflection shifting on the tiles. Steam curls off wet knees and shoulders; one knee slides against the other under the surface. Everything below the surface stays in the water. Cinematic, shallow depth of field, heavy film grain, tile green and steam white.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/2ff58bcb117213d6.mp4"><img src="assets/showcase/wan-2-6-spicy--pool-rise.gif" alt="A swimmer rises out of a rooftop infinity pool at blue hour, water running off her shoulders as she slicks her wet hair back with both hands and opens her eyes toward camera, city towers glowing behind." width="230"></a></td><td valign="top"><b>Rooftop pool rise at blue hour, slicking hair back</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/2ff58bcb117213d6.mp4">▶ clip completo</a></sub><br><br>She rises further out of the water, sheets of it running off her shoulders and swimsuit, slicks her wet hair straight back with both hands and opens her eyes toward camera, droplets scattering. Blue-hour city towers glow behind, slow-motion water detail, ambient pool lap and distant traffic.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/65c8f2b8dbc700bc.mp4"><img src="assets/showcase/wan-2-6-spicy--slatted-light-pov.gif" alt="First-person view down a red satin bed at legs in black lace-top stockings, bars of light from a window blind moving across them." width="230"></a></td><td valign="top"><b>POV: slatted morning light moving across stockinged legs</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/65c8f2b8dbc700bc.mp4">▶ clip completo</a></sub><br><br>Her toes flex and hook deeper into the silk, one knee slowly straightening, the sheets sliding and rippling under her legs. The slatted bars of light creep across her thighs as the blind stirs in the draught. Handheld point-of-view sway, warm red and gold, quiet morning room tone.</td></tr>
</table>

### Wan 2.6

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-6/200161e5024b4f12.mp4"><img src="assets/showcase/wan-2-6--counter-slide-approach.gif" alt="A woman with wet hair in an oversized white shirt slides off a dark kitchen counter and walks toward the camera, a wine glass and a steaming pan behind her." width="230"></a></td><td valign="top"><b>Late-night kitchen: she slides off the counter toward the lens</b><br><sub><code>alibaba/wan-2.6/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-6/200161e5024b4f12.mp4">▶ clip completo</a></sub><br><br>She sets the glass down, slides off the counter onto her feet and walks toward the lens, the oversized shirt swinging open at the hem over bare legs while the front stays crossed and buttoned at the chest. She stops close, tips her head, and pushes her wet hair back off her face. Wine swings in the abandoned glass, steam drifts from a pan behind her. Slow push in, framed from the ribs up, warm downlight against black. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.6/4bbb55b80b0482d7.mp4"><img src="assets/showcase/wan-2-6--cast-three-clips.gif" alt="A man in a wet overcoat and a woman in a rain-soaked white shirt meet in a neon-lit brick alley in the rain and pull close." width="230"></a></td><td valign="top"><b>Recast a couple from a reference clip into a neon rain street</b><br><sub><code>alibaba/wan-2.6/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.6/4bbb55b80b0482d7.mp4">▶ clip completo</a></sub><br><br>Cast: one man and one woman. Cast the two people and the street from the supplied clips into a new scene: the same pair now meet under neon in the rain. The two of them end up pressed together under the neon, clothes soaked through. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 2.5

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-5/ded29f1cc881124b.mp4"><img src="assets/showcase/wan-2-5--dressing-room-robe.gif" alt="Dressing room robe" width="230"></a></td><td valign="top"><b>Dressing room robe</b><br><sub><code>alibaba/wan-2.5/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-5/ded29f1cc881124b.mp4">▶ clip completo</a></sub><br><br>Backstage in a dressing room: a dancer in a sequined costume reaches for a silk robe and pulls it on over her costume as she turns to the bulb-lit mirror. She catches her own eye, then looks back over her bare shoulder toward the lens. Bulbs flicker, feathers stir in the draft, smoke drifts through the beam. Slow push toward the mirror. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 2.2 Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy/0a7d0b59032f86aa.mp4"><img src="assets/showcase/wan-2-2-spicy--wolf-turn-and-look-back.gif" alt="A woman with wolf ears, seen from behind in a moonlit forest, turns her bare shoulders and looks back over her shoulder with glowing gold eyes." width="230"></a></td><td valign="top"><b>First and last frame: a wolf-eared glance back in moonlight</b><br><sub><code>alibaba/wan-2.2-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy/0a7d0b59032f86aa.mp4">▶ clip completo</a></sub><br><br>Start on her back, wolf ears and bare shoulders in moonlight, and end on the supplied final frame: she looks back over her shoulder, irises gone gold. Bare back and wolf ears in the moonlight, shoulder blades shifting as she turns. Cinematic, shallow depth of field, heavy film grain, moon silver and forest black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/38f04ab8005e193f.mp4"><img src="assets/showcase/wan-2-2-spicy--gym-dawn-breath.gif" alt="A woman lowers her leg off a gym bench at dawn, rolls her shoulders back and straightens up, wiping sweat from her collarbone as low window light moves across the concrete behind her." width="230"></a></td><td valign="top"><b>Dawn gym cooldown: stretch, shoulder roll, catch a breath</b><br><sub><code>alibaba/wan-2.2-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/38f04ab8005e193f.mp4">▶ clip completo</a></sub><br><br>She lowers her leg off the bench, rolls her shoulders back and straightens up, wiping sweat from her collarbone with the back of her wrist, chest rising as she catches her breath. Dawn light shifts across the concrete, dust drifting in the beam.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/showcase/wan-2-2-spicy--one-pace-closer.gif" alt="A woman in an open white shirt leans across a dark bed toward the camera, fingertip at her lip, then breaks into a slow half smile; lamp glow and a blue window behind." width="230"></a></td><td valign="top"><b>Locked-camera bedroom shot: one slow pace closer, then a smile</b><br><sub><code>alibaba/wan-2.2-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4">▶ clip completo</a></sub><br><br>She crawls one slow pace closer toward the viewer, weight shifting onto the reaching hand, the open white shirt sliding further down off her shoulder. She draws her fingertip away from her lip, tips her head to the side and holds the viewer&#x27;s gaze, then breaks into a slow half smile. Her hair swings forward. Warm lamp glow on the left, cold blue window behind, no camera move, shallow focus, quiet room tone.</td></tr>
</table>

### Wan 2.2 Spicy LoRA

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/928d00c859a4fc39.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--three-loras-stacked.gif" alt="A woman in a champagne satin wrap turns in a dark gilded room; the fabric slips off one shoulder and her bare back catches the gold key light." width="230"></a></td><td valign="top"><b>Three LoRAs stacked on one slow satin turn</b><br><sub><code>alibaba/wan-2.2-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/928d00c859a4fc39.mp4">▶ clip completo</a></sub><br><br>With all three LoRAs stacked - style, fabric and lighting - she turns on the spot and the satin catches the dark gold key light. The satin slides off one shoulder as she turns, the dark gold key raking the bare back. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/d48338ae0374953f.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--extend-the-stack.gif" alt="The satin wrap falls away as the woman turns from the gold light and walks off with her bare back to the camera, continuing the earlier clip for eight more seconds." width="230"></a></td><td valign="top"><b>Extend a clip eight more seconds with the same LoRAs</b><br><sub><code>alibaba/wan-2.2-spicy-lora/video-extend</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/d48338ae0374953f.mp4">▶ clip completo</a></sub><br><br>She turns away from the light and the satin falls off the other shoulder. Continue the clip for another eight seconds with the same LoRAs attached: the stillness breaks and she turns away from the light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/b47e28f395798f05.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--tail-rise-continue.gif" alt="A woman in fox ears, a black silk robe and long gloves kneels on a velvet rug in a crimson room beside a table lamp, a plush fox tail curled behind her." width="230"></a></td><td valign="top"><b>Continue a clip: fox-ear costume in crimson lamplight</b><br><sub><code>alibaba/wan-2.2-spicy-lora/video-extend</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/b47e28f395798f05.mp4">▶ clip completo</a></sub><br><br>Continuing the same unbroken take: she rises up from her knees, the plush fox tail sweeping in a slow arc across the velvet rug behind her, gathers the black silk robe closed with one gloved hand and turns fully toward the camera, the tail settling against her leg; she tilts her head and holds the look. One continuous move with no cut, deep crimson lamp light, soft shadows, film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/e19d8c98cdbfd616.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--candlelit-crypt.gif" alt="Candle flames sway across a crypt as a painted elven sorceress lifts her hand from a stone armrest, turns toward camera and a sheer lace sleeve slides down her forearm, embers drifting upward." width="230"></a></td><td valign="top"><b>Gothic sorceress rises from a candlelit throne</b><br><sub><code>alibaba/wan-2.2-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/e19d8c98cdbfd616.mp4">▶ clip completo</a></sub><br><br>The candle flames gutter and sway across the crypt as she lifts her hand from the armrest, turns her head toward camera and the sheer lace sleeve slides down her forearm, embers drifting upward through the frame. Slow push-in, deep crimson and obsidian, low choral drone.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/5250c042ec231d01.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--airbrush-pool-hold.gif" alt="A flat airbrush-style illustration of a woman in a black bikini sitting at the edge of a neon-lit rooftop pool, pushing her wet hair back as the water ripples." width="230"></a></td><td valign="top"><b>Airbrushed pool illustration that stays flat when it moves</b><br><sub><code>alibaba/wan-2.2-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/5250c042ec231d01.mp4">▶ clip completo</a></sub><br><br>The illustration comes alive while keeping its flat airbrushed print look: the pool water ripples and laps at her legs, the neon arcs pulse and their reflections wobble across the surface, water keeps running off her hair and shoulders. She lowers her chin from the sky, opens her eyes and turns her face toward the viewer, then draws one hand up out of the water and slowly pushes her wet hair back off her shoulder. Gentle slow push in, banded gradient shading, halftone and print grain held stable throughout, black bikini stays on, no drift toward photorealism.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/658e7278d63095b1.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--closing-hold.gif" alt="A woman in a long dark coat stands at a wall of rain-streaked windows at night, city lights blurred beyond, and turns her head back over her shoulder." width="230"></a></td><td valign="top"><b>End an extended clip on a settled hold for the next join</b><br><sub><code>alibaba/wan-2.2-spicy-lora/video-extend</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/658e7278d63095b1.mp4">▶ clip completo</a></sub><br><br>She stops at the top of the stairs, turns her head back toward the crypt and holds still as the candles steady behind her. Camera locked.</td></tr>
</table>

### Wan 2.2 LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-lora/94000f2077317c6c.mp4"><img src="assets/showcase/wan-2-2-lora--rooftop-walk.gif" alt="An illustrated office worker pushes off a rooftop railing, straightens the blazer over her shoulder and walks along the roof, city lights and a vending machine glow sliding past behind her." width="230"></a></td><td valign="top"><b>Anime rooftop walk at night with a smooth tracking move</b><br><sub><code>alibaba/wan-2.2-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-lora/94000f2077317c6c.mp4">▶ clip completo</a></sub><br><br>She pushes off the railing, straightens her blazer over one shoulder and turns to walk along the rooftop, city lights and the vending machine glow sliding past behind her, hair lifting in the night wind. Smooth tracking move, anime cel-shaded style held stable.</td></tr>
</table>

### Qwen Image 2.1

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Slats slip dress</b><br><sub><code>alibaba/qwen-image-2.1/edit</code></sub><br><br>Keep the bed, the linen, the blinds, the striped light and her pose exactly as they are. Dress her in a sheer ivory slip that the striped light passes through, the strap fallen off one shoulder, the hem gathered at her thigh. Match the existing grain, colour grade and the way the sun falls across the fabric. Change nothing else in the frame.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Boudoir window slats</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code></sub><br><br>Photograph of an adult woman lying on her side across rumpled white linen, seen from behind, one arm folded under her head and a sheet gathered across her hip. Late morning sun through venetian blinds lays hard parallel stripes across her back, her shoulder and the bedding. Medium-format film look, soft grain, honey and cream palette, warm skin against cool shadow. Calm and unposed.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp" alt="Lace and lamplight" width="230"></a></td><td valign="top"><b>Lace and lamplight</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp">tamaño completo</a></sub><br><br>Low-key studio portrait of an adult woman kneeling on a dark velvet chaise in a black lace bodysuit and sheer stockings, seen from behind, looking back over her shoulder. A single hard lamp from the left gives one edge of her body and drops the rest to near black; lace texture catches the light where it crosses her spine. 85mm, shallow depth of field, heavy grain, oxblood and black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp" alt="Two figures one sheet" width="230"></a></td><td valign="top"><b>Two figures one sheet</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp">tamaño completo</a></sub><br><br>Intimate two-figure composition on a bed at dawn: a woman lying on her back with her eyes closed, the white sheet drawn up and gathered across her chest and tucked under her arms, and a man beside her propped on one elbow, bare shoulders above the sheet, his hand resting on the sheet over her stomach. Cool blue window light from the left, one warm bedside lamp still on behind them. Skin tones held apart by the two light sources. Shallow focus, fine grain, unhurried and quiet, tasteful and covered.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp" alt="Dawn to candlelight" width="230"></a></td><td valign="top"><b>Dawn to candlelight</b><br><sub><code>alibaba/qwen-image-2.1/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp">tamaño completo</a></sub><br><br>Keep both figures, the bed, their poses and the framing exactly as they are. Change the dawn window light to a single group of candles on the left nightstand: warm flickering light raking low across both bodies, the room falling to deep amber and black behind them, highlights only along the edges of skin and sheet. Keep the shadows consistent with the new light source.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Two references one chaise</b><br><sub><code>alibaba/qwen-image-2.1/edit</code></sub><br><br>Merge the two references into a single frame. Place the woman from the first image, lying on her side in the same pose, on the dark velvet chaise from the second image. Keep her face and body from the first reference, and the chaise, the single hard lamp and the oxblood palette from the second. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Qwen Image 2.1 LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Boudoir into anime</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code></sub><br><br>Transform into anime. Flat cel shading, clean linework, anime illustration. Keep her pose, the sheet across her hip, the bed, the blinds and the striped direction of the light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp" alt="Anime boudoir lora" width="230"></a></td><td valign="top"><b>Anime boudoir lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp">tamaño completo</a></sub><br><br>storybook anime illustration of an adult woman reclining across rumpled linen in a sunlit attic room, seen from behind over her bare back and shoulder, one arm folded behind her head, a sheet drawn up across her hip and waist. Morning light through a slatted window falling in stripes across her back. Soft cel-shaded figure, warm hand-painted background, honey and cream palette, tasteful and covered.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp" alt="Relight the chaise" width="230"></a></td><td valign="top"><b>Relight the chaise</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp">tamaño completo</a></sub><br><br>Relight the scene: a low warm candle cluster from the right at mattress level and cool blue moonlight through a window behind her. Keep her pose, the lace, the chaise and the framing unchanged.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp" alt="Watercolor lace lora" width="230"></a></td><td valign="top"><b>Watercolor lace lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp">tamaño completo</a></sub><br><br>watercolor anime of an adult woman kneeling on a dark velvet chaise in a black lace bodysuit and sheer stockings, seen from behind, glancing back over her shoulder. Transparent washes, pale paper texture, a single warm lamp from the left leaving most of the figure in deep wash, oxblood and ink.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp" alt="Impressionist bathers lora" width="230"></a></td><td valign="top"><b>Impressionist bathers lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp">tamaño completo</a></sub><br><br>Monet Style, two bathers at the edge of a still pond at first light, both seen from behind — one seated on the bank wrapped in a pale towel with her bare shoulders showing, one standing waist-deep in the water with her back to us. Mist dissolving the far shore, loose impressionist brushwork, dappled light on wet skin and towel, pastel palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp" alt="Two weights stacked" width="230"></a></td><td valign="top"><b>Two weights stacked</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp">tamaño completo</a></sub><br><br>watercolor anime of an adult woman stepping out of a claw-foot bath in a winter bathroom at dusk, seen from behind, steam rising and fogging the window, a large towel wrapped and held at her chest with her bare back and shoulders showing, warm lamplight behind fogged glass, transparent washes, pale paper texture, soft ink linework.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp" alt="Next scene after dark" width="230"></a></td><td valign="top"><b>Next scene after dark</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp">tamaño completo</a></sub><br><br>Next Scene: hours later, exactly the same two people — one woman and one man, no other figures in the room — asleep and turned toward each other under the same sheet on the same bed. The window has gone full dark and only the low bedside lamp is still burning. Same framing, same bedding, same lens, same two faces.</td></tr>
</table>

### MiniMax H3 Image LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp"><img src="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp" alt="Same woman new scene" width="230"></a></td><td valign="top"><b>Same woman new scene</b><br><sub><code>minimax/h3-image-lora/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp">tamaño completo</a></sub><br><br>Picture 1 is the woman. Put her on a sunlit balcony in a white linen shirt, wind in her hair, late afternoon light. Keep her face and hairstyle.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/282e8d89d6c8fff0.webp"><img src="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/282e8d89d6c8fff0.webp" alt="Vhs still doorway" width="230"></a></td><td valign="top"><b>Vhs still doorway</b><br><sub><code>minimax/h3-image-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/282e8d89d6c8fff0.webp">tamaño completo</a></sub><br><br>vh5tape, a paused VHS frame: a woman in a slip dress leaning in a doorway at night, pink and cyan light on wet asphalt, tracking lines across the bottom of the frame.</td></tr>
</table>

### Qwen Image 3.0 Pro

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/35af732b62f21e2c.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/35af732b62f21e2c.webp" alt="Two gladiators stand forehead to forehead in a torchlit arena above the lines MARCUS VS DRAVEN, XIV OCTOBER and ARENA VETUS." width="230"></a></td><td valign="top"><b>Gladiator fight poster with three clean lines of type</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/35af732b62f21e2c.webp">tamaño completo</a></sub><br><br>Cinematic fight poster, underground arena. Two gladiators stand forehead to forehead in a stare-down, oiled torsos catching torchlight, breath visible, sand and dust in the air. Three lines of clean typography set across the lower third: the words MARCUS VS DRAVEN on one line, XIV OCTOBER on the next, ARENA VETUS on the last. 65mm, shallow depth of field, heavy grain, torch orange against black, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp" alt="Fashion magazine cover with a large condensed SPICY masthead and small-caps cover lines over a studio portrait" width="230"></a></td><td valign="top"><b>Fashion magazine cover with masthead and cover lines</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp">tamaño completo</a></sub><br><br>A glossy fashion magazine cover, full-bleed portrait of an adult woman in a black lace bodysuit under a sheer open kimono, arms raised adjusting her hair, studio rim light on a deep charcoal background; masthead text &#x27;SPICY&#x27; in large condensed type across the top, cover lines reading &#x27;THE LATE SHIFT&#x27; and &#x27;ISSUE 07&#x27; in small caps, high-end print typography, razor-sharp 2K detail.</td></tr>
</table>

### Qwen Image 3.0

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp" alt="Chalk handwriting reading TODAY’S DRAUGHT – MOONWELL on a rain-beaded shop window, behind it a woman holding up a glowing green potion bottle." width="230"></a></td><td valign="top"><b>Chalk lettering on a rainy apothecary window at night</b><br><sub><code>alibaba/qwen-image-3.0/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp">tamaño completo</a></sub><br><br>Cinematic film still, an apothecary shop window at night. Chalk handwriting on the glass reads TODAY&#x27;S DRAUGHT - MOONWELL; behind it a woman tilts a glowing potion bottle, one camisole strap slipped to her elbow, the liquid&#x27;s green light thrown up under her jaw. Rain beads on the outside of the glass. 35mm, shallow depth of field, heavy grain, potion green against night blue, restrained and tasteful.</td></tr>
</table>

### Seedream 5.0 Pro

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Bathhouse marble two</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>Cinematic film still, Roman marble bathhouse. Close two-shot on the stepped ledges: a woman on the upper step tips a brass basin of water over her shoulder and it sheets down her bare back, while the man on the step below watches from a hand&#x27;s breadth away, her knee almost at his chest; everything below the chest is lost in thick steam. One hard clerestory shaft cuts the vapour and catches wet skin and wet Carrara marble alike. 65mm, shallow depth of field, warm amber against stone grey, heavy grain, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp" alt="Champagne satin back" width="230"></a></td><td valign="top"><b>Champagne satin back</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp">tamaño completo</a></sub><br><br>Cinematic film still, a woman sits at a tall window wrapped in champagne satin, seen entirely from behind so the frame is one unbroken line of back; the satin has slipped from the shoulder blade to the small of the back and pools there. Cold morning light from the window, warm lamp from inside. 85mm, shallow depth of field, heavy grain, champagne and slate palette, restrained and tasteful.</td></tr>
</table>

### Qwen Image Edit Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp" alt="Boudoir i2i" width="230"></a></td><td valign="top"><b>Boudoir i2i</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp">tamaño completo</a></sub><br><br>Change the light to a warm sunset glow raking across her skin from the window, keep the pose and the room, cinematic colour, 35mm film grain</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp" alt="Lingerie and hanger" width="230"></a></td><td valign="top"><b>Lingerie and hanger</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp">tamaño completo</a></sub><br><br>Keep the woman, the bed and the hotel room exactly as they are. Change her outfit to a black lace bodysuit with sheer black stockings, and change the brass door hanger text to read &#x27;BACK AT MIDNIGHT&#x27;. Keep the same pose, framing, lighting and colour grade.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp" alt="Latex and neon" width="230"></a></td><td valign="top"><b>Latex and neon</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp">tamaño completo</a></sub><br><br>Keep the rider, the motorcycle and the neon garage exactly as they are. Change her outfit to a glossy black latex bodysuit with a deep front zip and long gloves, add sheer black stockings, and change the neon sign on the back wall to read &#x27;AFTER HOURS&#x27;. Keep the same pose, framing, magenta and cyan lighting and colour grade.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp" alt="Midday to candlelit" width="230"></a></td><td valign="top"><b>Midday to candlelit</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp">tamaño completo</a></sub><br><br>Keep the woman, her pose at the railing, the balcony, the iron rail and the geranium pots exactly as they are, and keep the same framing and camera angle. Change the time of day from hard midday sun to late night: the sky becomes deep blue-black with stars, the sea goes dark, and the whole scene is now lit only by a cluster of candles standing along the balcony rail, so warm amber candlelight rakes across her from below and everything else falls into deep shadow. Change her white cotton sundress to a black silk slip dress. Keep her face and body identical.</td></tr>
</table>

### Seedream 5.0 Lite

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp" alt="Two refs poster size" width="230"></a></td><td valign="top"><b>Two refs poster size</b><br><sub><code>bytedance/seedream-5.0-lite/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp">tamaño completo</a></sub><br><br>Cast: one man. Build one poster-shaped frame from these two references: the figure from the first, the location from the second, shot backlit and soaking wet so water traces the line of the body and the rim light does the rest. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp" alt="Siren rocks strip" width="230"></a></td><td valign="top"><b>Siren rocks strip</b><br><sub><code>bytedance/seedream-5.0-lite/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp">tamaño completo</a></sub><br><br>Cinematic film still, 21:9 ultra-wide. Close on the two of them: her scaled hip and his soaked shirt pressed together, water sheeting off both, her head tipped back. On black sea rocks a mermaid and a sailor are hit by the same breaking wave, scales and soaked cloth pressed together, both drenched; the horizon line runs the full width of the frame under a storm-lit sky. Lighthouse beam raking across the spray. 65mm anamorphic, heavy grain, storm green and pewter palette, restrained and tasteful.</td></tr>
</table>

### Qwen Image 2

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp" alt="Cyber alley bilingual" width="230"></a></td><td valign="top"><b>Cyber alley bilingual</b><br><sub><code>alibaba/qwen-image-2/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp">tamaño completo</a></sub><br><br>Cinematic film still, rain-soaked cyberpunk alley at 3am. A woman stands behind a fogged shopfront window looking back over her shoulder; her thin white shirt is soaked through and clings to her shoulder blades, a faint glowing chrome port at the nape of her neck. Bilingual neon signage in Chinese and English reading 夜宵 NIGHT NOODLES and 义体维修 CHROME REPAIR throws hard magenta and cyan across the wet fabric and across the patch of condensation she has wiped clear with one palm. 35mm anamorphic, shallow depth of field, heavy film grain, teal and magenta palette, restrained and tasteful.</td></tr>
</table>

### Qwen Image 2512 LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp" alt="Storybook onsen" width="230"></a></td><td valign="top"><b>Storybook onsen</b><br><sub><code>alibaba/qwen-image-2512-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp">tamaño completo</a></sub><br><br>storybook anime illustration of a gay couple, two rugged men in their mid thirties with stubble and broad shoulders, relaxing together at the edge of an outdoor hot spring at dusk, loose yukata open at the chest and slipping off their shoulders, one resting his head on the other&#x27;s shoulder, steam rising, lanterns glowing, soft pastel palette.</td></tr>
</table>

### Z-Image Spicy Pro

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Vista previa no disponible en GitHub.<br><a href="https://spicyapi.ai/es/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">Míralo en spicyapi.ai</a></sub></td><td valign="top"><b>Moon pool two silhouettes</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code></sub><br><br>Cast: one man and one woman. Cinematic film still, a moonlit spirit spring at night. Two wet silhouettes stand at the water&#x27;s edge in near-total backlight, reduced to pure outline, water tracking down the line of the waist; glowing sigils drift on the water surface and cast faint light upward. 65mm, shallow depth of field, heavy grain, moon silver and spirit cyan, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp" alt="High key pov" width="230"></a></td><td valign="top"><b>High key pov</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp">tamaño completo</a></sub><br><br>First-person POV photograph from the foot of a bed: an adult woman reclining back against white pillows in an ivory silk slip, her bare legs stretched toward the camera in the foreground, red pedicure, a thin gold ankle chain, soft blown-out window light flooding the white sheets, minimal high-key composition, editorial portrait, 35mm.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp" alt="Garter product still" width="230"></a></td><td valign="top"><b>Garter product still</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp">tamaño completo</a></sub><br><br>Luxury product-advertising still, immaculate studio lighting, no logos. Cropped from ribs to mid-thigh: an adult woman&#x27;s hands rest on a black satin belt at her hip; she wears a matching black silk outfit and sheer stockings against a seamless charcoal backdrop. A single hard key light rakes across the satin, catching every fibre and the sheen of the stockings; a faceted crystal perfume bottle stands on a small plinth in the near foreground, in razor focus. Commercial editorial finish, deep shadow.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp" alt="Backlit curtain shadow" width="230"></a></td><td valign="top"><b>Backlit curtain shadow</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp">tamaño completo</a></sub><br><br>Photograph shot from inside a dark bedroom looking at a floor-to-ceiling gauzy linen curtain lit from behind by a cluster of candles on the floor. The silhouette of an adult woman is projected onto the fabric from the far side: she stands in profile, arms raised, a loose robe around her shoulders, hair loose. Only the soft dark shape and a warm amber rim read through the cloth — pure backlit shadow play. A second smaller silhouette of a candle flame flickers at the lower left, wax pooling on a saucer in the sharp near foreground. Deep black room, honey-gold glow through the weave, visible linen texture, faint smoke drifting. Vertical composition, 50mm, shallow focus on the fabric. No text, no logos.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp" alt="Full size portrait" width="230"></a></td><td valign="top"><b>Full size portrait</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp">tamaño completo</a></sub><br><br>Editorial portrait, an adult woman in a sheer black slip standing against a bare plaster wall, single hard window light from camera right raking across the fabric, deep shadow filling the left of the frame, medium format film look, fine grain, cream and charcoal palette.</td></tr>
</table>

### Z-Image Spicy

<sub>🌶️ Edición Spicy · <a href="https://spicyapi.ai/es/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp" alt="Leather studs low key" width="230"></a></td><td valign="top"><b>Leather studs low key</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp">tamaño completo</a></sub><br><br>Cinematic portrait, low key. A man in a studded leather jacket worn open over bare skin, a single hard light from one side giving only half the body and dropping the rest to black; studs catch as small specular points. 85mm, shallow depth of field, heavy grain, black and oxblood palette, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp" alt="Blind stripe boudoir" width="230"></a></td><td valign="top"><b>Blind stripe boudoir</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp">tamaño completo</a></sub><br><br>Photograph of an adult woman lying on her side across rumpled white linen in a black lace bodysuit, morning sun through venetian blinds casting hard stripes across her skin and the sheets, one arm stretched above her head, eyes closed, calm and warm, medium format film look, soft grain, honey and cream palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp" alt="Fire escape dusk" width="230"></a></td><td valign="top"><b>Fire escape dusk</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp">tamaño completo</a></sub><br><br>35mm film photograph, warm grain and halation, Portra colour. An adult woman sits out on a Brooklyn fire escape at dusk in a black lace-trim slip and an unbuttoned men&#x27;s dress shirt, bare feet resting through the metal grating, an ashtray and a longneck beer beside her, head tipped back against the railing with her eyes closed. Brick wall, string lights, blue-hour sky, shallow focus.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp" alt="Own legs pov" width="230"></a></td><td valign="top"><b>Own legs pov</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp">tamaño completo</a></sub><br><br>First-person point of view from a low chair looking down at my own crossed legs, morning sun cutting in through a tall window in hard bright stripes. Bare legs in sheer black lace-top stockings and black satin shorts, one foot in a slipper half hanging off the toes, a chipped ceramic coffee mug held between my knees, a book open on my thigh. Warm parquet floor, dust in the sunbeam, wide 24mm perspective, natural skin texture, 35mm colour film grain, unposed and lazy. Adult woman. No text, no logos.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp" alt="Expanded one liner" width="230"></a></td><td valign="top"><b>Expanded one liner</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp">tamaño completo</a></sub><br><br>Adult woman in a silk robe at a rain-streaked window, candlelight.</td></tr>
</table>

### Z-Image

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp" alt="Gym mirror selfie" width="230"></a></td><td valign="top"><b>Gym mirror selfie</b><br><sub><code>alibaba/z-image-turbo/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp">tamaño completo</a></sub><br><br>iPhone mirror selfie, an adult woman in a charcoal sports bra and low-slung grey joggers standing in an empty late-night gym, midriff bare, one hand holding the phone, hair damp, casual confident smirk, overhead fluorescent light, slight motion blur, authentic amateur snapshot look.</td></tr>
</table>

### Z-Image Turbo LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp" alt="Realism rain window" width="230"></a></td><td valign="top"><b>Realism rain window</b><br><sub><code>alibaba/z-image-turbo-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp">tamaño completo</a></sub><br><br>Realism, a beautiful mature woman in her early thirties with sharp cheekbones and red lipstick, wearing a low-cut black satin slip dress, sits on a window ledge at night, one strap slipping off her shoulder, rain on the glass, city lights blurred behind her, one knee drawn up, soft lamp light on her face, 35mm film grain.</td></tr>
</table>

### Seedream 4.0

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp" alt="Coat street person merge" width="230"></a></td><td valign="top"><b>Coat street person merge</b><br><sub><code>bytedance/seedream-4.0/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp">tamaño completo</a></sub><br><br>Compose one frame from these three references: the woman from the first, wearing the long coat from the second, standing on the street from the third at night. Waist-up: the coat hangs open over a thin camisole and the streetlight behind drives straight through the fabric. The coat hangs open over a thin camisole and a streetlight behind her throws the light straight through the fabric. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Prefect Pony XL

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/prefect-pony-xl/67076d7e84936c95.webp"><img src="https://cdn.spicyapi.ai/models/examples/prefect-pony-xl/67076d7e84936c95.webp" alt="Silver knight" width="230"></a></td><td valign="top"><b>Silver knight</b><br><sub><code>prefect/pony-xl/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/prefect-pony-xl/67076d7e84936c95.webp">tamaño completo</a></sub><br><br>score_9, score_8_up, 1girl, solo, long white hair, ornate silver armor, red cape, holding a longsword, standing on castle ramparts at dawn, dramatic sky, full body, detailed armor</td></tr>
</table>

### FLUX.1 Dev LoRA

<sub>Modelo estándar, nivel en el catálogo: unrestricted · <a href="https://spicyapi.ai/es/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es">página del modelo</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp"><img src="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp" alt="Mj mix red gown" width="230"></a></td><td valign="top"><b>Mj mix red gown</b><br><sub><code>black-forest-labs/flux-1-dev-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp">tamaño completo</a></sub><br><br>MJ v6, editorial fashion photograph of a beautiful woman in a red satin gown with a plunging neckline and an open back, descending marble stairs and glancing over her bare shoulder, dramatic side light, glossy magazine look.</td></tr>
</table>


Algunos resultados contienen desnudos; en esos casos aquí solo se muestran el prompt y la petición, y el resultado está enlazado en spicyapi.ai.

Lo que enseñan estos ejemplos:

1. **Describe lo que cambia, no lo que ya está.** "She turns slowly from the window toward camera" da por hecho que el primer fotograma ya la muestra junto a la ventana.
2. **Di quién aparece en el plano.** Una línea como `Cast: two women.` evita que el modelo se invente personas de más.
3. **Fija la cámara.** "Locked-off camera, no move" o "the camera stays on her back" eliminan toda una categoría de fallos.
4. **Dale al movimiento una causa física.** Una corriente de aire mueve la seda, el vapor empaña el cristal, una ráfaga levanta la bata.
5. **Fija el final cuando importe.** Si pasas `last_image_url`, puedes aprobar el aspecto final como imagen fija antes de pagar por el movimiento.

---

## Cómo escribir un prompt de video NSFW que funcione

```
[Who: adult, age range, look] + [One main action] + [Secondary motion: hair, fabric, light]
+ [Setting] + [Lighting] + [Camera move] + [Style / film look]
```

Es decir: quién (adulto, rango de edad, aspecto) + una acción principal + un movimiento secundario (pelo, tela, luz) + escenario + iluminación + movimiento de cámara + estilo / acabado de película. Los prompts se escriben en inglés.

| Sí | No |
|---|---|
| "She slowly slides one strap off her shoulder and looks up at the camera." | "Sexy woman being hot." |
| Una acción principal por cada clip de 5 segundos | Una rutina entera en un solo clip |
| Nombra la cámara: *slow push-in*, *static*, *orbit left* | "Cinematic camera" |
| Describe las fuentes de luz: *candlelight*, *window light*, *neon rim* | "Good lighting" |
| Indica una edad adulta: *in her 30s*, *adult man in his 40s* | Descripciones que sugieran juventud |
| Deja que el primer fotograma defina el vestuario y el escenario | Volver a describir todo lo que la imagen ya muestra |

**Fiabilidad del movimiento, de más a menos fiable:** respirar y parpadear → pelo y tela al viento → agua, vapor, humo, parpadeo de velas → giro lento de cabeza, mirada por encima del hombro → caminar hacia la cámara o alejándose de ella → estirarse, darse la vuelta → bailar → contacto entre dos personas → acción rápida o acrobática.

---

## Los prompts

Cada prompt indica el modelo para el que se escribió. La mayoría funcionan en cualquier modelo Spicy de imagen a video; usa un modelo más barato para los borradores y uno más potente para la versión final.

### Boudoir y lencería

La categoría NSFW de imagen a video más fiable: un solo sujeto, luz suave y movimientos pequeños. Si eres nuevo, empieza aquí.

#### B01 · Dormitorio en la hora dorada

```text
A woman in her late 20s in black lace lingerie slowly turns toward the camera in a dim bedroom. Warm light from a bedside lamp throws soft shadows across her skin. She runs her fingers through her long dark hair and arches her back slightly. Slow push-in from medium shot to close-up on her face. Shallow depth of field, cinematic color grade, light film grain.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b01-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Foto de cintura para arriba de una mujer adulta en lencería de encaje negro, luz cálida de lámpara, dormitorio de fondo.  
**Consejo:** El modelo conserva el vestuario de tu primer fotograma, así que empieza con el sujeto ya en lencería y con una luz cálida a juego.

#### B02 · Bata de seda que cae del hombro

```text
Close-up of an adult woman's shoulder as an ivory silk robe slowly slides down her arm, revealing bare skin. The fabric falls in slow motion and the camera follows it down. Warm amber candlelight, soft bokeh in the background, natural skin glow, shallow depth of field.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b02-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Encuadre cerrado del hombro y la clavícula, bata de seda color marfil colocada holgadamente, luz de velas.  
**Consejo:** Empieza con la bata ya medio caída de un hombro; el modelo continúa el movimiento en lugar de inventarlo.

#### B03 · Espejo del tocador

```text
A woman in her 30s in sheer white lingerie sits at a vintage vanity, applying red lipstick while watching herself in an ornate mirror. She presses her lips together, then turns to the camera with a slow smile. Soft window light from the left, vintage film tone, 35mm look, shallow depth of field.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b03-es) | 1080p · 5 s · 16:9 | $0.7125 | Intermedio |

**Primer fotograma:** Mujer adulta sentada frente a un tocador con su reflejo visible, lencería transparente, luz suave de ventana.  
**Consejo:** Los reflejos se mantienen mejor en Wan 2.6 y Seedance que en los niveles económicos. Deja el espejo dentro del primer fotograma.

#### B04 · Sábanas de satén rojo

```text
An adult woman lies on her side across red satin sheets in a matching red lace bodysuit. She slowly stretches one arm above her head, lengthening her body. The camera dollies from her feet up along her figure in one smooth move. Deep crimson key light from one side, cool blue fill from the other, fashion editorial mood.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b04-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta tumbada sobre satén rojo, body de encaje rojo, iluminación en dos tonos.  
**Consejo:** Indicar la dirección del dolly da un movimiento de barrido limpio. Las paletas de rojo sobre rojo se renderizan bien.

#### B05 · Champán en el diván

```text
A woman in her 30s in a black velvet corset and stockings reclines on a chaise longue. She raises a champagne glass toward the camera so the liquid catches the light, takes a slow sip and holds eye contact with the lens. Warm tungsten light, dark moody background, film noir atmosphere.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b05-es) | 1080p · 5 s · 16:9 | $0.7125 | Intermedio |

**Primer fotograma:** Mujer adulta en un diván con una copa de champán en la mano, corsé, iluminación en clave baja.  
**Consejo:** Los objetos se comportan mejor en Wan 2.6 o Seedance 2.0. Limítate a un solo gesto.

#### B06 · Balcón al atardecer

```text
A woman in her late 20s in a sheer black negligee stands on a balcony at twilight with blurred city lights behind her. A light breeze lifts the fabric and her hair. She leans on the railing and slowly looks back over her shoulder at the camera. Backlit rim light outlines her figure, anamorphic flare, atmospheric haze.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b06-es) | 1080p · 5 s · 16:9 | $0.95 | Intermedio |

**Primer fotograma:** Mujer adulta de espaldas en un balcón al anochecer, camisón transparente, bokeh de la ciudad.  
**Consejo:** El viento es uno de los movimientos más fiables en cualquier modelo de video. Úsalo para dar vida sin arriesgar la anatomía.

#### B07 · Macro de encaje y perlas

```text
Extreme close-up of a strand of pearls resting on an adult woman's collarbone above white lace. Her breathing makes the pearls rise and fall gently. Slow rack focus from the pearls to the lace edge. Soft high-key studio light, creamy tones, luxury beauty-ad feel.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b07-es) | 720p · 5 s · 1:1 | $0.19 | Principiante |

**Primer fotograma:** Macro de perlas sobre la clavícula y encaje blanco, iluminación en clave alta.  
**Consejo:** La respiración es el movimiento más fiable de todos. El encuadre macro oculta manos y caras, lo que elimina la mayoría de los artefactos.

#### B08 · Subiéndose la media

```text
An adult woman sits on the edge of a bed and slowly draws a sheer black stocking up her leg, smoothing it with both hands. Low camera angle, slow tilt up following her hands. Warm bedroom light, shallow depth of field, soft film grain.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b08-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta sentada en una cama, con una media puesta y la otra a medio subir, ángulo bajo.  
**Consejo:** Encuadra de la rodilla hacia arriba para que las manos se vean grandes y sencillas.

#### B09 · Alfombra de piel junto a la chimenea

```text
A woman in her 30s lies on a white fur rug in front of a crackling fireplace, wearing a cream silk slip. Firelight flickers across her skin as she rolls slowly onto her back and closes her eyes. Static camera, warm orange light, cosy winter-cabin mood.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b09-es) | 720p · 5 s · 16:9 | $0.4105 | Principiante |

**Primer fotograma:** Mujer adulta sobre una alfombra de piel junto a una chimenea, combinación de seda color crema, luz del fuego.  
**Consejo:** Una cámara fija con la luz del fuego en movimiento da mucha sensación de movimiento con muy poco riesgo.

#### B10 · Lluvia en la ventana

```text
An adult woman in an oversized white shirt, unbuttoned low, sits on a window seat watching rain run down the glass. She draws her knees up and rests her chin on them, then glances at the camera. Cool blue daylight from the window, soft interior shadows, quiet melancholy mood, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b10-es) | 720p · 8 s · 16:9 | $0.304 | Principiante |

**Primer fotograma:** Mujer adulta en el asiento de una ventana con una camisa blanca abierta, ventana con lluvia, luz fría.  
**Consejo:** LTX 2.3 Spicy permite tomas más largas a bajo costo; mantén la acción lenta cuando pases de 5 segundos.

#### B11 · Travelling por el detalle de la espalda

```text
The camera tracks slowly down the bare back of an adult woman wearing only an open-back evening gown, from her neck to the small of her back. She shifts her weight and her shoulder blades move under the skin. Warm side light sculpts the spine, dark background, elegant and intimate.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b11-es) | 720p · 5 s · 9:16 | $1.14 | Intermedio |

**Primer fotograma:** Mujer adulta de espaldas con un vestido de espalda descubierta, luz lateral cálida.  
**Consejo:** Las espaldas perdonan mucho en anatomía y se ven caras. Seedance maneja bien el micromovimiento de la piel.

#### B12 · Venda de satén

```text
An adult woman with a black satin blindfold kneels on white sheets in black lingerie. She tilts her head as if listening and a slow smile forms. Soft diffused light, high-contrast black and white palette, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b12-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta de rodillas sobre sábanas blancas, venda de satén en los ojos, lencería negra.  
**Consejo:** Una venda en los ojos elimina por completo los artefactos en los ojos y añade tensión al plano.

#### B13 · Solo joyas

```text
Artistic portrait of a nude adult woman in her 30s lying on black velvet, covered only by layered gold necklaces and bracelets that catch the light. She slowly turns her wrist and the jewelry glints. Single overhead spotlight, deep shadows, luxurious editorial style, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b13-es) | 1080p · 5 s · 3:4 | $2.85 | Avanzado |

**Primer fotograma:** Mujer adulta sobre terciopelo negro con joyas doradas, foco cenital, sombras que cubren el cuerpo.  
**Consejo:** El desnudo insinuado con sombras estratégicas se ve de alta gama y lo aceptan más plataformas cuando lo vuelves a publicar.

#### B14 · Estiramiento matutino en la cama

```text
Soft morning light pours through sheer curtains as a woman in her late 20s wakes in white sheets, wearing a loose camisole. She stretches both arms overhead, arches her back and smiles sleepily at the camera. Airy pastel tones, static camera, lifestyle film look.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b14-es) | 768p · 5 s · 16:9 | $0.42 | Principiante |

**Primer fotograma:** Mujer adulta entre sábanas blancas con una camiseta de tirantes, luz de ventana por la mañana.  
**Consejo:** MiniMax H3 hace bien los estiramientos naturales de cuerpo entero. En este modelo el prompt es opcional; a menudo basta con el primer fotograma.

#### B15 · Atando el corsé

```text
Close-up from behind as an adult woman tightens the ribbon laces of a black corset, pulling them in rhythmic tugs. Her waist draws in with each pull. Candlelit boudoir, warm tones, shallow depth of field, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b15-es) | 720p · 5 s · 9:16 | $0.871 | Intermedio |

**Primer fotograma:** Vista de espaldas de una mujer adulta con un corsé negro a medio atar, luz de velas.  
**Consejo:** Los movimientos repetitivos de las manos funcionan si las manos se quedan en la misma zona del encuadre.

#### B16 · Revelación con abrigo de piel

```text
A woman in her 30s stands in a dark hotel corridor wearing a long faux-fur coat. She opens it slowly toward the camera to show black lingerie underneath, then lets it slip to her elbows. Warm practical wall sconces, glossy floor reflections, glamorous noir mood, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b16-es) | 1080p · 5 s · 9:16 | $0.7125 | Intermedio |

**Primer fotograma:** Mujer adulta en el pasillo de un hotel con un abrigo de piel sintética cerrado.  
**Consejo:** Abrir una prenda es un movimiento único y predecible. Haz que el color del abrigo sea distinto del de la lencería.

### Desnudo artístico y bellas artes

El desnudo tratado como estudio de la figura: luz escultórica, siluetas, poses clásicas. Funciona bien en todos los modelos Spicy porque el movimiento es mínimo.

#### F01 · Venus clásica

```text
A nude adult woman reclines on draped white linen in the pose of a Renaissance Venus painting. She slowly turns her face toward the viewer. Soft north-window light, oil-painting color palette, gentle film grain, static camera, museum-quality composition.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f01-es) | 1080p · 5 s · 16:9 | $2.85 | Intermedio |

**Primer fotograma:** Mujer adulta desnuda reclinada sobre paños blancos, iluminación de pintura clásica.  
**Consejo:** Nombrar una pose de la historia del arte le da al modelo una base de composición sólida.

#### F02 · Juego de sombras

```text
Slatted light from window blinds falls across the nude torso of an adult woman standing in a dark room. She breathes slowly and turns a few degrees, so the stripes of light slide across her skin. High-contrast black and white, film noir, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f02-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Torso de una mujer adulta en una habitación oscura con franjas de luz de persiana, blanco y negro.  
**Consejo:** Los patrones de luz dura crean movimiento sin que el cuerpo se mueva. Ideal para modelos baratos.

#### F03 · Paisaje corporal

```text
Extreme close-up macro shot gliding slowly over the curves of an adult woman's hip and waist, lit so the skin looks like sand dunes at dusk. Warm raking light, abstract composition, ultra-shallow depth of field, slow lateral camera move.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f03-es) | 1080p · 8 s · 21:9 | $0.456 | Intermedio |

**Primer fotograma:** Macro abstracto de las curvas de la cadera y la cintura con luz cálida rasante.  
**Consejo:** Los paisajes corporales abstractos nunca muestran cara ni manos, así que casi no tienen artefactos.

#### F04 · Flotando bajo el agua

```text
A nude adult woman floats weightlessly underwater in a flowing white silk sheet. The fabric billows around her body as light rays pierce the surface above. Her hair drifts slowly. Ethereal blue-green tones, slow motion, dreamlike.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f04-es) | 720p · 5 s · 9:16 | $1.14 | Avanzado |

**Primer fotograma:** Mujer adulta bajo el agua envuelta en seda blanca, rayos de luz desde arriba.  
**Consejo:** El movimiento bajo el agua es lento por naturaleza, y los modelos lo manejan con soltura.

#### F05 · Pintura corporal que gotea

```text
Metallic gold paint drips slowly down the bare shoulders and back of an adult woman standing against a matte black backdrop. She rolls her shoulders and the paint streaks catch the studio light. Hard key light, glossy highlights, art-gallery aesthetic, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f05-es) | 1080p · 5 s · 4:5 | $0.7125 | Intermedio |

**Primer fotograma:** Espalda de una mujer adulta con trazos de pintura dorada, fondo negro.  
**Consejo:** Los líquidos que se mueven sobre la piel causan mucho impacto y son fiables en Wan 2.6.

#### F06 · Ninfa del bosque

```text
A nude adult woman with ivy woven into her long hair stands in a misty forest clearing at dawn, partly hidden by ferns. She reaches up to touch a hanging branch. Shafts of sunlight through fog, soft greens and golds, fairy-tale mood, slow dolly-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f06-es) | 720p · 5 s · 16:9 | $0.4105 | Principiante |

**Primer fotograma:** Mujer adulta en un bosque con niebla, helechos en primer plano, hiedra en el pelo.  
**Consejo:** El follaje en primer plano sirve también como censura natural para las plataformas que la exigen.

#### F07 · Estudio de figura en estudio

```text
Classical figure study of a nude adult man in his 30s seated on a wooden stool in a photography studio, grey seamless backdrop. He slowly shifts his weight and turns his head toward the light. Single large softbox, sculpted muscle definition, black and white, locked-off camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/es/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f07-es) | 1080p · 5 s · 3:4 | $0.26 | Principiante |

**Primer fotograma:** Hombre adulto desnudo sentado en un taburete, fondo gris, una sola ventana de luz, blanco y negro.  
**Consejo:** Seedance 1.5 Pro Spicy tiene bloqueo de cámara, ideal para trabajo de figura en estudio.

#### F08 · Baño de leche

```text
Top-down view of an adult woman lying in a milk bath scattered with pink rose petals, only her face, shoulders and hands above the surface. She slowly lifts one hand and the milk runs off her fingers. Soft diffused overhead light, pastel palette, dreamy beauty aesthetic.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f08-es) | 720p · 5 s · 1:1 | $0.19 | Principiante |

**Primer fotograma:** Plano cenital de una mujer adulta en un baño de leche con pétalos de rosa.  
**Consejo:** La superficie opaca de la leche controla la exposición de forma natural. El encuadre cenital es muy estable.

#### F09 · Silueta estirándose

```text
Full-body silhouette of an adult woman against a glowing orange sunset window. She raises her arms overhead and stretches slowly, her profile sharp against the light. No visible detail, pure shape and gradient, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f09-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Silueta de perfil de una mujer adulta contra una ventana al atardecer.  
**Consejo:** Las siluetas se leen como desnudo sin mostrar nada. Se pueden publicar casi en cualquier sitio.

#### F10 · Dunas del desierto

```text
Wide shot of a nude adult woman walking slowly away from the camera across rippled golden sand dunes at sunset, a long sheer scarf trailing in the wind. Long shadows, warm gradient sky, epic cinematic scale, slow drone pull-back.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f10-es) | 1080p · 5 s · 21:9 | $0.95 | Intermedio |

**Primer fotograma:** Plano general de una mujer adulta de espaldas sobre dunas de arena, con un pañuelo que ondea tras ella.  
**Consejo:** Alejarse caminando es uno de los movimientos de cuerpo entero más seguros.

#### F11 · Piel mojada en estudio

```text
Studio close-up of an adult man's shoulders and chest, skin misted with water droplets. He breathes deeply and droplets roll down slowly. Hard rim lights from both sides against black, high contrast, fitness editorial style, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f11-es) | 1080p · 5 s · 3:4 | $2.85 | Intermedio |

**Primer fotograma:** Hombros y pecho de un hombre adulto con gotas de agua, contraluz sobre fondo negro.  
**Consejo:** El contraluz sobre la piel mojada se ve premium y oculta los problemas de textura.

#### F12 · Desenvolviendo la tela

```text
An adult woman stands in a white studio wrapped in a long sheet of red chiffon. A fan off-camera slowly unwinds the fabric into the air around her, revealing her bare shoulders and back. Clean high-key light, vivid red against white, slow motion.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f12-es) | 720p · 5 s · 9:16 | $0.4105 | Principiante |

**Primer fotograma:** Mujer adulta envuelta en gasa roja en un estudio blanco.  
**Consejo:** Describir un ventilador fuera de plano le da al modelo una causa física para el movimiento.

#### F13 · Humo y forma

```text
Coloured smoke in violet and teal curls slowly around the nude figure of an adult woman standing in a black studio, veiling and revealing her body. She turns her head to watch it drift. Low-key light, surreal fashion-art mood, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f13-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta en un estudio negro rodeada de humo de colores.  
**Consejo:** El humo es de los movimientos más fiables y añade pudor de serie.

#### F14 · Arcilla de escultor

```text
An adult couple in their 30s, both nude and partly covered in pale grey clay, sit back to back on a studio floor like a living sculpture. They breathe in unison and slowly lean their heads together. Soft top light, monochrome stone tones, locked-off camera, gallery installation feel.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/es/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f14-es) | 720p · 5 s · 16:9 | $0.13 | Intermedio |

**Primer fotograma:** Dos adultos espalda con espalda cubiertos de arcilla gris, suelo de estudio, monocromo.  
**Consejo:** El encuadre espalda con espalda mantiene los dos cuerpos claramente separados.

### Parejas y romance

Dos adultos que dan su consentimiento. Los clips con dos personas son más difíciles: mantén la acción lenta, dale a cada persona ropa o un color distinto y prioriza los ángulos laterales.

#### C01 · Baile lento en el dormitorio

```text
An adult couple in their 30s slow dance barefoot in a candlelit bedroom. She wears a black slip dress, he wears an open white shirt. They sway together, foreheads touching, his hand on her lower back. Warm candlelight, soft focus, intimate romantic mood, slow orbit around them.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c01-es) | 720p · 5 s · 16:9 | $1.14 | Intermedio |

**Primer fotograma:** Pareja adulta abrazada en un dormitorio iluminado con velas, vestido negro y camisa blanca.  
**Consejo:** Los colores de ropa distintos ayudan al modelo a mantener separados los dos cuerpos.

#### C02 · Primer plano de un beso

```text
Tight close-up of an adult couple, faces in profile, lips inches apart. They lean in slowly and share a soft, lingering kiss, her hand rising to his jaw. Golden backlight through her hair, shallow depth of field, romantic film look.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c02-es) | 1080p · 5 s · 16:9 | $2.85 | Intermedio |

**Primer fotograma:** Primer plano de perfil de un hombre y una mujer adultos a punto de besarse, contraluz dorado.  
**Consejo:** El encuadre de perfil es mucho más estable para los besos que los ángulos frontales.

#### C03 · Abrazo en la playa al atardecer

```text
An adult couple in swimwear stand waist-deep in the ocean at sunset, wrapped in each other's arms as gentle waves roll past. He kisses her shoulder and she tilts her head back and laughs. Warm orange and pink sky, sparkling water, slow drone push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c03-es) | 1080p · 5 s · 21:9 | $0.7125 | Intermedio |

**Primer fotograma:** Pareja adulta abrazada en el mar al atardecer, con el agua por la cintura.  
**Consejo:** El agua a la altura de la cintura oculta las zonas más difíciles de renderizar en planos de dos personas.

#### C04 · La mañana siguiente

```text
Morning light through sheer curtains. An adult couple lies tangled in white sheets, her head on his bare chest. He slowly traces a finger along her arm and she smiles with her eyes closed. Soft airy tones, static camera, tender lifestyle mood.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c04-es) | 768p · 5 s · 16:9 | $0.42 | Principiante |

**Primer fotograma:** Pareja adulta tumbada entre sábanas blancas, la cabeza de ella sobre el pecho de él, luz de la mañana.  
**Consejo:** Los movimientos pequeños de manos en una pareja quieta son mucho más fiables que el movimiento de cuerpo entero.

#### C05 · Beso en el cuello

```text
An adult man stands behind an adult woman in a dim loft and slowly kisses the side of her neck. She closes her eyes and leans back into him, her hand reaching up into his hair. Moody blue and amber lighting, shallow depth of field, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c05-es) | 720p · 5 s · 9:16 | $1.14 | Intermedio |

**Primer fotograma:** Hombre adulto detrás de una mujer adulta, con la cara cerca de su cuello, luz tenue de loft.  
**Consejo:** Situar a uno detrás de la otra mantiene las caras separadas y se lee con claridad.

#### C06 · Baño para dos

```text
An adult couple relaxes in a large freestanding bathtub full of foam, she leans back against his chest. He pours warm water over her shoulder from his cupped hands. Candles around the tub, steam rising, warm golden tones, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c06-es) | 1080p · 5 s · 16:9 | $0.7125 | Intermedio |

**Primer fotograma:** Pareja adulta en una bañera exenta llena de espuma, velas, vapor.  
**Consejo:** La espuma y el vapor ayudan a la vez con la continuidad y con el pudor.

#### C07 · Bajando la cremallera del vestido

```text
Close-up from behind: an adult man slowly draws down the zipper of an adult woman's emerald evening dress, the fabric parting to reveal her bare back. She glances over her shoulder at him. Warm lamp light, rich jewel tones, shallow depth of field.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c07-es) | 720p · 5 s · 9:16 | $1.14 | Intermedio |

**Primer fotograma:** Espalda de una mujer adulta con un vestido esmeralda y la mano de un hombre en la cremallera.  
**Consejo:** Encuadra la cremallera y la espalda. Dos manos en una zona pequeña es el límite para la mayoría de los modelos.

#### C08 · Silueta en la ducha

```text
Behind a steamed-up glass shower door, the blurred silhouettes of an adult couple embrace under running water. Their shapes move slowly together as droplets streak down the glass. Soft warm backlight, heavy steam, intimate and suggestive, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c08-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Cristal de ducha empañado con las formas borrosas de dos adultos detrás.  
**Consejo:** El cristal esmerilado hace de censura y oculta por completo los errores de anatomía.

#### C09 · Contra la pared

```text
In a narrow hallway lit by a single red neon sign, an adult man gently presses an adult woman against the wall, their foreheads touching. She pulls him closer by his collar. Red and blue neon, deep shadows, cinematic tension, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c09-es) | 720p · 5 s · 16:9 | $0.871 | Intermedio |

**Primer fotograma:** Pareja adulta en un pasillo iluminado con neón, ella contra la pared, frente con frente.  
**Consejo:** El contraste de colores neón ayuda al modelo a separar las dos figuras.

#### C10 · Llevada en brazos a la cama

```text
An adult man carries an adult woman in his arms through a moonlit bedroom and gently lays her down on the bed. She keeps her arms around his neck and pulls him down with her. Cool moonlight through tall windows, soft shadows, romantic cinematic mood, tracking shot.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/es/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c10-es) | 720p · 5 s · 16:9 | $2.16 | Avanzado |

**Primer fotograma:** Hombre adulto llevando en brazos a una mujer adulta en un dormitorio iluminado por la luna.  
**Consejo:** Levantar y cargar a alguien es un movimiento avanzado. Seedance 2.5 Spicy es el que mejor maneja el peso y el contacto.

#### C11 · Sábanas enredadas

```text
Overhead shot of an adult couple lying tangled in rumpled grey silk sheets, hands intertwined above their heads. Their chests rise and fall slowly and the sheet shifts. Soft window light, muted editorial palette, static overhead camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c11-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Vista cenital de una pareja adulta entre sábanas de seda gris, con las manos entrelazadas.  
**Consejo:** El encuadre cenital aplana la profundidad y mantiene estables los planos de dos personas.

#### C12 · Aceite de masaje

```text
An adult woman lies face-down on a massage table draped in a white towel while an adult man pours warm oil into his palm and slowly glides his hands up her back. Warm spa lighting, candles, glossy skin highlights, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c12-es) | 768p · 5 s · 16:9 | $0.42 | Principiante |

**Primer fotograma:** Mujer adulta boca abajo en una camilla de masaje, las manos de un hombre sobre su espalda.  
**Consejo:** Unas manos sobre una espalda son un movimiento sencillo y repetible, con poco riesgo de artefactos.

#### C13 · Dos mujeres a la luz de las velas

```text
Two adult women in their late 20s, one in black lace and one in white satin, sit face to face on a velvet sofa. One slowly brushes the other's hair behind her ear and they share a soft smile before leaning in. Warm candlelight, rich burgundy tones, intimate mood, slow orbit.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c13-es) | 720p · 5 s · 16:9 | $1.14 | Intermedio |

**Primer fotograma:** Dos mujeres adultas en un sofá de terciopelo, una con encaje negro y otra con satén blanco.  
**Consejo:** La ropa contrastada (negro frente a blanco) mantiene estables las identidades durante todo el clip.

#### C14 · Azotea de noche

```text
Two adult men in their 30s lean against a rooftop railing at night, city skyline glittering behind them. One loosens the other's tie and pulls him into a slow kiss. Cool blue night tones with warm city bokeh, gentle breeze, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c14-es) | 1080p · 5 s · 16:9 | $0.95 | Intermedio |

**Primer fotograma:** Dos hombres adultos en una azotea de noche, con el skyline de la ciudad detrás.  
**Consejo:** Deja las manos sobre prendas como corbatas o cuellos para un movimiento limpio y legible.

### Actuación en solitario y baile

Ritmo y movimiento corporal. Usa modelos con buen movimiento (Seedance, MiniMax H3) y haz clips cortos.

#### D01 · Giro en la barra

```text
An adult pole dancer in her late 20s in a sparkling bikini spins slowly around a chrome pole on a small stage, hair flowing out behind her. Magenta and violet stage lights, haze, reflections on the pole, low-angle static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d01-es) | 720p · 5 s · 9:16 | $1.14 | Avanzado |

**Primer fotograma:** Bailarina de pole dance adulta sujetando una barra cromada, luces de escenario, ángulo bajo.  
**Consejo:** El movimiento de rotación es avanzado. Seedance 2.0 y 2.5 son los que mejor mantienen coherentes las extremidades.

#### D02 · Floor work sensual

```text
An adult dancer in a black bodysuit performs slow floor choreography on a glossy black stage, rolling from her side onto her knees and arching back. Single spotlight from above, haze, contemporary dance film aesthetic, slow lateral camera move.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d02-es) | 720p · 5 s · 16:9 | $1.14 | Avanzado |

**Primer fotograma:** Bailarina adulta sobre un escenario negro brillante con un body negro, foco.  
**Consejo:** Nombra la secuencia exacta de posiciones. Un "bailando" vago produce extremidades al azar.

#### D03 · Onda corporal

```text
A woman in her 20s in a cropped top and high-waisted shorts performs a slow body wave from chest to hips, facing the camera, in a neon-lit apartment. Pink and blue neon, music-video look, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d03-es) | 768p · 5 s · 9:16 | $0.42 | Intermedio |

**Primer fotograma:** Mujer adulta de frente a la cámara en un apartamento con luces de neón, top corto y shorts.  
**Consejo:** Un único paso de baile con nombre funciona mucho mejor que una rutina entera.

#### D04 · Baile frente al espejo

```text
An adult woman in lingerie dances slowly in front of a full-length mirror, swaying her hips and running her hands down her sides while watching her reflection. Warm bedroom lamp light, soft shadows, handheld camera feel.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d04-es) | 1080p · 5 s · 9:16 | $0.7125 | Intermedio |

**Primer fotograma:** Mujer adulta en lencería frente a un espejo de cuerpo entero.  
**Consejo:** Incluye el espejo en el primer fotograma para que el modelo tenga el reflejo que animar.

#### D05 · Baile en la silla

```text
An adult performer in a tuxedo jacket and heels sits backwards on a wooden chair on a dark stage, rolls her shoulders and slowly leans back, tipping her hat toward the camera. Single hard spotlight, cabaret mood, film grain, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d05-es) | 720p · 5 s · 9:16 | $0.871 | Intermedio |

**Primer fotograma:** Artista adulta sentada al revés en una silla, chaqueta de esmoquin y sombrero, foco.  
**Consejo:** Los objetos como sillas y sombreros anclan el movimiento y reducen la deriva.

#### D06 · Striptease con chaqueta

```text
An adult man in his 30s in a fitted black suit jacket over a bare chest stands under a spotlight and slowly slides the jacket off his shoulders, letting it fall to the floor. Smoky stage, amber light, confident smirk at the camera, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d06-es) | 720p · 5 s · 9:16 | $1.14 | Intermedio |

**Primer fotograma:** Hombre adulto con una chaqueta de traje sobre el torso desnudo, foco, escenario con humo.  
**Consejo:** Quitarse una sola capa exterior es un movimiento claro y único que los modelos manejan con fiabilidad.

#### D07 · Probándose lencería

```text
In a softly lit dressing room, an adult woman in a new pink lace set turns slowly in front of a mirror, checking her reflection over her shoulder and adjusting a strap. Warm vanity bulbs, pastel tones, lifestyle creator-content look, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d07-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta con un conjunto de encaje rosa en un camerino con bombillas de tocador.  
**Consejo:** Un formato muy bueno para promociones de creadores. Ajustarse un tirante es un movimiento de mano pequeño y fiable.

#### D08 · Rodando en la cama

```text
An adult woman in a white lace bodysuit rolls slowly from her stomach onto her back across a large bed, her hair spreading across the pillow, and looks up at the camera. Soft overhead light, clean white bedding, static overhead camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d08-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Vista cenital de una mujer adulta tumbada boca abajo en una cama blanca.  
**Consejo:** El ángulo cenital convierte el giro en un movimiento plano y legible.

#### D09 · Cae la toalla

```text
An adult woman stands in a steamy bathroom wrapped in a white towel, her hair wet. She looks over her shoulder at the camera, smiles, and lets the towel slip down to her lower back. Warm diffused light, steam, from behind, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d09-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta de espaldas con una toalla blanca, baño lleno de vapor.  
**Consejo:** Grabar de espaldas mantiene la revelación sencilla y la anatomía fácil.

#### D10 · Caminando en tacones

```text
An adult woman in black lingerie, stockings and stiletto heels walks slowly toward the camera down a dim hotel corridor, hips swaying, holding eye contact. Warm sconce lights, glossy floor reflections, low-angle tracking shot moving backward.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d10-es) | 720p · 5 s · 9:16 | $0.4105 | Principiante |

**Primer fotograma:** Mujer adulta en lencería y tacones al fondo del pasillo de un hotel.  
**Consejo:** Caminar hacia la cámara es uno de los movimientos de cuerpo entero más fiables.

#### D11 · Melena al viento

```text
Close-up of an adult woman in a sheer black top on a windy beach at sunset. She throws her head back and flips her long hair, laughing, as the wind catches it. Golden backlight, lens flare, slow motion.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d11-es) | 768p · 5 s · 9:16 | $0.42 | Principiante |

**Primer fotograma:** Primer plano de una mujer adulta en una playa al atardecer, top transparente, pelo largo.  
**Consejo:** El pelo y el viento son de los mejores movimientos en todos los modelos.

#### D12 · Secuencia de yoga

```text
An adult woman in minimal sportswear moves slowly from downward dog into cobra pose on a mat in a sunlit loft studio. Controlled, fluid motion, soft morning light, clean minimalist interior, static side-on camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d12-es) | 1080p · 5 s · 16:9 | $0.7125 | Intermedio |

**Primer fotograma:** Mujer adulta sobre una esterilla de yoga en perro boca abajo, vista lateral, loft soleado.  
**Consejo:** Una cámara lateral más posturas de yoga con nombre mantienen predecibles las extremidades.

#### D13 · Danza del abanico de cabaret

```text
A burlesque performer in her 30s on a red-curtained stage slowly opens and closes two large white feather fans, revealing glimpses of a sequined costume beneath. Warm spotlight, glittering particles in the air, vintage cabaret mood, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d13-es) | 1080p · 5 s · 16:9 | $0.95 | Intermedio |

**Primer fotograma:** Artista de burlesque adulta en un escenario con telón rojo sujetando abanicos de plumas.  
**Consejo:** Las plumas y los abanicos dan mucho movimiento sin mover el cuerpo.

#### D14 · Pista de baile de discoteca

```text
An adult woman in a metallic mini dress dances on a crowded nightclub floor, arms raised, head tilted back, strobe lights flashing. Green and magenta lasers, haze, handheld camera, music-video energy.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d14-es) | 720p · 5 s · 9:16 | $0.871 | Intermedio |

**Primer fotograma:** Mujer adulta con un vestido metalizado en la pista de una discoteca, láseres.  
**Consejo:** Seedance 2.0 Fast Spicy incluye sonido, así que el clip trae el ambiente sonoro de la discoteca.

### Baño, ducha y agua

El agua, el vapor y la piel mojada aportan realismo. Las cámaras fijas o lentas mantienen creíble la física del agua.

#### W01 · Ducha con vapor

```text
An adult woman stands under a rainfall shower, eyes closed, water streaming over her hair and bare shoulders as she runs her hands back through her wet hair. Dense steam, warm light behind her, glass wall with droplets, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w01-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta bajo una ducha de lluvia, de los hombros hacia arriba, vapor.  
**Consejo:** El agua corriendo más el vapor es muy fiable. Mantén la cámara quieta.

#### W02 · Baño de espuma de lujo

```text
An adult woman relaxes in a clawfoot tub overflowing with foam in a marble bathroom, holding a glass of wine. She lifts one leg slowly out of the bubbles and foam slides down it. Candles, warm golden light, luxury lifestyle mood, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w02-es) | 720p · 5 s · 16:9 | $0.4105 | Principiante |

**Primer fotograma:** Mujer adulta en una bañera con patas llena de espuma y una copa de vino, baño de mármol.  
**Consejo:** La espuma oculta el cuerpo y da un movimiento lento y agradable.

#### W03 · Saliendo de la piscina

```text
An adult woman in a white swimsuit climbs out of a turquoise infinity pool, water streaming off her body, and slicks her wet hair back with both hands. Bright midday sun, sparkling water, luxury villa background, low-angle static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w03-es) | 1080p · 5 s · 16:9 | $2.85 | Intermedio |

**Primer fotograma:** Mujer adulta en el borde de una piscina infinita con un traje de baño blanco.  
**Consejo:** El agua que resbala por la piel luce la física de Seedance.

#### W04 · Escena bajo la lluvia

```text
An adult woman in a soaked white shirt stands in the rain on an empty city street at night, face turned up to the sky, eyes closed. Rain pours over her, neon reflections shimmer on the wet asphalt. Cinematic blue and pink tones, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w04-es) | 1080p · 5 s · 16:9 | $0.7125 | Intermedio |

**Primer fotograma:** Mujer adulta con una camisa blanca mojada en una calle con neones bajo la lluvia, de noche.  
**Consejo:** La lluvia y los reflejos de neón aportan muchísimo valor de producción.

#### W05 · Poza con cascada

```text
An adult woman stands waist-deep in a jungle pool beneath a small waterfall, water cascading over her shoulders and back. She tilts her head back into the stream. Lush green foliage, shafts of sunlight, mist, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w05-es) | 1080p · 5 s · 16:9 | $0.95 | Intermedio |

**Primer fotograma:** Mujer adulta de espaldas bajo una cascada en la selva, con el agua por la cintura.  
**Consejo:** El agua a la altura de la cintura es un recorte natural y fácil.

#### W06 · Aceite y sol

```text
An adult woman lying on a sun lounger slowly smooths tanning oil over her shoulders and arms, skin glistening in bright afternoon sun. Poolside setting, palm shadows, warm saturated colours, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w06-es) | 768p · 5 s · 9:16 | $0.42 | Principiante |

**Primer fotograma:** Mujer adulta en una tumbona junto a una piscina, bikini, sol intenso.  
**Consejo:** La piel brillante y el sol duro dan realismo al instante.

#### W07 · Olas del mar

```text
Wide shot of a nude adult woman lying on wet sand at the waterline as gentle waves wash over her legs and recede. Blue hour light, soft pastel sky, long exposure feel, slow drone descent.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w07-es) | 1080p · 8 s · 21:9 | $0.456 | Principiante |

**Primer fotograma:** Plano general de una mujer adulta tumbada en la orilla, hora azul.  
**Consejo:** LTX maneja movimientos naturales largos y tranquilos a bajo costo.

#### W08 · Jacuzzi de noche

```text
An adult woman relaxes in a steaming outdoor hot tub on a snowy mountain deck at night, arms resting on the edge. Snow falls softly, she tilts her head back and exhales a cloud of breath. Warm underwater lights, cold blue surroundings, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w08-es) | 720p · 5 s · 16:9 | $0.871 | Principiante |

**Primer fotograma:** Mujer adulta en un jacuzzi exterior, terraza nevada de noche.  
**Consejo:** El contraste entre la nieve y el vapor da un fotograma muy potente como miniatura.

#### W09 · Tarde en el onsen

```text
An adult woman in her 30s sits in a steaming Japanese outdoor onsen surrounded by rocks and maple trees, a folded towel on her head. She lifts water in her cupped hands and lets it pour over her shoulder. Soft evening light, lanterns, steam, locked-off camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/es/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w09-es) | 720p · 5 s · 16:9 | $0.13 | Principiante |

**Primer fotograma:** Mujer adulta en un onsen al aire libre con rocas y arces, vapor.  
**Consejo:** El bloqueo de cámara de Seedance 1.5 Pro es ideal para escenas de baño tranquilas.

#### W10 · Pareja en la ducha de cristal

```text
Inside a modern glass shower, an adult couple stands under the water facing each other, her hands on his chest. He brushes wet hair from her face. Warm light, steam, water droplets on glass in the foreground, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w10-es) | 1080p · 5 s · 9:16 | $0.7125 | Intermedio |

**Primer fotograma:** Pareja adulta en una ducha de cristal, frente a frente, vapor.  
**Consejo:** Las gotas en el cristal en primer plano suavizan la imagen y ocultan pequeños errores.

### Fantasía, ciencia ficción y cosplay

Personajes de fantasía adultos. El vestuario y los efectos hacen el trabajo pesado; describe un solo elemento mágico o tecnológico cada vez.

#### X01 · Hechicera elfa oscura

```text
An adult dark elf sorceress with silver hair and pointed ears stands in a ruined temple, wearing a revealing black leather and silver armour set. Violet magic swirls around her hands as she raises them. Candles, floating embers, dark fantasy art style, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x01-es) | 1080p · 5 s · 16:9 | $2.85 | Intermedio |

**Primer fotograma:** Mujer elfa oscura adulta con una armadura reveladora en un templo en ruinas.  
**Consejo:** Un efecto mágico cada vez mantiene legible el encuadre.

#### X02 · Revelación de la súcubo

```text
An adult succubus with curved horns and a slender tail stands in a red-lit gothic chamber in black lingerie. Her dark wings slowly unfurl behind her and she smiles at the camera. Crimson and black palette, smoke, dramatic backlight.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x02-es) | 1080p · 5 s · 9:16 | $0.95 | Intermedio |

**Primer fotograma:** Súcubo adulta con las alas plegadas en una cámara gótica roja.  
**Consejo:** Unas alas que se despliegan son un único movimiento grande que los modelos renderizan bien.

#### X03 · Reina guerrera

```text
An adult warrior queen in her 30s in minimal bronze armour and a fur cape stands on a cliff above a battlefield at dawn. Wind whips her cape and hair as she raises her sword. Epic fantasy lighting, dust, cinematic low-angle shot.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x03-es) | 720p · 5 s · 16:9 | $1.14 | Intermedio |

**Primer fotograma:** Mujer guerrera adulta con armadura de bronce y capa de piel sobre un acantilado.  
**Consejo:** Una capa al viento añade mucho movimiento mientras el cuerpo permanece quieto.

#### X04 · Club cyberpunk

```text
An adult cyberpunk dancer with glowing circuit tattoos and a holographic bodysuit dances slowly on a neon stage in a futuristic club. Holograms flicker around her. Cyan and magenta neon, rain on the window behind, blade-runner mood.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x04-es) | 720p · 5 s · 9:16 | $0.871 | Intermedio |

**Primer fotograma:** Bailarina cyberpunk adulta con tatuajes luminosos en un escenario de neón.  
**Consejo:** Los detalles que emiten luz (tatuajes, hologramas) se animan bien y quedan impresionantes.

#### X05 · Sirena en la superficie

```text
An adult mermaid with long red hair rises from a moonlit sea and rests her arms on a rock, water streaming from her bare shoulders. Her iridescent tail flicks behind her. Silver moonlight, gentle waves, fantasy realism.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x05-es) | 1080p · 5 s · 16:9 | $0.7125 | Intermedio |

**Primer fotograma:** Sirena adulta descansando sobre una roca en un mar iluminado por la luna.  
**Consejo:** El pelo largo cubriendo el pecho es el recorte natural clásico.

#### X06 · Trono de la reina dragón

```text
An adult queen in a sheer golden gown lounges on an obsidian throne. A small dragon curls around the throne and breathes a thin ribbon of fire into the air as she strokes its head. Torchlight, gold and black palette, epic fantasy cinematography.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/es/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x06-es) | 720p · 5 s · 16:9 | $2.16 | Avanzado |

**Primer fotograma:** Reina adulta en un trono de obsidiana con un pequeño dragón.  
**Consejo:** La interacción entre una criatura y una persona es avanzada. Seedance 2.5 Spicy mantiene coherentes a ambos.

#### X07 · Pin-up en la estación espacial

```text
An adult astronaut in a half-unzipped white flight suit floats weightlessly by a large window on a space station, Earth glowing below. Her hair drifts in zero gravity and she smiles at the camera. Cool blue light, retro sci-fi pin-up feel.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x07-es) | 768p · 5 s · 16:9 | $0.42 | Principiante |

**Primer fotograma:** Mujer adulta con un traje de vuelo a medio abrir junto a una ventana de una estación espacial.  
**Consejo:** La gravedad cero justifica el movimiento flotante, lo que disimula la física torpe.

#### X08 · Seducción vampírica

```text
An adult vampire countess in a low-cut crimson velvet gown descends a candlelit stone staircase in a gothic castle, trailing her fingers along the banister. She pauses and smiles, a hint of fangs. Candlelight, deep reds and blacks, gothic horror romance.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x08-es) | 720p · 5 s · 16:9 | $1.14 | Intermedio |

**Primer fotograma:** Mujer vampiro adulta con un vestido carmesí en una escalera gótica.  
**Consejo:** Las escaleras dan un movimiento natural hacia el objetivo que favorece a la cámara.

#### X09 · Diosa de la primavera

```text
An adult goddess with flowers woven into her hair stands in a sunlit meadow, draped only in trailing vines and petals. Blossoms burst open around her as she lifts her arms. Soft golden light, floating pollen, painterly fantasy style.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x09-es) | 1080p · 5 s · 16:9 | $0.95 | Principiante |

**Primer fotograma:** Mujer adulta en un prado cubierta de enredaderas y flores.  
**Consejo:** Los pétalos y las flores son partículas suaves que los modelos animan con facilidad.

#### X10 · Sesión de fotos de cosplay

```text
An adult cosplayer in her 20s in a fitted black catsuit with cat ears poses in a photo studio, turning her hips and looking over her shoulder at the camera. Coloured gel lights in pink and blue, studio flashes firing, behind-the-scenes vibe.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x10-es) | 720p · 5 s · 9:16 | $0.4105 | Principiante |

**Primer fotograma:** Cosplayer adulta con un catsuit y orejas de gato, estudio iluminado con geles de color.  
**Consejo:** El encuadre de detrás de cámaras hace que los movimientos al posar parezcan naturales.

#### X11 · El despertar de la androide

```text
A nude adult female android with seamless white panels and faint blue seams lies on a lab table. Her eyes open, blue light pulses along the seams, and she slowly sits up. Clean white lab, cool light, sci-fi film look, slow push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x11-es) | 1080p · 5 s · 16:9 | $2.85 | Intermedio |

**Primer fotograma:** Androide adulta sobre una mesa blanca de laboratorio, con los ojos cerrados.  
**Consejo:** Los paneles de piel sintética se leen como ciencia ficción y evitan los problemas de realismo.

#### X12 · Baile de máscaras

```text
At a candlelit Venetian masquerade, an adult woman in a gold lace mask and a low-backed black gown turns from a crowd of masked guests and walks toward the camera. Rich gold and black palette, candle bokeh, baroque interior, slow dolly back.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x12-es) | 1080p · 5 s · 16:9 | $0.7125 | Intermedio |

**Primer fotograma:** Mujer adulta con una máscara de encaje dorado y vestido negro en un baile de máscaras.  
**Consejo:** Las máscaras ocultan los artefactos faciales y añaden misterio.

### Estilo anime y hentai

Todos los personajes de esta sección tienen un diseño explícitamente adulto. Genera el primer fotograma con Prefect Pony XL y luego anímalo con Vidu Q3 Spicy o Wan 2.2 Spicy.

#### A01 · Noche en el onsen (anime)

```text
Anime style. An adult woman in her 20s with long purple hair relaxes in a steaming outdoor hot spring at night, a towel wrapped around her. Steam drifts, cherry petals fall onto the water, she smiles and closes her eyes. Soft lantern light, clean cel shading.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a01-es) | 720p · 5 s · 16:9 | $0.7125 | Principiante |

**Primer fotograma:** Mujer adulta de anime en un onsen de noche con una toalla, farolillos.  
**Consejo:** Vidu Q3 Spicy maneja bien el movimiento anime; baja movement_amplitude para escenas tranquilas.

#### A02 · Episodio de playa

```text
Anime style. An adult woman with short blonde hair in a red bikini runs along the shoreline in slow motion, splashing water, hair bouncing. Bright summer sky, sparkling sea, vibrant colours, classic anime beach-episode framing.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a02-es) | 720p · 5 s · 16:9 | $0.7125 | Principiante |

**Primer fotograma:** Mujer adulta de anime con un bikini rojo en una playa.  
**Consejo:** Mantén diseños de personaje claramente adultos: proporciones adultas, cara adulta y edad indicada.

#### A03 · Transformación mágica

```text
Anime style. An adult sorceress spins as ribbons of pink light wrap around her body and form an elegant, revealing magical gown. Sparkles burst around her, hair lifts upward, dramatic transformation sequence, glowing background.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a03-es) | 1080p · 5 s · 9:16 | $0.76 | Intermedio |

**Primer fotograma:** Hechicera adulta de anime en pleno giro con cintas de luz.  
**Consejo:** Las transformaciones son movimientos de cintas y partículas, algo que los modelos de anime hacen bien.

#### A04 · Dormitorio waifu

```text
Anime style. An adult woman with long silver hair lies on her side on a bed in an oversized shirt, propped on one elbow. She blinks slowly and gives a soft smile to the camera, curtains moving in the breeze. Warm afternoon light, detailed anime background.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a04-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta de anime tumbada en una cama con una camisa enorme.  
**Consejo:** Los pequeños movimientos faciales en primeros fotogramas de anime son muy estables en Wan 2.2 Spicy.

#### A05 · Baile de la reina demonio

```text
Anime style. An adult demon queen with horns, red eyes and a black lace outfit dances slowly in a throne room, her tail swaying. Purple fire flickers in braziers, dark fantasy anime aesthetic, dramatic lighting.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a05-es) | 720p · 5 s · 9:16 | $0.7125 | Intermedio |

**Primer fotograma:** Reina demonio adulta de anime con un conjunto de encaje negro en un salón del trono.  
**Consejo:** La cola y el pelo añaden movimiento sin coreografías complejas.

#### A06 · Ecchi en gravedad cero

```text
Anime style. An adult space pilot in a skin-tight flight suit floats in a spaceship cabin, her long hair drifting in zero gravity. She stretches lazily and smiles. Soft blue interior lights, stars through the window, sci-fi anime style.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a06-es) | 720p · 5 s · 16:9 | $0.7125 | Principiante |

**Primer fotograma:** Mujer adulta de anime con traje de vuelo flotando en la cabina de una nave espacial.  
**Consejo:** La gravedad cero hace que el movimiento flotante del anime parezca intencionado.

#### A07 · Encargada de la casa de baños

```text
Anime style. An adult woman in a loose summer yukata kneels by a steaming wooden bath and pours water from a wooden ladle. The yukata slips slightly off one shoulder. Warm lantern light, steam, traditional Japanese interior.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a07-es) | 720p · 5 s · 16:9 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta de anime con yukata arrodillada junto a una bañera de madera.  
**Consejo:** Los escenarios tradicionales con vapor perdonan errores y crean ambiente.

#### A08 · Visita nocturna de la súcubo

```text
Anime style. An adult succubus with bat wings perches on a moonlit window sill, her tail curling. She slowly leans forward toward the camera with a playful smile. Blue moonlight, pink rim light, gothic anime aesthetic.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a08-es) | 720p · 5 s · 9:16 | $0.7125 | Intermedio |

**Primer fotograma:** Súcubo adulta de anime en el alféizar de una ventana a la luz de la luna.  
**Consejo:** Inclinarse hacia la cámara crea intimidad con un movimiento mínimo.

#### A09 · Anfitriona de maid café

```text
Anime style. An adult woman in her 20s in a classic black and white maid outfit with a short skirt bows slightly, then winks at the camera while holding a tray. Pastel cafe interior, soft lighting, cheerful anime style.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a09-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Mujer adulta de anime con uniforme de maid sujetando una bandeja, interior de cafetería.  
**Consejo:** Indica una edad adulta y usa proporciones adultas en el primer fotograma de todos los personajes de anime.

#### A10 · Azotea de neón (anime)

```text
Anime style. An adult woman in a cropped leather jacket and bodysuit stands on a rooftop in a neon city at night, the wind blowing her hair. She turns and looks back at the camera. Pink and cyan neon, rain, detailed cyberpunk anime background.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/es/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a10-es) | 1080p · 5 s · 16:9 | $0.76 | Intermedio |

**Primer fotograma:** Mujer adulta de anime en una azotea con neones de noche, chaqueta de cuero.  
**Consejo:** El viento y un giro de cabeza son los dos movimientos anime más fiables.

### Sensualidad comercial apta para marcas

Estética de anuncios de lencería, trajes de baño y perfumes para marcas para adultos y promociones de creadores. Sugerente, no explícito, así que también sirve para plataformas con normas más estrictas.

#### M01 · Spot para una marca de lencería

```text
High-end lingerie commercial. An adult model in an ivory silk and lace set walks slowly across a sunlit Parisian apartment and stops by the window, turning to camera. Clean luxury aesthetic, soft daylight, subtle camera glide, magazine-grade color.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m01-es) | 1080p · 5 s · 9:16 | $2.85 | Intermedio |

**Primer fotograma:** Modelo adulta con lencería color marfil en un luminoso apartamento parisino.  
**Consejo:** El lenguaje de anuncio premium ("commercial", "magazine-grade") eleva el aspecto general.

#### M02 · Anuncio de perfume

```text
Luxury perfume advertisement. An adult woman in a flowing black satin dress closes her eyes as golden light and slow-motion mist swirl around her bare shoulders. A glass perfume bottle glints in the foreground. Dreamy, sensual, high-fashion color grade.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/es/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m02-es) | 1080p · 5 s · 16:9 | $0.95 | Intermedio |

**Primer fotograma:** Mujer adulta en satén negro con un frasco de perfume en primer plano.  
**Consejo:** Wan 2.7 Spicy puede añadir audio generado para que parezca un anuncio terminado.

#### M03 · Giro para catálogo de trajes de baño

```text
E-commerce swimwear video. An adult model in a one-piece swimsuit turns slowly 360 degrees on a white studio cyclorama to show the fit from all sides. Even soft lighting, clean white background, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m03-es) | 720p · 5 s · 9:16 | $0.4105 | Principiante |

**Primer fotograma:** Modelo adulta con un traje de baño entero sobre un ciclorama blanco.  
**Consejo:** Un giro completo y lento es el formato estándar de producto y se renderiza con fiabilidad.

#### M04 · Detrás de cámaras de una sesión boudoir

```text
Behind-the-scenes of a boudoir photoshoot. An adult woman in a black bodysuit poses on a bed while a softbox flashes. She laughs between poses and shifts into a new position. Warm studio light, candid documentary feel, handheld camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m04-es) | 768p · 5 s · 16:9 | $0.42 | Principiante |

**Primer fotograma:** Mujer adulta posando en una cama con una ventana de luz a la vista, set boudoir.  
**Consejo:** El encuadre de detrás de cámaras hace que el movimiento imperfecto parezca auténtico.

#### M05 · Portada de revista

```text
Living magazine cover. An adult model in a sheer black blazer and nothing underneath holds a confident pose against a bold red backdrop, then slowly turns her chin toward the camera. Hard fashion light, glossy editorial finish, static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m05-es) | 1080p · 5 s · 3:4 | $2.85 | Intermedio |

**Primer fotograma:** Modelo adulta con un blazer transparente sobre un fondo rojo, luz editorial.  
**Consejo:** Un movimiento mínimo sobre una imagen potente es el aspecto de "cinemagraph".

#### M06 · Presentación de una marca fitness

```text
Fitness apparel ad. An adult athlete in a sports bra and leggings finishes a set, towels sweat from her neck and smiles at the camera. Gritty gym, hard top light, glistening skin, energetic handheld camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/es/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m06-es) | 720p · 5 s · 9:16 | $0.871 | Principiante |

**Primer fotograma:** Atleta adulta con un sujetador deportivo en un gimnasio de aspecto crudo.  
**Consejo:** Seedance 2.0 Fast Spicy añade sonido, útil para anuncios en redes sociales.

#### M07 · Promoción de una suite de hotel

```text
Luxury hotel promo. The camera glides through a penthouse suite at dusk, past a champagne bucket, to an adult woman in a silk robe standing at the floor-to-ceiling window over the city. She turns and raises her glass. Warm interior light, city lights, smooth gimbal move.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m07-es) | 1080p · 10 s · 16:9 | $1.425 | Intermedio |

**Primer fotograma:** Suite de ático al anochecer con una mujer adulta en bata de seda junto a la ventana.  
**Consejo:** Wan 2.6 Spicy admite tomas de 10 segundos para recorridos de cámara más largos.

#### M08 · Anuncio de joyería

```text
Fine jewelry ad. Close-up of an adult woman's bare neck and collarbone as a diamond necklace is fastened by unseen hands. She tilts her head and the diamonds sparkle. Black background, precise beauty lighting, macro detail.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m08-es) | 1080p · 5 s · 1:1 | $2.85 | Intermedio |

**Primer fotograma:** Primer plano del cuello y la clavícula de una mujer adulta, fondo negro.  
**Consejo:** El encuadre macro de belleza es premium y casi no tiene artefactos.

#### M09 · Loción corporal

```text
Skincare commercial. An adult woman wrapped in a white towel smooths body lotion down her leg on the edge of a bathtub. Soft daylight, clean white bathroom, dewy skin, gentle camera tilt down.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m09-es) | 1080p · 5 s · 9:16 | $0.285 | Principiante |

**Primer fotograma:** Mujer adulta con una toalla sentada en el borde de una bañera, aplicándose loción.  
**Consejo:** Un lenguaje limpio de anuncio de producto lo mantiene apto para marcas.

#### M10 · Teaser de creadora

```text
Vertical social teaser. An adult creator in a silk robe sits on her bed, looks straight at the camera, raises a finger to her lips with a playful smile, then winks. Soft ring-light glow, cosy bedroom, static phone camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m10-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Creadora adulta con bata de seda en una cama, de frente a la cámara, aro de luz.  
**Consejo:** Los teasers cortos y sugerentes llevan clics a plataformas de pago sin salirse de las normas de las redes sociales.

### Plantillas reutilizables de movimiento y cámara

Prompts listos para usar que solo describen el movimiento y la cámara. Combínalos con cualquier primer fotograma; funcionan porque los modelos de imagen a video ya ven al sujeto.

#### T01 · Acercamiento lento

```text
Slow, steady push-in from medium shot to close-up. Subject breathes naturally and blinks once. Hair moves slightly. Lighting stays consistent.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t01-es) | 480p · 5 s · cualquier relación de aspecto | $0.095 | Principiante |

**Primer fotograma:** Cualquier sujeto adulto bien iluminado, plano medio.  
**Consejo:** La plantilla universal más segura. Haz los borradores a 480p y vuelve a renderizar los mejores a 720p.

#### T02 · Órbita a la izquierda

```text
Camera orbits slowly to the left around the subject, keeping them centred. Subject stays mostly still and follows the camera with their eyes.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/es/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t02-es) | 720p · 5 s · cualquier relación de aspecto | $1.14 | Intermedio |

**Primer fotograma:** Sujeto adulto centrado, con algo de profundidad en el fondo.  
**Consejo:** Las órbitas necesitan un modelo con buena coherencia 3D. Seedance es la opción más segura.

#### T03 · Mirada por encima del hombro

```text
Subject facing away slowly turns their head to look back over their shoulder at the camera and smiles. Static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t03-es) | 720p · 5 s · cualquier relación de aspecto | $0.19 | Principiante |

**Primer fotograma:** Sujeto adulto de espaldas o en vista de tres cuartos de espaldas.  
**Consejo:** Funciona con cualquier primer fotograma de espaldas.

#### T04 · Viento y tela

```text
A steady breeze moves the subject's hair and clothing. Fabric ripples and flows. Subject stays still and relaxed. Static camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/es/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t04-es) | 720p · 5 s · cualquier relación de aspecto | $0.19 | Principiante |

**Primer fotograma:** Sujeto adulto con ropa holgada y pelo largo.  
**Consejo:** Da vida a cualquier imagen fija sin tocar la anatomía.

#### T05 · Revelación con tilt hacia arriba

```text
Camera starts at the subject's feet and tilts up slowly along the body to end on their face. Subject stands still and looks into the lens at the end.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t05-es) | 720p · 5 s · 9:16 | $0.19 | Principiante |

**Primer fotograma:** Plano vertical de cuerpo entero de un sujeto adulto de pie.  
**Consejo:** Usa un primer fotograma vertical de cuerpo entero.

#### T06 · Revelación con dolly hacia atrás

```text
Camera starts on a close-up of the subject's face and pulls back slowly to reveal the full room around them. Subject stays still with a subtle smile.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/es/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t06-es) | 720p · 5 s · 16:9 | $0.475 | Intermedio |

**Primer fotograma:** Primer plano de la cara de un sujeto adulto con indicios de la habitación.  
**Consejo:** El modelo tiene que inventarse la habitación, así que descríbela en una línea si el primer fotograma es cerrado.

#### T07 · Espontáneo cámara en mano

```text
Handheld phone-camera feel with slight natural shake. Subject laughs, glances away, then back at the camera, adjusting their hair.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/es/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t07-es) | 768p · 5 s · 9:16 | $0.42 | Principiante |

**Primer fotograma:** Encuadre informal, estilo selfie, de un sujeto adulto.  
**Consejo:** El temblor de la cámara en mano hace que el video con IA parezca grabado de verdad por un creador.

#### T08 · Cambio de foco

```text
Focus shifts slowly from an object in the foreground to the subject in the background. Subject turns toward the camera as they come into focus.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/es/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t08-es) | 720p · 5 s · 16:9 | $0.4105 | Intermedio |

**Primer fotograma:** Objeto en primer plano enfocado y un sujeto adulto desenfocado detrás.  
**Consejo:** Pon un objeto claro en primer plano (una copa, una flor, una vela) en el primer fotograma.

#### T09 · Cinemagraph con cámara fija

```text
Completely static camera. Only small natural motion: breathing, a slow blink, candle flicker, curtains moving slightly. Everything else stays still.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/es/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t09-es) | 720p · 5 s · cualquier relación de aspecto | $0.13 | Principiante |

**Primer fotograma:** Cualquier imagen fija bien compuesta de un sujeto adulto con una fuente de luz o una cortina.  
**Consejo:** El bloqueo de cámara de Seedance 1.5 Pro Spicy, sumado al precio por segundo más bajo, lo convierte en el mejor motor para cinemagraphs.

#### T10 · Transición del fotograma inicial al final

```text
Smooth, natural transition from the opening pose to the closing pose. Subject moves continuously with no cuts. Lighting and wardrobe stay consistent.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/es/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t10-es) | 720p · 8 s · cualquier relación de aspecto | $0.304 | Avanzado |

**Primer fotograma:** Dos imágenes fijas del mismo sujeto adulto: pose inicial y pose final.  
**Consejo:** Envía un last_image_url con la pose final. Wan 2.2 Spicy y Seedance 2.x admiten primer + último fotograma.

### Prompts de estilo con LoRA (Wan 2.2 Spicy LoRA)

Prompts pensados para combinarse con un LoRA de estilo. Pon primero la palabra de activación del LoRA y centra el resto del prompt en el movimiento.

#### L01 · LoRA de estilo anime

```text
<trigger word>, anime style, an adult woman with long pink hair in a loose kimono sits by a window at night, cherry petals drifting past, she turns and smiles, soft cel shading, gentle camera push-in.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l01-es) | 480p · 5 s · 16:9 | $0.12 | Intermedio |

**Primer fotograma:** Mujer adulta estilo anime junto a una ventana, generada con Prefect Pony XL.  
**Consejo:** Pasa el LoRA de anime en high_noise_loras para definir la composición; una intensidad de 0.8 es un buen punto de partida.

#### L02 · LoRA de fotografía analógica

```text
<trigger word>, 35mm film photograph, an adult woman in a white slip dress on an unmade bed in morning light, she stretches and pulls the sheet around her, visible grain, faded warm tones.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l02-es) | 720p · 5 s · 16:9 | $0.24 | Intermedio |

**Primer fotograma:** Mujer adulta en una cama deshecha con luz de la mañana.  
**Consejo:** Los LoRAs de textura (grano, tipo de película) van en low_noise_loras, que actúan al final de la eliminación de ruido.

#### L03 · LoRA de pintura al óleo

```text
<trigger word>, oil painting, a nude adult woman reclining on red velvet in a baroque interior, candlelight flickers across her skin, visible brush strokes, rich chiaroscuro.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l03-es) | 720p · 5 s · 4:5 | $0.24 | Intermedio |

**Primer fotograma:** Imagen de estilo barroco de una mujer adulta reclinada sobre terciopelo rojo.  
**Consejo:** Los LoRAs de estilo pueden desviarse con el movimiento; limita el movimiento a la luz y la respiración.

#### L04 · LoRA de coherencia de personaje

```text
<trigger word>, the same adult woman walks toward the camera down a hotel corridor in a red dress, confident smile, warm sconce lighting, low-angle tracking shot.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l04-es) | 720p · 5 s · 9:16 | $0.24 | Avanzado |

**Primer fotograma:** Tu personaje ficticio en el pasillo de un hotel, vestido rojo.  
**Consejo:** Entrena LoRAs de personaje solo con personajes ficticios, o contigo mismo o con adultos que hayan dado su consentimiento documentado.

#### L05 · LoRA cyberpunk de neón

```text
<trigger word>, cyberpunk, an adult woman with glowing tattoos leans against a wet alley wall under neon signs, rain falling, she exhales smoke and looks at the camera.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l05-es) | 480p · 5 s · 16:9 | $0.12 | Intermedio |

**Primer fotograma:** Mujer adulta en un callejón de neón con tatuajes luminosos.  
**Consejo:** Combina como máximo un LoRA de estilo con un LoRA de iluminación. Con más de dos suelen entrar en conflicto.

#### L06 · Extender un clip

```text
Continue the motion naturally from the last frame. Same subject, same wardrobe, same lighting. She slowly turns away and walks toward the window.
```

| Modelo | Ajustes | Costo por ejecución | Nivel |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/es/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l06-es) | 720p · 5 s · cualquier relación de aspecto | $0.24 | Avanzado |

**Primer fotograma:** El clip terminado que quieres continuar, pasado como video_url.  
**Consejo:** Usa el endpoint video-extend (alibaba/wan-2.2-spicy-lora/video-extend) con los mismos LoRAs para encadenar 5 s + 5 s + 5 s.


---

## Prompts de imagen para el primer fotograma

Un video de imagen a video solo es tan bueno como su primer fotograma. Estos prompts generan primeros fotogramas limpios y bien iluminados de sujetos adultos que se animan bien: un solo sujeto (o una pareja claramente separada), fondo sencillo, manos relajadas y la cara despejada u oculta a propósito. Los primeros fotogramas fotorrealistas usan Qwen Image 2.1, el modelo de imagen sin censura recomendado en SpicyAPI; los de anime usan Prefect Pony XL.

#### R01 · Boudoir con luz de ventana

```text
Photorealistic boudoir portrait of a woman in her early 30s sitting on the edge of an unmade bed in black lace lingerie, soft window light from the left, warm neutral bedroom, relaxed hands resting on her knees, looking at the camera, 85mm lens, shallow depth of field, natural skin texture.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r01-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R02 · Retrato con bata de seda

```text
Photorealistic portrait of an adult woman in her late 20s in an ivory silk robe slipping off one shoulder, standing by a candlelit vanity, warm amber light, soft bokeh, calm expression, editorial beauty photography.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r02-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R03 · Reclinada sobre satén rojo

```text
Wide editorial photograph of an adult woman lying on her side on red satin sheets in a red lace bodysuit, crimson key light from the right, cool blue fill from the left, full body in frame, clean composition, high-end fashion photography.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r03-es) · `aspect_ratio=3:2` `resolution=1k` · $0.024 por imagen

#### R04 · Tacones en el pasillo del hotel

```text
Full-body photograph of an adult woman in her 30s in black lingerie, stockings and stiletto heels standing at the far end of a dim hotel corridor, warm wall sconces, glossy floor reflections, low camera angle, cinematic color grade.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r04-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R05 · Ducha de lluvia

```text
Photorealistic shot of an adult woman from the shoulders up under a rainfall shower, eyes closed, water running through her hair, dense steam, warm backlight, glass wall with droplets, tasteful framing.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r05-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R06 · Estudio de figura en monocromo

```text
Black and white fine-art figure study of a nude adult man in his 30s seated on a wooden stool, grey seamless backdrop, single large softbox from above left, sculpted shadows, classical pose, museum print quality.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r06-es) · `aspect_ratio=4:5` `resolution=1k` · $0.024 por imagen

#### R07 · Torso con sombras de persiana

```text
High-contrast black and white photograph of an adult woman's torso in a dark room, hard striped light from window blinds across her skin, film noir mood, abstract and artistic, face out of frame.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r07-es) · `aspect_ratio=1:1` `resolution=1k` · $0.024 por imagen

#### R08 · Pareja en un dormitorio con velas

```text
Cinematic photograph of an adult couple in their 30s standing close in a candlelit bedroom, she wears a black slip dress, he wears an open white shirt, foreheads touching, side view, clear separation of the two figures, warm candlelight, shallow depth of field.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r08-es) · `aspect_ratio=3:2` `resolution=1k` · $0.024 por imagen

#### R09 · Dos mujeres en un sofá de terciopelo

```text
Editorial photograph of two adult women in their late 20s sitting face to face on a burgundy velvet sofa, one in black lace, one in white satin, soft smiles, warm candlelight, rich interior, clearly distinct outfits.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r09-es) · `aspect_ratio=3:2` `resolution=1k` · $0.024 por imagen

#### R10 · Saliendo de la piscina infinita

```text
Photorealistic shot of an adult woman in a white one-piece swimsuit at the edge of a turquoise infinity pool, hands on the ledge about to climb out, bright midday sun, luxury villa background, low angle.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r10-es) · `aspect_ratio=3:2` `resolution=1k` · $0.024 por imagen

#### R11 · Calle de neón bajo la lluvia

```text
Cinematic night photograph of an adult woman in a soaked white shirt standing on an empty city street in the rain, face turned up, neon signs reflecting in wet asphalt, blue and pink palette, 35mm film look.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r11-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R12 · Hechicera elfa oscura

```text
Fantasy art photograph of an adult dark elf woman with silver hair and pointed ears in revealing black leather and silver armour, standing in a ruined candlelit temple, violet magic glow in her open hands, dramatic rim light, highly detailed.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r12-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R13 · Cámara de la súcubo

```text
Dark fantasy portrait of an adult succubus with curved horns, folded black wings and a slender tail, wearing black lingerie, standing in a red-lit gothic chamber, smoke, dramatic backlight, detailed skin and wings.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r13-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R14 · Androide en una mesa de laboratorio

```text
Sci-fi photograph of an adult female android with seamless white synthetic panels and faint blue seams lying on a clean white lab table, eyes closed, cool clinical light, minimalist lab, film still.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r14-es) · `aspect_ratio=3:2` `resolution=1k` · $0.024 por imagen

#### R15 · Invitada al baile de máscaras

```text
Baroque masquerade photograph of an adult woman in a gold lace mask and a low-backed black gown, candlelit Venetian ballroom with masked guests softly blurred behind her, gold and black palette.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r15-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R16 · Onsen anime

```text
score_9, score_8_up, anime style, 1woman, adult, mature female, long purple hair, towel, outdoor hot spring, night, steam, cherry blossoms, paper lanterns, soft smile, detailed background
```

[Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r16-es) · `size=1216*832` · $0.015 por imagen

#### R17 · Playa anime

```text
score_9, score_8_up, anime style, 1woman, adult, mature female, short blonde hair, red bikini, beach, running, splashing water, summer sky, vibrant colors, dynamic pose
```

[Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r17-es) · `size=1216*832` · $0.015 por imagen

#### R18 · Reina demonio anime

```text
score_9, score_8_up, anime style, 1woman, adult, mature female, demon queen, horns, red eyes, tail, black lace outfit, throne room, purple fire braziers, dramatic lighting, confident expression
```

[Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r18-es) · `size=832*1216` · $0.015 por imagen

#### R19 · Dormitorio anime de pelo plateado

```text
score_9, score_8_up, anime style, 1woman, adult, mature female, long silver hair, oversized shirt, lying on side, bed, propped on elbow, afternoon light, curtains, soft smile, detailed room
```

[Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r19-es) · `size=1216*832` · $0.015 por imagen

#### R20 · Azotea cyberpunk anime

```text
score_9, score_8_up, anime style, 1woman, adult, mature female, cropped leather jacket, bodysuit, rooftop, neon city, night, rain, wind in hair, looking back, cyberpunk
```

[Prefect Pony XL](https://spicyapi.ai/es/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r20-es) · `size=1216*832` · $0.015 por imagen

#### R21 · Catálogo de lencería

```text
Clean e-commerce photograph of an adult model in an ivory silk and lace lingerie set standing on a white studio cyclorama, even soft lighting, full body, neutral pose, catalog style.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r21-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R22 · Selfie de creadora

```text
Casual smartphone-style selfie of an adult woman in her late 20s in a silk robe sitting on her bed, ring-light glow, cosy bedroom, natural makeup, playful expression, realistic phone photo.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r22-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R23 · Atleta en el gimnasio

```text
Photorealistic shot of an adult female athlete in a sports bra and leggings in a gritty gym, towel around her neck, hard top light, glistening skin, confident look at the camera.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r23-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen

#### R24 · Boudoir masculino

```text
Photorealistic boudoir portrait of an adult man in his 30s lying back on white sheets, bare chest, grey sweatpants, soft morning window light, relaxed smile, shallow depth of field, editorial style.
```

[Qwen Image 2.1](https://spicyapi.ai/es/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r24-es) · `aspect_ratio=2:3` `resolution=1k` · $0.024 por imagen


**Lista de control del primer fotograma:** sujeto grande en el encuadre · manos relajadas o fuera de plano · fondo sencillo y despejado · iluminación acorde con el ambiente que quieres en movimiento · en parejas, cuerpos bien separados y ropa de colores distintos · resolución al menos igual a la del video que vas a renderizar.

---

## Prompts negativos

Úsalos en los modelos que aceptan el campo `negative_prompt` (Wan 2.6 Spicy y Wan 2.7 Spicy en SpicyAPI). En los demás modelos, incorpora los elementos más importantes al prompt principal en positivo ("natural skin texture", "consistent anatomy").

**Universales**
```
blurry, low quality, jpeg artifacts, watermark, text, logo, deformed, distorted, disfigured,
bad anatomy, extra limbs, extra fingers, fused fingers, mutated hands, long neck, cross-eyed
```

**Realismo**
```
plastic skin, airbrushed, mannequin, doll-like, uncanny valley, waxy face, overexposed,
oversaturated, cartoon, 3d render
```

**Movimiento y continuidad**
```
flickering, morphing, warping background, sudden cuts, identity change, clothing change,
extra person, duplicate body, jittery motion, frozen frames
```

**Anime**
```
worst quality, low quality, bad hands, messy lines, off-model, inconsistent eyes, extra digits,
childlike proportions
```

---

## Guía rápida de cámara, iluminación y movimiento

**Movimientos de cámara**

| Término | Efecto | Fiabilidad |
|---|---|---|
| `static camera` / `locked-off` | La cámara no se mueve | Máxima |
| `slow push-in` | Se acerca al sujeto | Alta |
| `pull back` / `dolly out` | Se aleja y revela la habitación | Alta |
| `tilt up` / `tilt down` | Gira en vertical recorriendo el cuerpo | Alta |
| `tracking shot` | Sigue al sujeto de lado | Media |
| `orbit left / right` | Rodea al sujeto | Media (mejor en Seedance) |
| `handheld` | Ligero temblor natural, aspecto de video de creador | Media |
| `rack focus` | El foco pasa del primer plano al sujeto | Media |
| `drone descent` / `drone pull-back` | Movimiento amplio desde lo alto | Media |
| `POV` | Vista en primera persona | Más baja |

**Iluminación según el ambiente**

| Ambiente | Escribe |
|---|---|
| Romántico | warm candlelight, golden tones, soft diffused light |
| Dramático | single hard key light, deep shadows, chiaroscuro |
| Etéreo | backlit, glowing highlights, haze, bloom |
| Noir | slatted blinds light, black and white, cigarette smoke |
| Lujo | soft beauty lighting, no harsh shadows, glossy highlights |
| Misterioso | rim light only, face in shadow, silhouette |
| Natural | window light, golden hour, soft ambient |
| Neón | magenta and cyan neon, wet reflections, rain |

**Guía de duración**

| Contenido | Duración | Por qué |
|---|---|---|
| Respiración, cinemagraph | 4–5 s | Con un movimiento mínimo se mantiene la calidad |
| Un gesto o un giro de cabeza | 5 s | Una sola acción clara |
| Caminar, revelar, recorrido de cámara | 5–8 s | Movimiento continuo pero sencillo |
| Baile, escenas de dos personas | 5 s | Los clips más largos acumulan artefactos |
| Escenas más largas | Extiende por partes | Usa `video-extend` o encadena usando el último fotograma |

---

## Consejos por modelo

- **Seedance 2.5 / Seedance 2.0 / Wan 3.0 (estándar, unrestricted)**: úsalos cuando quieras texto a video o referencia a video (poner a tu personaje de `@Image1` en una escena nueva). Aceptan prompts para adultos, pero no están ajustados para contenido explícito como las ediciones Spicy.
- **Wan 2.2 Spicy** (desde $0.019/s): la duración es exactamente de 5 u 8 segundos. Admite `last_image_url` para fijar el final, y `enable_prompt_expansion`. Borrador a 480p, versión final a 720p.
- **Wan 2.2 Spicy LoRA** (desde $0.024/s): hasta tres LoRAs mediante `loras`, `high_noise_loras` (composición, movimiento) y `low_noise_loras` (textura, detalle). El endpoint `video-extend` continúa un clip con los mismos LoRAs.
- **LTX 2.3 Spicy** (desde $0.019/s): hasta 20 segundos por llamada, prompt opcional. Bueno para tomas largas y tranquilas.
- **Seedance 1.5 Pro Spicy** (desde $0.012/s): `camera_fixed` bloquea la cámara. El motor más barato para cinemagraphs.
- **Seedance 2.0 Mini / Fast / 2.0 Spicy**: primer + último fotograma, audio generado opcional, la mejor coherencia de movimiento por dólar. 2.0 Spicy llega hasta 4K.
- **Seedance 2.5 Spicy** (desde $0.216/s): tomas de 4–30 segundos, hasta 1080p nativo. Úsalo para versiones finales y movimientos difíciles (levantar a alguien, contacto entre dos personas).
- **MiniMax H3 Spicy** (desde $0.038/s): movimiento natural de cuerpo entero, 3–15 segundos, prompt opcional.
- **Vidu Q3 Spicy** (desde $0.0665/s): anime y movimiento estilizado; `movement_amplitude` controla cuánto se mueven las cosas.
- **Wan 2.6 Spicy / Wan 2.7 Spicy**: aceptan `negative_prompt` y tu propio `audio_url`; Wan 2.6 tiene `shot_type` para varios planos y Wan 2.7 puede generar audio.

---

## El flujo de imagen a video

```
1. Primer fotograma → Qwen Image 2.1 (fotorrealista, desde $0.024) o Prefect Pony XL (anime)
2. Retocar detalles → Qwen Image Edit Spicy (cambia ropa, pose o iluminación con una instrucción)
3. Borrador         → Wan 2.2 Spicy o LTX 2.3 Spicy a 480p, 3–5 variaciones
4. Render final     → el prompt del mejor borrador en Seedance 2.0 Spicy / 2.5 Spicy o Wan 2.6 Spicy a 720p–1080p
5. Extender         → video-extend de Wan 2.2 Spicy LoRA, o encadenar con el último fotograma
6. Pulir            → Video Upscaler, Lip Sync o Video Sound Effects
```

Un clip típico de 5 segundos hecho así cuesta unos **$0.024 (primer fotograma) + $0.29 (tres borradores a 480p) + $1.14 (una versión final a 720p con Seedance 2.0 Spicy) ≈ $1.45**.

---

## Ejecuta un prompt en 60 segundos

**Sin código:** pega cualquier prompt en [SpicyAPI Studio › imagen a video](https://spicyapi.ai/es/create/image-to-video?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=run-es) o en el [generador de videos con IA sin censura](https://spicyapi.ai/es/create/uncensored-ai-video-generator?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=run-es), sube tu primer fotograma y revisa el precio antes de generar.

**cURL:**

```bash
export SPICY_API_KEY="sk-spicy-..."   # https://spicyapi.ai/es/console

curl -s https://api.spicyapi.ai/api/v1/jobs/createTask \
  -H "Authorization: Bearer $SPICY_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: $(uuidgen)" \
  -d '{
    "model": "alibaba/wan-2.2-spicy/image-to-video",
    "input": {
      "image_url": "https://example.com/first-frame.jpg",
      "prompt": "A woman in her late 20s in black lace lingerie slowly turns toward the camera in a dim bedroom. Slow push-in, warm lamp light.",
      "duration_seconds": 5,
      "resolution": "720p"
    }
  }'

# Consulta hasta que data.state sea "succeeded" y luego descarga data.output.assets[0].url
curl -s "https://api.spicyapi.ai/api/v1/jobs/recordInfo?taskId=TASK_ID" \
  -H "Authorization: Bearer $SPICY_API_KEY"
```

**Python (solo biblioteca estándar):**

```python
import json, os, time, urllib.request, uuid

API = "https://api.spicyapi.ai/api/v1"
HEADERS = {"Authorization": f"Bearer {os.environ['SPICY_API_KEY']}", "Content-Type": "application/json"}

def call(method, path, body=None, extra_headers=None):
    req = urllib.request.Request(API + path, method=method, headers={**HEADERS, **(extra_headers or {})},
                                 data=json.dumps(body).encode() if body else None)
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["data"]

task = call("POST", "/jobs/createTask", {
    "model": "alibaba/wan-2.2-spicy/image-to-video",
    "input": {"image_url": "https://example.com/first-frame.jpg",
              "prompt": "She turns slowly toward the camera, silk robe slipping off one shoulder, candlelight, slow push-in.",
              "duration_seconds": 5, "resolution": "480p"},
}, {"Idempotency-Key": str(uuid.uuid4())})

while task["state"] in ("queued", "running"):
    time.sleep(5)
    task = call("GET", f"/jobs/recordInfo?taskId={task['taskId']}")

print(task["state"], task.get("output", {}).get("assets", [{}])[0].get("url"))
```

¿Lo prefieres dentro de Claude Code, Cursor o Codex? Instala **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.es.md)** y pídeselo sin más: *"anima esta imagen con el prompt B02 de nsfw-ai-video-prompts"*.

---

## Deja que un LLM escriba tus prompts

Pega este prompt de sistema en cualquier modelo de chat (en SpicyAPI, [Grok 4.7](https://spicyapi.ai/es/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=llm-es) o [DeepSeek V4.1 Flash](https://spicyapi.ai/es/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=llm-es) funcionan bien a través del endpoint compatible con OpenAI):

```text
You write prompts for adult image-to-video models. Every character is an adult; always state an age of 21 or older
and never use descriptors that suggest youth. Never depict real, identifiable people.
Given a short idea and a description of the first frame, return ONE prompt of 40–80 words that:
1) describes only what changes from the first frame, 2) has exactly one main action,
3) adds one secondary motion (hair, fabric, light, water, steam), 4) names one camera move,
5) names the light sources, 6) ends with a short style phrase. Also return a 1-line negative prompt.
```

---

## Preguntas frecuentes

### ¿Cuáles son los mejores prompts de video con IA NSFW para Wan 2.2?
Prompts cortos, con una sola acción y un movimiento de cámara con nombre: consulta [Boudoir y lencería](#boudoir-y-lencería) y [Plantillas reutilizables de movimiento y cámara](#plantillas-reutilizables-de-movimiento-y-cámara). Wan 2.2 Spicy genera exactamente 5 u 8 segundos, así que escribe una acción por clip y usa `last_image_url` cuando necesites un final concreto.

### ¿Cómo se escribe un prompt NSFW de imagen a video?
Parte de un primer fotograma sólido y describe solo el movimiento: una acción principal, un movimiento secundario, la cámara y la luz. Que no pase de 40–80 palabras. Consulta [Cómo escribir un prompt de video NSFW que funcione](#cómo-escribir-un-prompt-de-video-nsfw-que-funcione).

### ¿Qué modelo es mejor para imagen a video NSFW?
En calidad, Seedance 2.5 Spicy y Seedance 2.0 Spicy. En precio, Wan 2.2 Spicy y LTX 2.3 Spicy (desde $0.019/s). Para anime, Vidu Q3 Spicy. Para estilos personalizados, Wan 2.2 Spicy LoRA. Compáralos en las [clasificaciones de SpicyAPI](https://spicyapi.ai/es/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=faq-es).

### ¿Por qué mis videos NSFW con IA salen con la anatomía mal?
Normalmente, por demasiado movimiento para la duración del clip. Acórtalo a 5 segundos, limítalo a una sola acción, deja las manos fuera de plano o relajadas, usa ángulos laterales o de espaldas para los planos de cuerpo entero y elige un modelo más potente (Seedance 2.x) para escenas de dos personas.

### ¿Puedo usar estos prompts con Stable Diffusion o ComfyUI?
Sí. Los prompts de primer fotograma funcionan en cualquier flujo de SDXL, Pony o Z-Image, y los prompts de video funcionan con Wan 2.2 autoalojado en ComfyUI. Cuenta con tener que ajustar la intensidad y los pasos en local.

### ¿Cuánto cuesta generar un video NSFW con IA?
En SpicyAPI (catálogo del 2026-09-27), un clip de 5 segundos cuesta desde $0.06 (Seedance 1.5 Pro Spicy, 480p) o $0.095 (Wan 2.2 Spicy, 480p) hasta unos $5.40 (Seedance 2.5 Spicy a 1080p). Cada prompt de arriba indica su propio costo.

### ¿Hay algún generador de prompts de video NSFW gratis?
Usa el [prompt de sistema para LLM](#deja-que-un-llm-escriba-tus-prompts) de arriba con cualquier modelo de chat, incluidos los locales en Ollama o LM Studio.

---

## Reglas

- **Solo adultos.** Nada de contenido sexual que involucre a menores de 18 años o a quien parezca menor de 18, en ningún estilo, incluido el anime. "En realidad tiene 500 años" no es una excepción.
- **Nada de personas reales sin consentimiento documentado.** Nada de deepfakes sexuales, de cambios de cara de personas reales en contenido sexual ni de fotos reales "desvestidas". Las figuras públicas no son una excepción.
- **Cumple la ley** del lugar donde vives y donde vive tu público, y las normas de las plataformas donde publiques.
- Normas completas de SpicyAPI: [Política de contenidos](https://spicyapi.ai/es/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=rules-es) · [Política de uso aceptable](https://spicyapi.ai/es/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=rules-es).

## Relacionados

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.es.md)**: lista seleccionada de herramientas, APIs y modelos de IA sin censura para imagen, video y texto.
- **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.es.md)**: genera imágenes y videos NSFW desde Claude Code, Cursor, Codex y otros agentes.
- Datos legibles por máquina: [`data/video-prompts.json`](data/video-prompts.json), [`data/image-prompts.json`](data/image-prompts.json), [`data/showcase.json`](data/showcase.json).

## Cómo contribuir

Se aceptan pull requests con prompts. Añádelos a `data/video-prompts.json` (solo personajes adultos, una acción principal, modelo + ajustes + consejo) y luego ejecuta `python3 scripts/build_readme.py`. Las comprobaciones de estilo CI están en `scripts/check_prompts.py`.

## Licencia

Prompts y documentación: [CC0 1.0](LICENSE). Las vistas previas de `assets/showcase/` son fragmentos GIF cortos de resultados de ejemplo de SpicyAPI; los clips completos siguen en la CDN de SpicyAPI.

<p align="center"><sub>⭐ Dale una estrella al repositorio si algún prompt te ha ahorrado unos cuantos intentos.</sub></p>
