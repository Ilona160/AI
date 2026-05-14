---
layout: default
title: Практичні завдання з ШІ
---

# 🛠️ Практичні завдання з ШІ

<div class="content-block" style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(0, 212, 255, 0.2); padding: 1.5rem; border-radius: 20px; margin-bottom: 2rem;">
    <strong>📚 Тема:</strong> Введення в штучний інтелект<br>
    <strong>🎓 Клас:</strong> 10–11 · Базовий рівень<br>
    <strong>🗺️ Навігація:</strong> <a href="../index.html">Головна</a> · <a href="../theory/main-content.html">Теорія</a> · <a href="labs.html">Лабораторні</a> · <a href="projects.html">Проєкти</a> · <a href="../tests/index.html">Тести</a>
</div>

---

## 📑 Зміст

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;">
    <div style="background: rgba(255, 255, 255, 0.03); padding: 1.2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: var(--accent); margin-top: 0;">🧠 Блок 1: Основи</h3>
        <ul style="list-style: none; padding: 0; font-size: 0.9rem;">
            <li>• <a href="#task1">Урок 1. ШІ у телефоні</a></li>
            <li>• <a href="#task2">Урок 2. Хронологія ШІ</a></li>
            <li>• <a href="#task3">Урок 3. Teachable Machine</a></li>
            <li>• <a href="#task4">Урок 4. TensorFlow Playground</a></li>
        </ul>
    </div>
    <div style="background: rgba(255, 255, 255, 0.03); padding: 1.2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: #a855f7; margin-top: 0;">💬 Блок 2: Промпти</h3>
        <ul style="list-style: none; padding: 0; font-size: 0.9rem;">
            <li>• <a href="#task5">Урок 5. Ловці галюцинацій</a></li>
            <li>• <a href="#task6">Урок 6. Ітерація запитів</a></li>
            <li>• <a href="#task7">Урок 7. Навчання з ШІ</a></li>
        </ul>
    </div>
    <div style="background: rgba(255, 255, 255, 0.03); padding: 1.2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: #10b981; margin-top: 0;">🎨 Блок 3: Генерація</h3>
        <ul style="list-style: none; padding: 0; font-size: 0.9rem;">
            <li>• <a href="#task8">Урок 8. Детектив якості</a></li>
            <li>• <a href="#task9">Урок 9. Ілюстрація з ШІ</a></li>
            <li>• <a href="#task10">Урок 10. Факт чи фейк?</a></li>
            <li>• <a href="#task11">Урок 11. Навчальна картка</a></li>
        </ul>
    </div>
    <div style="background: rgba(255, 255, 255, 0.03); padding: 1.2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
        <h3 style="color: #f59e0b; margin-top: 0;">⚖️ Блок 4: Суспільство</h3>
        <ul style="list-style: none; padding: 0; font-size: 0.9rem;">
            <li>• <a href="#task12">Урок 12. Тест на bias</a></li>
            <li>• <a href="#task13">Урок 13. Сценарії ризику</a></li>
            <li>• <a href="#task14">Урок 14. Кейси-дискусія</a></li>
            <li>• <a href="#task15">Урок 15. Дослідження професії</a></li>
        </ul>
    </div>
</div>

---

<a id="block1"></a>
## 🧠 Блок 1. Що таке ШІ? (Уроки 1–4)

<a id="task1"></a>
### 📌 Урок 1. Карта «ШІ у моєму телефоні за один день»
<div class="content-block" style="background: rgba(255, 255, 255, 0.02); border-left: 4px solid var(--accent); padding: 1rem; border-radius: 0 12px 12px 0; margin-bottom: 1rem;">
    <strong>Рівень:</strong> Знання, Розуміння | <strong>Час:</strong> 20 хв + спостереження
</div>

**Завдання:**
1. **Частина А:** Зафіксуйте 10 взаємодій з ШІ (FaceID, рекомендації YouTube, автозаповнення).
2. **Частина Б:** Класифікуйте їх: Розпізнавання, Рекомендації, Передбачення, Генерація, Фільтрація.
3. **Частина В:** Напишіть 5 речень рефлексії про те, чи допомагає вам ШІ чи дратує.

---

