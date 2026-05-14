---
layout: default
title: Тести для самоперевірки
---

# 📝 Тести з поясненнями

Виберіть відповідь. Якщо ви помилитеся, система покаже правильний варіант та причину.

<div class="content-block">
  <p><strong>1. Який тип ШІ спеціалізується лише на одній конкретній задачі?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Неправильно. Загальний ШІ (AGI) — це гіпотетичний ШІ майбутнього, рівний людині.')">Загальний ШІ (AGI)</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! ANI (Narrow AI) — це ШІ, який ми маємо сьогодні (шахи, рекомендації, розпізнавання облич).')">Вузький ШІ (ANI)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Неправильно. Надзагальний ШІ — це стадія, коли ШІ значно перевершить людський розум.')">Надзагальний ШІ (ASI)</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>2. Як називається процес, коли ШІ впевнено вигадує факти?</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Регресія — це метод прогнозування чисел, а не помилка тексту.')">Регресія</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Вірно! Галюцинація виникає, коли модель намагається передбачити наступне слово, не маючи реальних знань про факти.')">Галюцинація</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Токенізація — це просто поділ тексту на шматочки для обробки.')">Токенізація</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>3. Яка архітектура лежить в основі сучасних LLM (як-от ChatGPT)?</strong></p>
  <button class="quiz-btn" onclick="check(this, true, '✅ Точно! Архітектура Transformer, представлена Google у 2017 році, дозволила моделям розуміти контекст довгих текстів.')">Трансформер (Transformer)</button>
  <button class="quiz-btn" onclick="check(this, false, '❌ Лінійна регресія — це найпростіша математична модель, вона не може писати тексти.')">Лінійна регресія</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>4. Метод навчання за принципом «винагорода за правильну дію»:</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Навчання з учителем використовує готові пари «питання-відповідь».')">Навчання з учителем</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Правильно! Це схоже на дресирування: алгоритм отримує бали за успіх і намагається їх максимізувати.')">Навчання з підкріпленням</button>
  <p class="feedback"></p>
</div>

<div class="content-block">
  <p><strong>5. Промпт-інженерія — це:</strong></p>
  <button class="quiz-btn" onclick="check(this, false, '❌ Це технічна робота з «залізом», а не запитами.')">Збирання ПК</button>
  <button class="quiz-btn" onclick="check(this, true, '✅ Саме так! Це вміння формулювати задачі так, щоб ШІ зрозумів контекст, роль та очікуваний формат.')">Мистецтво запитів до ШІ</button>
  <p class="feedback"></p>
</div>
