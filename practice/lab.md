---
layout: default
title: Лабораторні роботи з ШІ
---

# 🧪 Лабораторний практикум: Дослідження ШІ

<div class="content-block" style="background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(0, 212, 255, 0.3); padding: 1.5rem; border-radius: 20px; margin-bottom: 2rem;">
    <strong>📊 Інструкція:</strong> Кожна робота розрахована на 45 хвилин. Виконуйте завдання у звіті (електронному або паперовому). Використовуйте гіперпосилання на інструменти для виконання тестів.
</div>

---

## 📑 Зміст практикуму

<div class="content-block" style="background: rgba(0, 242, 255, 0.03); border: 1px solid rgba(0, 242, 255, 0.2); padding: 1.5rem; border-radius: 20px;">
    <ul style="list-style: none; padding: 0; margin: 0; line-height: 2.2;">
        <li style="margin-bottom: 8px;">
            <a href="#lab1" style="color: #00f2ff; text-decoration: none; font-weight: 500; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.2rem;">🧠</span> Лабораторна №1. Аналіз алгоритмів (YouTube/Netflix)
            </a>
        </li>
        <li style="margin-bottom: 8px;">
            <a href="#lab2" style="color: #00f2ff; text-decoration: none; font-weight: 500; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.2rem;">🛡️</span> Лабораторна №2. Біометрія та Face ID
            </a>
        </li>
        <li style="margin-bottom: 8px;">
            <a href="#lab3" style="color: #00f2ff; text-decoration: none; font-weight: 500; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.2rem;">✍️</span> Лабораторна №3. Майстерність промпт-інжинірингу
            </a>
        </li>
        <li style="margin-bottom: 8px;">
            <a href="#lab4" style="color: #00f2ff; text-decoration: none; font-weight: 500; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.2rem;">🔍</span> Лабораторна №4. Детекція галюцинацій та фейків
            </a>
        </li>
        <li>
            <a href="#lab5" style="color: #00f2ff; text-decoration: none; font-weight: 500; display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.2rem;">⚖️</span> Лабораторна №5. Етичний аудит та Bias
            </a>
        </li>
    </ul>
</div>

---

<a id="lab1"></a>
## 🧠 Лабораторна робота №1. Аналіз рекомендаційних систем

<div class="content-block" style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(0, 212, 255, 0.2); padding: 2rem; border-radius: 24px; margin-bottom: 2rem;">
    <p><strong>Мета:</strong> Зрозуміти механіку роботи ANI (Вузького ШІ) на прикладі розважальних платформ.</p>
    
    <h4>Завдання 1. Реверс-інжиніринг стрічки</h4>
    <p>Проаналізуйте свою стрічку <a href="https://www.youtube.com" target="_blank" style="color: var(--accent);">YouTube</a> або <a href="https://www.netflix.com" target="_blank" style="color: var(--accent);">Netflix</a>. Які саме дані (Data Points) зібрав алгоритм?</p>
    <ul>
        <li>Час перегляду конкретного відео (у %)</li>
        <li>Взаємодія (лайки/дизлайки)</li>
        <li>Демографічні дані</li>
    </ul>

    <h4>Завдання 2. Дослідження типів навчання</h4>
    <p>Опишіть, як Netflix використовує три типи ML:</p>
    <ol>
        <li><strong>З учителем:</strong> Передбачення оцінки фільму.</li>
        <li><strong>Без учителя:</strong> Кластеризація (напр. "Любителі аніме").</li>
        <li><strong>З підкріпленням:</strong> Вибір обкладинки фільму (Reward за клік).</li>
    </ol>

    <div style="background: rgba(0, 212, 255, 0.05); padding: 1rem; border-radius: 12px; border-left: 4px solid var(--accent); margin-top: 1rem;">
        <strong>📝 Звіт:</strong> Чи вважаєте ви "бульбашку фільтрів" загрозою для критичного мислення? Наведіть 2 аргументи.
    </div>
</div>

<a id="lab2"></a>
## 🛡️ Лабораторна робота №2. Біометрія та 3D-моделювання

<div class="content-block" style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(0, 212, 255, 0.2); padding: 2rem; border-radius: 24px; margin-bottom: 2rem;">
    <p><strong>Мета:</strong> Вивчити принцип роботи комп'ютерного зору на прикладі Face ID.</p>
    
    <h4>Завдання 1. Алгоритм розпізнавання</h4>
    <p>Складіть блок-схему роботи Face ID за кроками:</p>
    <pre style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 8px; font-size: 0.85rem; color: #10b981;">
1. Проекція 30 000 точок (Інфрачервоне світло)
2. Побудова 3D-карти обличчя
3. Кодування у векторний "відбиток"
4. Порівняння відстані між векторами
    </pre>

    <h4>Завдання 2. Тест на вразливість</h4>
    <p>Дайте відповідь: чому система не спрацьовує на фотографію, але може помилитися на близнюку? Як на роботу впливає повна темрява?</p>

    <div style="background: rgba(0, 212, 255, 0.05); padding: 1rem; border-radius: 12px; border-left: 4px solid var(--accent); margin-top: 1rem;">
        <strong>📝 Звіт:</strong> Опишіть ризик зберігання біометричних даних у хмарі порівняно зі зберіганням локально на пристрої.
    </div>
