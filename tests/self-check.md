---
layout: default
title: Тести для самоперевірки
---

# 📝 Самоперевірка знань: Повний тест

Оберіть варіант відповіді. Після натискання ви побачите правильний результат та коротке пояснення.

<div class="content-block">
  <p><strong>1. Який тип ШІ здатний виконувати лише одну конкретну задачу?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Неправильно. AGI — це штучний розум людського рівня, якого ще не існує.')">Загальний ШІ (AGI)</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! ANI (Вузький ШІ) — це всі сучасні системи: від шахів до ChatGPT.')">Вузький ШІ (ANI)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Неправильно. ASI (Надзагальний ШІ) — це гіпотетичний інтелект, що перевершує людину.')">Надзагальний ШІ (ASI)</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>2. Як називається явище, коли ШІ впевнено генерує вигадані дані?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Регресія — це математичний метод прогнозування.')">Регресія</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! Галюцинація стається, коли модель прогнозує слова, не перевіряючи факти.')">Галюцинація</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Токенізація — це лише спосіб подрібнення тексту для ШІ.')">Токенізація</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>3. Яка архітектура лежить в основі сучасних мовних моделей (LLM)?</strong></p>
  <button class="quiz-btn" onclick="check(this, true, '✅ Правильно! Архітектура Transformer змінила все у 2017 році.')">Трансформер (Transformer)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Це застаріла технологія, що не підходить для мови.')">Експертна система</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>4. Метод навчання за принципом «винагорода за правильну дію»:</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Навчання з учителем використовує готові відповіді.')">Навчання з учителем</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! Алгоритм вчиться методом спроб та помилок, отримуючи бонуси.')">Навчання з підкріпленням</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>5. Що таке «токен» у контексті роботи LLM?</strong></p>
  <button class="quiz-btn" onclick="check(this, true, '✅ Так! Це «цеглинка» тексту, яку модель перетворює на числа.')">Одиниця тексту (слово або його частина)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Ні, це не фінансова одиниця в цьому контексті.')">Електронна валюта</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>6. Коли офіційно народився ШІ як наука?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Тоді ШІ ще не існувало.')">1945</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! Дартмутський семінар 1956 року став початком галузі.')">1956</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>7. Промпт-інженерія — це:</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Це робота з «залізом».')">Збирання комп'ютерів</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Правильно! Це вміння ставити ШІ чіткі та зрозумілі завдання.')">Мистецтво правильних запитів</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>8. Як називається копіювання людських стереотипів нейромережею?</strong></p>
  <button class="quiz-btn" onclick="check(this, true, '✅ Так. Це Bias (упередженість), що виникає через помилки в навчальних даних.')">Упередженість (Bias)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Це метод збільшення кількості даних.')">Аугментація</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>9. Що можна безпечно вводити в ШІ?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Ніколи не діліться паролями!')">Паролі</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно. Загальновідомі факти не є конфіденційними.')">Загальні історичні факти</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>10. Основна мета використання ШІ в майбутньому:</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Це занадто радикальний і малоймовірний сценарій.')">Повна заміна людини</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Так! ШІ має стати інструментом, що підсилює наші можливості.')">Аугментація можливостей людини</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>11. Що відбувається у процесі перенавчання (Overfitting) моделі?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Модель не втрачає пам\'ять, навпаки — запам\'ятовує забагато деталей.')">Модель забуває раніше вивчені дані</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! Модель «зазубрює» тренувальні дані разом із шумом і втрачає здатність до узагальнення.')">Модель ідеально працює на тренувальних даних, але дає збій на нових</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Зниження швидкості — це апаратна проблема, а не помилка навчання.')">Знижується швидкість обчислень через брак ресурсів</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>12. Який механізм дозволяє моделям Transformer визначати зв\'язки між словами незалежно від відстані між ними?</strong></p>
  <button class="quiz-btn" onclick="check(this, true, '✅ Правильно! Механізм Self-Attention (увага до себе) дозволяє фокусуватися на релевантних частинах контексту.')">Механізм уваги (Self-Attention)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Градієнтний спуск оптимізує ваги, а не відслідковує контекстні зв\'язки слів.')">Градієнтний спуск (Gradient Descent)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Дерева рішень — окремий класичний алгоритм ML, не пов\'язаний з LLM.')">Дерево рішень</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>13. Який підхід використовується для донавчання базової моделі під конкретну прикладну задачу?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Повне перенавчання з нуля потребує величезних ресурсів і рідко застосовується.')">Навчання з нуля (Pre-training)</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Так! Fine-tuning дозволяє адаптувати вже навчену модель під вузькопрофільні завдання.')">Тонке налаштування (Fine-tuning)</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>14. Що означає технологія RAG (Retrieval-Augmented Generation)?</strong></p>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! RAG спочатку шукає релевантні факти у зовнішній базі, а потім генерує відповідь, зменшуючи галюцинації.')">Поєднання пошуку інформації в зовнішніх джерелах із генерацією</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Це опис роботи алгоритмів комп\'ютерного зору (Computer Vision).')">Метод розпізнавання облич на фото</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Це архітектура для генерації зображень (GAN), а не текстовий пошук.')">Генеративно-змагальна мережа</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>15. Метод перевірки, чи здатна машина демонструвати інтелектуальну поведінку, невідрізнену від людської:</strong></p>
  <button class="quiz-btn" onclick="check(this, true, '✅ Правильно! Тест Тюрінга, запропонований Аланом Тюрінгом у 1950 році.')">Тест Тюрінга</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ CAPTCHA навпаки створена, щоб відрізнити бота від реальної людини.')">Тест CAPTCHA</button>
  <p class="feedback"></p>
</div>
