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
  <b>116 готовых NSFW-промптов для AI-видео, 24 промптов для первого кадра и 128 примеров с реальными результатами — для Wan 2.2 Spicy, Seedance Spicy, MiniMax H3 Spicy, LTX 2.3 Spicy, Vidu Q3 Spicy и других image-to-video моделей без цензуры.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/video%20prompts-116-ff4d6d" alt="116 промптов для видео">
  <img src="https://img.shields.io/badge/first--frame%20prompts-24-8b5cf6" alt="24 промптов для изображений">
  <img src="https://img.shields.io/badge/showcase-128-10b981" alt="128 примеров">
  <img src="https://img.shields.io/badge/updated-2026-09-27-blue" alt="Обновлено 2026-09-27">
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

Характеристики моделей и цены взяты из публичного каталога SpicyAPI по состоянию на 2026-09-27.

## Содержание

- [Модели в подборке](#модели-в-подборке)
- [Примеры: реальные результаты и их промпты](#примеры-реальные-результаты-и-их-промпты)
- [Как написать работающий NSFW-промпт для видео](#как-написать-работающий-nsfw-промпт-для-видео)
- [Промпты](#промпты)
  - [Будуар и бельё](#будуар-и-бельё) (16)
  - [Художественное ню и файн-арт](#художественное-ню-и-файн-арт) (14)
  - [Пары и романтика](#пары-и-романтика) (14)
  - [Сольные выступления и танец](#сольные-выступления-и-танец) (14)
  - [Ванна, душ и вода](#ванна-душ-и-вода) (10)
  - [Фэнтези, научная фантастика и косплей](#фэнтези-научная-фантастика-и-косплей) (12)
  - [Аниме и хентай-стиль](#аниме-и-хентай-стиль) (10)
  - [Реклама и чувственность без риска для бренда](#реклама-и-чувственность-без-риска-для-бренда) (10)
  - [Готовые шаблоны движения и камеры](#готовые-шаблоны-движения-и-камеры) (10)
  - [Промпты под стилевые LoRA (Wan 2.2 Spicy LoRA)](#промпты-под-стилевые-lora-wan-22-spicy-lora) (6)
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

**Видеомодели**

| Модель | Тип | Задачи | Длительность | От | Spicy Index | Freedom |
|---|---|---|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/ru/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–30 s | $0.216/s | 56.5 | ✅ 96.7 |
| [Seedance 2.5](https://spicyapi.ai/ru/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 4–30 s | $0.1234/s | 69.5 | ◐ 80.9 |
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–15 s | $0.114/s | 61.5 | ✅ 93.3 |
| [Seedance 2.0](https://spicyapi.ai/ru/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 4–15 s | $0.07/s | 81.5 | ◐ 70.4 |
| [Wan 3.0 Prime](https://spicyapi.ai/ru/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 2–30 s | $0.0612/s | 76.5 | ◐ 78 |
| [Wan 3.0](https://spicyapi.ai/ru/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 2–30 s | $0.045/s | 76.5 | ✅ 96 |
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 3–15 s | $0.038/s | 29.5 | ✅ 97.5 |
| [MiniMax H3](https://spicyapi.ai/ru/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 4–15 s | $0.025/s | 72.5 | 🧪 33.3 |
| [MiniMax H3 Singularity LoRA](https://spicyapi.ai/ru/models/minimax-h3-singularity-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V | 3–15 s | $0.06/s | 72.8 | ✅ 100 |
| [LTX 2.5](https://spicyapi.ai/ru/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, T2V | 5–20 s | $0.09/s | 66 | ◐ 80.3 |
| [Wan 3.0 Pro Prime](https://spicyapi.ai/ru/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 2–30 s | $0.234/s | 76.5 | ◐ 82 |
| [Wan 3.0 Pro](https://spicyapi.ai/ru/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 2–30 s | $0.144/s | 76.5 | ◐ 82 |
| [MiniMax H3 LoRA](https://spicyapi.ai/ru/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 3–15 s | $0.05/s | 75.2 | ✅ 98.3 |
| [HappyHorse 1.1](https://spicyapi.ai/ru/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 3–15 s | $0.14/s | 62.5 | ⚠️ 65.1 |
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–15 s | $0.0387/s | 44.5 | ✅ 93.3 |
| [Seedance 2.0 Mini](https://spicyapi.ai/ru/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 4–15 s | $0.01097/s | 64.5 | ⚠️ 64.9 |
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 2–15 s | $0.1235/s | 46.5 | ✅ 100 |
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 3–20 s | $0.019/s | 33.5 | ◐ 89.2 |
| [LTX 2.3 Spicy LoRA](https://spicyapi.ai/ru/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 3–20 s | $0.0285/s | 34.8 | ◐ 83.8 |
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–15 s | $0.081/s | 44.5 | ✅ 90 |
| [Seedance 2.0 Fast](https://spicyapi.ai/ru/models/seedance-2-0-fast?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 4–15 s | $0.02254/s | 64.5 | ⚠️ 68.2 |
| [Vidu Q3 Turbo](https://spicyapi.ai/ru/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V | 1–16 s | $0.042/s | 39.5 | ✅ 93.3 |
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 1–16 s | $0.0665/s | 46.5 | ✅ 96.7 |
| [Vidu Q3](https://spicyapi.ai/ru/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V | 1–16 s | $0.07/s | 46.5 | ✅ 93.3 |
| [Vidu Q3 Pro](https://spicyapi.ai/ru/models/vidu-q3-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V | 1–16 s | $0.054/s | 36.5 | ✅ 93.3 |
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ru/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 4–12 s | $0.012/s | 48.5 | ✅ 96.7 |
| [Seedance 1.5 Pro](https://spicyapi.ai/ru/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, T2V | 4–12 s | $0.0112/s | 46 | ✅ 90 |
| [Wan 2.6 Flash](https://spicyapi.ai/ru/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V | 5, 10, 15 s | $0.0225/s | 31.5 | ✅ 100 |
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 5, 10, 15 s | $0.095/s | 46.5 | ✅ 96.7 |
| [Wan 2.6](https://spicyapi.ai/ru/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, Ref2V, T2V | 5, 10, 15 s | $0.065/s | 58.5 | 🧪 8.7 |
| [Wan 2.5](https://spicyapi.ai/ru/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V, T2V | 5, 10 s | $0.045/s | 46 | ✅ 99 |
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V | 5, 8 s | $0.019/s | 23.5 | ✅ 91.2 |
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | I2V, Extend | 5, 8 s | $0.024/s | 25 | ◐ 74.8 |
| [Wan 2.2 LoRA](https://spicyapi.ai/ru/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | I2V | 5, 8 s | $0.024/s | 22.5 | ◐ 88.8 |

**Модели изображений** (первые кадры и стоп-кадры)

| Модель | Тип | Задачи | От | Spicy Index | Freedom |
|---|---|---|---|---|---|
| [Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.024/image | 73 | ✅ 96.3 |
| [Qwen Image 2.1 LoRA](https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.03/image | 80.5 | ✅ 92 |
| [MiniMax H3 Image LoRA](https://spicyapi.ai/ru/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.042/image | 74.5 | ✅ 100 |
| [Qwen Image 3.0 Pro](https://spicyapi.ai/ru/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.04/image | 56 | ✅ 98 |
| [Qwen Image 3.0](https://spicyapi.ai/ru/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.03/image | 56 | ✅ 96 |
| [Seedream 5.0 Pro](https://spicyapi.ai/ru/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.036/image | 73 | ✅ 94.3 |
| [Qwen Image Edit Spicy](https://spicyapi.ai/ru/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | Edit | $0.038/image | 14 | ✅ 96 |
| [Seedream 5.0 Lite](https://spicyapi.ai/ru/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.0345/image | 73 | ✅ 96 |
| [Qwen Image 2](https://spicyapi.ai/ru/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.035/image | 34 | ✅ 96.7 |
| [Qwen Image 2512 LoRA](https://spicyapi.ai/ru/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.03/image | 50.5 | ✅ 92.5 |
| [Z-Image Spicy Pro](https://spicyapi.ai/ru/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | T2I | $0.019/image | 38 | ✅ 100 |
| [Z-Image Spicy](https://spicyapi.ai/ru/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | 🌶️ Spicy | T2I | $0.01235/image | 32 | ✅ 98.8 |
| [Z-Image](https://spicyapi.ai/ru/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | T2I | $0.01/image | 17 | ✅ 100 |
| [Z-Image Turbo LoRA](https://spicyapi.ai/ru/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.012/image | 46.5 | ✅ 95 |
| [Seedream 4.0](https://spicyapi.ai/ru/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | Edit, T2I | $0.03/image | 74 | ◐ 74.7 |
| [Prefect Pony XL](https://spicyapi.ai/ru/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | T2I | $0.015/image | 30 | 🧪 36 |
| [FLUX.1 Dev LoRA](https://spicyapi.ai/ru/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=model-table-ru) | Стандартная | T2I | $0.018/image | 32.5 | ◐ 75 |


Порядок соответствует каталогу SpicyAPI: сначала самые популярные, внутри семейства — сначала новые версии. 🌶️ Spicy-версии настроены на контент для взрослых; стандартные модели в этом списке имеют в каталоге уровень `unrestricted` (провайдер их не фильтрует), поэтому тоже подходят для промптов 18+ и добавляют text-to-video и reference-to-video. Цены указаны для самого дешёвого уровня; точные данные всегда на странице модели. **Spicy Index** (предварительная оценка возможностей) и **Freedom** (насколько надёжно пять уровней откровенности рендерятся так, как запрошено) взяты из публичных [рейтингов SpicyAPI](https://spicyapi.ai/ru/leaderboards?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=models-ru): ✅ 90+ · ◐ 70–89 · ⚠️ ниже 70 · 🧪 меньше 15 тестовых запусков. Неудачные запуски возвращаются автоматически.

---

## Примеры: реальные результаты и их промпты

128 реальных примеров со страниц моделей и из [библиотеки промптов](https://spicyapi.ai/ru/prompts?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru) SpicyAPI. В каждом примере результат стоит рядом с точным промптом, который его создал. Модели идут от самых популярных, внутри семейства — от новых версий: Spicy-версии и стандартные модели с уровнем `unrestricted` в каталоге. Нажмите на превью, чтобы открыть видео в полном качестве.

### Seedance 2.5 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/561b3b36ee1cdc88.mp4"><img src="assets/showcase/seedance-2-5-spicy--onsen-rise-embrace.gif" alt="Onsen rise embrace" width="230"></a></td><td valign="top"><b>Onsen rise embrace</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/561b3b36ee1cdc88.mp4">▶ полное видео</a></sub><br><br>The two women rise toward camera only as far as the collarbone, water sheeting off their shoulders, and the steam banks thick across the surface in front of them. One slides behind the other and wraps both arms around her from behind, her forearm crossing high over the chest; they settle cheek to cheek and hold the look into the lens while the water swells and slaps the rocks. Slow push in on their faces and shoulders, framed from the collarbone up the whole time. Dusk light on wet skin, drifting snow beyond. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.5-spicy/0510366bd110c007.mp4"><img src="assets/showcase/seedance-2-5-spicy--onsen-two-rise.gif" alt="Two women in a steaming outdoor hot spring at dusk, first facing the camera with the water at their shoulders, then seen from behind with bare backs above the waterline" width="230"></a></td><td valign="top"><b>Two women rising from a misty outdoor hot spring</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.5-spicy/0510366bd110c007.mp4">▶ полное видео</a></sub><br><br>Cast: two women. The camera stays on their backs as they rise, and stops there. In the mist of an outdoor hot spring at dusk, first one and then the other rises only until the waterline reaches the small of the back and no further; they hold there, steam closing over the surface behind them. Nothing below the waterline ever leaves the water. Locked framing. Cinematic, heavy film grain, steam white and rock grey, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/8ae0a0222aa9f90f.mp4"><img src="assets/showcase/seedance-2-5-spicy--steam-glass-handprint.gif" alt="Behind fogged shower glass in a dark bathroom, a woman drags her palm down the pane and leans in until her face comes into focus through the clear streak" width="230"></a></td><td valign="top"><b>Face pressed close behind steamed shower glass</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/8ae0a0222aa9f90f.mp4">▶ полное видео</a></sub><br><br>Her palm drags straight down the fogged glass, carving one long clear streak from the wiped patch to the bottom edge, and her fingertips lift away. She immediately steps forward and leans into that clear streak: her face arrives close to the glass and comes into sharp focus through it, wet skin and lashes clearly visible, water beading and running around her cheek. She holds there, eyes level with the lens, and breathes out against the glass so a small bloom of fog spreads and fades. The framing stays tight on the glass panel the entire time. Do not pull back, do not widen the shot, do not change the camera angle. Running water, muffled room tone, one slow breath.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/fec77dab61baeb3a.mp4"><img src="assets/showcase/seedance-2-5-spicy--hotel-window-turn.gif" alt="A woman in an ivory silk slip turning from a floor-to-ceiling hotel window at night, city lights behind her" width="230"></a></td><td valign="top"><b>Silk slip turn at a night hotel window</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/fec77dab61baeb3a.mp4">▶ полное видео</a></sub><br><br>She turns slowly from the window toward camera, the silk slip catching the city light as it moves, one hand trailing along the glass, then she tilts her head and holds the look. Subtle handheld drift, warm lamp against cool skyline, quiet room tone.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/c5f2690c42576a26.mp4"><img src="assets/showcase/seedance-2-5-spicy--pov-hand-pull.gif" alt="A first-person shot of a woman in black satin taking the viewer&#x27;s hand and running through a neon night market, laughing back over her shoulder" width="230"></a></td><td valign="top"><b>First-person: pulled by the hand through a night market</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/c5f2690c42576a26.mp4">▶ полное видео</a></sub><br><br>She closes her hand around the viewer&#x27;s and pulls, breaking into a run and towing the camera after her through the neon stalls, laughing back over her shoulder once. Handheld first-person motion, neon streaking past, crowd noise and sizzling griddles.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/b8be819fa36bd881.mp4"><img src="assets/showcase/seedance-2-5-spicy--opera-stair-train.gif" alt="A woman in a backless black velvet gown and long gloves climbs a marble opera house staircase, glancing back over her shoulder as the train drags behind her" width="230"></a></td><td valign="top"><b>Backless gown gliding up an opera house staircase</b><br><sub><code>bytedance/seedance-2.5-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5-spicy/b8be819fa36bd881.mp4">▶ полное видео</a></sub><br><br>She holds the look back over her bare shoulder, then turns and continues up two more steps, the velvet train dragging heavily behind her across the marble, her gloved hand sliding along the brass banister. The chandelier flares a little brighter and the gilt catches, deep shadows swinging across the wall. Slow dolly following her up the stairs, hushed hall reverb, no music.</td></tr>
</table>

### Seedance 2.5

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5/7ceb81a8701180d6.mp4"><img src="assets/showcase/seedance-2-5--night-train-press.gif" alt="In a dim night train carriage, a woman in a long dark coat with bare legs stands at the door; a man steps in behind her and they end up face to face as tunnel lights strobe" width="230"></a></td><td valign="top"><b>Night train crowd presses two strangers together</b><br><sub><code>bytedance/seedance-2.5/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-5/7ceb81a8701180d6.mp4">▶ полное видео</a></sub><br><br>A woman alone in a night train carriage, coat falling open over bare legs, stands as the train lurches and catches the overhead rail; a man steps in behind her at the stop and the crowd presses them chest to back against the door. Her head tips onto his shoulder, his hand finds her hip, neither looks at the other. Tunnel lights strobe across their faces. Slow push in through the carriage, warm light against black glass. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/seedance-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Fantasy trailer: two leads close the distance</b><br><sub><code>bytedance/seedance-2.5/reference-to-video</code></sub><br><br>Cast: a mixed crowd of men and women of different ages and skin tones. Cut a fantasy trailer from the thirty supplied boards: the distance between the two leads closes board by board until the last is face to face. Bodies come closer board by board until the last is skin to skin. Cinematic, heavy film grain.</td></tr>
</table>

### Seedance 2.0 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4"><img src="assets/showcase/seedance-2-0-spicy--velvet-spiral-turn.gif" alt="A backlit silhouette turns inside a red velvet stage curtain, the fabric wound across her front and her bare shoulders catching a rim of light" width="230"></a></td><td valign="top"><b>Velvet curtain spiral turn in red backlight</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/fd580ae58de668b5.mp4">▶ полное видео</a></sub><br><br>The velvet curtain sweeps across her as she turns inside it, wrapping her body in one continuous spiral of fabric, then billows out behind her as she steps toward the light. Her bare shoulders and the line of her back come into the glow; the curtain stays wound across her front as she moves. Backlight flares through the gap and dims. Slow push toward the silhouette, velvet rippling the whole time. Cinematic, heavy film grain, deep red and black, glowing rim light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-spicy/d65d988b0c120dd8.mp4"><img src="assets/showcase/seedance-2-0-spicy--velvet-curtain-turn-4k.gif" alt="Velvet curtain turn 4k" width="230"></a></td><td valign="top"><b>Velvet curtain turn 4k</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-spicy/d65d988b0c120dd8.mp4">▶ полное видео</a></sub><br><br>Cast: one woman. The camera stays on her silhouette as the curtain shifts around it. A silhouette turns behind a velvet curtain and the fabric sweeps across and catches there. Pure backlight, no detail beyond outline. Cinematic, heavy film grain, deep red-black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/00246b5b1923cf62.mp4"><img src="assets/showcase/seedance-2-0-spicy--fogged-mirror-lean.gif" alt="A woman in a loosely tied waffle robe wiping a streak through a fogged bathroom mirror and leaning toward her reflection" width="230"></a></td><td valign="top"><b>Wiping a fogged bathroom mirror in a waffle robe</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/00246b5b1923cf62.mp4">▶ полное видео</a></sub><br><br>She wipes a wider streak through the fogged mirror, steam curling back across the glass, then leans in closer to her reflection and exhales, the robe slipping a little further off her shoulder. Slow push toward the mirror, warm vanity bulbs, water dripping.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/31eeaff5e2446da8.mp4"><img src="assets/showcase/seedance-2-0-spicy--darkroom-safelight.gif" alt="Under a red darkroom safelight, a woman in an open shirt rocks a developer tray, then lifts a dripping print into the light and glances at the camera" width="230"></a></td><td valign="top"><b>Red-safelight darkroom with a dripping print</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/31eeaff5e2446da8.mp4">▶ полное видео</a></sub><br><br>She rocks the developer tray with the tongs, then lifts the dripping print up into the red safelight and turns it to look at it, glancing sideways at the camera. The open shirt slides further off one shoulder. Slow dolly in, safelight steady, chemical ripples reflecting on the ceiling.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/0842ecee1511d6d9.mp4"><img src="assets/showcase/seedance-2-0-spicy--library-ladder-dust.gif" alt="A woman in a cream blouse and dark skirt on a rolling library ladder pulls a heavy book from a high shelf, dust drifting through the window light as she turns and smiles" width="230"></a></td><td valign="top"><b>Library ladder, a pulled book and a plume of dust</b><br><sub><code>bytedance/seedance-2.0-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-spicy/0842ecee1511d6d9.mp4">▶ полное видео</a></sub><br><br>She pulls a heavy book from the top shelf, releasing a plume of dust that ignites in the window shaft, and looks down over her shoulder toward the lens as the ladder rolls a few inches along its rail. Camera cranes slowly up to meet her.</td></tr>
</table>

### Seedance 2.0

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/seedance-2-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0/2142f319602eb377.mp4"><img src="assets/showcase/seedance-2-0--same-suit-three-cities.gif" alt="A dark-haired male model in an unbuttoned charcoal suit with no shirt walks toward the camera on a night street as the wind blows the jacket open, traffic lights blurred behind him" width="230"></a></td><td valign="top"><b>Same model, same open suit, a third city at night</b><br><sub><code>bytedance/seedance-2.0/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0/2142f319602eb377.mp4">▶ полное видео</a></sub><br><br>The camera stays on him as the wind takes the jacket fully open. The same model, the same unbuttoned suit, a third city corner at night: the wind takes the jacket open as he walks toward camera, traffic streaking behind. The wind takes the jacket fully open over a bare chest as he walks in; medium close. Cinematic, shallow depth of field, heavy film grain, cold street blue.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0/b22ec0154e2e4b0d.mp4"><img src="assets/showcase/seedance-2-0--character-into-location.gif" alt="A woman in a sheer black robe over black lace walks between white sheets drying on a rooftop at sunset and glances back over her shoulder" width="230"></a></td><td valign="top"><b>Put your character on a new rooftop at sunset</b><br><sub><code>bytedance/seedance-2.0/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0/b22ec0154e2e4b0d.mp4">▶ полное видео</a></sub><br><br>The woman from @Image1, in the same sheer black robe, steps out onto the rooftop from @Image2 at sunset. She walks slowly between the drying white sheets; the wind lifts one sheet across her body and lets it fall away. She stops at the parapet, the robe sliding off one shoulder, and glances back over her shoulder into camera. Warm golden backlight, slow tracking shot, no cuts.</td></tr>
</table>

### Wan 3.0 Prime

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-3-0-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-prime/00cef285db666750.mp4"><img src="assets/showcase/wan-3-0-prime--balcony-robe-wind.gif" alt="At golden hour on a high hotel balcony, a man embraces a woman as the wind blows her champagne silk robe sideways over a city skyline" width="230"></a></td><td valign="top"><b>Hotel balcony embrace as the wind lifts a silk robe</b><br><sub><code>alibaba/wan-3.0-prime/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-prime/00cef285db666750.mp4">▶ полное видео</a></sub><br><br>Golden hour on a hotel balcony: she stands at the rail in a champagne silk robe that lifts and falls in the wind, and he comes up behind her and closes both arms around her waist. She leans back into him and turns her face up to his. The robe streams sideways, the city hazes gold below. Slow orbit around the pair at the rail. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-prime/e2f09083882d90e4.mp4"><img src="assets/showcase/wan-3-0-prime--lighthouse-one-night.gif" alt="A bearded keeper in a wool sweater and a woman in a rain-soaked white blouse stand at a lighthouse rail in a storm as the sweeping beam lights them and passes" width="230"></a></td><td valign="top"><b>Storm at a lighthouse, two strangers in the beam</b><br><sub><code>alibaba/wan-3.0-prime/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-prime/e2f09083882d90e4.mp4">▶ полное видео</a></sub><br><br>Cast: one man and one woman. Thirty seconds at a lighthouse through one night: the keeper and the visitor who came up out of the fog, the revolving beam sweeping across the two of them once every few seconds and leaving them in dark between passes. The visitor&#x27;s soaked shirt clings to the chest; the beam finds a bare throat, then leaves them dark; close two-shot. Foghorn and sea. Cinematic, heavy film grain, beam white in fog green.</td></tr>
</table>

### Wan 3.0

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0/067c4e121975b1cc.mp4"><img src="assets/showcase/wan-3-0--ten-boards-travel-cut.gif" alt="Two climbers in red and blue down jackets stand before a snowy peak, then a couple wrapped in one blanket outside a tent at dawn" width="230"></a></td><td valign="top"><b>Travel short cut from storyboards and an ambience track</b><br><sub><code>alibaba/wan-3.0/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0/067c4e121975b1cc.mp4">▶ полное видео</a></sub><br><br>Cast: a mixed crowd of men and women of different ages and skin tones. Cut a travel short from the ten supplied boards and the supplied ambience track: the distance between the two travellers is the thread that runs through every shot. The two travellers keep ending up shoulder to shoulder, sun-flushed skin and open collars. Cinematic, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3-0/5f28d071ae584a56.mp4"><img src="assets/showcase/wan-3-0--lingerie-window-turn.gif" alt="A woman in a short ivory silk chemise stands at a window with sheer curtains, turns slowly toward the lens and lifts her eyes to the camera" width="230"></a></td><td valign="top"><b>Dawn window turn in a silk chemise</b><br><sub><code>alibaba/wan-3.0/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3-0/5f28d071ae584a56.mp4">▶ полное видео</a></sub><br><br>She turns from the window toward the lens in one slow movement, the silk chemise settling against her as she comes round, and lifts her eyes to camera. The sheer curtain drifts across the light behind her. Slow push in, no cut, dawn light strengthening.</td></tr>
</table>

### MiniMax H3 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Steam room turn</b><br><sub><code>minimax/h3-spicy/image-to-video</code></sub><br><br>She turns in the steam room, water beading down the shoulder blades, the steam swirling where she moves and closing again behind her. Water beads and runs the length of her spine as she turns, the towel slipping at the hip; close. Slow, single turn. Cinematic, shallow depth of field, heavy film grain, warm cedar and white vapour.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/3ab0c4145b288d90.mp4"><img src="assets/showcase/minimax-h3-spicy--neon-window.gif" alt="Night interior: a woman on an apartment windowsill exhaling smoke against rain-streaked glass while a red neon sign pulses across her face" width="230"></a></td><td valign="top"><b>Red neon cigarette smoke by the window blinds</b><br><sub><code>minimax/h3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/3ab0c4145b288d90.mp4">▶ полное видео</a></sub><br><br>She exhales a slow plume of smoke against the rain-streaked glass, the neon sign outside pulses red across her face, and she turns her head toward camera without changing expression. Blind shadows creep, rain runs down the window, distant traffic.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/5b1f11a28c987479.mp4"><img src="assets/showcase/minimax-h3-spicy--pov-glove-tap.gif" alt="Pov glove tap" width="230"></a></td><td valign="top"><b>Pov glove tap</b><br><sub><code>minimax/h3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/5b1f11a28c987479.mp4">▶ полное видео</a></sub><br><br>First person point of view, the camera never moves. She leans in toward the lens until her face and shoulders fill the frame, reaches out and presses one gloved fingertip against the lens, holds eye contact, then tilts her head and smiles. She keeps the black leather harness, satin camisole, long opera gloves and choker on the whole time. The hard overhead light rakes her collarbone and the background stays pure black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/c581dd66c32e8f29.mp4"><img src="assets/showcase/minimax-h3-spicy--greenhouse-mist.gif" alt="In a humid glasshouse full of banana leaves and ferns, a woman in a white cotton sundress sprays a brass mister, then wipes her brow and turns her face up to the light" width="230"></a></td><td valign="top"><b>Misting plants in a sunlit greenhouse</b><br><sub><code>minimax/h3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-spicy/c581dd66c32e8f29.mp4">▶ полное видео</a></sub><br><br>She squeezes the brass mister twice and a fine haze drifts through the green light; the big banana leaves nod under the water. She wipes the back of her wrist across her forehead, pushes a damp strand of hair off her neck and turns her face up into the sunlight coming through the glass roof, breathing out. Slow push in, humid air, droplets falling from the ferns, birdsong outside.</td></tr>
</table>

### MiniMax H3

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/minimax-h3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/e7e1d9d42f04a009.mp4"><img src="assets/showcase/minimax-h3--cup-then-two-in-one-shirt.gif" alt="A woman in an oversized white shirt holds a coffee cup at a kitchen counter while a shirtless man stands in the dim room behind her" width="230"></a></td><td valign="top"><b>Tilt up from a coffee cup to a morning-after kitchen</b><br><sub><code>minimax/h3/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/e7e1d9d42f04a009.mp4">▶ полное видео</a></sub><br><br>The cup is lifted out of frame by a hand, then the camera tilts up: she is wearing an oversized men&#x27;s shirt, and further back in the dim room a man is just getting up. Slow tilt and rack focus. Cinematic, shallow depth of field, heavy film grain, morning grey-gold.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/7efb827ad33aabfc.mp4"><img src="assets/showcase/minimax-h3--red-dress-theatre-three-angles.gif" alt="A woman in a long-sleeved red dress with a high slit and a low back walks through an ornate empty theatre onto the stage, followed from behind" width="230"></a></td><td valign="top"><b>Red slit dress crossing a theatre stage, a third angle</b><br><sub><code>minimax/h3/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3/7efb827ad33aabfc.mp4">▶ полное видео</a></sub><br><br>The camera stays on her, the slit opening with every step. The same actress in the same high-slit red dress on the same theatre stage, shot from a third angle: she crosses to the proscenium and turns, the slit opening and closing with the walk, follow-spot tracking her. The slit opens over the thigh with every step, the bodice cut low at the back; medium close tracking. Cinematic, shallow depth of field, heavy film grain, crimson and gold.</td></tr>
</table>

### LTX 2.5

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/ltx-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/ef31b81ab1470620.mp4"><img src="assets/showcase/ltx-2-5--surf-lift-embrace.gif" alt="Surf lift embrace" width="230"></a></td><td valign="top"><b>Surf lift embrace</b><br><sub><code>lightricks/ltx-2.5/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/ef31b81ab1470620.mp4">▶ полное видео</a></sub><br><br>She turns into him in the shallows and hooks a wet arm around his neck; he takes her waist and lifts her against him, and she wraps a leg around his hip as the swell breaks around them both. Water sheets off their skin into the low sun. She leans back in his arms, throat to the light, and laughs. Handheld, camera drifting closer through the surf, gold backlight, spray in the air. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/5c83fe7b1b557753.mp4"><img src="assets/showcase/ltx-2-5--copper-tub-candlelight.gif" alt="Copper tub candlelight" width="230"></a></td><td valign="top"><b>Copper tub candlelight</b><br><sub><code>lightricks/ltx-2.5/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-5/5c83fe7b1b557753.mp4">▶ полное видео</a></sub><br><br>A woman lowers herself into a candlelit copper tub, water rising to her shoulders as she sinks back and tips her head against the rim, one wet arm draped over the edge. Steam climbs through the candlelight, water laps and settles, a drop falls from her fingertips to the stone floor. Slow push in along the length of the tub, warm flame light on wet skin, deep shadow. Cinematic, very shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 3.0 Pro Prime

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-3-0-pro-prime?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro-prime/5143df366cca3f75.mp4"><img src="assets/showcase/wan-3-0-pro-prime--dancer-three-stages-4k.gif" alt="A dancer in layered grey-white chiffon spins on a dark stage as a follow spot from behind turns the skirt translucent and glowing" width="230"></a></td><td valign="top"><b>Backlit dancer spinning in translucent chiffon</b><br><sub><code>alibaba/wan-3.0-pro-prime/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro-prime/5143df366cca3f75.mp4">▶ полное видео</a></sub><br><br>The same dancer, the same layered chiffon, a third stage: the follow spot comes from behind this time and the fabric goes translucent as she turns through it. The chiffon glows as the backlight comes up; close. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 3.0 Pro

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro/57c86b075f9fadb0.mp4"><img src="assets/showcase/wan-3-0-pro--same-two-three-times.gif" alt="White sheets in morning light, then the same couple on a sofa at night by a city window as he lights her cigarette" width="230"></a></td><td valign="top"><b>Same couple, same apartment, different times of day</b><br><sub><code>alibaba/wan-3.0-pro/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3.0-pro/57c86b075f9fadb0.mp4">▶ полное видео</a></sub><br><br>The camera stays on the same two people in all three. The same two people, the same apartment, three times of day: morning light across the bed, dusk with the two of them in the kitchen, night with the two of them on the balcony sharing one cigarette. Same faces, same room, rendered at 4K. Cinematic, shallow depth of field, heavy film grain, warm interior against cold window light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-pro/115148ffd12fa417.mp4"><img src="assets/showcase/wan-3-0-pro--silk-shoulder-turn.gif" alt="A woman in a champagne satin slip dress by a rain-streaked window at night turns to face the camera" width="230"></a></td><td valign="top"><b>Rainy-window turn as a silk strap slips</b><br><sub><code>alibaba/wan-3.0-pro/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-3-0-pro/115148ffd12fa417.mp4">▶ полное видео</a></sub><br><br>She turns her shoulders slowly toward camera, the silk catching the light, her breath settling as she stops. Slow push-in, one hard key from the left, rain on the window behind her.</td></tr>
</table>

### MiniMax H3 LoRA

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/minimax-h3-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/8df03dd8cf5dbff7.mp4"><img src="assets/showcase/minimax-h3-lora--hotel-window-dawn.gif" alt="Hotel window dawn" width="230"></a></td><td valign="top"><b>Hotel window dawn</b><br><sub><code>minimax/h3-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/8df03dd8cf5dbff7.mp4">▶ полное видео</a></sub><br><br>From this exact frame: he turns away from the window, walks toward the camera tying the belt of his robe, and stops with a half smile. Slow handheld push-in. Audio: morning city hum through the glass, bare feet on carpet.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/12d5eb4bbb9c2d0d.mp4"><img src="assets/showcase/minimax-h3-lora--character-lora-plus-references.gif" alt="Character lora plus references" width="230"></a></td><td valign="top"><b>Character lora plus references</b><br><sub><code>minimax/h3-lora/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-lora/12d5eb4bbb9c2d0d.mp4">▶ полное видео</a></sub><br><br>Picture 1 is the woman, Picture 2 is the hotel room. She walks into the room at night, drops her coat on the bed and turns to the mirror, pushing her hair back. Slow dolly. Audio: door closing, heels on carpet, a low bass line from the next room.</td></tr>
</table>

### HappyHorse 1.1

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/happyhorse-1-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/happyhorse-1-1/4d22782ccf7d7385.mp4"><img src="assets/showcase/happyhorse-1-1--sea-walk-wet-slip.gif" alt="Sea walk wet slip" width="230"></a></td><td valign="top"><b>Sea walk wet slip</b><br><sub><code>alibaba/happyhorse-1.1/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/happyhorse-1-1/4d22782ccf7d7385.mp4">▶ полное видео</a></sub><br><br>A woman walks out of the sea at dusk in a soaked slip that clings to every line of her, wringing her hair out over one shoulder as she comes. She stops ankle deep, plants her feet, and looks straight down the lens while the swell breaks white behind her and drags back. Wind takes the wet fabric against her. Slow push in from the waterline, low gold light through spray. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Seedance 2.0 Mini Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini-spicy/0e9a1972d379e9f6.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--robe-tie-pulled.gif" alt="Robe tie pulled" width="230"></a></td><td valign="top"><b>Robe tie pulled</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini-spicy/0e9a1972d379e9f6.mp4">▶ полное видео</a></sub><br><br>Cast: two women. The camera stays on her waist and the hand at the belt, nothing above the ribs. Close on the waist only: another hand rests on the knotted belt of the bathrobe and stays there. The frame never goes above the ribs or below the hip. Cinematic, very shallow depth of field, heavy film grain, low warm light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/a5cd491837869375.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--fridge-glow-exit.gif" alt="A woman in an oversized white shirt in the blue glow of an open refrigerator at night, closing the door with her hip as the room goes dark" width="230"></a></td><td valign="top"><b>Late-night fridge glow, then lights out</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/a5cd491837869375.mp4">▶ полное видео</a></sub><br><br>She lowers the bottle, shuts the refrigerator door with her hip and the room drops to darkness except for a thin sliver of street light, then she pads barefoot out of frame. Static camera, cold blue to warm black, fridge hum and bare feet on tile.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/c839b6bc8eb47b74.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--fogged-shower-streak.gif" alt="Behind fogged shower glass, a woman in a black bikini drags her palm down the steamed pane, backlit by a bright window as steam rolls across the frame" width="230"></a></td><td valign="top"><b>Hand streak on a fogged shower glass</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/c839b6bc8eb47b74.mp4">▶ полное видео</a></sub><br><br>Locked-off camera, no move. Steam keeps rolling across the frame and the glass fogs further. She presses her palm flat on the glass and drags it slowly downward, leaving one clear streak that immediately re-fogs, then turns her head and sweeps her wet hair across to the other shoulder. She keeps the black bikini on the whole time. Water runs down the outside of the glass, the backlight stays blown out and cold, and her body stays only a soft outline through the fog. No camera move, no cut.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/e03de02a8cc1d691.mp4"><img src="assets/showcase/seedance-2-0-mini-spicy--van-door-sunrise.gif" alt="A woman sits in the open side door of a white van in a red crop top and flannel shirt, sipping from a mug as the sun rises over a desert of mesas" width="230"></a></td><td valign="top"><b>Desert sunrise coffee from an open van door</b><br><sub><code>bytedance/seedance-2.0-mini-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-mini-spicy/e03de02a8cc1d691.mp4">▶ полное видео</a></sub><br><br>She pulls the flannel closed against the cold, sips from the mug and lets her head tip back into the sunrise with her eyes closed. Steam off the mug catches the rim light; the sun climbs and the orange rim strengthens. Camera drifts slowly in from outside the van.</td></tr>
</table>

### Seedance 2.0 Mini

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/seedance-2-0-mini?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/3968a086dd25eadf.mp4"><img src="assets/showcase/seedance-2-0-mini--latte-then-robe.gif" alt="A latte on a sunlit white kitchen counter is lifted out of frame as the camera tilts up to a woman in a loose white bathrobe who smiles softly at the viewer" width="230"></a></td><td valign="top"><b>Tilt up from a latte to a morning bathrobe</b><br><sub><code>bytedance/seedance-2.0-mini/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/3968a086dd25eadf.mp4">▶ полное видео</a></sub><br><br>Cast: one woman. The latte is lifted away and the camera tilts up to a woman in a white terry bathrobe tied closed, leaning on the counter with a sleepy half-smile toward the lens, morning light coming in hard from the side. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/8cc520660c695a11.mp4"><img src="assets/showcase/seedance-2-0-mini--same-couple-three-angles.gif" alt="A backlit couple in white shirts sit close on a park bench under trees, foreheads together, then settle back as she drapes her legs across his lap" width="230"></a></td><td valign="top"><b>Same couple on a park bench from a new angle</b><br><sub><code>bytedance/seedance-2.0-mini/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-mini/8cc520660c695a11.mp4">▶ полное видео</a></sub><br><br>The same couple on the same park bench from a third angle: they settle back into each other against a low backlight that fuses the two outlines into one. Her bare legs come across his lap as they settle back; medium close. Cinematic, shallow depth of field, heavy film grain, late-gold palette.</td></tr>
</table>

### Wan 2.7 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4"><img src="assets/showcase/wan-2-7-spicy--silk-draught-pull.gif" alt="A gust drags cream silk off a woman’s bare shoulder and back on a beach at dusk, then blows it back across her as she turns her head toward the light." width="230"></a></td><td valign="top"><b>A gust pulls silk off the shoulder, the camera follows the fabric</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/131308db4dc88808.mp4">▶ полное видео</a></sub><br><br>The draught drags the silk off her in one continuous pull, baring the whole slope of the shoulder and the line of the spine as the fabric slips away, then a second gust throws it back across her hip. She turns her head toward the light as the silk settles against her arm. The camera slides slowly along the body following the silk. Low gold light, dust turning in the beam, very shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.7-spicy/287f6caf66e84d8c.mp4"><img src="assets/showcase/wan-2-7-spicy--silk-drifts-own-track.gif" alt="Close-up of a woman’s bare back and shoulder on a dim beach as a length of cream silk drifts across it in the wind." width="230"></a></td><td valign="top"><b>Close-up: silk drifting across a bare back in low gold light</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.7-spicy/287f6caf66e84d8c.mp4">▶ полное видео</a></sub><br><br>Cast: one woman. The camera stays on her as the silk crosses her. Silk is drawn slowly across the body by the draught; cut to the supplied slow music track. The silk drags across a bare shoulder, the waist and the whole line of the spine in turn; very close. Cinematic, very shallow depth of field, heavy film grain, low gold light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/c1dab148533285b8.mp4"><img src="assets/showcase/wan-2-7-spicy--backstage-mirror-turn.gif" alt="A showgirl in a fringed emerald sequin leotard finishes adjusting a shoulder strap at a bulb-lit backstage mirror, then turns her head to camera and raises an eyebrow before stepping out of frame." width="230"></a></td><td valign="top"><b>Showgirl checks the mirror backstage, then turns to camera</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/c1dab148533285b8.mp4">▶ полное видео</a></sub><br><br>She finishes adjusting the sequin strap, checks herself in the bulb-lit mirror, then turns her head to camera and raises one eyebrow before stepping out of frame toward the stage. Bulbs flicker, feathers stir in the draft, smoke drifts, muffled orchestra and applause building behind the wall.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/09b29059d5b8b826.mp4"><img src="assets/showcase/wan-2-7-spicy--dune-silk-throw.gif" alt="A woman in a dark slip dress throws a huge sheet of indigo silk overhead on a desert dune at night, a lantern at her feet and the Milky Way above." width="230"></a></td><td valign="top"><b>Night dune: a sheet of indigo silk thrown into the wind</b><br><sub><code>alibaba/wan-2.7-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-7-spicy/09b29059d5b8b826.mp4">▶ полное видео</a></sub><br><br>She sweeps the huge sheet of indigo silk down and across in front of her, then throws it back up so it billows overhead and fills the sky, turning under it with her head tipped back. Sand streams off the crest of the dune in the wind and the lantern flame gutters, throwing her shadow long across the ripples. Slow arc around her, starfield steady above, wind and snapping fabric.</td></tr>
</table>

### LTX 2.3 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Steam mirror towel</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code></sub><br><br>She presses both palms to the fogged glass and drags them slowly down, carving two clear streaks, then steps in and leans her forehead against the mirror, rolling her shoulders back and letting the wet hair fall away from her neck. Her reflection sharpens through the streaks and her eyes open toward the lens. The towel stays knotted above the chest throughout. Steam rolls across the ceiling, water beads and runs down the glass, the bulbs flicker. Slow push toward the mirror. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/6d4795df0ff9089b.mp4"><img src="assets/showcase/ltx-2-3-spicy--rain-car.gif" alt="Rain car" width="230"></a></td><td valign="top"><b>Rain car</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/6d4795df0ff9089b.mp4">▶ полное видео</a></sub><br><br>She turns further toward the driver&#x27;s seat, wet shirt clinging as she moves, pushes a soaked strand of hair back and mouths something with a tired smile. Rain streams down the windscreen, neon reflections crawl across the glass, wipers sweep once.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/f719693ce2b6ad2b.mp4"><img src="assets/showcase/ltx-2-3-spicy--hearth-chaise-heels.gif" alt="Hearth chaise heels" width="230"></a></td><td valign="top"><b>Hearth chaise heels</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/f719693ce2b6ad2b.mp4">▶ полное видео</a></sub><br><br>The fire surges and the orange light flickers across her bare legs and the green velvet. She uncrosses her ankles and re-crosses them the other way, the pointed heels tipping, then slides her free hand slowly up the black silk robe and draws the hem a little higher on her thigh before letting it settle. She tips her head back against the chaise, keeps her eyes on the camera and one corner of her mouth lifts. Locked-off camera, no camera move, logs cracking and popping.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/0eccc200eb648e68.mp4"><img src="assets/showcase/ltx-2-3-spicy--drive-in-bonnet.gif" alt="Drive in bonnet" width="230"></a></td><td valign="top"><b>Drive in bonnet</b><br><sub><code>lightricks/ltx-2.3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy/0eccc200eb648e68.mp4">▶ полное видео</a></sub><br><br>The projector beam flickers and the blank screen pulses brighter then dimmer, washing her face in shifting blue light. She uncrosses her ankles on the warm bonnet, pushes herself up on one elbow, tips the paper cup back and grins toward the camera, then pulls the striped blanket up over one knee. Headlights sweep past behind her and the dusk sky deepens. Locked-off wide shot, no camera move, crickets and a distant tinny speaker.</td></tr>
</table>

### LTX 2.3 Spicy LoRA

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/ltx-2-3-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Vhs grain two on bed</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code></sub><br><br>Cast: one man and one woman. The camera stays on the two of them from the shoulders up, and never tilts below the collarbone. Push the whole frame to 1990s VHS: two people sitting at the edge of an unmade bed in low lamplight, one bare shoulder and a sheet held at the chest, her head tipping onto his shoulder; scan lines, chroma bleed and tape wobble crawl across the image. Handheld, low light, heavy analogue grain, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/673813a5c0f4f554.mp4"><img src="assets/showcase/ltx-2-3-spicy-lora--neon-rooftop.gif" alt="Neon rooftop" width="230"></a></td><td valign="top"><b>Neon rooftop</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/673813a5c0f4f554.mp4">▶ полное видео</a></sub><br><br>The glowing cyan circuits along her arms and spine pulse in sequence as she completes the turn, holographic billboards flickering behind her, rain hissing on the rooftop. Slow arc around her silhouette, volumetric neon fog, synth bass swell.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/6470b2a1b89cbe1c.mp4"><img src="assets/showcase/ltx-2-3-spicy-lora--gouache-poster-pier.gif" alt="Gouache poster pier" width="230"></a></td><td valign="top"><b>Gouache poster pier</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/6470b2a1b89cbe1c.mp4">▶ полное видео</a></sub><br><br>The painted illustration comes alive without losing its flat printed look: the striped umbrella canopy ripples in the sea breeze, her hair lifts and the gulls glide across the turquoise sky. She lowers her sunglasses with one finger, glances over the top of them at the camera and smiles, then swings the dangling sandal off her toe. The sea sparkles behind the bathing huts. Gentle slow push in, gouache brush texture and screen-print grain held stable throughout.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/e151f11d0696350f.mp4"><img src="assets/showcase/ltx-2-3-spicy-lora--strength-sweep.gif" alt="Strength sweep" width="230"></a></td><td valign="top"><b>Strength sweep</b><br><sub><code>lightricks/ltx-2.3-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/ltx-2-3-spicy-lora/e151f11d0696350f.mp4">▶ полное видео</a></sub><br><br>She drives up out of the squat, the bar flexing on her shoulders, chalk dust bursting off her hands into the lamp beam, and racks the bar with a heavy metallic clang before straightening and exhaling at the lens. Handheld, slight shake on the rack, haze rolling through the light.</td></tr>
</table>

### Seedance 2.0 Fast Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-fast-spicy/518ad024b9b8a2dc.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--pool-cannonball-crowd.gif" alt="At a floodlit outdoor pool at night, swimmers in competition suits crouch on the edge and dive in one after another, spray bursting white" width="230"></a></td><td valign="top"><b>Floodlit night pool, swimmers diving one after another</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2.0-fast-spicy/518ad024b9b8a2dc.mp4">▶ полное видео</a></sub><br><br>Cast: a mixed crowd of men and women of different ages and skin tones. A night pool: one after another they hit the water, the splashes blowing up white in the floodlights, the surface never settling; someone hauls themselves out at the near edge, soaked. Wet swimwear clinging as one of them hauls out at the near edge, water running off the shoulders; close at the lip of the pool. Cinematic, heavy film grain, chlorine cyan and floodlight white.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/1461db51e6ecc0b1.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--balcony-laundry-turn.gif" alt="A woman in a bikini top and denim cutoffs pinning a sheet to a washing line on a sunlit balcony, turning to camera with a grin" width="230"></a></td><td valign="top"><b>Sunny balcony laundry turn with a grin</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/1461db51e6ecc0b1.mp4">▶ полное видео</a></sub><br><br>The sheet billows and drops as she pins it to the line, then she turns fully toward camera, pushes windblown hair off her face and grins. Bright midday sun, fabric snapping in the breeze, cicadas and distant sea.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/7eaa3a9aae761e79.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--pillow-pov-lean.gif" alt="Pillow pov lean" width="230"></a></td><td valign="top"><b>Pillow pov lean</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/7eaa3a9aae761e79.mp4">▶ полное видео</a></sub><br><br>First person point of view, the camera stays where it is on the pillow and does not move. She lowers herself closer toward the lens, her long hair falling forward around the edges of the frame, holds eye contact and smiles. She keeps the black lace top and the black satin robe on the whole time and stays fully dressed. Candlelight flickers behind her; the background stays black. Only her movement, no camera move, no cut.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/09bed565d0700cae.mp4"><img src="assets/showcase/seedance-2-0-fast-spicy--pool-hall-break.gif" alt="A woman in a black satin slip dress leans over a green pool table under hanging lamps, breaks the rack, then straightens up and looks toward the camera through drifting smoke" width="230"></a></td><td valign="top"><b>Pool hall break shot in a black satin slip dress</b><br><sub><code>bytedance/seedance-2.0-fast-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-2-0-fast-spicy/09bed565d0700cae.mp4">▶ полное видео</a></sub><br><br>She strikes the break — the cue drives forward, the rack scatters across the felt, and she straightens up and looks at the lens as the balls settle. Smoke rolls through the lamp beam from the impact. Camera holds low at table height.</td></tr>
</table>

### Vidu Q3 Turbo

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/vidu-q3-turbo?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>One still push in</b><br><sub><code>vidu/q3-turbo/image-to-video</code></sub><br><br>The camera stays on her the whole way in. Slow push in on the same still, and nothing else: the frame tightens by degrees. The frame tightens until it holds only a bare shoulder and the sheet at her hip. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Vidu Q3 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/334a9b5ae943a9b6.mp4"><img src="assets/showcase/vidu-q3-spicy--wet-hair-lift-gaze.gif" alt="Wet hair lift gaze" width="230"></a></td><td valign="top"><b>Wet hair lift gaze</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/334a9b5ae943a9b6.mp4">▶ полное видео</a></sub><br><br>She lifts her face slowly out of the fall of wet hair, water running off her chin and throat, and opens her eyes straight into the lens. Her lips part on an exhale and she tilts her head, hair peeling away from her cheek in wet strands, one bare shoulder rolling forward into frame. Slow push in, water still dripping, cold blue light, condensation in the air. Cinematic, very shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/2d08be3cd91a6d59.mp4"><img src="assets/showcase/vidu-q3-spicy--ryokan-pour.gif" alt="Ryokan pour" width="230"></a></td><td valign="top"><b>Ryokan pour</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/2d08be3cd91a6d59.mp4">▶ полное видео</a></sub><br><br>She finishes pouring, sets the flask down and lifts her eyes to camera with a small smile, steam rising from the cup, the yukata sliding a fraction lower on her shoulder. Paper shoji glow, evening cicadas, very slow push-in.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/7b5a55df8a3bffec.mp4"><img src="assets/showcase/vidu-q3-spicy--booth-heel-drop.gif" alt="Booth heel drop" width="230"></a></td><td valign="top"><b>Booth heel drop</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/7b5a55df8a3bffec.mp4">▶ полное видео</a></sub><br><br>She rolls the black stiletto off her pointed toes and it drops onto the velvet, then draws that leg down along the back of the booth and crosses it over the other. Her other hand pulls the fallen strap back up onto her bare shoulder and she holds the look into the lens, lifting her chin. The red neon on the right breathes brighter and the amber sconce flickers. Slow low tracking dolly moving in past the edge of the table, quiet bar room tone.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/3a5edfd4e36921ff.mp4"><img src="assets/showcase/vidu-q3-spicy--wheel-and-hands.gif" alt="Wheel and hands" width="230"></a></td><td valign="top"><b>Wheel and hands</b><br><sub><code>vidu/q3-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/vidu-q3-spicy/3a5edfd4e36921ff.mp4">▶ полное видео</a></sub><br><br>The wheel keeps spinning and the clay wall rises under her hands, then she opens the rim with her thumbs and it flares outward. She lifts one wet hand off, wipes her forearm across her cheek leaving a grey streak, and glances up at the camera with a small smile before going back to the pot. Slip water runs down the wheel head. Slow push in, wheel hum and wet clay.</td></tr>
</table>

### Vidu Q3

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Blind light reach</b><br><sub><code>vidu/q3/image-to-video</code></sub><br><br>The blind slats of light slide up their bare backs as one of them shifts and reaches across the sheets for the other. The far one turns their face into the pillow. Slow push along the bed, dust turning in the light bars, curtain breathing at the window. Cinematic, shallow depth of field, heavy film grain, warm morning light.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/vidu-q3?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Blinds light two bodies</b><br><sub><code>vidu/q3/image-to-video</code></sub><br><br>Cast: one man and one woman. Locked-off camera, tight on two bare shoulders and upper backs with a white sheet drawn up over both of them from the waist down, so the sheet fills the lower third of the frame. Nothing moves but the light: hard blind stripes travel slowly across their shoulders and across the sheet as the sun drops. Cinematic, heavy film grain, amber stripes on shadow, restrained and tasteful.</td></tr>
</table>

### Seedance 1.5 Pro Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro-spicy/da11e751bcf25dd0.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--silk-breathing-locked.gif" alt="Silk breathing locked" width="230"></a></td><td valign="top"><b>Silk breathing locked</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro-spicy/da11e751bcf25dd0.mp4">▶ полное видео</a></sub><br><br>Cast: one man and one woman. Locked-off camera, absolutely no movement: the silk sheet over the two of them rises and falls with their breathing, a bare shoulder and one arm outside it, nothing else in the frame moves. Cinematic, shallow depth of field, heavy film grain, low warm lamp light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/c16f53eee15a669f.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--locked-hotel-sheets.gif" alt="Locked hotel sheets" width="230"></a></td><td valign="top"><b>Locked hotel sheets</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/c16f53eee15a669f.mp4">▶ полное видео</a></sub><br><br>Camera stays locked off. Her crossed ankles rock slowly and one foot flexes. She slides one hand out from behind her head and rests it on her stomach, her fingers tracing a slow circle on the camisole, while her other hand stays tucked behind her head. Her chest rises with a long breath. Nothing else in frame moves except the light shifting on the sheets.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/f22c2b64fc387ebf.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--stocking-and-heel.gif" alt="Stocking and heel" width="230"></a></td><td valign="top"><b>Stocking and heel</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/f22c2b64fc387ebf.mp4">▶ полное видео</a></sub><br><br>Slow push-in along the floor from the dangling stiletto heel up toward her hands. She rolls the black stocking the rest of the way down to her ankle and slips it off over her toes, flexes her bare foot, then lets the patent heel swing twice on the toes of her other foot and drops it to the floor. She stays in the black lace outfit the whole time. Hard overhead key light, everything else stays black, extremely shallow focus. Continuous dolly, no cut.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/45a9fa4e438db221.mp4"><img src="assets/showcase/seedance-1-5-pro-spicy--tail-sweep-arc.gif" alt="Tail sweep arc" width="230"></a></td><td valign="top"><b>Tail sweep arc</b><br><sub><code>bytedance/seedance-1.5-pro-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1-5-pro-spicy/45a9fa4e438db221.mp4">▶ полное видео</a></sub><br><br>The fluffy tail sweeps slowly across the rug behind her. She shifts her weight on her knees, tucks a strand of hair behind her ear and holds the camera&#x27;s gaze over her shoulder, then breaks into a small laugh and looks away. Warm bedside lamp light, soft shadows moving on the rug. Slow arc around to her left.</td></tr>
</table>

### Seedance 1.5 Pro

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/seedance-1-5-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro/251525c66c0fb58a.mp4"><img src="assets/showcase/seedance-1-5-pro--seance-candle-bare-feet.gif" alt="Seance candle bare feet" width="230"></a></td><td valign="top"><b>Seance candle bare feet</b><br><sub><code>bytedance/seedance-1.5-pro/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedance-1.5-pro/251525c66c0fb58a.mp4">▶ полное видео</a></sub><br><br>Cast: one woman. Locked-off camera, absolutely no movement: a woman lies back across a chaise in a candlelit parlour, one bare foot hooked over the arm of it, the other knee drawn up, her robe fallen open at the knee. The candle flames lean and recover and their shadows sway up her calf and thigh; nothing else in the frame moves. Cinematic, heavy film grain, candle gold in near black.</td></tr>
</table>

### Wan 2.6 Flash

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-2-6-flash?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-flash/6b7cd6d830945dc6.mp4"><img src="assets/showcase/wan-2-6-flash--three-angles-one-scene.gif" alt="A man and a woman lean across a bar table in conversation, covered from three angles that end on their two faces almost touching." width="230"></a></td><td valign="top"><b>One bar conversation covered from three ever-closer angles</b><br><sub><code>alibaba/wan-2.6-flash/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-flash/6b7cd6d830945dc6.mp4">▶ полное видео</a></sub><br><br>Cast: one man and one woman. The camera stays on the two of them, closer with every angle. The same quiet conversation covered from three angles, each one closer than the last, ending on the two faces almost touching. Each angle closer: shoulders, then throats, then only the space between two mouths. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 2.6 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Green tub turn in</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code></sub><br><br>One turns in the water and moves behind the other. The front one tips her head back onto the other&#x27;s shoulder and they turn their faces together. Framed from behind and above the shoulder line, the water surface holding steady at chest height the whole time. The bath swells against the green enamel, steam tearing and closing between their faces. Slow push in over the rim. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-spicy/3271dbc80ff97d8d.mp4"><img src="assets/showcase/wan-2-6-spicy--bathtub-knees-steam.gif" alt="Two pairs of knees rise above the waterline of a green enamel bathtub as steam curls off the water." width="230"></a></td><td valign="top"><b>Steam and knees above the waterline of a green bathtub</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.6-spicy/3271dbc80ff97d8d.mp4">▶ полное видео</a></sub><br><br>Cast: two women. The camera stays on the knees and the waterline. Two pairs of knees cross above the bathtub waterline, steam curling off, the water&#x27;s reflection shifting on the tiles. Steam curls off wet knees and shoulders; one knee slides against the other under the surface. Everything below the surface stays in the water. Cinematic, shallow depth of field, heavy film grain, tile green and steam white.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/2ff58bcb117213d6.mp4"><img src="assets/showcase/wan-2-6-spicy--pool-rise.gif" alt="A swimmer rises out of a rooftop infinity pool at blue hour, water running off her shoulders as she slicks her wet hair back with both hands and opens her eyes toward camera, city towers glowing behind." width="230"></a></td><td valign="top"><b>Rooftop pool rise at blue hour, slicking hair back</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/2ff58bcb117213d6.mp4">▶ полное видео</a></sub><br><br>She rises further out of the water, sheets of it running off her shoulders and swimsuit, slicks her wet hair straight back with both hands and opens her eyes toward camera, droplets scattering. Blue-hour city towers glow behind, slow-motion water detail, ambient pool lap and distant traffic.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/65c8f2b8dbc700bc.mp4"><img src="assets/showcase/wan-2-6-spicy--slatted-light-pov.gif" alt="First-person view down a red satin bed at legs in black lace-top stockings, bars of light from a window blind moving across them." width="230"></a></td><td valign="top"><b>POV: slatted morning light moving across stockinged legs</b><br><sub><code>alibaba/wan-2.6-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-6-spicy/65c8f2b8dbc700bc.mp4">▶ полное видео</a></sub><br><br>Her toes flex and hook deeper into the silk, one knee slowly straightening, the sheets sliding and rippling under her legs. The slatted bars of light creep across her thighs as the blind stirs in the draught. Handheld point-of-view sway, warm red and gold, quiet morning room tone.</td></tr>
</table>

### Wan 2.6

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-2-6?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-6/200161e5024b4f12.mp4"><img src="assets/showcase/wan-2-6--counter-slide-approach.gif" alt="A woman with wet hair in an oversized white shirt slides off a dark kitchen counter and walks toward the camera, a wine glass and a steaming pan behind her." width="230"></a></td><td valign="top"><b>Late-night kitchen: she slides off the counter toward the lens</b><br><sub><code>alibaba/wan-2.6/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-6/200161e5024b4f12.mp4">▶ полное видео</a></sub><br><br>She sets the glass down, slides off the counter onto her feet and walks toward the lens, the oversized shirt swinging open at the hem over bare legs while the front stays crossed and buttoned at the chest. She stops close, tips her head, and pushes her wet hair back off her face. Wine swings in the abandoned glass, steam drifts from a pan behind her. Slow push in, framed from the ribs up, warm downlight against black. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.6/4bbb55b80b0482d7.mp4"><img src="assets/showcase/wan-2-6--cast-three-clips.gif" alt="A man in a wet overcoat and a woman in a rain-soaked white shirt meet in a neon-lit brick alley in the rain and pull close." width="230"></a></td><td valign="top"><b>Recast a couple from a reference clip into a neon rain street</b><br><sub><code>alibaba/wan-2.6/reference-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.6/4bbb55b80b0482d7.mp4">▶ полное видео</a></sub><br><br>Cast: one man and one woman. Cast the two people and the street from the supplied clips into a new scene: the same pair now meet under neon in the rain. The two of them end up pressed together under the neon, clothes soaked through. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 2.5

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-2-5?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-5/ded29f1cc881124b.mp4"><img src="assets/showcase/wan-2-5--dressing-room-robe.gif" alt="Dressing room robe" width="230"></a></td><td valign="top"><b>Dressing room robe</b><br><sub><code>alibaba/wan-2.5/text-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-5/ded29f1cc881124b.mp4">▶ полное видео</a></sub><br><br>Backstage in a dressing room: a dancer in a sequined costume reaches for a silk robe and pulls it on over her costume as she turns to the bulb-lit mirror. She catches her own eye, then looks back over her bare shoulder toward the lens. Bulbs flicker, feathers stir in the draft, smoke drifts through the beam. Slow push toward the mirror. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Wan 2.2 Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy/0a7d0b59032f86aa.mp4"><img src="assets/showcase/wan-2-2-spicy--wolf-turn-and-look-back.gif" alt="A woman with wolf ears, seen from behind in a moonlit forest, turns her bare shoulders and looks back over her shoulder with glowing gold eyes." width="230"></a></td><td valign="top"><b>First and last frame: a wolf-eared glance back in moonlight</b><br><sub><code>alibaba/wan-2.2-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy/0a7d0b59032f86aa.mp4">▶ полное видео</a></sub><br><br>Start on her back, wolf ears and bare shoulders in moonlight, and end on the supplied final frame: she looks back over her shoulder, irises gone gold. Bare back and wolf ears in the moonlight, shoulder blades shifting as she turns. Cinematic, shallow depth of field, heavy film grain, moon silver and forest black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/38f04ab8005e193f.mp4"><img src="assets/showcase/wan-2-2-spicy--gym-dawn-breath.gif" alt="A woman lowers her leg off a gym bench at dawn, rolls her shoulders back and straightens up, wiping sweat from her collarbone as low window light moves across the concrete behind her." width="230"></a></td><td valign="top"><b>Dawn gym cooldown: stretch, shoulder roll, catch a breath</b><br><sub><code>alibaba/wan-2.2-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/38f04ab8005e193f.mp4">▶ полное видео</a></sub><br><br>She lowers her leg off the bench, rolls her shoulders back and straightens up, wiping sweat from her collarbone with the back of her wrist, chest rising as she catches her breath. Dawn light shifts across the concrete, dust drifting in the beam.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4"><img src="assets/showcase/wan-2-2-spicy--one-pace-closer.gif" alt="A woman in an open white shirt leans across a dark bed toward the camera, fingertip at her lip, then breaks into a slow half smile; lamp glow and a blue window behind." width="230"></a></td><td valign="top"><b>Locked-camera bedroom shot: one slow pace closer, then a smile</b><br><sub><code>alibaba/wan-2.2-spicy/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy/3d2ca819ea4a2a2d.mp4">▶ полное видео</a></sub><br><br>She crawls one slow pace closer toward the viewer, weight shifting onto the reaching hand, the open white shirt sliding further down off her shoulder. She draws her fingertip away from her lip, tips her head to the side and holds the viewer&#x27;s gaze, then breaks into a slow half smile. Her hair swings forward. Warm lamp glow on the left, cold blue window behind, no camera move, shallow focus, quiet room tone.</td></tr>
</table>

### Wan 2.2 Spicy LoRA

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/928d00c859a4fc39.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--three-loras-stacked.gif" alt="A woman in a champagne satin wrap turns in a dark gilded room; the fabric slips off one shoulder and her bare back catches the gold key light." width="230"></a></td><td valign="top"><b>Three LoRAs stacked on one slow satin turn</b><br><sub><code>alibaba/wan-2.2-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/928d00c859a4fc39.mp4">▶ полное видео</a></sub><br><br>With all three LoRAs stacked - style, fabric and lighting - she turns on the spot and the satin catches the dark gold key light. The satin slides off one shoulder as she turns, the dark gold key raking the bare back. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/d48338ae0374953f.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--extend-the-stack.gif" alt="The satin wrap falls away as the woman turns from the gold light and walks off with her bare back to the camera, continuing the earlier clip for eight more seconds." width="230"></a></td><td valign="top"><b>Extend a clip eight more seconds with the same LoRAs</b><br><sub><code>alibaba/wan-2.2-spicy-lora/video-extend</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2.2-spicy-lora/d48338ae0374953f.mp4">▶ полное видео</a></sub><br><br>She turns away from the light and the satin falls off the other shoulder. Continue the clip for another eight seconds with the same LoRAs attached: the stillness breaks and she turns away from the light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/b47e28f395798f05.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--tail-rise-continue.gif" alt="A woman in fox ears, a black silk robe and long gloves kneels on a velvet rug in a crimson room beside a table lamp, a plush fox tail curled behind her." width="230"></a></td><td valign="top"><b>Continue a clip: fox-ear costume in crimson lamplight</b><br><sub><code>alibaba/wan-2.2-spicy-lora/video-extend</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/b47e28f395798f05.mp4">▶ полное видео</a></sub><br><br>Continuing the same unbroken take: she rises up from her knees, the plush fox tail sweeping in a slow arc across the velvet rug behind her, gathers the black silk robe closed with one gloved hand and turns fully toward the camera, the tail settling against her leg; she tilts her head and holds the look. One continuous move with no cut, deep crimson lamp light, soft shadows, film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/e19d8c98cdbfd616.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--candlelit-crypt.gif" alt="Candle flames sway across a crypt as a painted elven sorceress lifts her hand from a stone armrest, turns toward camera and a sheer lace sleeve slides down her forearm, embers drifting upward." width="230"></a></td><td valign="top"><b>Gothic sorceress rises from a candlelit throne</b><br><sub><code>alibaba/wan-2.2-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/e19d8c98cdbfd616.mp4">▶ полное видео</a></sub><br><br>The candle flames gutter and sway across the crypt as she lifts her hand from the armrest, turns her head toward camera and the sheer lace sleeve slides down her forearm, embers drifting upward through the frame. Slow push-in, deep crimson and obsidian, low choral drone.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/5250c042ec231d01.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--airbrush-pool-hold.gif" alt="A flat airbrush-style illustration of a woman in a black bikini sitting at the edge of a neon-lit rooftop pool, pushing her wet hair back as the water ripples." width="230"></a></td><td valign="top"><b>Airbrushed pool illustration that stays flat when it moves</b><br><sub><code>alibaba/wan-2.2-spicy-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/5250c042ec231d01.mp4">▶ полное видео</a></sub><br><br>The illustration comes alive while keeping its flat airbrushed print look: the pool water ripples and laps at her legs, the neon arcs pulse and their reflections wobble across the surface, water keeps running off her hair and shoulders. She lowers her chin from the sky, opens her eyes and turns her face toward the viewer, then draws one hand up out of the water and slowly pushes her wet hair back off her shoulder. Gentle slow push in, banded gradient shading, halftone and print grain held stable throughout, black bikini stays on, no drift toward photorealism.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/658e7278d63095b1.mp4"><img src="assets/showcase/wan-2-2-spicy-lora--closing-hold.gif" alt="A woman in a long dark coat stands at a wall of rain-streaked windows at night, city lights blurred beyond, and turns her head back over her shoulder." width="230"></a></td><td valign="top"><b>End an extended clip on a settled hold for the next join</b><br><sub><code>alibaba/wan-2.2-spicy-lora/video-extend</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-spicy-lora/658e7278d63095b1.mp4">▶ полное видео</a></sub><br><br>She stops at the top of the stairs, turns her head back toward the crypt and holds still as the candles steady behind her. Camera locked.</td></tr>
</table>

### Wan 2.2 LoRA

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/wan-2-2-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-lora/94000f2077317c6c.mp4"><img src="assets/showcase/wan-2-2-lora--rooftop-walk.gif" alt="An illustrated office worker pushes off a rooftop railing, straightens the blazer over her shoulder and walks along the roof, city lights and a vending machine glow sliding past behind her." width="230"></a></td><td valign="top"><b>Anime rooftop walk at night with a smooth tracking move</b><br><sub><code>alibaba/wan-2.2-lora/image-to-video</code> · <a href="https://cdn.spicyapi.ai/models/examples/wan-2-2-lora/94000f2077317c6c.mp4">▶ полное видео</a></sub><br><br>She pushes off the railing, straightens her blazer over one shoulder and turns to walk along the rooftop, city lights and the vending machine glow sliding past behind her, hair lifting in the night wind. Smooth tracking move, anime cel-shaded style held stable.</td></tr>
</table>

### Qwen Image 2.1

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Slats slip dress</b><br><sub><code>alibaba/qwen-image-2.1/edit</code></sub><br><br>Keep the bed, the linen, the blinds, the striped light and her pose exactly as they are. Dress her in a sheer ivory slip that the striped light passes through, the strap fallen off one shoulder, the hem gathered at her thigh. Match the existing grain, colour grade and the way the sun falls across the fabric. Change nothing else in the frame.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Boudoir window slats</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code></sub><br><br>Photograph of an adult woman lying on her side across rumpled white linen, seen from behind, one arm folded under her head and a sheet gathered across her hip. Late morning sun through venetian blinds lays hard parallel stripes across her back, her shoulder and the bedding. Medium-format film look, soft grain, honey and cream palette, warm skin against cool shadow. Calm and unposed.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp" alt="Lace and lamplight" width="230"></a></td><td valign="top"><b>Lace and lamplight</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/9026afbc1b31b054.webp">полный размер</a></sub><br><br>Low-key studio portrait of an adult woman kneeling on a dark velvet chaise in a black lace bodysuit and sheer stockings, seen from behind, looking back over her shoulder. A single hard lamp from the left gives one edge of her body and drops the rest to near black; lace texture catches the light where it crosses her spine. 85mm, shallow depth of field, heavy grain, oxblood and black.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp" alt="Two figures one sheet" width="230"></a></td><td valign="top"><b>Two figures one sheet</b><br><sub><code>alibaba/qwen-image-2.1/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/5be97dddae40fea1.webp">полный размер</a></sub><br><br>Intimate two-figure composition on a bed at dawn: a woman lying on her back with her eyes closed, the white sheet drawn up and gathered across her chest and tucked under her arms, and a man beside her propped on one elbow, bare shoulders above the sheet, his hand resting on the sheet over her stomach. Cool blue window light from the left, one warm bedside lamp still on behind them. Skin tones held apart by the two light sources. Shallow focus, fine grain, unhurried and quiet, tasteful and covered.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp" alt="Dawn to candlelight" width="230"></a></td><td valign="top"><b>Dawn to candlelight</b><br><sub><code>alibaba/qwen-image-2.1/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1/076b9798c6725479.webp">полный размер</a></sub><br><br>Keep both figures, the bed, their poses and the framing exactly as they are. Change the dawn window light to a single group of candles on the left nightstand: warm flickering light raking low across both bodies, the room falling to deep amber and black behind them, highlights only along the edges of skin and sheet. Keep the shadows consistent with the new light source.</td></tr>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Two references one chaise</b><br><sub><code>alibaba/qwen-image-2.1/edit</code></sub><br><br>Merge the two references into a single frame. Place the woman from the first image, lying on her side in the same pose, on the dark velvet chaise from the second image. Keep her face and body from the first reference, and the chaise, the single hard lamp and the oxblood palette from the second. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Qwen Image 2.1 LoRA

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Boudoir into anime</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code></sub><br><br>Transform into anime. Flat cel shading, clean linework, anime illustration. Keep her pose, the sheet across her hip, the bed, the blinds and the striped direction of the light.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp" alt="Anime boudoir lora" width="230"></a></td><td valign="top"><b>Anime boudoir lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/aa7226a5cb0b02ab.webp">полный размер</a></sub><br><br>storybook anime illustration of an adult woman reclining across rumpled linen in a sunlit attic room, seen from behind over her bare back and shoulder, one arm folded behind her head, a sheet drawn up across her hip and waist. Morning light through a slatted window falling in stripes across her back. Soft cel-shaded figure, warm hand-painted background, honey and cream palette, tasteful and covered.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp" alt="Relight the chaise" width="230"></a></td><td valign="top"><b>Relight the chaise</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/4b43e7a4c1c22600.webp">полный размер</a></sub><br><br>Relight the scene: a low warm candle cluster from the right at mattress level and cool blue moonlight through a window behind her. Keep her pose, the lace, the chaise and the framing unchanged.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp" alt="Watercolor lace lora" width="230"></a></td><td valign="top"><b>Watercolor lace lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/fc557b745f18eaa8.webp">полный размер</a></sub><br><br>watercolor anime of an adult woman kneeling on a dark velvet chaise in a black lace bodysuit and sheer stockings, seen from behind, glancing back over her shoulder. Transparent washes, pale paper texture, a single warm lamp from the left leaving most of the figure in deep wash, oxblood and ink.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp" alt="Impressionist bathers lora" width="230"></a></td><td valign="top"><b>Impressionist bathers lora</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/00a929d320ae30f7.webp">полный размер</a></sub><br><br>Monet Style, two bathers at the edge of a still pond at first light, both seen from behind — one seated on the bank wrapped in a pale towel with her bare shoulders showing, one standing waist-deep in the water with her back to us. Mist dissolving the far shore, loose impressionist brushwork, dappled light on wet skin and towel, pastel palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp" alt="Two weights stacked" width="230"></a></td><td valign="top"><b>Two weights stacked</b><br><sub><code>alibaba/qwen-image-2.1-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/6c0bbae0930616ba.webp">полный размер</a></sub><br><br>watercolor anime of an adult woman stepping out of a claw-foot bath in a winter bathroom at dusk, seen from behind, steam rising and fogging the window, a large towel wrapped and held at her chest with her bare back and shoulders showing, warm lamplight behind fogged glass, transparent washes, pale paper texture, soft ink linework.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp" alt="Next scene after dark" width="230"></a></td><td valign="top"><b>Next scene after dark</b><br><sub><code>alibaba/qwen-image-2.1-lora/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2-1-lora/201aee2b06812453.webp">полный размер</a></sub><br><br>Next Scene: hours later, exactly the same two people — one woman and one man, no other figures in the room — asleep and turned toward each other under the same sheet on the same bed. The window has gone full dark and only the low bedside lamp is still burning. Same framing, same bedding, same lens, same two faces.</td></tr>
</table>

### MiniMax H3 Image LoRA

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/minimax-h3-image-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp"><img src="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp" alt="Same woman new scene" width="230"></a></td><td valign="top"><b>Same woman new scene</b><br><sub><code>minimax/h3-image-lora/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/e290cf84e4acb5af.webp">полный размер</a></sub><br><br>Picture 1 is the woman. Put her on a sunlit balcony in a white linen shirt, wind in her hair, late afternoon light. Keep her face and hairstyle.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/282e8d89d6c8fff0.webp"><img src="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/282e8d89d6c8fff0.webp" alt="Vhs still doorway" width="230"></a></td><td valign="top"><b>Vhs still doorway</b><br><sub><code>minimax/h3-image-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/minimax-h3-image-lora/282e8d89d6c8fff0.webp">полный размер</a></sub><br><br>vh5tape, a paused VHS frame: a woman in a slip dress leaning in a doorway at night, pink and cyan light on wet asphalt, tracking lines across the bottom of the frame.</td></tr>
</table>

### Qwen Image 3.0 Pro

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/qwen-image-3-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/35af732b62f21e2c.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/35af732b62f21e2c.webp" alt="Two gladiators stand forehead to forehead in a torchlit arena above the lines MARCUS VS DRAVEN, XIV OCTOBER and ARENA VETUS." width="230"></a></td><td valign="top"><b>Gladiator fight poster with three clean lines of type</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0-pro/35af732b62f21e2c.webp">полный размер</a></sub><br><br>Cinematic fight poster, underground arena. Two gladiators stand forehead to forehead in a stare-down, oiled torsos catching torchlight, breath visible, sand and dust in the air. Three lines of clean typography set across the lower third: the words MARCUS VS DRAVEN on one line, XIV OCTOBER on the next, ARENA VETUS on the last. 65mm, shallow depth of field, heavy grain, torch orange against black, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp" alt="Fashion magazine cover with a large condensed SPICY masthead and small-caps cover lines over a studio portrait" width="230"></a></td><td valign="top"><b>Fashion magazine cover with masthead and cover lines</b><br><sub><code>alibaba/qwen-image-3.0-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3-0-pro/bbfab34deec5085a.webp">полный размер</a></sub><br><br>A glossy fashion magazine cover, full-bleed portrait of an adult woman in a black lace bodysuit under a sheer open kimono, arms raised adjusting her hair, studio rim light on a deep charcoal background; masthead text &#x27;SPICY&#x27; in large condensed type across the top, cover lines reading &#x27;THE LATE SHIFT&#x27; and &#x27;ISSUE 07&#x27; in small caps, high-end print typography, razor-sharp 2K detail.</td></tr>
</table>

### Qwen Image 3.0

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/qwen-image-3-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp" alt="Chalk handwriting reading TODAY’S DRAUGHT – MOONWELL on a rain-beaded shop window, behind it a woman holding up a glowing green potion bottle." width="230"></a></td><td valign="top"><b>Chalk lettering on a rainy apothecary window at night</b><br><sub><code>alibaba/qwen-image-3.0/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-3.0/7a046426d3e70c90.webp">полный размер</a></sub><br><br>Cinematic film still, an apothecary shop window at night. Chalk handwriting on the glass reads TODAY&#x27;S DRAUGHT - MOONWELL; behind it a woman tilts a glowing potion bottle, one camisole strap slipped to her elbow, the liquid&#x27;s green light thrown up under her jaw. Rain beads on the outside of the glass. 35mm, shallow depth of field, heavy grain, potion green against night blue, restrained and tasteful.</td></tr>
</table>

### Seedream 5.0 Pro

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/seedream-5-0-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Bathhouse marble two</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code></sub><br><br>Cinematic film still, Roman marble bathhouse. Close two-shot on the stepped ledges: a woman on the upper step tips a brass basin of water over her shoulder and it sheets down her bare back, while the man on the step below watches from a hand&#x27;s breadth away, her knee almost at his chest; everything below the chest is lost in thick steam. One hard clerestory shaft cuts the vapour and catches wet skin and wet Carrara marble alike. 65mm, shallow depth of field, warm amber against stone grey, heavy grain, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp" alt="Champagne satin back" width="230"></a></td><td valign="top"><b>Champagne satin back</b><br><sub><code>bytedance/seedream-5.0-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-pro/8f96701b135f64c0.webp">полный размер</a></sub><br><br>Cinematic film still, a woman sits at a tall window wrapped in champagne satin, seen entirely from behind so the frame is one unbroken line of back; the satin has slipped from the shoulder blade to the small of the back and pools there. Cold morning light from the window, warm lamp from inside. 85mm, shallow depth of field, heavy grain, champagne and slate palette, restrained and tasteful.</td></tr>
</table>

### Qwen Image Edit Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/qwen-image-spicy-edit?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp" alt="Boudoir i2i" width="230"></a></td><td valign="top"><b>Boudoir i2i</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5ae28cdb921ffbef.webp">полный размер</a></sub><br><br>Change the light to a warm sunset glow raking across her skin from the window, keep the pose and the room, cinematic colour, 35mm film grain</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp" alt="Lingerie and hanger" width="230"></a></td><td valign="top"><b>Lingerie and hanger</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/5511ef893ad0395f.webp">полный размер</a></sub><br><br>Keep the woman, the bed and the hotel room exactly as they are. Change her outfit to a black lace bodysuit with sheer black stockings, and change the brass door hanger text to read &#x27;BACK AT MIDNIGHT&#x27;. Keep the same pose, framing, lighting and colour grade.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp" alt="Latex and neon" width="230"></a></td><td valign="top"><b>Latex and neon</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/0b8d123323790a2b.webp">полный размер</a></sub><br><br>Keep the rider, the motorcycle and the neon garage exactly as they are. Change her outfit to a glossy black latex bodysuit with a deep front zip and long gloves, add sheer black stockings, and change the neon sign on the back wall to read &#x27;AFTER HOURS&#x27;. Keep the same pose, framing, magenta and cyan lighting and colour grade.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp" alt="Midday to candlelit" width="230"></a></td><td valign="top"><b>Midday to candlelit</b><br><sub><code>alibaba/qwen-image-spicy-edit/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-spicy-edit/c6eb2b0782685ed4.webp">полный размер</a></sub><br><br>Keep the woman, her pose at the railing, the balcony, the iron rail and the geranium pots exactly as they are, and keep the same framing and camera angle. Change the time of day from hard midday sun to late night: the sky becomes deep blue-black with stars, the sea goes dark, and the whole scene is now lit only by a cluster of candles standing along the balcony rail, so warm amber candlelight rakes across her from below and everything else falls into deep shadow. Change her white cotton sundress to a black silk slip dress. Keep her face and body identical.</td></tr>
</table>

### Seedream 5.0 Lite

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/seedream-5-0-lite?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp" alt="Two refs poster size" width="230"></a></td><td valign="top"><b>Two refs poster size</b><br><sub><code>bytedance/seedream-5.0-lite/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/3fd75a8e556e62d1.webp">полный размер</a></sub><br><br>Cast: one man. Build one poster-shaped frame from these two references: the figure from the first, the location from the second, shot backlit and soaking wet so water traces the line of the body and the rim light does the rest. Cinematic, shallow depth of field, heavy film grain.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp" alt="Siren rocks strip" width="230"></a></td><td valign="top"><b>Siren rocks strip</b><br><sub><code>bytedance/seedream-5.0-lite/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-5.0-lite/b8735fe777c8eb31.webp">полный размер</a></sub><br><br>Cinematic film still, 21:9 ultra-wide. Close on the two of them: her scaled hip and his soaked shirt pressed together, water sheeting off both, her head tipped back. On black sea rocks a mermaid and a sailor are hit by the same breaking wave, scales and soaked cloth pressed together, both drenched; the horizon line runs the full width of the frame under a storm-lit sky. Lighthouse beam raking across the spray. 65mm anamorphic, heavy grain, storm green and pewter palette, restrained and tasteful.</td></tr>
</table>

### Qwen Image 2

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/alibaba-qwen-image-2?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp"><img src="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp" alt="Cyber alley bilingual" width="230"></a></td><td valign="top"><b>Cyber alley bilingual</b><br><sub><code>alibaba/qwen-image-2/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/alibaba-qwen-image-2/9944fb81c5b817b4.webp">полный размер</a></sub><br><br>Cinematic film still, rain-soaked cyberpunk alley at 3am. A woman stands behind a fogged shopfront window looking back over her shoulder; her thin white shirt is soaked through and clings to her shoulder blades, a faint glowing chrome port at the nape of her neck. Bilingual neon signage in Chinese and English reading 夜宵 NIGHT NOODLES and 义体维修 CHROME REPAIR throws hard magenta and cyan across the wet fabric and across the patch of condensation she has wiped clear with one palm. 35mm anamorphic, shallow depth of field, heavy film grain, teal and magenta palette, restrained and tasteful.</td></tr>
</table>

### Qwen Image 2512 LoRA

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/qwen-image-2512-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp"><img src="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp" alt="Storybook onsen" width="230"></a></td><td valign="top"><b>Storybook onsen</b><br><sub><code>alibaba/qwen-image-2512-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/qwen-image-2512-lora/37125836822ec18f.webp">полный размер</a></sub><br><br>storybook anime illustration of a gay couple, two rugged men in their mid thirties with stubble and broad shoulders, relaxing together at the edge of an outdoor hot spring at dusk, loose yukata open at the chest and slipping off their shoulders, one resting his head on the other&#x27;s shoulder, steam rising, lanterns glowing, soft pastel palette.</td></tr>
</table>

### Z-Image Spicy Pro

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><sub>Превью на GitHub не показано.<br><a href="https://spicyapi.ai/ru/models/z-image-spicy-pro?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">Смотреть на spicyapi.ai</a></sub></td><td valign="top"><b>Moon pool two silhouettes</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code></sub><br><br>Cast: one man and one woman. Cinematic film still, a moonlit spirit spring at night. Two wet silhouettes stand at the water&#x27;s edge in near-total backlight, reduced to pure outline, water tracking down the line of the waist; glowing sigils drift on the water surface and cast faint light upward. 65mm, shallow depth of field, heavy grain, moon silver and spirit cyan, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp" alt="High key pov" width="230"></a></td><td valign="top"><b>High key pov</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/f212667ed7d0360d.webp">полный размер</a></sub><br><br>First-person POV photograph from the foot of a bed: an adult woman reclining back against white pillows in an ivory silk slip, her bare legs stretched toward the camera in the foreground, red pedicure, a thin gold ankle chain, soft blown-out window light flooding the white sheets, minimal high-key composition, editorial portrait, 35mm.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp" alt="Garter product still" width="230"></a></td><td valign="top"><b>Garter product still</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/1cb429fdef1fd514.webp">полный размер</a></sub><br><br>Luxury product-advertising still, immaculate studio lighting, no logos. Cropped from ribs to mid-thigh: an adult woman&#x27;s hands rest on a black satin belt at her hip; she wears a matching black silk outfit and sheer stockings against a seamless charcoal backdrop. A single hard key light rakes across the satin, catching every fibre and the sheen of the stockings; a faceted crystal perfume bottle stands on a small plinth in the near foreground, in razor focus. Commercial editorial finish, deep shadow.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp" alt="Backlit curtain shadow" width="230"></a></td><td valign="top"><b>Backlit curtain shadow</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/fa9a364011f6e14c.webp">полный размер</a></sub><br><br>Photograph shot from inside a dark bedroom looking at a floor-to-ceiling gauzy linen curtain lit from behind by a cluster of candles on the floor. The silhouette of an adult woman is projected onto the fabric from the far side: she stands in profile, arms raised, a loose robe around her shoulders, hair loose. Only the soft dark shape and a warm amber rim read through the cloth — pure backlit shadow play. A second smaller silhouette of a candle flame flickers at the lower left, wax pooling on a saucer in the sharp near foreground. Deep black room, honey-gold glow through the weave, visible linen texture, faint smoke drifting. Vertical composition, 50mm, shallow focus on the fabric. No text, no logos.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp" alt="Full size portrait" width="230"></a></td><td valign="top"><b>Full size portrait</b><br><sub><code>alibaba/z-image-spicy-pro/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy-pro/61b5c56ad845ab07.webp">полный размер</a></sub><br><br>Editorial portrait, an adult woman in a sheer black slip standing against a bare plaster wall, single hard window light from camera right raking across the fabric, deep shadow filling the left of the frame, medium format film look, fine grain, cream and charcoal palette.</td></tr>
</table>

### Z-Image Spicy

<sub>🌶️ Spicy-версия · <a href="https://spicyapi.ai/ru/models/z-image-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp" alt="Leather studs low key" width="230"></a></td><td valign="top"><b>Leather studs low key</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/36b1a32feba49df3.webp">полный размер</a></sub><br><br>Cinematic portrait, low key. A man in a studded leather jacket worn open over bare skin, a single hard light from one side giving only half the body and dropping the rest to black; studs catch as small specular points. 85mm, shallow depth of field, heavy grain, black and oxblood palette, restrained and tasteful.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp" alt="Blind stripe boudoir" width="230"></a></td><td valign="top"><b>Blind stripe boudoir</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/2da39b210f7cb985.webp">полный размер</a></sub><br><br>Photograph of an adult woman lying on her side across rumpled white linen in a black lace bodysuit, morning sun through venetian blinds casting hard stripes across her skin and the sheets, one arm stretched above her head, eyes closed, calm and warm, medium format film look, soft grain, honey and cream palette.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp" alt="Fire escape dusk" width="230"></a></td><td valign="top"><b>Fire escape dusk</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/aa3ba7ea60addfbc.webp">полный размер</a></sub><br><br>35mm film photograph, warm grain and halation, Portra colour. An adult woman sits out on a Brooklyn fire escape at dusk in a black lace-trim slip and an unbuttoned men&#x27;s dress shirt, bare feet resting through the metal grating, an ashtray and a longneck beer beside her, head tipped back against the railing with her eyes closed. Brick wall, string lights, blue-hour sky, shallow focus.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp" alt="Own legs pov" width="230"></a></td><td valign="top"><b>Own legs pov</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/642b40ccba5d8d2f.webp">полный размер</a></sub><br><br>First-person point of view from a low chair looking down at my own crossed legs, morning sun cutting in through a tall window in hard bright stripes. Bare legs in sheer black lace-top stockings and black satin shorts, one foot in a slipper half hanging off the toes, a chipped ceramic coffee mug held between my knees, a book open on my thigh. Warm parquet floor, dust in the sunbeam, wide 24mm perspective, natural skin texture, 35mm colour film grain, unposed and lazy. Adult woman. No text, no logos.</td></tr>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp" alt="Expanded one liner" width="230"></a></td><td valign="top"><b>Expanded one liner</b><br><sub><code>alibaba/z-image-spicy/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-spicy/1585120b8cb8ed01.webp">полный размер</a></sub><br><br>Adult woman in a silk robe at a rain-streaked window, candlelight.</td></tr>
</table>

### Z-Image

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/z-image?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp" alt="Gym mirror selfie" width="230"></a></td><td valign="top"><b>Gym mirror selfie</b><br><sub><code>alibaba/z-image-turbo/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image/67dac9fb93f37737.webp">полный размер</a></sub><br><br>iPhone mirror selfie, an adult woman in a charcoal sports bra and low-slung grey joggers standing in an empty late-night gym, midriff bare, one hand holding the phone, hair damp, casual confident smirk, overhead fluorescent light, slight motion blur, authentic amateur snapshot look.</td></tr>
</table>

### Z-Image Turbo LoRA

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/z-image-turbo-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp"><img src="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp" alt="Realism rain window" width="230"></a></td><td valign="top"><b>Realism rain window</b><br><sub><code>alibaba/z-image-turbo-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/z-image-turbo-lora/d6887daba464dd40.webp">полный размер</a></sub><br><br>Realism, a beautiful mature woman in her early thirties with sharp cheekbones and red lipstick, wearing a low-cut black satin slip dress, sits on a window ledge at night, one strap slipping off her shoulder, rain on the glass, city lights blurred behind her, one knee drawn up, soft lamp light on her face, 35mm film grain.</td></tr>
</table>

### Seedream 4.0

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/seedream-4-0?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp"><img src="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp" alt="Coat street person merge" width="230"></a></td><td valign="top"><b>Coat street person merge</b><br><sub><code>bytedance/seedream-4.0/edit</code> · <a href="https://cdn.spicyapi.ai/models/examples/seedream-4.0/c70db7252425c84e.webp">полный размер</a></sub><br><br>Compose one frame from these three references: the woman from the first, wearing the long coat from the second, standing on the street from the third at night. Waist-up: the coat hangs open over a thin camisole and the streetlight behind drives straight through the fabric. The coat hangs open over a thin camisole and a streetlight behind her throws the light straight through the fabric. Cinematic, shallow depth of field, heavy film grain.</td></tr>
</table>

### Prefect Pony XL

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/prefect-pony-xl?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/prefect-pony-xl/67076d7e84936c95.webp"><img src="https://cdn.spicyapi.ai/models/examples/prefect-pony-xl/67076d7e84936c95.webp" alt="Silver knight" width="230"></a></td><td valign="top"><b>Silver knight</b><br><sub><code>prefect/pony-xl/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/prefect-pony-xl/67076d7e84936c95.webp">полный размер</a></sub><br><br>score_9, score_8_up, 1girl, solo, long white hair, ornate silver armor, red cape, holding a longsword, standing on castle ramparts at dawn, dramatic sky, full body, detailed armor</td></tr>
</table>

### FLUX.1 Dev LoRA

<sub>Стандартная модель, уровень в каталоге: unrestricted · <a href="https://spicyapi.ai/ru/models/flux-1-dev-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=showcase-ru">страница модели</a></sub>

<table>
<tr><td width="250" align="center" valign="top"><a href="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp"><img src="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp" alt="Mj mix red gown" width="230"></a></td><td valign="top"><b>Mj mix red gown</b><br><sub><code>black-forest-labs/flux-1-dev-lora/text-to-image</code> · <a href="https://cdn.spicyapi.ai/models/examples/flux-1-dev-lora/f5710c5884856f03.webp">полный размер</a></sub><br><br>MJ v6, editorial fashion photograph of a beautiful woman in a red satin gown with a plunging neckline and an open back, descending marble stairs and glancing over her bare shoulder, dramatic side light, glossy magazine look.</td></tr>
</table>


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

### Будуар и бельё

Самая надёжная категория NSFW image-to-video: один человек в кадре, мягкий свет, небольшие движения. Если вы новичок, начните отсюда.

#### B01 · Спальня в золотой час

```text
A woman in her late 20s in black lace lingerie slowly turns toward the camera in a dim bedroom. Warm light from a bedside lamp throws soft shadows across her skin. She runs her fingers through her long dark hair and arches her back slightly. Slow push-in from medium shot to close-up on her face. Shallow depth of field, cinematic color grade, light film grain.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b01-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Фото по пояс: взрослая женщина в чёрном кружевном белье, тёплый свет лампы, спальня на фоне.  
**Совет:** Модель сохраняет одежду из первого кадра, поэтому начинайте с кадра, где героиня уже в белье и в таком же тёплом свете.

#### B02 · Шёлковый халат с плеча

```text
Close-up of an adult woman's shoulder as an ivory silk robe slowly slides down her arm, revealing her bare shoulder. The fabric falls in slow motion and the camera follows it down. Warm amber candlelight, soft bokeh in the background, natural skin glow, shallow depth of field.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b02-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Плотный кадр плеча и ключицы, свободно наброшенный халат из шёлка цвета слоновой кости, свет свечей.  
**Совет:** Начните с халата, уже наполовину спущенного с одного плеча: модель продолжит движение, а не будет его придумывать.

#### B03 · Туалетный столик с зеркалом

```text
A woman in her 30s in sheer white lingerie sits at a vintage vanity, applying red lipstick while watching herself in an ornate mirror. She presses her lips together, then turns to the camera with a slow smile. Soft window light from the left, vintage film tone, 35mm look, shallow depth of field.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b03-ru) | 1080p · 5 s · 16:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая женщина за туалетным столиком, видно отражение, полупрозрачное бельё, мягкий свет из окна.  
**Совет:** Отражения держатся лучше на Wan 2.6 и Seedance, чем на бюджетных уровнях. Зеркало должно быть в первом кадре.

#### B04 · Красные атласные простыни

```text
An adult woman lies on her side across red satin sheets in a matching red lace bodysuit. She slowly stretches one arm above her head, lengthening her body. The camera dollies from her feet up along her figure in one smooth move. Deep crimson key light from one side, cool blue fill from the other, fashion editorial mood.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b04-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина лежит на красном атласе, красное кружевное боди, двухцветное освещение.  
**Совет:** Если назвать направление долли, получится чистое плавное движение. Палитра «красное на красном» рендерится хорошо.

#### B05 · Шампанское на шезлонге

```text
A woman in her 30s in a black velvet corset and stockings reclines on a chaise longue. She raises a champagne glass toward the camera so the liquid catches the light, takes a slow sip and holds eye contact with the lens. Warm tungsten light, dark moody background, film noir atmosphere.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b05-ru) | 1080p · 5 s · 16:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая женщина на кушетке с бокалом шампанского, корсет, низкий ключ.  
**Совет:** Реквизит ведёт себя лучше на Wan 2.6 или Seedance 2.0. Ограничьтесь одним жестом.

#### B06 · Балкон в сумерках

```text
A woman in her late 20s in a sheer black negligee stands on a balcony at twilight with blurred city lights behind her. A light breeze lifts the fabric and her hair. She leans on the railing and slowly looks back over her shoulder at the camera. Backlit rim light outlines her figure, anamorphic flare, atmospheric haze.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b06-ru) | 1080p · 5 s · 16:9 | $0.95 | Средний |

**Первый кадр:** Взрослая женщина со спины на балконе в сумерках, полупрозрачный пеньюар, боке ночного города.  
**Совет:** Ветер — одно из самых надёжных движений в любой видеомодели. Он оживляет кадр без риска для анатомии.

#### B07 · Кружево и жемчуг крупным планом

```text
Extreme close-up of a strand of pearls resting on an adult woman's collarbone above white lace. Her breathing makes the pearls rise and fall gently. Slow rack focus from the pearls to the lace edge. Soft high-key studio light, creamy tones, luxury beauty-ad feel.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b07-ru) | 720p · 5 s · 1:1 | $0.19 | Начальный |

**Первый кадр:** Макро: жемчуг на ключице и белое кружево, высокий ключ.  
**Совет:** Дыхание — самое надёжное движение. Макрокадр скрывает руки и лица, а это убирает большинство артефактов.

#### B08 · Чулок

```text
An adult woman sits on the edge of a bed and slowly draws a sheer black stocking up her leg, smoothing it with both hands. Low camera angle, slow tilt up following her hands. Warm bedroom light, shallow depth of field, soft film grain.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b08-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина сидит на кровати, один чулок надет, второй наполовину, нижний ракурс.  
**Совет:** Кадрируйте от колена и выше, чтобы руки оставались крупными и простыми.

#### B09 · Меховой ковёр у камина

```text
A woman in her 30s lies on a white fur rug in front of a crackling fireplace, wearing a cream silk slip. Firelight flickers across her skin as she rolls slowly onto her back and closes her eyes. Static camera, warm orange light, cosy winter-cabin mood.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b09-ru) | 720p · 5 s · 16:9 | $0.4105 | Начальный |

**Первый кадр:** Взрослая женщина на меховом ковре у камина, кремовая шёлковая комбинация, свет огня.  
**Совет:** Статичная камера и живой свет огня дают ощущение большого движения почти без риска.

#### B10 · Дождь за окном

```text
An adult woman in an oversized white shirt, unbuttoned low, sits on a window seat watching rain run down the glass. She draws her knees up and rests her chin on them, then glances at the camera. Cool blue daylight from the window, soft interior shadows, quiet melancholy mood, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b10-ru) | 720p · 8 s · 16:9 | $0.304 | Начальный |

**Первый кадр:** Взрослая женщина на подоконнике в расстёгнутой белой рубашке, окно в каплях дождя, холодный свет.  
**Совет:** LTX 2.3 Spicy дёшево делает длинные дубли; после 5 секунд держите действие медленным.

#### B11 · Спина: следящий кадр

```text
The camera tracks slowly down the bare back of an adult woman wearing only an open-back evening gown, from her neck to the small of her back. She shifts her weight and her shoulder blades move under the skin. Warm side light sculpts the spine, dark background, elegant and intimate.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b11-ru) | 720p · 5 s · 9:16 | $1.14 | Средний |

**Первый кадр:** Взрослая женщина со спины в платье с открытой спиной, тёплый боковой свет.  
**Совет:** Спина прощает ошибки анатомии и выглядит дорого. Seedance хорошо передаёт микродвижения кожи.

#### B12 · Атласная повязка на глаза

```text
An adult woman with a black satin blindfold kneels on white sheets in black lingerie. She tilts her head as if listening and a slow smile forms. Soft diffused light, high-contrast black and white palette, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b12-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина стоит на коленях на белых простынях, атласная повязка на глазах, чёрное бельё.  
**Совет:** Повязка полностью убирает артефакты глаз и добавляет кадру напряжения.

#### B13 · Только украшения

```text
Artistic portrait of a nude adult woman in her 30s lying on black velvet, covered only by layered gold necklaces and bracelets that catch the light. She slowly turns her wrist and the jewelry glints. Single overhead spotlight, deep shadows, luxurious editorial style, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b13-ru) | 1080p · 5 s · 3:4 | $2.85 | Продвинутый |

**Первый кадр:** Взрослая женщина на чёрном бархате с золотыми украшениями, верхний прожектор, тени закрывают тело.  
**Совет:** Подразумеваемая нагота с продуманными тенями выглядит дорого и проходит модерацию большего числа платформ при репосте.

#### B14 · Утреннее потягивание в постели

```text
Soft morning light pours through sheer curtains as a woman in her late 20s wakes in white sheets, wearing a loose camisole. She stretches both arms overhead, arches her back and smiles sleepily at the camera. Airy pastel tones, static camera, lifestyle film look.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b14-ru) | 768p · 5 s · 16:9 | $0.42 | Начальный |

**Первый кадр:** Взрослая женщина в белом постельном белье, в майке-камисоли, утренний свет из окна.  
**Совет:** MiniMax H3 хорошо делает естественные потягивания всем телом. Промпт для этой модели необязателен: часто хватает одного первого кадра.

#### B15 · Шнуровка корсета

```text
Close-up from behind as an adult woman tightens the ribbon laces of a black corset, pulling them in rhythmic tugs. Her waist draws in with each pull. Candlelit boudoir, warm tones, shallow depth of field, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b15-ru) | 720p · 5 s · 9:16 | $0.871 | Средний |

**Первый кадр:** Взрослая женщина со спины в частично зашнурованном чёрном корсете, свет свечей.  
**Совет:** Повторяющиеся движения рук допустимы, если руки остаются в одной области кадра.

#### B16 · Под шубой

```text
A woman in her 30s stands in a dark hotel corridor wearing a long faux-fur coat. She opens it slowly toward the camera to show black lingerie underneath, then lets it slip to her elbows. Warm practical wall sconces, glossy floor reflections, glamorous noir mood, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=b16-ru) | 1080p · 5 s · 9:16 | $0.7125 | Средний |

**Первый кадр:** Взрослая женщина в гостиничном коридоре в застёгнутой шубе из искусственного меха.  
**Совет:** Распахнуть одежду — одно предсказуемое движение. Цвет шубы должен отличаться от цвета белья.

### Художественное ню и файн-арт

Обнажённая натура как этюд с натуры: скульптурный свет, силуэты, классические позы. Хорошо работает на любой Spicy-модели, потому что движения минимальны.

#### F01 · Классическая Венера

```text
A nude adult woman reclines on draped white linen in the pose of a Renaissance Venus painting. She slowly turns her face toward the viewer. Soft north-window light, oil-painting color palette, gentle film grain, static camera, museum-quality composition.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f01-ru) | 1080p · 5 s · 16:9 | $2.85 | Средний |

**Первый кадр:** Обнажённая взрослая женщина полулежит на белой драпировке, свет как на классической картине.  
**Совет:** Название позы из истории искусства даёт модели сильную композиционную подсказку.

#### F02 · Игра теней

```text
Slatted light from window blinds falls across the bare back and shoulders of an adult woman standing in a dark room, seen from behind. She breathes slowly and turns a few degrees, so the stripes of light slide across her skin. High-contrast black and white, film noir, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f02-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина со спины в тёмной комнате, полосы света от жалюзи на спине, чёрно-белое изображение.  
**Совет:** Жёсткий рисунок света создаёт движение без движения тела. Отлично для дешёвых моделей.

#### F03 · Пейзаж тела

```text
Extreme close-up macro shot gliding slowly over the curves of an adult woman's hip and waist, lit so the skin looks like sand dunes at dusk. Warm raking light, abstract composition, ultra-shallow depth of field, slow lateral camera move.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f03-ru) | 1080p · 8 s · 21:9 | $0.456 | Средний |

**Первый кадр:** Абстрактное макро изгибов бедра и талии в тёплом скользящем свете.  
**Совет:** Абстрактный «пейзаж тела» не показывает ни лица, ни рук, поэтому почти не даёт артефактов.

#### F04 · Под водой

```text
A nude adult woman floats weightlessly underwater in a flowing white silk sheet. The fabric billows around her body as light rays pierce the surface above. Her hair drifts slowly. Ethereal blue-green tones, slow motion, dreamlike.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f04-ru) | 720p · 5 s · 9:16 | $1.14 | Продвинутый |

**Первый кадр:** Взрослая женщина под водой, обёрнутая белым шёлком, лучи света сверху.  
**Совет:** Движение под водой медленное по своей природе, и модели передают его изящно.

#### F05 · Стекающая краска

```text
Metallic gold paint drips slowly down the bare shoulders and back of an adult woman standing against a matte black backdrop. She rolls her shoulders and the paint streaks catch the studio light. Hard key light, glossy highlights, art-gallery aesthetic, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f05-ru) | 1080p · 5 s · 4:5 | $0.7125 | Средний |

**Первый кадр:** Спина взрослой женщины с золотыми мазками краски, чёрный фон.  
**Совет:** Жидкость, стекающая по коже, эффектна и надёжно получается на Wan 2.6.

#### F06 · Лесная нимфа

```text
A nude adult woman with ivy woven into her long hair stands in a misty forest clearing at dawn, partly hidden by ferns. She reaches up to touch a hanging branch. Shafts of sunlight through fog, soft greens and golds, fairy-tale mood, slow dolly-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f06-ru) | 720p · 5 s · 16:9 | $0.4105 | Начальный |

**Первый кадр:** Взрослая женщина в туманном лесу, папоротники на переднем плане, плющ в волосах.  
**Совет:** Листва на переднем плане заодно служит естественной цензурой для платформ, где она нужна.

#### F07 · Студийный этюд с натуры

```text
Classical figure study of a nude adult man in his 30s seated on a wooden stool in a photography studio, grey seamless backdrop. He slowly shifts his weight and turns his head toward the light. Single large softbox, sculpted muscle definition, black and white, locked-off camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ru/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f07-ru) | 1080p · 5 s · 3:4 | $0.26 | Начальный |

**Первый кадр:** Обнажённый взрослый мужчина на табурете, серый фон, один софтбокс, чёрно-белое изображение.  
**Совет:** У Seedance 1.5 Pro Spicy есть фиксация камеры — идеально для студийных этюдов.

#### F08 · Молочная ванна

```text
Top-down view of an adult woman lying in a milk bath scattered with pink rose petals, only her face, shoulders and hands above the surface. She slowly lifts one hand and the milk runs off her fingers. Soft diffused overhead light, pastel palette, dreamy beauty aesthetic.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f08-ru) | 720p · 5 s · 1:1 | $0.19 | Начальный |

**Первый кадр:** Кадр сверху: взрослая женщина в молочной ванне с лепестками роз.  
**Совет:** Непрозрачная поверхность молока естественно ограничивает видимое. Кадр сверху очень стабилен.

#### F09 · Силуэт и потягивание

```text
Full-body silhouette of an adult woman against a glowing orange sunset window. She raises her arms overhead and stretches slowly, her profile sharp against the light. No visible detail, pure shape and gradient, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f09-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Силуэт взрослой женщины на фоне окна с закатом, профиль.  
**Совет:** Силуэт читается как ню, ничего не показывая. Можно публиковать почти где угодно.

#### F10 · Песчаные дюны

```text
Wide shot of a nude adult woman walking slowly away from the camera across rippled golden sand dunes at sunset, a long sheer scarf trailing in the wind. Long shadows, warm gradient sky, epic cinematic scale, slow drone pull-back.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f10-ru) | 1080p · 5 s · 21:9 | $0.95 | Средний |

**Первый кадр:** Общий план: взрослая женщина со спины на песчаных дюнах, за ней развевается шарф.  
**Совет:** Уход от камеры — одно из самых безопасных движений в полный рост.

#### F11 · Мокрая кожа в студии

```text
Studio close-up of an adult man's shoulders and chest, skin misted with water droplets. He breathes deeply and droplets roll down slowly. Hard rim lights from both sides against black, high contrast, fitness editorial style, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f11-ru) | 1080p · 5 s · 3:4 | $2.85 | Средний |

**Первый кадр:** Плечи и грудь взрослого мужчины в каплях воды, контровой свет на чёрном фоне.  
**Совет:** Контровой свет на мокрой коже выглядит премиально и скрывает проблемы с текстурой.

#### F12 · Ткань соскальзывает

```text
An adult woman stands in a white studio wrapped in a long sheet of red chiffon. A fan off-camera slowly unwinds the fabric into the air around her, revealing her bare shoulders and back. Clean high-key light, vivid red against white, slow motion.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f12-ru) | 720p · 5 s · 9:16 | $0.4105 | Начальный |

**Первый кадр:** Взрослая женщина, обёрнутая красным шифоном, в белой студии.  
**Совет:** Упоминание вентилятора за кадром даёт модели физическую причину движения.

#### F13 · Дым и форма

```text
Coloured smoke in violet and teal curls slowly around the nude figure of an adult woman standing in a black studio, the smoke veiling her body as it drifts. She turns her head to watch it. Low-key light, surreal fashion-art mood, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f13-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина в чёрной студии в клубах цветного дыма.  
**Совет:** Дым — одно из самых надёжных движений и к тому же встроенная скромность.

#### F14 · Глина скульптора

```text
An adult couple in their 30s, both nude and partly covered in pale grey clay, sit back to back on a studio floor like a living sculpture. They breathe in unison and slowly lean their heads together. Soft top light, monochrome stone tones, locked-off camera, gallery installation feel.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ru/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=f14-ru) | 720p · 5 s · 16:9 | $0.13 | Средний |

**Первый кадр:** Двое взрослых спина к спине, покрытые серой глиной, пол студии, монохром.  
**Совет:** Кадр «спина к спине» чётко разделяет два тела.

### Пары и романтика

Двое взрослых по взаимному согласию. Сцены с двумя людьми сложнее: держите действие медленным, одевайте каждого в свой наряд или цвет и выбирайте боковые ракурсы.

#### C01 · Медленный танец в спальне

```text
An adult couple in their 30s slow dance barefoot in a candlelit bedroom. She wears a black slip dress, he wears an open white shirt. They sway together, foreheads touching, his hand on her lower back. Warm candlelight, soft focus, intimate romantic mood, slow orbit around them.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c01-ru) | 720p · 5 s · 16:9 | $1.14 | Средний |

**Первый кадр:** Взрослая пара обнимается в спальне при свечах, чёрное платье и белая рубашка.  
**Совет:** Одежда разных цветов помогает модели не смешивать два тела.

#### C02 · Поцелуй крупным планом

```text
Tight close-up of an adult couple, faces in profile, lips inches apart. They lean in slowly and share a soft, lingering kiss, her hand rising to his jaw. Golden backlight through her hair, shallow depth of field, romantic film look.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c02-ru) | 1080p · 5 s · 16:9 | $2.85 | Средний |

**Первый кадр:** Крупный план в профиль: взрослые мужчина и женщина вот-вот поцелуются, золотой контровой свет.  
**Совет:** Для поцелуев профиль гораздо стабильнее, чем фронтальный ракурс.

#### C03 · Объятия на пляже на закате

```text
An adult couple in swimwear stand waist-deep in the ocean at sunset, wrapped in each other's arms as gentle waves roll past. He kisses her shoulder and she tilts her head back and laughs. Warm orange and pink sky, sparkling water, slow drone push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c03-ru) | 1080p · 5 s · 21:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая пара обнимается в море на закате, по пояс в воде.  
**Совет:** Вода по пояс скрывает самые трудные для рендера зоны в сценах с двумя людьми.

#### C04 · Утро после

```text
Morning light through sheer curtains. An adult couple lies tangled in white sheets, her head on his bare chest. He slowly traces a finger along her arm and she smiles with her eyes closed. Soft airy tones, static camera, tender lifestyle mood.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c04-ru) | 768p · 5 s · 16:9 | $0.42 | Начальный |

**Первый кадр:** Взрослая пара лежит в белых простынях, её голова у него на груди, утренний свет.  
**Совет:** Небольшие движения рук у неподвижной пары гораздо надёжнее, чем движение всем телом.

#### C05 · Поцелуй в шею

```text
An adult man stands behind an adult woman in a dim loft and slowly kisses the side of her neck. She closes her eyes and leans back into him, her hand reaching up into his hair. Moody blue and amber lighting, shallow depth of field, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c05-ru) | 720p · 5 s · 9:16 | $1.14 | Средний |

**Первый кадр:** Взрослый мужчина за спиной взрослой женщины, его лицо у её шеи, приглушённый свет лофта.  
**Совет:** Мизансцена «он за её спиной» разводит лица и хорошо читается.

#### C06 · Ванна на двоих

```text
An adult couple relaxes in a large freestanding bathtub full of foam, she leans back against his chest. He pours warm water over her shoulder from his cupped hands. Candles around the tub, steam rising, warm golden tones, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c06-ru) | 1080p · 5 s · 16:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая пара в отдельно стоящей ванне с пеной, свечи, пар.  
**Совет:** Пена и пар одновременно помогают с непрерывностью и со скромностью кадра.

#### C07 · Молния на платье

```text
Close-up from behind: an adult man slowly draws down the zipper of an adult woman's emerald evening dress, the fabric parting to reveal her bare back. She glances over her shoulder at him. Warm lamp light, rich jewel tones, shallow depth of field.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c07-ru) | 720p · 5 s · 9:16 | $1.14 | Средний |

**Первый кадр:** Спина взрослой женщины в изумрудном платье, мужская рука на молнии.  
**Совет:** Кадрируйте молнию и спину. Две руки в одной небольшой области — предел для большинства моделей.

#### C08 · Силуэты в душе

```text
Behind a steamed-up glass shower door, the blurred silhouettes of an adult couple embrace under running water. Their shapes move slowly together as droplets streak down the glass. Soft warm backlight, heavy steam, intimate and suggestive, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c08-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Запотевшее стекло душа, за ним размытые очертания двух взрослых.  
**Совет:** Матовое стекло работает как цензура и полностью скрывает ошибки анатомии.

#### C09 · У стены

```text
In a narrow hallway lit by a single red neon sign, an adult man gently presses an adult woman against the wall, their foreheads touching. She pulls him closer by his collar. Red and blue neon, deep shadows, cinematic tension, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c09-ru) | 720p · 5 s · 16:9 | $0.871 | Средний |

**Первый кадр:** Взрослая пара в неоновом коридоре, женщина у стены, касаются лбами.  
**Совет:** Контраст неоновых цветов помогает модели разделить две фигуры.

#### C10 · На руках в постель

```text
An adult man carries an adult woman in his arms through a moonlit bedroom and gently lays her down on the bed. She keeps her arms around his neck and pulls him down with her. Cool moonlight through tall windows, soft shadows, romantic cinematic mood, tracking shot.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/ru/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c10-ru) | 720p · 5 s · 16:9 | $2.16 | Продвинутый |

**Первый кадр:** Взрослый мужчина несёт взрослую женщину на руках в спальне в лунном свете.  
**Совет:** Поднять и нести — продвинутое движение. Лучше всего вес и контакт передаёт Seedance 2.5 Spicy.

#### C11 · Смятые простыни

```text
Overhead shot of an adult couple lying tangled in rumpled grey silk sheets, hands intertwined above their heads. Their chests rise and fall slowly and the sheet shifts. Soft window light, muted editorial palette, static overhead camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c11-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Вид сверху: взрослая пара на серых шёлковых простынях, пальцы переплетены.  
**Совет:** Кадр сверху сглаживает глубину и стабилизирует сцены с двумя людьми.

#### C12 · Массажное масло

```text
An adult woman lies face-down on a massage table draped in a white towel while an adult man pours warm oil into his palm and slowly glides his hands up her back. Warm spa lighting, candles, glossy skin highlights, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c12-ru) | 768p · 5 s · 16:9 | $0.42 | Начальный |

**Первый кадр:** Взрослая женщина лежит лицом вниз на массажном столе, мужские руки над её спиной.  
**Совет:** Руки на спине — простое повторяемое движение с низким риском артефактов.

#### C13 · Две женщины при свечах

```text
Two adult women in their late 20s, one in black lace and one in white satin, sit face to face on a velvet sofa. One slowly brushes the other's hair behind her ear and they share a soft smile before leaning in. Warm candlelight, rich burgundy tones, intimate mood, slow orbit.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c13-ru) | 720p · 5 s · 16:9 | $1.14 | Средний |

**Первый кадр:** Две взрослые женщины на бархатном диване, одна в чёрном кружеве, другая в белом атласе.  
**Совет:** Контрастная одежда (чёрное и белое) сохраняет внешность каждой на протяжении всего ролика.

#### C14 · Ночь на крыше

```text
Two adult men in their 30s lean against a rooftop railing at night, city skyline glittering behind them. One loosens the other's tie and pulls him into a slow kiss. Cool blue night tones with warm city bokeh, gentle breeze, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=c14-ru) | 1080p · 5 s · 16:9 | $0.95 | Средний |

**Первый кадр:** Двое взрослых мужчин ночью на крыше, позади панорама города.  
**Совет:** Держите руки на деталях одежды — галстуке или воротнике, — чтобы движение было чистым и понятным.

### Сольные выступления и танец

Ритм и движение тела. Берите модели с сильной динамикой (Seedance, MiniMax H3) и делайте ролики короткими.

#### D01 · Вращение на пилоне

```text
An adult pole dancer in her late 20s in a sparkling bikini spins slowly around a chrome pole on a small stage, hair flowing out behind her. Magenta and violet stage lights, haze, reflections on the pole, low-angle static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d01-ru) | 720p · 5 s · 9:16 | $1.14 | Продвинутый |

**Первый кадр:** Взрослая танцовщица на пилоне держится за хромированный шест, сценический свет, нижний ракурс.  
**Совет:** Вращение — продвинутое движение. Seedance 2.0 и 2.5 лучше всего сохраняют согласованность конечностей.

#### D02 · Чувственный партер

```text
An adult dancer in a black bodysuit performs slow floor choreography on a glossy black stage, rolling from her side onto her knees and arching back. Single spotlight from above, haze, contemporary dance film aesthetic, slow lateral camera move.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d02-ru) | 720p · 5 s · 16:9 | $1.14 | Продвинутый |

**Первый кадр:** Взрослая танцовщица на глянцевой чёрной сцене в чёрном боди, прожектор.  
**Совет:** Называйте точную последовательность положений. Расплывчатое «танцует» даёт случайные конечности.

#### D03 · Волна телом

```text
A woman in her 20s in a cropped top and high-waisted shorts performs a slow body wave from chest to hips, facing the camera, in a neon-lit apartment. Pink and blue neon, music-video look, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d03-ru) | 768p · 5 s · 9:16 | $0.42 | Средний |

**Первый кадр:** Взрослая женщина лицом к камере в квартире с неоном, кроп-топ и шорты.  
**Совет:** Одно названное танцевальное движение работает гораздо лучше, чем целая хореография.

#### D04 · Танец у зеркала

```text
An adult woman in lingerie dances slowly in front of a full-length mirror, swaying her hips and running her hands down her sides while watching her reflection. Warm bedroom lamp light, soft shadows, handheld camera feel.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d04-ru) | 1080p · 5 s · 9:16 | $0.7125 | Средний |

**Первый кадр:** Взрослая женщина в белье перед зеркалом в полный рост.  
**Совет:** Добавьте зеркало в первый кадр, чтобы модели было что анимировать в отражении.

#### D05 · Танец со стулом

```text
An adult performer in a tuxedo jacket and heels sits backwards on a wooden chair on a dark stage, rolls her shoulders and slowly leans back, tipping her hat toward the camera. Single hard spotlight, cabaret mood, film grain, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d05-ru) | 720p · 5 s · 9:16 | $0.871 | Средний |

**Первый кадр:** Взрослый исполнитель на развёрнутом спинкой вперёд стуле, смокинг и шляпа, прожектор.  
**Совет:** Реквизит вроде стула или шляпы закрепляет движение и уменьшает дрейф.

#### D06 · Пиджак падает

```text
An adult man in his 30s in a fitted black suit jacket over a bare chest stands under a spotlight and slowly slides the jacket off his shoulders, letting it fall to the floor. Smoky stage, amber light, confident smirk at the camera, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d06-ru) | 720p · 5 s · 9:16 | $1.14 | Средний |

**Первый кадр:** Взрослый мужчина в пиджаке на голое тело, прожектор, сцена в дыму.  
**Совет:** Снять один верхний слой — ясное одиночное движение, с которым модели справляются надёжно.

#### D07 · Примерка белья

```text
In a softly lit dressing room, an adult woman in a new pink lace set turns slowly in front of a mirror, checking her reflection over her shoulder and adjusting a strap. Warm vanity bulbs, pastel tones, lifestyle creator-content look, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d07-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина в розовом кружевном комплекте в гримёрке с лампами у зеркала.  
**Совет:** Отличный формат для промо авторов. Поправить бретельку — небольшое и надёжное движение руки.

#### D08 · Перекат на кровати

```text
An adult woman in a white lace bodysuit rolls slowly from her stomach onto her back across a large bed, her hair spreading across the pillow, and looks up at the camera. Soft overhead light, clean white bedding, static overhead camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d08-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Вид сверху: взрослая женщина лежит лицом вниз на белой кровати.  
**Совет:** Ракурс сверху превращает перекат в плоское, хорошо читаемое движение.

#### D09 · Взгляд в полотенце

```text
An adult woman stands in a steamy bathroom wrapped in a white towel, her hair wet. She looks over her shoulder at the camera, smiles, and pulls the towel snug around her. Warm diffused light, steam, from behind, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d09-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина со спины в белом полотенце, ванная в пару.  
**Совет:** Съёмка со спины упрощает движение и анатомию.

#### D10 · Походка на каблуках

```text
An adult woman in black lingerie, stockings and stiletto heels walks slowly toward the camera down a dim hotel corridor, hips swaying, holding eye contact. Warm sconce lights, glossy floor reflections, low-angle tracking shot moving backward.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d10-ru) | 720p · 5 s · 9:16 | $0.4105 | Начальный |

**Первый кадр:** Взрослая женщина в белье и на каблуках в конце гостиничного коридора.  
**Совет:** Шаг к камере — одно из самых надёжных движений в полный рост.

#### D11 · Волосы на ветру

```text
Close-up of an adult woman in a sheer black top on a windy beach at sunset. She throws her head back and flips her long hair, laughing, as the wind catches it. Golden backlight, lens flare, slow motion.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d11-ru) | 768p · 5 s · 9:16 | $0.42 | Начальный |

**Первый кадр:** Крупный план: взрослая женщина на пляже на закате, полупрозрачный топ, длинные волосы.  
**Совет:** Волосы и ветер — движения высшей надёжности для любой модели.

#### D12 · Йога-поток

```text
An adult woman in minimal sportswear moves slowly from downward dog into cobra pose on a mat in a sunlit loft studio. Controlled, fluid motion, soft morning light, clean minimalist interior, static side-on camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d12-ru) | 1080p · 5 s · 16:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая женщина на коврике для йоги в позе собаки мордой вниз, вид сбоку, солнечный лофт.  
**Совет:** Камера сбоку и названные позы йоги делают конечности предсказуемыми.

#### D13 · Кабаре с веерами

```text
A burlesque performer in her 30s on a red-curtained stage slowly opens and closes two large white feather fans, revealing glimpses of a sequined costume beneath. Warm spotlight, glittering particles in the air, vintage cabaret mood, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d13-ru) | 1080p · 5 s · 16:9 | $0.95 | Средний |

**Первый кадр:** Взрослая исполнительница бурлеска на сцене с красным занавесом держит веера из перьев.  
**Совет:** Перья и веера дают сильное движение без движения тела.

#### D14 · Танцпол в клубе

```text
An adult woman in a metallic mini dress dances on a crowded nightclub floor, arms raised, head tilted back, strobe lights flashing. Green and magenta lasers, haze, handheld camera, music-video energy.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=d14-ru) | 720p · 5 s · 9:16 | $0.871 | Средний |

**Первый кадр:** Взрослая женщина в платье с металлическим отливом на танцполе клуба, лазеры.  
**Совет:** Seedance 2.0 Fast Spicy генерирует звук, так что ролик получается с атмосферой клуба.

### Ванна, душ и вода

Вода, пар и мокрая кожа добавляют реализма. Статичная или медленная камера сохраняет правдоподобную физику воды.

#### W01 · Душ в пару

```text
An adult woman stands under a rainfall shower, eyes closed, water streaming over her hair and bare shoulders as she runs her hands back through her wet hair. Dense steam, warm light behind her, glass wall with droplets, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w01-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Взрослая женщина под тропическим душем, от плеч и выше, пар.  
**Совет:** Струи воды и пар очень надёжны. Держите камеру неподвижной.

#### W02 · Роскошная ванна с пеной

```text
An adult woman relaxes in a clawfoot tub overflowing with foam in a marble bathroom, holding a glass of wine. She lifts one leg slowly out of the bubbles and foam slides down it. Candles, warm golden light, luxury lifestyle mood, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w02-ru) | 720p · 5 s · 16:9 | $0.4105 | Начальный |

**Первый кадр:** Взрослая женщина в ванне на ножках с пеной и бокалом вина, мраморная ванная.  
**Совет:** Пена скрывает тело и даёт медленное, приятное глазу движение.

#### W03 · Выход из бассейна

```text
An adult woman in a white swimsuit climbs out of a turquoise infinity pool, water streaming off her body, and slicks her wet hair back with both hands. Bright midday sun, sparkling water, luxury villa background, low-angle static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w03-ru) | 1080p · 5 s · 16:9 | $2.85 | Средний |

**Первый кадр:** Взрослая женщина у края бассейна-инфинити в белом купальнике.  
**Совет:** Вода, стекающая по коже, показывает физику Seedance во всей красе.

#### W04 · Сцена под дождём

```text
An adult woman in a soaked white shirt stands in the rain on an empty city street at night, face turned up to the sky, eyes closed. Rain pours over her, neon reflections shimmer on the wet asphalt. Cinematic blue and pink tones, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w04-ru) | 1080p · 5 s · 16:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая женщина в мокрой белой рубашке ночью на дождливой неоновой улице.  
**Совет:** Дождь и неоновые отражения сильно поднимают продакшн-уровень.

#### W05 · Водопад

```text
An adult woman stands waist-deep in a jungle pool beneath a small waterfall, water cascading over her shoulders and back. She tilts her head back into the stream. Lush green foliage, shafts of sunlight, mist, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w05-ru) | 1080p · 5 s · 16:9 | $0.95 | Средний |

**Первый кадр:** Взрослая женщина со спины под водопадом в джунглях, по пояс в воде.  
**Совет:** Вода по пояс — простой естественный кроп.

#### W06 · Масло и солнце

```text
An adult woman lying on a sun lounger slowly smooths tanning oil over her shoulders and arms, skin glistening in bright afternoon sun. Poolside setting, palm shadows, warm saturated colours, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w06-ru) | 768p · 5 s · 9:16 | $0.42 | Начальный |

**Первый кадр:** Взрослая женщина на шезлонге у бассейна, бикини, яркое солнце.  
**Совет:** Глянцевая кожа и жёсткое солнце сразу дают реализм.

#### W07 · Океанские волны

```text
Wide shot of an adult woman in a white linen wrap lying on wet sand at the waterline as gentle waves wash over her legs and recede. Blue hour light, soft pastel sky, long exposure feel, slow drone descent.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w07-ru) | 1080p · 8 s · 21:9 | $0.456 | Начальный |

**Первый кадр:** Общий план: взрослая женщина лежит у кромки воды, синий час.  
**Совет:** LTX недорого передаёт длинное, спокойное природное движение.

#### W08 · Ночь в горячей купели

```text
An adult woman relaxes in a steaming outdoor hot tub on a snowy mountain deck at night, arms resting on the edge. Snow falls softly, she tilts her head back and exhales a cloud of breath. Warm underwater lights, cold blue surroundings, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w08-ru) | 720p · 5 s · 16:9 | $0.871 | Начальный |

**Первый кадр:** Взрослая женщина в уличной горячей купели, заснеженная терраса ночью.  
**Совет:** Контраст снега и пара делает сильный кадр для превью.

#### W09 · Вечер в онсэне

```text
An adult woman in her 30s sits in a steaming Japanese outdoor onsen surrounded by rocks and maple trees, a folded towel on her head. She lifts water in her cupped hands and lets it pour over her shoulder. Soft evening light, lanterns, steam, locked-off camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ru/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w09-ru) | 720p · 5 s · 16:9 | $0.13 | Начальный |

**Первый кадр:** Взрослая женщина в открытом онсэне среди камней и клёнов, пар.  
**Совет:** Фиксация камеры в Seedance 1.5 Pro идеальна для спокойных сцен в купальне.

#### W10 · Двое в стеклянном душе

```text
Inside a modern glass shower, an adult couple stands under the water facing each other, her hands on his chest. He brushes wet hair from her face. Warm light, steam, water droplets on glass in the foreground, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=w10-ru) | 1080p · 5 s · 9:16 | $0.7125 | Средний |

**Первый кадр:** Взрослая пара в стеклянной душевой лицом друг к другу, пар.  
**Совет:** Капли на стекле на переднем плане смягчают картинку и скрывают мелкие ошибки.

### Фэнтези, научная фантастика и косплей

Взрослые фэнтезийные персонажи. Основную работу делают костюмы и эффекты; описывайте по одному магическому или технологическому элементу за раз.

#### X01 · Тёмная эльфийка-чародейка

```text
An adult dark elf sorceress with silver hair and pointed ears stands in a ruined temple, wearing a revealing black leather and silver armour set. Violet magic swirls around her hands as she raises them. Candles, floating embers, dark fantasy art style, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x01-ru) | 1080p · 5 s · 16:9 | $2.85 | Средний |

**Первый кадр:** Взрослая тёмная эльфийка в откровенных доспехах в разрушенном храме.  
**Совет:** Один магический эффект за раз сохраняет кадр читаемым.

#### X02 · Суккуб раскрывает крылья

```text
An adult succubus with curved horns and a slender tail stands in a red-lit gothic chamber in black lingerie. Her dark wings slowly unfurl behind her and she smiles at the camera. Crimson and black palette, smoke, dramatic backlight.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x02-ru) | 1080p · 5 s · 9:16 | $0.95 | Средний |

**Первый кадр:** Взрослая суккуб со сложенными крыльями в красном готическом зале.  
**Совет:** Раскрывающиеся крылья — одно крупное движение, которое модели хорошо рендерят.

#### X03 · Королева-воительница

```text
An adult warrior queen in her 30s in minimal bronze armour and a fur cape stands on a cliff above a battlefield at dawn. Wind whips her cape and hair as she raises her sword. Epic fantasy lighting, dust, cinematic low-angle shot.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x03-ru) | 720p · 5 s · 16:9 | $1.14 | Средний |

**Первый кадр:** Взрослая воительница в бронзовых доспехах и меховом плаще на утёсе.  
**Совет:** Плащ на ветру даёт большое движение, пока тело остаётся неподвижным.

#### X04 · Киберпанк-клуб

```text
An adult cyberpunk dancer with glowing circuit tattoos and a holographic bodysuit dances slowly on a neon stage in a futuristic club. Holograms flicker around her. Cyan and magenta neon, rain on the window behind, blade-runner mood.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x04-ru) | 720p · 5 s · 9:16 | $0.871 | Средний |

**Первый кадр:** Взрослая киберпанк-танцовщица со светящимися татуировками на неоновой сцене.  
**Совет:** Светящиеся детали (татуировки, голограммы) хорошо анимируются и выглядят эффектно.

#### X05 · Русалка у поверхности

```text
An adult mermaid with long red hair rises from a moonlit sea and rests her arms on a rock, water streaming from her bare shoulders. Her iridescent tail flicks behind her. Silver moonlight, gentle waves, fantasy realism.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x05-ru) | 1080p · 5 s · 16:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая русалка отдыхает на камне в море под луной.  
**Совет:** Длинные волосы, закрывающие грудь, — классический естественный кроп.

#### X06 · Трон королевы драконов

```text
An adult queen in a sheer golden gown lounges on an obsidian throne. A small dragon curls around the throne and breathes a thin ribbon of fire into the air as she strokes its head. Torchlight, gold and black palette, epic fantasy cinematography.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.5 Spicy](https://spicyapi.ai/ru/models/seedance-2-5-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x06-ru) | 720p · 5 s · 16:9 | $2.16 | Продвинутый |

**Первый кадр:** Взрослая королева на обсидиановом троне с маленьким драконом.  
**Совет:** Взаимодействие существа и человека — продвинутый уровень. Seedance 2.5 Spicy сохраняет согласованность обоих.

#### X07 · Пин-ап на космической станции

```text
An adult astronaut in a half-unzipped white flight suit floats weightlessly by a large window on a space station, Earth glowing below. Her hair drifts in zero gravity and she smiles at the camera. Cool blue light, retro sci-fi pin-up feel.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x07-ru) | 768p · 5 s · 16:9 | $0.42 | Начальный |

**Первый кадр:** Взрослая женщина в наполовину расстёгнутом лётном комбинезоне у иллюминатора космической станции.  
**Совет:** Невесомость объясняет «плавающее» движение и скрывает неловкую физику.

#### X08 · Соблазнение вампирши

```text
An adult vampire countess in a low-cut crimson velvet gown descends a candlelit stone staircase in a gothic castle, trailing her fingers along the banister. She pauses and smiles, a hint of fangs. Candlelight, deep reds and blacks, gothic horror romance.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x08-ru) | 720p · 5 s · 16:9 | $1.14 | Средний |

**Первый кадр:** Взрослая вампирша в багровом платье на готической лестнице.  
**Совет:** Лестница даёт естественное, удобное для камеры движение к объективу.

#### X09 · Богиня весны

```text
An adult goddess with flowers woven into her hair stands in a sunlit meadow, draped only in trailing vines and petals. Blossoms burst open around her as she lifts her arms. Soft golden light, floating pollen, painterly fantasy style.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x09-ru) | 1080p · 5 s · 16:9 | $0.95 | Начальный |

**Первый кадр:** Взрослая женщина на лугу, обвитая лозами и цветами.  
**Совет:** Лепестки и цветы — мягкие частицы, которые модели легко анимируют.

#### X10 · Фотосессия косплея

```text
An adult cosplayer in her 20s in a fitted black catsuit with cat ears poses in a photo studio, turning her hips and looking over her shoulder at the camera. Coloured gel lights in pink and blue, studio flashes firing, behind-the-scenes vibe.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x10-ru) | 720p · 5 s · 9:16 | $0.4105 | Начальный |

**Первый кадр:** Взрослая косплеерша в кэтсьюте с кошачьими ушками, студия с цветными гелями.  
**Совет:** Кадр «за кулисами» делает движения при позировании естественными.

#### X11 · Пробуждение андроида

```text
An adult female android with a seamless white synthetic body and faint blue seams lies on a lab table. Her eyes open, blue light pulses along the seams, and she slowly sits up. Clean white lab, cool light, sci-fi film look, slow push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x11-ru) | 1080p · 5 s · 16:9 | $2.85 | Средний |

**Первый кадр:** Взрослая женщина-андроид на белом лабораторном столе, глаза закрыты.  
**Совет:** Панели синтетической кожи читаются как sci-fi и обходят проблемы реализма.

#### X12 · Маскарад

```text
At a candlelit Venetian masquerade, an adult woman in a gold lace mask and a low-backed black gown turns from a crowd of masked guests and walks toward the camera. Rich gold and black palette, candle bokeh, baroque interior, slow dolly back.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=x12-ru) | 1080p · 5 s · 16:9 | $0.7125 | Средний |

**Первый кадр:** Взрослая женщина в золотой кружевной маске и чёрном платье на маскараде.  
**Совет:** Маски скрывают артефакты лица и добавляют загадки.

### Аниме и хентай-стиль

Все персонажи здесь явно нарисованы взрослыми. Сгенерируйте первый кадр в Qwen Image 2.1 LoRA с аниме-LoRA, затем анимируйте в Vidu Q3 Spicy или Wan 2.2 Spicy.

#### A01 · Ночь в онсэне (аниме)

```text
Anime style. An adult woman in her 20s with long purple hair relaxes in a steaming outdoor hot spring at night, a towel wrapped around her. Steam drifts, cherry petals fall onto the water, she smiles and closes her eyes. Soft lantern light, clean cel shading.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a01-ru) | 720p · 5 s · 16:9 | $0.7125 | Начальный |

**Первый кадр:** Аниме: взрослая женщина ночью в онсэне с полотенцем, фонари.  
**Совет:** Vidu Q3 Spicy хорошо справляется с аниме-движением; для спокойных сцен уменьшайте movement_amplitude.

#### A02 · Пляжная серия

```text
Anime style. An adult woman with short blonde hair in a red bikini runs along the shoreline in slow motion, splashing water, hair bouncing. Bright summer sky, sparkling sea, vibrant colours, classic anime beach-episode framing.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a02-ru) | 720p · 5 s · 16:9 | $0.7125 | Начальный |

**Первый кадр:** Аниме: взрослая женщина в красном бикини на пляже.  
**Совет:** Дизайн персонажей должен быть явно взрослым: взрослые пропорции, взрослое лицо, указанный возраст.

#### A03 · Магическое превращение

```text
Anime style. An adult sorceress spins as ribbons of pink light wrap around her body and form an elegant, revealing magical gown. Sparkles burst around her, hair lifts upward, dramatic transformation sequence, glowing background.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a03-ru) | 1080p · 5 s · 9:16 | $0.76 | Средний |

**Первый кадр:** Аниме: взрослая чародейка в середине вращения, ленты света.  
**Совет:** Превращения — это движение лент и частиц, которое аниме-модели делают хорошо.

#### A04 · Спальня вайфу

```text
Anime style. An adult woman with long silver hair lies on her side on a bed in an oversized shirt, propped on one elbow. She blinks slowly and gives a soft smile to the camera, curtains moving in the breeze. Warm afternoon light, detailed anime background.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a04-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Аниме: взрослая женщина лежит на кровати в оверсайз-рубашке.  
**Совет:** Небольшие движения лица на аниме-кадрах очень стабильны на Wan 2.2 Spicy.

#### A05 · Танец королевы демонов

```text
Anime style. An adult demon queen with horns, red eyes and a black lace outfit dances slowly in a throne room, her tail swaying. Purple fire flickers in braziers, dark fantasy anime aesthetic, dramatic lighting.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a05-ru) | 720p · 5 s · 9:16 | $0.7125 | Средний |

**Первый кадр:** Аниме: взрослая королева демонов в чёрном кружевном наряде в тронном зале.  
**Совет:** Хвост и волосы добавляют движения без сложной хореографии.

#### A06 · Этти в невесомости

```text
Anime style. An adult space pilot in a skin-tight flight suit floats in a spaceship cabin, her long hair drifting in zero gravity. She stretches lazily and smiles. Soft blue interior lights, stars through the window, sci-fi anime style.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a06-ru) | 720p · 5 s · 16:9 | $0.7125 | Начальный |

**Первый кадр:** Аниме: взрослая женщина в лётном комбинезоне парит в каюте космического корабля.  
**Совет:** Невесомость делает «плавающее» аниме-движение намеренным.

#### A07 · Банщица

```text
Anime style. An adult woman in a loose summer yukata kneels by a steaming wooden bath and pours water from a wooden ladle. The yukata slips slightly off one shoulder. Warm lantern light, steam, traditional Japanese interior.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a07-ru) | 720p · 5 s · 16:9 | $0.19 | Начальный |

**Первый кадр:** Аниме: взрослая женщина в юкате стоит на коленях у деревянной купели.  
**Совет:** Традиционные интерьеры с паром прощают ошибки и создают атмосферу.

#### A08 · Ночной визит суккуба

```text
Anime style. An adult succubus with bat wings perches on a moonlit window sill, her tail curling. She slowly leans forward toward the camera with a playful smile. Blue moonlight, pink rim light, gothic anime aesthetic.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a08-ru) | 720p · 5 s · 9:16 | $0.7125 | Средний |

**Первый кадр:** Аниме: взрослая суккуб на подоконнике в лунном свете.  
**Совет:** Наклон к камере создаёт близость при минимальном движении.

#### A09 · Хостес мейд-кафе

```text
Anime style. An adult woman in her 20s in a classic black and white maid outfit with a short skirt bows slightly, then winks at the camera while holding a tray. Pastel cafe interior, soft lighting, cheerful anime style.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a09-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Аниме: взрослая женщина в костюме горничной с подносом, интерьер кафе.  
**Совет:** Для каждого аниме-персонажа указывайте взрослый возраст и используйте взрослые пропорции в первом кадре.

#### A10 · Неоновая крыша (аниме)

```text
Anime style. An adult woman in a cropped leather jacket and bodysuit stands on a rooftop in a neon city at night, the wind blowing her hair. She turns and looks back at the camera. Pink and cyan neon, rain, detailed cyberpunk anime background.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Vidu Q3 Spicy](https://spicyapi.ai/ru/models/vidu-q3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=a10-ru) | 1080p · 5 s · 16:9 | $0.76 | Средний |

**Первый кадр:** Аниме: взрослая женщина ночью на неоновой крыше, кожаная куртка.  
**Совет:** Ветер и поворот головы — два самых надёжных движения в аниме.

### Реклама и чувственность без риска для бренда

Эстетика рекламы белья, купальников и парфюма для взрослых брендов и промо авторов. Намёк, а не откровенность, поэтому подходит и для платформ со строгими правилами.

#### M01 · Ролик бренда белья

```text
High-end lingerie commercial. An adult model in an ivory silk and lace set walks slowly across a sunlit Parisian apartment and stops by the window, turning to camera. Clean luxury aesthetic, soft daylight, subtle camera glide, magazine-grade color.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m01-ru) | 1080p · 5 s · 9:16 | $2.85 | Средний |

**Первый кадр:** Взрослая модель в белье цвета слоновой кости в светлой парижской квартире.  
**Совет:** Язык премиальной рекламы («commercial», «magazine-grade») поднимает общий уровень картинки.

#### M02 · Реклама парфюма

```text
Luxury perfume advertisement. An adult woman in a flowing black satin dress closes her eyes as golden light and slow-motion mist swirl around her bare shoulders. A glass perfume bottle glints in the foreground. Dreamy, sensual, high-fashion color grade.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.7 Spicy](https://spicyapi.ai/ru/models/wan-2-7-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m02-ru) | 1080p · 5 s · 16:9 | $0.95 | Средний |

**Первый кадр:** Взрослая женщина в чёрном атласе, флакон духов на переднем плане.  
**Совет:** Wan 2.7 Spicy может добавить сгенерированный звук для ощущения готовой рекламы.

#### M03 · Каталог купальников: поворот

```text
E-commerce swimwear video. An adult model in a one-piece swimsuit turns slowly 360 degrees on a white studio cyclorama to show the fit from all sides. Even soft lighting, clean white background, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m03-ru) | 720p · 5 s · 9:16 | $0.4105 | Начальный |

**Первый кадр:** Взрослая модель в слитном купальнике на белой циклораме.  
**Совет:** Медленный полный поворот — стандартный формат для товара, и он надёжно рендерится.

#### M04 · За кадром будуарной съёмки

```text
Behind-the-scenes of a boudoir photoshoot. An adult woman in a black bodysuit poses on a bed while a softbox flashes. She laughs between poses and shifts into a new position. Warm studio light, candid documentary feel, handheld camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m04-ru) | 768p · 5 s · 16:9 | $0.42 | Начальный |

**Первый кадр:** Взрослая женщина позирует на кровати, в кадре виден софтбокс, будуарная площадка.  
**Совет:** Кадр «за кулисами» делает неидеальное движение достоверным.

#### M05 · Обложка журнала

```text
Living magazine cover. An adult model in an oversized black blazer over a black lace bralette holds a confident pose against a bold red backdrop, then slowly turns her chin toward the camera. Hard fashion light, glossy editorial finish, static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m05-ru) | 1080p · 5 s · 3:4 | $2.85 | Средний |

**Первый кадр:** Взрослая модель в чёрном оверсайз-блейзере на красном фоне, редакционный свет.  
**Совет:** Минимальное движение на сильном статичном кадре — это и есть эффект «синемаграфа».

#### M06 · Презентация фитнес-бренда

```text
Fitness apparel ad. An adult athlete in a sports bra and leggings finishes a set, towels sweat from her neck and smiles at the camera. Gritty gym, hard top light, glistening skin, energetic handheld camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Fast Spicy](https://spicyapi.ai/ru/models/seedance-2-0-fast-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m06-ru) | 720p · 5 s · 9:16 | $0.871 | Начальный |

**Первый кадр:** Взрослая спортсменка в спортивном топе в суровом спортзале.  
**Совет:** Seedance 2.0 Fast Spicy добавляет звук — удобно для рекламы в соцсетях.

#### M07 · Промо гостиничного люкса

```text
Luxury hotel promo. The camera glides through a penthouse suite at dusk, past a champagne bucket, to an adult woman in a silk robe standing at the floor-to-ceiling window over the city. She turns and raises her glass. Warm interior light, city lights, smooth gimbal move.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m07-ru) | 1080p · 10 s · 16:9 | $1.425 | Средний |

**Первый кадр:** Пентхаус в сумерках, взрослая женщина в шёлковом халате у окна.  
**Совет:** Wan 2.6 Spicy поддерживает дубли по 10 секунд для длинных пролётов камеры.

#### M08 · Реклама ювелирных украшений

```text
Fine jewelry ad. Close-up of an adult woman's bare neck and collarbone as a diamond necklace is fastened by unseen hands. She tilts her head and the diamonds sparkle. Black background, precise beauty lighting, macro detail.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m08-ru) | 1080p · 5 s · 1:1 | $2.85 | Средний |

**Первый кадр:** Крупный план шеи и ключицы взрослой женщины, чёрный фон.  
**Совет:** Бьюти-макро выглядит премиально и почти не даёт артефактов.

#### M09 · Лосьон для тела

```text
Skincare commercial. An adult woman wrapped in a white towel smooths body lotion down her leg on the edge of a bathtub. Soft daylight, clean white bathroom, dewy skin, gentle camera tilt down.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m09-ru) | 1080p · 5 s · 9:16 | $0.285 | Начальный |

**Первый кадр:** Взрослая женщина в полотенце на краю ванны наносит лосьон.  
**Совет:** Чистый язык рекламы продукта сохраняет кадр безопасным для бренда.

#### M10 · Тизер автора

```text
Vertical social teaser. An adult creator in a silk robe sits on her bed, looks straight at the camera, raises a finger to her lips with a playful smile, then winks. Soft ring-light glow, cosy bedroom, static phone camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=m10-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Взрослая авторка в шёлковом халате на кровати лицом к камере, кольцевая лампа.  
**Совет:** Короткие намекающие тизеры приводят клики на платные платформы и при этом не нарушают правил соцсетей.

### Готовые шаблоны движения и камеры

Универсальные промпты, которые описывают только движение и камеру. Сочетайте их с любым первым кадром: они работают, потому что модель image-to-video уже видит персонажа.

#### T01 · Медленный наезд

```text
Slow, steady push-in from medium shot to close-up. Subject breathes naturally and blinks once. Hair moves slightly. Lighting stays consistent.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t01-ru) | 480p · 5 s · любое соотношение сторон | $0.095 | Начальный |

**Первый кадр:** Любой хорошо освещённый взрослый персонаж, средний план.  
**Совет:** Самый безопасный универсальный шаблон. Черновики делайте в 480p, удачные варианты перерендерите в 720p.

#### T02 · Облёт влево

```text
Camera orbits slowly to the left around the subject, keeping them centred. Subject stays mostly still and follows the camera with their eyes.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Spicy](https://spicyapi.ai/ru/models/seedance-2-0-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t02-ru) | 720p · 5 s · любое соотношение сторон | $1.14 | Средний |

**Первый кадр:** Взрослый персонаж в центре кадра, у фона есть глубина.  
**Совет:** Облёту нужна модель с хорошей 3D-согласованностью. Самый надёжный выбор — Seedance.

#### T03 · Взгляд через плечо

```text
Subject facing away slowly turns their head to look back over their shoulder at the camera and smiles. Static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t03-ru) | 720p · 5 s · любое соотношение сторон | $0.19 | Начальный |

**Первый кадр:** Взрослый персонаж со спины или в три четверти со спины.  
**Совет:** Работает с любым первым кадром со спины.

#### T04 · Ветер и ткань

```text
A steady breeze moves the subject's hair and clothing. Fabric ripples and flows. Subject stays still and relaxed. Static camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [LTX 2.3 Spicy](https://spicyapi.ai/ru/models/ltx-2-3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t04-ru) | 720p · 5 s · любое соотношение сторон | $0.19 | Начальный |

**Первый кадр:** Взрослый персонаж в свободной ткани, длинные волосы.  
**Совет:** Оживляет любой статичный кадр, не затрагивая анатомию.

#### T05 · Наклон вверх

```text
Camera starts at the subject's feet and tilts up slowly along the body to end on their face. Subject stands still and looks into the lens at the end.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t05-ru) | 720p · 5 s · 9:16 | $0.19 | Начальный |

**Первый кадр:** Вертикальный кадр в полный рост: взрослый персонаж стоит.  
**Совет:** Используйте вертикальный первый кадр в полный рост.

#### T06 · Отъезд назад

```text
Camera starts on a close-up of the subject's face and pulls back slowly to reveal the full room around them. Subject stays still with a subtle smile.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.6 Spicy](https://spicyapi.ai/ru/models/wan-2-6-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t06-ru) | 720p · 5 s · 16:9 | $0.475 | Средний |

**Первый кадр:** Крупный план лица взрослого персонажа, комната едва угадывается.  
**Совет:** Модели придётся придумать комнату, поэтому опишите её одной строкой, если первый кадр плотный.

#### T07 · Ручная камера, без постановки

```text
Handheld phone-camera feel with slight natural shake. Subject laughs, glances away, then back at the camera, adjusting their hair.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [MiniMax H3 Spicy](https://spicyapi.ai/ru/models/minimax-h3-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t07-ru) | 768p · 5 s · 9:16 | $0.42 | Начальный |

**Первый кадр:** Непринуждённый кадр взрослого персонажа в стиле селфи.  
**Совет:** Покачивание ручной камеры делает AI-видео похожим на настоящие съёмки автора.

#### T08 · Перевод фокуса

```text
Focus shifts slowly from an object in the foreground to the subject in the background. Subject turns toward the camera as they come into focus.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 2.0 Mini Spicy](https://spicyapi.ai/ru/models/seedance-2-0-mini-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t08-ru) | 720p · 5 s · 16:9 | $0.4105 | Средний |

**Первый кадр:** Предмет на переднем плане в фокусе, взрослый персонаж размыт позади.  
**Совет:** Поместите в первый кадр чёткий предмет на переднем плане (бокал, цветок, свечу).

#### T09 · Синемаграф со статичной камерой

```text
Completely static camera. Only small natural motion: breathing, a slow blink, candle flicker, curtains moving slightly. Everything else stays still.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Seedance 1.5 Pro Spicy](https://spicyapi.ai/ru/models/seedance-1-5-pro-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t09-ru) | 720p · 5 s · любое соотношение сторон | $0.13 | Начальный |

**Первый кадр:** Любой выстроенный статичный кадр взрослого персонажа с источником света или занавеской.  
**Совет:** Фиксация камеры и самая низкая цена за секунду делают Seedance 1.5 Pro Spicy лучшим движком для синемаграфов.

#### T10 · Морфинг от первого кадра к последнему

```text
Smooth, natural transition from the opening pose to the closing pose. Subject moves continuously with no cuts. Lighting and wardrobe stay consistent.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy](https://spicyapi.ai/ru/models/wan-2-2-spicy?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=t10-ru) | 720p · 8 s · любое соотношение сторон | $0.304 | Продвинутый |

**Первый кадр:** Два кадра одного и того же взрослого персонажа: начальная поза и финальная поза.  
**Совет:** Передайте last_image_url с целевой позой. Wan 2.2 Spicy и Seedance 2.x поддерживают первый + последний кадр.

### Промпты под стилевые LoRA (Wan 2.2 Spicy LoRA)

Промпты для работы в паре со стилевой LoRA. Ставьте триггерное слово LoRA первым, а остальной промпт посвятите движению.

#### L01 · Аниме-LoRA

```text
<trigger word>, anime style, an adult woman with long pink hair in a loose kimono sits by a window at night, cherry petals drifting past, she turns and smiles, soft cel shading, gentle camera push-in.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l01-ru) | 480p · 5 s · 16:9 | $0.12 | Средний |

**Первый кадр:** Взрослая женщина в аниме-стиле у окна, сгенерирована в Qwen Image 2.1 LoRA с аниме-LoRA.  
**Совет:** Передайте аниме-LoRA в high_noise_loras, чтобы задать композицию; сила 0.8 — хорошая отправная точка.

#### L02 · LoRA плёночной фотографии

```text
<trigger word>, 35mm film photograph, an adult woman in a white slip dress on an unmade bed in morning light, she stretches and pulls the sheet around her, visible grain, faded warm tones.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l02-ru) | 720p · 5 s · 16:9 | $0.24 | Средний |

**Первый кадр:** Взрослая женщина на неубранной кровати в утреннем свете.  
**Совет:** Текстурные LoRA (зерно, плёнка) кладите в low_noise_loras: они действуют на поздних шагах шумоподавления.

#### L03 · LoRA масляной живописи

```text
<trigger word>, oil painting, a nude adult woman reclining on red velvet in a baroque interior, candlelight flickers across her skin, visible brush strokes, rich chiaroscuro.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l03-ru) | 720p · 5 s · 4:5 | $0.24 | Средний |

**Первый кадр:** Изображение в стиле барокко: взрослая женщина полулежит на красном бархате.  
**Совет:** Стилевые LoRA могут «плыть» при движении; ограничьте движение светом и дыханием.

#### L04 · LoRA для постоянства персонажа

```text
<trigger word>, the same adult woman walks toward the camera down a hotel corridor in a red dress, confident smile, warm sconce lighting, low-angle tracking shot.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l04-ru) | 720p · 5 s · 9:16 | $0.24 | Продвинутый |

**Первый кадр:** Ваш вымышленный персонаж в гостиничном коридоре, красное платье.  
**Совет:** Обучайте LoRA персонажей только на вымышленных персонажах или на себе / взрослых, давших задокументированное согласие.

#### L05 · Неоновая киберпанк-LoRA

```text
<trigger word>, cyberpunk, an adult woman with glowing tattoos leans against a wet alley wall under neon signs, rain falling, she exhales smoke and looks at the camera.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l05-ru) | 480p · 5 s · 16:9 | $0.12 | Средний |

**Первый кадр:** Взрослая женщина в неоновом переулке со светящимися татуировками.  
**Совет:** Сочетайте максимум одну стилевую LoRA и одну LoRA освещения. Больше двух обычно конфликтуют.

#### L06 · Продление ролика

```text
Continue the motion naturally from the last frame. Same subject, same wardrobe, same lighting. She slowly turns away and walks toward the window.
```

| Модель | Настройки | Цена за запуск | Уровень |
|---|---|---|---|
| [Wan 2.2 Spicy LoRA](https://spicyapi.ai/ru/models/wan-2-2-spicy-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=l06-ru) | 720p · 5 s · любое соотношение сторон | $0.24 | Продвинутый |

**Первый кадр:** Готовый ролик, который нужно продолжить, передаётся как video_url.  
**Совет:** Используйте эндпоинт video-extend (alibaba/wan-2.2-spicy-lora/video-extend) с теми же LoRA, чтобы склеить 5 s + 5 s + 5 s.


---

## Промпты для первого кадра

Image-to-video хорош ровно настолько, насколько хорош первый кадр. Эти промпты генерируют чистые, хорошо освещённые первые кадры со взрослыми персонажами, которые хорошо анимируются: один человек (или чётко разделённая пара), простой фон, расслабленные руки, лицо открыто или скрыто намеренно. Фотореалистичные первые кадры делаются в Qwen Image 2.1 — рекомендуемой модели изображений без цензуры на SpicyAPI; аниме-кадры — в Qwen Image 2.1 LoRA с открытой аниме-LoRA (той же, что и в собственных примерах SpicyAPI).

#### R01 · Будуар в свете из окна

```text
Photorealistic boudoir portrait of a woman in her early 30s sitting on the edge of an unmade bed in black lace lingerie, soft window light from the left, warm neutral bedroom, relaxed hands resting on her knees, looking at the camera, 85mm lens, shallow depth of field, natural skin texture.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r01-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R02 · Портрет в шёлковом халате

```text
Photorealistic portrait of an adult woman in her late 20s in an ivory silk robe slipping off one shoulder, standing by a candlelit vanity, warm amber light, soft bokeh, calm expression, editorial beauty photography.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r02-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R03 · На красном атласе

```text
Wide editorial photograph of an adult woman lying on her side on red satin sheets in a red lace bodysuit, crimson key light from the right, cool blue fill from the left, full body in frame, clean composition, high-end fashion photography.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r03-ru) · `aspect_ratio=3:2` `resolution=1k` · $0.024 за изображение

#### R04 · Каблуки в гостиничном коридоре

```text
Full-body photograph of an adult woman in her 30s in black lingerie, stockings and stiletto heels standing at the far end of a dim hotel corridor, warm wall sconces, glossy floor reflections, low camera angle, cinematic color grade.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r04-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R05 · Тропический душ

```text
Photorealistic shot of an adult woman from the shoulders up under a rainfall shower, eyes closed, water running through her hair, dense steam, warm backlight, glass wall with droplets, tasteful framing.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r05-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R06 · Монохромный этюд с натуры

```text
Black and white fine-art figure study of a nude adult man in his 30s seated on a wooden stool, grey seamless backdrop, single large softbox from above left, sculpted shadows, classical pose, museum print quality.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r06-ru) · `aspect_ratio=4:5` `resolution=1k` · $0.024 за изображение

#### R07 · Торс в тенях жалюзи

```text
High-contrast black and white photograph of an adult woman's torso in a dark room, hard striped light from window blinds across her skin, film noir mood, abstract and artistic, face out of frame.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r07-ru) · `aspect_ratio=1:1` `resolution=1k` · $0.024 за изображение

#### R08 · Пара в спальне при свечах

```text
Cinematic photograph of an adult couple in their 30s standing close in a candlelit bedroom, she wears a black slip dress, he wears an open white shirt, foreheads touching, side view, clear separation of the two figures, warm candlelight, shallow depth of field.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r08-ru) · `aspect_ratio=3:2` `resolution=1k` · $0.024 за изображение

#### R09 · Две женщины на бархатном диване

```text
Editorial photograph of two adult women in their late 20s sitting face to face on a burgundy velvet sofa, one in black lace, one in white satin, soft smiles, warm candlelight, rich interior, clearly distinct outfits.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r09-ru) · `aspect_ratio=3:2` `resolution=1k` · $0.024 за изображение

#### R10 · Выход из бассейна-инфинити

```text
Photorealistic shot of an adult woman in a white one-piece swimsuit at the edge of a turquoise infinity pool, hands on the ledge about to climb out, bright midday sun, luxury villa background, low angle.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r10-ru) · `aspect_ratio=3:2` `resolution=1k` · $0.024 за изображение

#### R11 · Неоновая улица под дождём

```text
Cinematic night photograph of an adult woman in a soaked white shirt standing on an empty city street in the rain, face turned up, neon signs reflecting in wet asphalt, blue and pink palette, 35mm film look.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r11-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R12 · Тёмная эльфийка-чародейка

```text
Fantasy art photograph of an adult dark elf woman with silver hair and pointed ears in revealing black leather and silver armour, standing in a ruined candlelit temple, violet magic glow in her open hands, dramatic rim light, highly detailed.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r12-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R13 · Зал суккуба

```text
Dark fantasy portrait of an adult succubus with curved horns, folded black wings and a slender tail, wearing black lingerie, standing in a red-lit gothic chamber, smoke, dramatic backlight, detailed skin and wings.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r13-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R14 · Андроид на лабораторном столе

```text
Sci-fi photograph of an adult female android with seamless white synthetic panels and faint blue seams lying on a clean white lab table, eyes closed, cool clinical light, minimalist lab, film still.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r14-ru) · `aspect_ratio=3:2` `resolution=1k` · $0.024 за изображение

#### R15 · Гостья маскарада

```text
Baroque masquerade photograph of an adult woman in a gold lace mask and a low-backed black gown, candlelit Venetian ballroom with masked guests softly blurred behind her, gold and black palette.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r15-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R16 · Аниме: онсэн

```text
storybook anime illustration of an adult woman in her 20s with long purple hair relaxing in an outdoor hot spring at night, a towel wrapped around her, steam drifting, cherry petals falling on the water, paper lanterns glowing, soft smile, clean cel shading, detailed background
```

[Qwen Image 2.1 LoRA](https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r16-ru) · `aspect_ratio=3:2` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) (`loras=[{"path": "https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora/resolve/main/qwen_image_2512_storybook_anime_lora.safetensors", "scale": 1}]`) · $0.03 за изображение

#### R17 · Аниме: пляж

```text
storybook anime illustration of an adult woman with short blonde hair in a red bikini running along the shoreline, water splashing around her ankles, bright summer sky, sparkling sea, dynamic pose, vivid colors
```

[Qwen Image 2.1 LoRA](https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r17-ru) · `aspect_ratio=3:2` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) (`loras=[{"path": "https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora/resolve/main/qwen_image_2512_storybook_anime_lora.safetensors", "scale": 1}]`) · $0.03 за изображение

#### R18 · Аниме: королева демонов

```text
watercolor anime of an adult demon queen with curved horns, red eyes and a slender tail, wearing a black lace outfit, seated in a throne room lit by purple fire braziers, confident expression, deep ink shadows, oxblood and violet washes
```

[Qwen Image 2.1 LoRA](https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r18-ru) · `aspect_ratio=2:3` `resolution=1k` · LoRA: [watercolor-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora) (`loras=[{"path": "https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora/resolve/main/qwen_image_2512_watercolor_anime_lora.safetensors", "scale": 1}]`) · $0.03 за изображение

#### R19 · Аниме: серебровласая героиня в спальне

```text
storybook anime illustration of an adult woman with long silver hair lying on her side on a bed in an oversized shirt, propped on one elbow, afternoon light through curtains, soft smile, cozy detailed room, soft cel shading
```

[Qwen Image 2.1 LoRA](https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r19-ru) · `aspect_ratio=3:2` `resolution=1k` · LoRA: [storybook-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora) (`loras=[{"path": "https://huggingface.co/neonforestmist/qwen-image-2512-storybook-anime-lora/resolve/main/qwen_image_2512_storybook_anime_lora.safetensors", "scale": 1}]`) · $0.03 за изображение

#### R20 · Аниме: киберпанк-крыша

```text
watercolor anime of an adult woman in a cropped leather jacket and bodysuit on a rooftop in a neon city at night, rain falling, wind in her hair, looking back over her shoulder, pink and cyan washes on wet paper texture
```

[Qwen Image 2.1 LoRA](https://spicyapi.ai/ru/models/qwen-image-2-1-lora?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r20-ru) · `aspect_ratio=3:2` `resolution=1k` · LoRA: [watercolor-anime LoRA](https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora) (`loras=[{"path": "https://huggingface.co/neonforestmist/qwen-image-2512-watercolor-anime-lora/resolve/main/qwen_image_2512_watercolor_anime_lora.safetensors", "scale": 1}]`) · $0.03 за изображение

#### R21 · Каталог белья

```text
Clean e-commerce photograph of an adult model in an ivory silk and lace lingerie set standing on a white studio cyclorama, even soft lighting, full body, neutral pose, catalog style.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r21-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R22 · Селфи автора

```text
Casual smartphone-style selfie of an adult woman in her late 20s in a silk robe sitting on her bed, ring-light glow, cosy bedroom, natural makeup, playful expression, realistic phone photo.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r22-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R23 · Спортсменка в зале

```text
Photorealistic shot of an adult female athlete in a sports bra and leggings in a gritty gym, towel around her neck, hard top light, glistening skin, confident look at the camera.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r23-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение

#### R24 · Мужской будуар

```text
Photorealistic boudoir portrait of an adult man in his 30s lying back on white sheets, bare chest, grey sweatpants, soft morning window light, relaxed smile, shallow depth of field, editorial style.
```

[Qwen Image 2.1](https://spicyapi.ai/ru/models/qwen-image-2-1?utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-video-prompts&utm_content=r24-ru) · `aspect_ratio=2:3` `resolution=1k` · $0.024 за изображение


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
На SpicyAPI (каталог от 2026-09-27) 5-секундный ролик стоит от $0.06 (Seedance 1.5 Pro Spicy, 480p) или $0.095 (Wan 2.2 Spicy, 480p) и до примерно $5.40 (Seedance 2.5 Spicy в 1080p). У каждого промпта выше указана своя цена.

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