</div>

<a id="lab3"></a>
## ✍️ Лабораторна робота №3. Майстерність промпт-інжинірингу

<div class="content-block" style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(0, 212, 255, 0.2); padding: 2rem; border-radius: 24px; margin-bottom: 2rem;">
    <p><strong>Мета:</strong> Опанувати техніки Few-shot та Chain-of-Thought.</p>
    <div style="display: flex; gap: 10px; margin-bottom: 1rem;">
        <a href="https://chatgpt.com" target="_blank" class="nav-link" style="font-size: 0.8rem;">🤖 До ChatGPT</a>
        <a href="https://gemini.google.com" target="_blank" class="nav-link" style="font-size: 0.8rem;">✨ До Gemini</a>
    </div>

    <h4>Завдання 1. Еволюція пояснення</h4>
    <p>Створіть запит для пояснення "Нейронних мереж" за 4 рівнями складності. Порівняйте відповіді.</p>
    
    <h4>Завдання 2. Техніка Few-shot</h4>
    <p>Навчіть ШІ спрощувати наукову мову. Надайте йому 2 приклади (напр. про спортсмена та підручник) і попросіть перефразувати визначення <em>"Дифузійної моделі"</em>.</p>

    <div style="background: rgba(0, 212, 255, 0.05); padding: 1rem; border-radius: 12px; border-left: 4px solid var(--accent); margin-top: 1rem;">
        <strong>📝 Звіт:</strong> Який елемент промпту (Роль, Контекст чи Приклад) найбільше вплинув на якість відповіді?
    </div>
</div>

<a id="lab4"></a>
## 🔍 Лабораторна робота №4. Детекція галюцинацій та фейків

<div class="content-block" style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(0, 212, 255, 0.2); padding: 2rem; border-radius: 24px; margin-bottom: 2rem;">
    <p><strong>Мета:</strong> Навчитися верифікувати інформацію від ШІ та розпізнавати дипфейки.</p>

    <h4>Завдання 1. Слідство над цитатами</h4>
    <p>Перевірте через <a href="https://scholar.google.com" target="_blank" style="color: var(--accent);">Google Scholar</a> цитату Стіва Джобса: <em>"ШІ — це нова електрика"</em>. Хто справжній автор? Чому ШІ помилився?</p>

    <h4>Завдання 2. Алгоритм детекції дипфейку</h4>
    <p>Використовуючи техніку <strong>Chain-of-thought</strong>, проаналізуйте будь-яке підозріле відео на YouTube за планом:</p>
    <ol>
        <li>Аналіз меж обличчя та артефактів.</li>
        <li>Природність моргання.</li>
        <li>Синхронізація звуку та губ.</li>
    </ol>

    <div style="background: rgba(0, 212, 255, 0.05); padding: 1rem; border-radius: 12px; border-left: 4px solid var(--accent); margin-top: 1rem;">
        <strong>📝 Звіт:</strong> Складіть таблицю: 3 корисних vs 3 шкідливих застосування дипфейків.
    </div>
</div>

<a id="lab5"></a>
## ⚖️ Лабораторна робота №5. Етичний аудит та Bias

<div class="content-block" style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 50, 50, 0.15); padding: 2rem; border-radius: 24px; margin-bottom: 2rem;">
    <p><strong>Мета:</strong> Дослідити упередженість алгоритмів у реальних кейсах.</p>

    <h4>Завдання 1. Аналіз кейсу Amazon та COMPAS</h4>
    <p>Чому ШІ відхиляв резюме зі словом "жіночий"? Чому алгоритм COMPAS частіше помилявся щодо темношкірих людей? Проаналізуйте зв'язок між історичними даними та результатом ШІ.</p>

    <h4>Завдання 2. Кібербезпека та клонування голосу</h4>
    <p>Ознайомтеся зі схемою шахрайства (FTC 2023). Розробіть <strong>"Сімейний протокол безпеки"</strong>, включаючи кодове слово та алгоритм перевірки дзвінків.</p>

    <div style="background: rgba(255, 50, 50, 0.05); padding: 1rem; border-radius: 12px; border-left: 4px solid #ff3232; margin-top: 1rem;">
        <strong>📝 Звіт:</strong> Хто відповідальний за дискримінацію ШІ: розробник, дані чи користувач? Аргументуйте.
    </div>
</div>

---

<div style="text-align: center; margin-top: 3rem; padding: 2rem; border: 1px solid var(--border); border-radius: 24px; background: rgba(255,255,255,0.02);">
    <h2>📊 Критерії оцінювання робіт</h2>
    <table style="width: 100%; border-collapse: collapse; margin-top: 10px;">
        <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
            <th style="padding: 10px;">Критерій</th>
            <th style="padding: 10px;">Бали</th>
        </tr>
        <tr><td style="padding: 10px;">Повнота виконання всіх завдань</td><td style="padding: 10px;">0–4</td></tr>
        <tr><td style="padding: 10px;">Глибина аналізу та аргументація</td><td style="padding: 10px;">0–4</td></tr>
        <tr><td style="padding: 10px;">Оформлення звіту та висновки</td><td style="padding: 10px;">0–4</td></tr>
    </table>
    <p style="margin-top: 20px;"><strong>Всього: 12 балів</strong></p>
</div>
