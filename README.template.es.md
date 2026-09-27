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
  <b>{{VIDEO_COUNT}} prompts de video con IA NSFW para copiar y pegar, {{IMAGE_COUNT}} prompts de imagen para el primer fotograma y {{SHOWCASE_COUNT}} ejemplos con resultados reales, para Wan 2.2 Spicy, Seedance Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy y otros modelos de imagen a video sin censura.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/video%20prompts-{{VIDEO_COUNT}}-ff4d6d" alt="{{VIDEO_COUNT}} prompts de video">
  <img src="https://img.shields.io/badge/first--frame%20prompts-{{IMAGE_COUNT}}-8b5cf6" alt="{{IMAGE_COUNT}} prompts de imagen">
  <img src="https://img.shields.io/badge/showcase-{{SHOWCASE_COUNT}}-10b981" alt="{{SHOWCASE_COUNT}} ejemplos reales">
  <img src="https://img.shields.io/badge/updated-{{READ_ON}}-blue" alt="Actualizado: {{READ_ON}}">
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

Los datos de los modelos y los precios proceden del catálogo público de SpicyAPI, consultado el {{READ_ON}}.

## Contenido

- [Modelos incluidos](#modelos-incluidos)
- [Ejemplos reales: resultados y sus prompts](#ejemplos-reales-resultados-y-sus-prompts)
- [Cómo escribir un prompt de video NSFW que funcione](#cómo-escribir-un-prompt-de-video-nsfw-que-funcione)
- [Los prompts](#los-prompts)
{{PROMPTS_TOC}}
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

{{MODEL_TABLE}}

El orden sigue el catálogo de SpicyAPI: primero los más populares y la versión más reciente. Las ediciones 🌶️ Spicy están ajustadas para contenido adulto; los modelos estándar de esta lista tienen el nivel `unrestricted` en el catálogo (el proveedor no los filtra), así que también sirven para prompts para adultos y añaden texto a video y referencia a video. Los precios corresponden al nivel más barato; la página del modelo es siempre la referencia. El **Spicy Index** (puntuación de capacidades preliminar) y el **Freedom** (con qué fiabilidad se generan tal como se pidieron cinco niveles de contenido explícito) proceden de las [clasificaciones públicas de SpicyAPI](https://spicyapi.ai/es/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=models-es): ✅ 90+ · ◐ 70–89 · ⚠️ menos de 70 · 🧪 menos de 15 pruebas. Las ejecuciones fallidas se reembolsan automáticamente.

---

## Ejemplos reales: resultados y sus prompts

{{SHOWCASE_COUNT}} casos reales sacados de las páginas de los modelos y de la [biblioteca de prompts](https://spicyapi.ai/es/prompts?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-es) de SpicyAPI. Cada caso muestra un resultado junto al prompt exacto que lo generó. Los modelos aparecen de más a menos popular y con la versión más reciente primero: ediciones Spicy y modelos estándar con nivel `unrestricted` en el catálogo. Haz clic en una vista previa para ver el clip en calidad completa.

{{SHOWCASE}}

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

{{PROMPTS}}

---

## Prompts de imagen para el primer fotograma

{{IMAGE_INTRO}}

{{IMAGE_PROMPTS}}

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

Según las pruebas de SpicyAPI (clasificación v2.1 y las reseñas de los modelos, 2026-09-27):

- **Wan 3.0** (desde $0.045/s): el mejor modelo de video NSFW para todo en las pruebas: Index 76.5, Freedom 96, generó todos los prompts de prueba explícitos. A partir de texto, una imagen fija o referencias, 2–30 s con sonido. Puede ir más allá de tu prompt, así que revisa los últimos segundos; la referencia a video rechaza fotos de caras reales.
- **Seedance 2.5 Spicy** (desde $0.216/s): es el que más lejos llega en los niveles más duros a partir de una imagen fija, hasta 4K. El estándar **Seedance 2.5** es el que más se ciñe a un guion largo (explícito 8/9) y cuesta menos.
- **MiniMax H3 LoRA / Singularity LoRA**: Freedom 98.3 / 100 con tus propios LoRAs; Singularity para acción rápida y caras lejanas.
- **Seedance 2.0 / 2.0 Fast / 2.0 Mini estándar** suavizan los prompts explícitos en las pruebas (explícito 0–2 de 9); usa sus ediciones 🌶️ Spicy para clips para adultos.
- **Seedance 2.5 / Seedance 2.0 / Wan 3.0 (estándar, unrestricted)**: úsalos cuando quieras texto a video o referencia a video (poner a tu personaje de `@Image1` en una escena nueva). Aceptan prompts para adultos, pero no están ajustados para contenido explícito como las ediciones Spicy.
- **Wan 2.2 Spicy** (desde $0.019/s): el Wan Spicy más barato; el nivel más alto a veces sale suavizado. La duración es exactamente de 5 u 8 segundos. Admite `last_image_url` para fijar el final, y `enable_prompt_expansion`. Borrador a 480p, versión final a 720p.
- **Wan 2.2 Spicy LoRA** (desde $0.024/s): hasta tres LoRAs mediante `loras`, `high_noise_loras` (composición, movimiento) y `low_noise_loras` (textura, detalle). El endpoint `video-extend` continúa un clip con los mismos LoRAs.
- **LTX 2.3 Spicy** (desde $0.019/s): 3–20 segundos por llamada, prompt opcional. Bueno para tomas largas y tranquilas; el nivel más alto se suaviza con más frecuencia que en Wan Spicy.
- **Seedance 1.5 Pro Spicy** (desde $0.012/s): `camera_fixed` bloquea la cámara. El motor más barato para cinemagraphs.
- **Seedance 2.0 Spicy / Mini Spicy / Fast Spicy**: primer + último fotograma, audio generado opcional. 2.0 Spicy llega hasta 4K (Freedom 93.3); Mini Spicy y Fast Spicy resolvieron el nivel explícito con menos fiabilidad en las pruebas (1/3 y 0/3), así que para planos explícitos es mejor 2.0 Spicy o Seedance 2.5 Spicy.
- **Detalles de Seedance 2.5 Spicy**: tomas de 4–30 segundos, hasta 1080p nativo con un nivel 4K. Úsalo para versiones finales y movimientos difíciles (levantar a alguien, contacto entre dos personas).
- **MiniMax H3 Spicy** (desde $0.038/s, Freedom 97.5): movimiento natural de cuerpo entero, 3–15 segundos, prompt opcional; bueno para grandes volúmenes. MiniMax H3 estándar es más barato y sus 14 clips de prueba salieron tal como se pidió (su puntuación está pendiente de una cobertura más completa).
- **Vidu Q3 Spicy** (desde $0.0665/s): anime y movimiento estilizado; `movement_amplitude` controla cuánto se mueven las cosas.
- **Wan 2.6 Spicy / Wan 2.7 Spicy**: aceptan `negative_prompt` y tu propio `audio_url`; Wan 2.6 tiene `shot_type` para varios planos y Wan 2.7 puede generar audio.

---

## El flujo de imagen a video

```
1. Primer fotograma → Qwen Image 2.1 (fotorrealista, desde $0.024) o Prefect Pony XL (anime)
2. Retocar detalles → Qwen Image Edit Spicy (cambia ropa, pose o iluminación con una instrucción)
3. Borrador         → Wan 2.6 Flash, Seedance 1.5 Pro Spicy o Wan 2.2 Spicy a 480p, 3–5 variaciones
4. Render final     → el prompt del mejor borrador en Wan 3.0, Seedance 2.5 Spicy o Wan 2.7 Spicy a 720p–1080p
5. Extender         → video-extend de Wan 2.2 Spicy LoRA, o encadenar con el último fotograma
6. Pulir            → Video Upscaler, Lip Sync o Video Sound Effects
```

Un clip típico de 5 segundos hecho así cuesta unos **$0.024 (primer fotograma) + $0.29 (tres borradores a 480p con Wan 2.2 Spicy) + $0.45 (una versión final a 720p con Wan 3.0) ≈ $0.76**.

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
En las pruebas de SpicyAPI: **Wan 3.0** para el mejor resultado general por dólar (Index 76.5, Freedom 96, generó todos los prompts de prueba explícitos, $0.45 por 5 s a 720p); **Seedance 2.5 Spicy**, **Wan 2.7 Spicy** y **Vidu Q3 Spicy** (Freedom 96.7–100) para la imagen a video más explícita; **MiniMax H3 LoRA** para tus propios estilos; **Wan 2.6 Flash** y **Seedance 1.5 Pro Spicy** si tienes poco presupuesto. Compáralos en las [clasificaciones de SpicyAPI](https://spicyapi.ai/es/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=faq-es).

### ¿Por qué mis videos NSFW con IA salen con la anatomía mal?
Normalmente, por demasiado movimiento para la duración del clip. Acórtalo a 5 segundos, limítalo a una sola acción, deja las manos fuera de plano o relajadas, usa ángulos laterales o de espaldas para los planos de cuerpo entero y elige un modelo más potente (Seedance 2.x) para escenas de dos personas.

### ¿Puedo usar estos prompts con Stable Diffusion o ComfyUI?
Sí. Los prompts de primer fotograma funcionan en cualquier flujo de SDXL, Pony o Z-Image, y los prompts de video funcionan con Wan 2.2 autoalojado en ComfyUI. Cuenta con tener que ajustar la intensidad y los pasos en local.

### ¿Cuánto cuesta generar un video NSFW con IA?
En SpicyAPI (catálogo del {{READ_ON}}), un clip de 5 segundos cuesta desde $0.06 (Seedance 1.5 Pro Spicy, 480p) o $0.095 (Wan 2.2 Spicy, 480p) hasta unos $5.40 (Seedance 2.5 Spicy a 1080p). Cada prompt de arriba indica su propio costo.

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
