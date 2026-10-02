<!--
  Этот файл генерирует scripts/build_readme.py из README.template.ru.md, data/*.json и data/i18n/ru.json.
  Редактируйте шаблон или данные, затем запустите: python3 scripts/build_readme.py
  Ключевые слова: NSFW промпты, NSFW промпты для видео, промпты для AI видео 18+, промпты для нейросети видео для взрослых,
  промпты image-to-video, промпты из фото в видео, Wan 2.2 промпты, примеры NSFW промптов Wan 2.2, Wan 2.2 Spicy,
  промпты Seedance Spicy, AI видео без цензуры, NSFW промпты для изображений, негативные промпты,
  nsfw ai video prompts, nsfw prompts, wan 2.2 nsfw prompt example, wan 2.2 image to video prompt guide, nsfw image to video prompts
-->

<p align="center"><a href="README.md">English</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fr.md">Français</a> · <a href="README.es.md">Español</a> · <b>Русский</b></p>

<h1 align="center">NSFW AI Video Prompts</h1>

<p align="center">
  <b>{{VIDEO_COUNT}} готовых NSFW-промптов для AI-видео, {{IMAGE_COUNT}} промптов для первого кадра и {{SHOWCASE_COUNT}} примеров с реальными результатами — для Wan 2.2 Spicy, Seedance Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy и других image-to-video моделей без цензуры.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/video%20prompts-{{VIDEO_COUNT}}-ff4d6d" alt="{{VIDEO_COUNT}} промптов для видео">
  <img src="https://img.shields.io/badge/first--frame%20prompts-{{IMAGE_COUNT}}-8b5cf6" alt="{{IMAGE_COUNT}} промптов для изображений">
  <img src="https://img.shields.io/badge/showcase-{{SHOWCASE_COUNT}}-10b981" alt="{{SHOWCASE_COUNT}} примеров">
  <img src="https://img.shields.io/badge/updated-{{READ_ON}}-blue" alt="Обновлено {{READ_ON}}">
  <img src="https://img.shields.io/badge/18%2B-adults%20only-red" alt="18+">
</p>

<p align="center">
  <a href="#примеры-реальные-результаты-и-их-промпты">Примеры</a> ·
  <a href="#промпты">Промпты</a> ·
  <a href="#промпты-для-первого-кадра">Первые кадры</a> ·
  <a href="#негативные-промпты">Негативные промпты</a> ·
  <a href="#шпаргалка-камера-свет-и-движение">Шпаргалка</a> ·
  <a href="#запустите-промпт-за-60-секунд">Запуск</a> ·
  <a href="#частые-вопросы-faq">FAQ</a>
</p>

> **Только 18+. Все персонажи в этом репозитории — взрослые.** В промптах намеренно указан взрослый возраст и нет описаний, намекающих на юность. Никогда не используйте эти промпты с изображениями реальных людей, которые не дали задокументированного согласия, и никогда не «раздевайте» фото реального человека. См. [Правила](#правила).

> Репозиторий ведёт команда [SpicyAPI](https://spicyapi.ai/ru?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=disclosure-ru), где можно запустить любой промпт отсюда. Промпты — это обычный текст, и они работают с любой image-to-video моделью, которая их принимает.

---

## Зачем этот репозиторий

Большинство списков «NSFW-промптов» — это свалка ключевых слов для статичных картинок Stable Diffusion. Видеомоделям нужно другое: **одно понятное движение, названное движение камеры и первый кадр, который уже задаёт внешний вид**. Каждый промпт здесь написан именно так, и к каждому прилагаются:

- **модель**, для которой он написан, с прямой ссылкой на страницу модели;
- **разрешение, длительность и соотношение сторон**;
- **цена одного запуска** по текущим ценам каталога;
- **описание первого кадра**, чтобы было понятно, с какого изображения начинать;
- **совет**, объясняющий, почему промпт работает или что может сломаться.

Советы — это практический опыт продакшна, а не результаты бенчмарков. Реальные результаты собраны в разделе [примеров](#примеры-реальные-результаты-и-их-промпты).

Характеристики моделей и цены взяты из публичного каталога SpicyAPI по состоянию на {{READ_ON}}.

## Содержание

- [Модели в подборке](#модели-в-подборке)
- [Примеры: реальные результаты и их промпты](#примеры-реальные-результаты-и-их-промпты)
- [Как написать работающий NSFW-промпт для видео](#как-написать-работающий-nsfw-промпт-для-видео)
- [Промпты](#промпты)
{{PROMPTS_TOC}}
- [Промпты для первого кадра](#промпты-для-первого-кадра)
- [Негативные промпты](#негативные-промпты)
- [Шпаргалка: камера, свет и движение](#шпаргалка-камера-свет-и-движение)
- [Советы по моделям](#советы-по-моделям)
- [Пайплайн image-to-video](#пайплайн-image-to-video)
- [Запустите промпт за 60 секунд](#запустите-промпт-за-60-секунд)
- [Пусть промпты пишет LLM](#пусть-промпты-пишет-llm)
- [Частые вопросы (FAQ)](#частые-вопросы-faq)
- [Правила](#правила)

---

## Модели в подборке

{{MODEL_TABLE}}

Порядок соответствует каталогу SpicyAPI: сначала самые популярные, внутри семейства — сначала новые версии. 🌶️ Spicy-версии настроены на контент для взрослых; стандартные модели в этом списке имеют в каталоге уровень `unrestricted` (провайдер их не фильтрует), поэтому тоже подходят для промптов 18+ и добавляют text-to-video и reference-to-video. Цены указаны для самого дешёвого уровня; точные данные всегда на странице модели. **Spicy Index** (предварительная оценка возможностей) и **Freedom** (насколько надёжно пять уровней откровенности рендерятся так, как запрошено) взяты из публичных [рейтингов SpicyAPI](https://spicyapi.ai/ru/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=models-ru): ✅ 90+ · ◐ 70–89 · ⚠️ ниже 70 · 🧪 меньше 15 тестовых запусков. Неудачные запуски возвращаются автоматически.

---

## Примеры: реальные результаты и их промпты

{{SHOWCASE_COUNT}} реальных примеров со страниц моделей и из [библиотеки промптов](https://spicyapi.ai/ru/prompts?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru) SpicyAPI. В каждом примере результат стоит рядом с точным промптом, который его создал. Модели идут от самых популярных, внутри семейства — от новых версий: Spicy-версии и стандартные модели с уровнем `unrestricted` в каталоге. Нажмите на превью, чтобы открыть видео в полном качестве.

{{SHOWCASE}}

Некоторые результаты содержат наготу; для них здесь показаны только промпт и запрос, а сам результат доступен по ссылке на spicyapi.ai.

Чему учат эти примеры:

1. **Описывайте то, что меняется, а не то, что уже есть.** «She turns slowly from the window toward camera» (она медленно поворачивается от окна к камере) предполагает, что в первом кадре она уже у окна.
2. **Укажите, кто в кадре.** Строка вроде `Cast: two women.` не даёт модели придумывать лишних людей.
3. **Зафиксируйте камеру.** «Locked-off camera, no move» или «the camera stays on her back» убирают целый класс ошибок.
4. **Дайте движению физическую причину.** Сквозняк тянет шёлк, пар затуманивает стекло, порыв ветра поднимает халат.
5. **Зафиксируйте концовку, если она важна.** С `last_image_url` можно утвердить финальный вид как статичный кадр, прежде чем платить за движение.

---

## Как написать работающий NSFW-промпт для видео

```
[Who: adult, age range, look] + [One main action] + [Secondary motion: hair, fabric, light]
+ [Setting] + [Lighting] + [Camera move] + [Style / film look]
```

(Кто: взрослый, возраст, внешность + одно главное действие + второстепенное движение: волосы, ткань, свет + место + освещение + движение камеры + стиль / киношный вид)

| Делайте | Не делайте |
|---|---|
| «She slowly slides one strap off her shoulder and looks up at the camera.» (медленно спускает бретельку с плеча и поднимает взгляд в камеру) | «Sexy woman being hot.» |
| Одно главное действие на 5-секундный ролик | Целую программу в одном ролике |
| Называйте камеру: *slow push-in*, *static*, *orbit left* | «Cinematic camera» |
| Описывайте источники света: *candlelight*, *window light*, *neon rim* | «Good lighting» |
| Указывайте взрослый возраст: *in her 30s*, *adult man in his 40s* | Описания, намекающие на юность |
| Пусть одежду и место задаёт первый кадр | Заново описывать всё, что уже есть на изображении |

**Надёжность движений, от самых надёжных к наименее надёжным:** дыхание и моргание → волосы и ткань на ветру → вода, пар, дым, мерцание свечи → медленный поворот головы, взгляд через плечо → шаг к камере или от неё → потягивание, перекат → танец → контакт двух людей → быстрые или акробатические движения.

---

## Промпты

Для каждого промпта указана модель, под которую он написан. Большинство работают на любой Spicy image-to-video модели: черновики делайте на модели подешевле, финал — на более сильной.

{{PROMPTS}}

---

## Промпты для первого кадра

{{IMAGE_INTRO}}

{{IMAGE_PROMPTS}}

**Чек-лист первого кадра:** персонаж крупно в кадре · руки расслаблены или вне кадра · простой, не загромождённый фон · свет, соответствующий настроению будущего видео · у пары — чётко разделённые тела и одежда разных цветов · разрешение не ниже, чем у видео, которое вы будете рендерить.

---

## Негативные промпты

Используйте их на моделях с полем `negative_prompt` (на SpicyAPI это Wan 2.6 Spicy и Wan 2.7 Spicy). Для других моделей перенесите самые важные пункты в основной промпт в позитивной форме («natural skin texture», «consistent anatomy»).

**Универсальный**
```
blurry, low quality, jpeg artifacts, watermark, text, logo, deformed, distorted, disfigured,
bad anatomy, extra limbs, extra fingers, fused fingers, mutated hands, long neck, cross-eyed
```

**Реализм**
```
plastic skin, airbrushed, mannequin, doll-like, uncanny valley, waxy face, overexposed,
oversaturated, cartoon, 3d render
```

**Движение и непрерывность**
```
flickering, morphing, warping background, sudden cuts, identity change, clothing change,
extra person, duplicate body, jittery motion, frozen frames
```

**Аниме**
```
worst quality, low quality, bad hands, messy lines, off-model, inconsistent eyes, extra digits,
childlike proportions
```

---

## Шпаргалка: камера, свет и движение

**Движения камеры**

| Термин | Эффект | Надёжность |
|---|---|---|
| `static camera` / `locked-off` | Камера не двигается | Максимальная |
| `slow push-in` | Наезд на персонажа | Высокая |
| `pull back` / `dolly out` | Отъезд, открывает комнату | Высокая |
| `tilt up` / `tilt down` | Вертикальный наклон камеры вдоль тела | Высокая |
| `tracking shot` | Камера следует за персонажем сбоку | Средняя |
| `orbit left / right` | Облёт вокруг персонажа | Средняя (лучше всего на Seedance) |
| `handheld` | Лёгкая естественная тряска, как в съёмках авторов | Средняя |
| `rack focus` | Фокус переходит с переднего плана → на персонажа | Средняя |
| `drone descent` / `drone pull-back` | Высокий размашистый пролёт | Средняя |
| `POV` | Вид от первого лица | Ниже |

**Свет под настроение**

| Настроение | Пишите |
|---|---|
| Романтика | warm candlelight, golden tones, soft diffused light |
| Драма | single hard key light, deep shadows, chiaroscuro |
| Воздушность | backlit, glowing highlights, haze, bloom |
| Нуар | slatted blinds light, black and white, cigarette smoke |
| Роскошь | soft beauty lighting, no harsh shadows, glossy highlights |
| Загадочность | rim light only, face in shadow, silhouette |
| Естественность | window light, golden hour, soft ambient |
| Неон | magenta and cyan neon, wet reflections, rain |

**Длительность**

| Содержание | Длина | Почему |
|---|---|---|
| Дыхание, синемаграф | 4–5 s | Минимум движения сохраняет качество |
| Один жест или поворот головы | 5 s | Одно понятное действие |
| Ходьба, раскрытие кадра, пролёт камеры | 5–8 s | Непрерывное, но простое движение |
| Танец, сцены с двумя людьми | 5 s | В длинных роликах накапливаются артефакты |
| Более длинные сцены | Продлевайте поэтапно | `video-extend` или цепочка по последнему кадру |

---

## Советы по моделям

По тестам SpicyAPI (рейтинг v2.1 и обзоры моделей, 2026-09-27):

- **Wan 3.0** (от $0.045/s): лучшая универсальная NSFW-видеомодель в тестах: Index 76.5, Freedom 96, все откровенные тестовые промпты отрендерены. Текст, статичный кадр или референсы, 2–30 s со звуком. Может зайти дальше вашего промпта, поэтому проверяйте последние секунды; reference-to-video отклоняет фото реальных лиц.
- **Seedance 2.5 Spicy** (от $0.216/s): из статичного кадра заходит дальше всех на самых жёстких уровнях, до 4K. Стандартная **Seedance 2.5** точнее всех следует длинному сценарию (откровенные 8/9) и стоит дешевле.
- **MiniMax H3 LoRA / Singularity LoRA**: Freedom 98.3 / 100 с вашими собственными LoRA; Singularity — для быстрых действий и дальних лиц.
- **Стандартные Seedance 2.0 / 2.0 Fast / 2.0 Mini** в тестах смягчают откровенные промпты (откровенные 0–2 из 9); для роликов 18+ берите их 🌶️ Spicy-версии.
- **Seedance 2.5 / Seedance 2.0 / Wan 3.0 (стандартные, unrestricted)**: берите их, когда нужен text-to-video или reference-to-video (перенести персонажа из `@Image1` в новую сцену). Они принимают промпты 18+, но не настроены на откровенный результат, как Spicy-версии.
- **Wan 2.2 Spicy** (от $0.019/s): самая дешёвая Wan Spicy; на самом жёстком уровне иногда смягчает результат. Длительность ровно 5 или 8 секунд. Поддерживает `last_image_url` для фиксации концовки и `enable_prompt_expansion`. Черновик в 480p, финал в 720p.
- **Wan 2.2 Spicy LoRA** (от $0.024/s): до трёх LoRA через `loras`, `high_noise_loras` (композиция, движение) и `low_noise_loras` (текстура, детали). Эндпоинт `video-extend` продолжает ролик с теми же LoRA.
- **LTX 2.3 Spicy** (от $0.019/s): 3–20 секунд за вызов, промпт необязателен. Хороша для длинных спокойных дублей; на верхнем уровне смягчает чаще, чем Wan Spicy.
- **Seedance 1.5 Pro Spicy** (от $0.012/s): `camera_fixed` фиксирует камеру. Самый дешёвый движок для синемаграфов.
- **Seedance 2.0 Spicy / Mini Spicy / Fast Spicy**: первый + последний кадр, опционально сгенерированный звук. 2.0 Spicy — до 4K (Freedom 93.3); Mini Spicy и Fast Spicy в тестах хуже справлялись с откровенным уровнем (1/3 и 0/3), поэтому для кадров без цензуры выбирайте 2.0 Spicy или Seedance 2.5 Spicy.
- **Seedance 2.5 Spicy**, подробнее: дубли 4–30 секунд, нативно до 1080p плюс уровень 4K. Используйте для финала и сложных движений (подъём на руки, контакт двух людей).
- **MiniMax H3 Spicy** (от $0.038/s, Freedom 97.5): естественное движение всего тела, 3–15 секунд, промпт необязателен; подходит для больших объёмов. Стандартная MiniMax H3 дешевле, и все 14 её тестовых роликов вышли так, как запрошено (её оценка ждёт более полного покрытия).
- **Vidu Q3 Spicy** (от $0.0665/s): аниме и стилизованное движение; `movement_amplitude` управляет амплитудой движения.
- **Wan 2.6 Spicy / Wan 2.7 Spicy**: принимают `negative_prompt` и ваш собственный `audio_url`; у Wan 2.6 есть `shot_type` для многокадровых роликов, Wan 2.7 умеет генерировать звук.

---

## Пайплайн image-to-video

```
1. Первый кадр      → Qwen Image 2.1 (фотореализм, от $0.024) или Qwen Image 2.1 LoRA + аниме-LoRA (аниме)
2. Правка деталей   → Qwen Image Edit Spicy (одежда, поза, свет — одной инструкцией)
3. Черновики        → Wan 2.6 Flash, Seedance 1.5 Pro Spicy или Wan 2.2 Spicy в 480p, 3–5 вариантов
4. Финальный рендер → промпт лучшего черновика на Wan 3.0, Seedance 2.5 Spicy или Wan 2.7 Spicy в 720p–1080p
5. Продление        → video-extend в Wan 2.2 Spicy LoRA или цепочка по последнему кадру
6. Доводка          → Video Upscaler, Lip Sync или Video Sound Effects
```

Типичный 5-секундный ролик, сделанный так, стоит примерно **$0.024 (первый кадр) + $0.29 (три черновика Wan 2.2 Spicy в 480p) + $0.45 (один финал Wan 3.0 в 720p) ≈ $0.76**.

---

## Запустите промпт за 60 секунд

**Без кода:** вставьте любой промпт в [SpicyAPI Studio › image-to-video](https://spicyapi.ai/ru/create/image-to-video?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=run-ru) или в [генератор AI-видео без цензуры](https://spicyapi.ai/ru/create/uncensored-ai-video-generator?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=run-ru), загрузите первый кадр и проверьте цену перед генерацией.

**cURL:**

```bash
export SPICY_API_KEY="sk-spicy-..."   # https://spicyapi.ai/ru/console

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

# Опрашивайте, пока data.state не станет "succeeded", затем скачайте data.output.assets[0].url
curl -s "https://api.spicyapi.ai/api/v1/jobs/recordInfo?taskId=TASK_ID" \
  -H "Authorization: Bearer $SPICY_API_KEY"
```

**Python (только стандартная библиотека):**

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

Хотите делать это прямо в Claude Code, Cursor или Codex? Установите **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.ru.md)** и просто попросите: *«анимируй это изображение промптом B02 из nsfw-ai-video-prompts»*.

---

## Пусть промпты пишет LLM

Вставьте этот системный промпт в любую чат-модель (на SpicyAPI через OpenAI-совместимый эндпоинт хорошо подходят [Grok 4.7](https://spicyapi.ai/ru/models/grok-4-7?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=llm-ru) и [DeepSeek V4.1 Flash](https://spicyapi.ai/ru/models/deepseek-v4-1-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=llm-ru)):

```text
You write prompts for adult image-to-video models. Every character is an adult; always state an age of 21 or older
and never use descriptors that suggest youth. Never depict real, identifiable people.
Given a short idea and a description of the first frame, return ONE prompt of 40–80 words that:
1) describes only what changes from the first frame, 2) has exactly one main action,
3) adds one secondary motion (hair, fabric, light, water, steam), 4) names one camera move,
5) names the light sources, 6) ends with a short style phrase. Also return a 1-line negative prompt.
```

---

## Частые вопросы (FAQ)

### Какие NSFW-промпты для AI-видео лучше всего подходят для Wan 2.2?
Короткие промпты с одним действием и названным движением камеры: см. [Будуар и бельё](#будуар-и-бельё) и [Готовые шаблоны движения и камеры](#готовые-шаблоны-движения-и-камеры). Wan 2.2 Spicy рендерит ровно 5 или 8 секунд, поэтому пишите одно действие на ролик и используйте `last_image_url`, когда нужна конкретная концовка.

### Как написать NSFW-промпт для image-to-video?
Начните с сильного первого кадра, затем описывайте только движение: одно главное действие, одно второстепенное движение, камеру и свет. Уложитесь в 40–80 слов. См. [Как написать работающий NSFW-промпт для видео](#как-написать-работающий-nsfw-промпт-для-видео).

### Какая модель лучше всего подходит для NSFW image-to-video?
По тестам SpicyAPI: **Wan 3.0** — лучший универсальный результат за свои деньги (Index 76.5, Freedom 96, все откровенные тестовые промпты отрендерены, $0.45 за 5 s в 720p); **Seedance 2.5 Spicy**, **Wan 2.7 Spicy** и **Vidu Q3 Spicy** (Freedom 96.7–100) — наименее фильтруемый image-to-video; **MiniMax H3 LoRA** — для собственных стилей; **Wan 2.6 Flash** и **Seedance 1.5 Pro Spicy** — при ограниченном бюджете. Сравните их в [рейтингах SpicyAPI](https://spicyapi.ai/ru/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=faq-ru).

### Почему в моих NSFW AI-видео ломается анатомия?
Обычно слишком много движения для длины ролика. Сократите до 5 секунд, оставьте одно действие, уберите руки из кадра или держите их расслабленными, для кадров в полный рост берите ракурс сбоку или со спины, а для сцен с двумя людьми выбирайте более сильную модель (Seedance 2.x).

### Можно ли использовать эти промпты в Stable Diffusion или ComfyUI?
Да. Промпты для первого кадра работают в любом воркфлоу SDXL, Pony или Z-Image, а промпты для видео — с локально развёрнутой Wan 2.2 в ComfyUI. Скорее всего, придётся подстроить strength и steps.

### Сколько стоит сгенерировать NSFW AI-видео?
На SpicyAPI (каталог от {{READ_ON}}) 5-секундный ролик стоит от $0.06 (Seedance 1.5 Pro Spicy, 480p) или $0.095 (Wan 2.2 Spicy, 480p) и до примерно $5.40 (Seedance 2.5 Spicy в 1080p). У каждого промпта выше указана своя цена.

### Есть ли бесплатный генератор NSFW-промптов для видео?
Используйте [системный промпт для LLM](#пусть-промпты-пишет-llm) выше с любой чат-моделью, включая локальные в Ollama или LM Studio.

---

## Правила

- **Только взрослые.** Никакого сексуального контента с участием лиц младше 18 лет или выглядящих младше 18, в любом стиле, включая аниме. «На самом деле ей 500 лет» — не исключение.
- **Никаких реальных людей без задокументированного согласия.** Никаких сексуальных дипфейков, замены лиц реальных людей в сексуальном контенте и «раздевания» реальных фото. Публичные личности — не исключение.
- **Соблюдайте закон** там, где живёте вы и ваша аудитория, а также правила платформ, на которых публикуете.
- Полные правила SpicyAPI: [Политика в отношении контента](https://spicyapi.ai/ru/legal/content-policy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=rules-ru) · [Правила допустимого использования](https://spicyapi.ai/ru/legal/acceptable-use?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=rules-ru).

## Связанные репозитории

- **[awesome-nsfw-ai](https://github.com/Spicy-API/awesome-nsfw-ai/blob/main/README.ru.md)**: подборка AI-инструментов, API и моделей без цензуры для изображений, видео и текста.
- **[nsfw-ai-image-prompts](https://github.com/Spicy-API/nsfw-ai-image-prompts/blob/main/README.ru.md)**: 104 NSFW-промпта для изображений и редактирования; для более качественных первых кадров.
- **[nsfw-ai-skill](https://github.com/Spicy-API/nsfw-ai-skill/blob/main/README.ru.md)**: генерация NSFW-изображений и видео из Claude Code, Cursor, Codex и других агентов.
- Машиночитаемые данные: [`data/video-prompts.json`](data/video-prompts.json), [`data/image-prompts.json`](data/image-prompts.json), [`data/showcase.json`](data/showcase.json).

## Участие в проекте

Пул-реквесты с промптами приветствуются. Добавляйте их в `data/video-prompts.json` (только взрослые персонажи, одно главное действие, модель + настройки + совет), затем запустите `python3 scripts/build_readme.py`. Проверки в стиле CI находятся в `scripts/check_prompts.py`.

## Лицензия

Промпты и документация: [CC0 1.0](LICENSE). Превью примеров в `assets/showcase/` — короткие GIF-фрагменты примеров результатов SpicyAPI; полные видео хранятся на CDN SpicyAPI.

<p align="center"><sub>⭐ Поставьте звезду репозиторию, если промпт сэкономил вам несколько перегенераций.</sub></p>