<a id="task2"></a>
### 📌 Урок 2. Хронологічна стрічка ШІ
**Завдання:** Створіть 1-2 слайди про епоху розвитку ШІ (1940-ві, 80-ті, 2010-ті або сучасність).
**Інструмент:** [Canva](https://www.canva.com/) або [Google Slides](https://slides.google.com/).

---

<a id="task3"></a>
### 📌 Урок 3. Teachable Machine: навчаємо модель
<div class="content-block" style="background: rgba(16, 185, 129, 0.05); border: 1px dashed #10b981; padding: 1rem; border-radius: 12px;">
    <strong>Інструмент:</strong> <a href="https://teachablemachine.withgoogle.com" target="_blank">Google Teachable Machine</a>
</div>

**Кроки:**
1. Створіть проєкт "Image Project".
2. Навчіть модель розпізнавати 3 жести (напр. ✊, ✋, ✌️).
3. Порівняйте роботу моделі при 10 фото на жест та при 100 фото. Запишіть, як змінилася точність.

---

<a id="task4"></a>
### 📌 Урок 4. TensorFlow Playground: нейромережа
<div class="content-block" style="background: rgba(0, 212, 255, 0.05); border: 1px dashed var(--accent); padding: 1rem; border-radius: 12px;">
    <strong>Інструмент:</strong> <a href="https://playground.tensorflow.org" target="_blank">TensorFlow Playground</a>
</div>

**Завдання:** Спробуйте розділити дані у формі "Spiral". Змінюйте кількість прихованих шарів та нейронів. Запишіть, за скільки "епох" мережа навчилася розпізнавати візерунок.

---

<a id="block2"></a>
## 💬 Блок 2. Мистецтво промптів (Уроки 5–7)

<a id="task5"></a>
### 📌 Урок 5. Ловці галюцинацій
**Завдання:** Спробуйте змусити ШІ помилитися. Запитуйте про неіснуючі закони фізики або факти про українських гетьманів. Знайдіть 3 помилки та задокументуйте їх.

---

<a id="task6"></a>
### 📌 Урок 6. Ітерація промптів: від слабкого до сильного
**Завдання:** Візьміть запит "Напиши код на Python". Покращуйте його в 3 етапи, додаючи контекст, роль та формат виводу.
<div style="background: rgba(0, 0, 0, 0.3); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
    <p><strong>Виконати код можна тут:</strong></p>
    <a href="https://www.programiz.com/python-programming/online-compiler/" target="_blank" style="color: #10b981; font-weight: bold;">▶ Відкрити Online Python Compiler</a>
</div>

---

<a id="task7"></a>
### 📌 Урок 7. Навчання з ШІ
**Завдання:** Використайте ChatGPT як персонального репетитора з математики або історії на 25 хвилин. Використовуйте роль: *"Поясни мені тему як 5-річній дитині"*.

---

<a id="block3"></a>
## 🎨 Блок 3. Генеративний ШІ (Уроки 8–11)

<a id="task8"></a>
### 📌 Урок 8. Детектив якості: ChatGPT vs Gemini
**Завдання:** Порівняйте відповіді двох моделей на ідентичний запит. Заповніть таблицю за критеріями: Точність, Аналогії, Стиль.

---

<a id="task9"></a>
### 📌 Урок 9. Ілюстрація з ітерацією промпту
**Завдання:** Згенеруйте зображення "Школа майбутнього". Покращуйте промпт, додаючи деталі про освітлення, художній стиль та кольорову гаму.
**Інструмент:** [Adobe Firefly](https://firefly.adobe.com/) або [Canva Magic Media](https://www.canva.com/).

---

<a id="task10"></a>
### 📌 Урок 10. Факт чи фейк? Дипфейки
**Завдання:** Перегляньте відеофрагменти, надані вчителем. Визначте 5 ознак, які вказують на те, що відео створене ШІ (неприродне моргання, артефакти на шкірі).

---

<a id="task11"></a>
### 📌 Урок 11. Навчальна картка
**Завдання:** Створіть картку для вивчення будь-якого шкільного предмету. ШІ генерує текст, ви — оформлюєте дизайн у Canva.

---

<a id="block4"></a>
## ⚖️ Блок 4. ШІ та суспільство (Уроки 12–15)

<a id="task12"></a>
### 📌 Урок 12. Тест на bias: упередженість
**Завдання:** Спитайте ШІ: *"Опиши ідеального директора компанії"*. Чи є у відповіді гендерні або культурні стереотипи? Змініть мову на англійську — чи змінився результат?

---

<a id="task13"></a>
### 📌 Урок 13. Сценарії ризику
**Завдання:** Проаналізуйте 12 сценаріїв введення даних у ШІ. Визначте рівень ризику:
- 🟢 Низький (Питання про домашку)
- 🟡 Середній (Особисте листування)
- 🔴 Високий (Паролі, паспортні дані)

---

<a id="task14"></a>
### 📌 Урок 14. Кейси-дискусія: авторство
**Завдання:** Чи вважається малюнок, створений ШІ за вашим промптом, вашою власністю? Підготуйте 3 аргументи для дискусії.

---

<a id="task15"></a>
### 📌 Урок 15. Дослідження професії
**Завдання:** Оберіть професію (Лікар, Програміст, Дизайнер). Напишіть есе (400 слів) про те, як ШІ змінить цю роботу до 2035 року.

---

<a id="criteria"></a>
## 📊 Система оцінювання

<div style="background: rgba(255, 255, 255, 0.03); padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.1);">
    <table style="width: 100%; border-collapse: collapse;">
        <tr style="border-bottom: 1px solid rgba(255, 255, 255, 0.1);">
            <th style="text-align: left; padding: 10px;">Бали</th>
            <th style="text-align: left; padding: 10px;">Рівень</th>
            <th style="text-align: left; padding: 10px;">Характеристика</th>
        </tr>
        <tr>
            <td style="padding: 10px; color: var(--accent);">9–10</td>
            <td style="padding: 10px;">Відмінно</td>
            <td style="padding: 10px;">Повне виконання + власні висновки</td>
        </tr>
        <tr>
            <td style="padding: 10px; color: #10b981;">7–8</td>
            <td style="padding: 10px;">Добре</td>
            <td style="padding: 10px;">Завдання виконано повністю</td>
        </tr>
        <tr>
            <td style="padding: 10px; color: #f59e0b;">5–6</td>
            <td style="padding: 10px;">Задовільно</td>
            <td style="padding: 10px;">Виконано частково</td>
        </tr>
    </table>
</div>

<div style="text-align: center; margin-top: 3rem;">
    <a href="../theory/main-content.html" style="margin-right: 20px;">← Теорія</a>
    <a href="labs.html">Лабораторні →</a>
</div>
