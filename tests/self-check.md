---
layout: default
title: Тести для самоперевірки
---

# 📝 Самоперевірка знань: Введення в ШІ

Пройдіть цей тест, щоб перевірити, наскільки засвоєно теоретичний матеріал курсу. Виберіть одну правильну відповідь.

<div id="quiz-container" class="content-block">
  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>1. Який тип ШІ здатний виконувати лише одну конкретну задачу (наприклад, грати в шахи)?</strong></p>
    <button class="quiz-btn" onclick="check(this, false)">Загальний ШІ (AGI)</button>
    <button class="quiz-btn" onclick="check(this, true)">Вузький ШІ (ANI)</button>
    <button class="quiz-btn" onclick="check(this, false)">Надзагальний ШІ (ASI)</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>2. Як називається процес, коли ШІ впевнено генерує вигадані або фактично невірні дані?</strong></p>
    <button class="quiz-btn" onclick="check(this, false)">Регресія</button>
    <button class="quiz-btn" onclick="check(this, true)">Галюцинація</button>
    <button class="quiz-btn" onclick="check(this, false)">Токенізація</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>3. Яка архітектура лежить в основі сучасних мовних моделей (LLM)?</strong></p>
    <button class="quiz-btn" onclick="check(this, true)">Трансформер (Transformer)</button>
    <button class="quiz-btn" onclick="check(this, false)">Лінійна регресія</button>
    <button class="quiz-btn" onclick="check(this, false)">Експертна система</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>4. Метод навчання, де агент отримує "винагороду" за правильну дію, називається:</strong></p>
    <button class="quiz-btn" onclick="check(this, false)">Навчання з учителем</button>
    <button class="quiz-btn" onclick="check(this, true)">Навчання з підкріпленням</button>
    <button class="quiz-btn" onclick="check(this, false)">Навчання без учителя</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>5. Що таке "токен" у контексті роботи LLM?</strong></p>
    <button class="quiz-btn" onclick="check(this, true)">Одиниця тексту (слово або частина слова), яку обробляє модель</button>
    <button class="quiz-btn" onclick="check(this, false)">Електронна валюта для оплати підписки</button>
    <button class="quiz-btn" onclick="check(this, false)">Пароль доступу до бази даних</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>6. Який рік вважається датою офіційного народження ШІ як науки (Дартмутський семінар)?</strong></p>
    <button class="quiz-btn" onclick="check(this, false)">1945</button>
    <button class="quiz-btn" onclick="check(this, true)">1956</button>
    <button class="quiz-btn" onclick="check(this, false)">1991</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>7. Промпт-інженерія — це:</strong></p>
    <button class="quiz-btn" onclick="check(this, false)">Збирання комп'ютерів для навчання ШІ</button>
    <button class="quiz-btn" onclick="check(this, true)">Мистецтво складання правильних запитів до ШІ</button>
    <button class="quiz-btn" onclick="check(this, false)">Створення вірусів за допомогою нейромереж</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>8. Як називається явище, коли алгоритм копіює людські стереотипи з навчальних даних?</strong></p>
    <button class="quiz-btn" onclick="check(this, true)">Упередженість (Bias)</button>
    <button class="quiz-btn" onclick="check(this, false)">Аугментація</button>
    <button class="quiz-btn" onclick="check(this, false)">Кластеризація</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>9. Що з переліченого НЕ є конфіденційною інформацією, яку не можна вводити в ШІ?</strong></p>
    <button class="quiz-btn" onclick="check(this, false)">Паролі від соцмереж</button>
    <button class="quiz-btn" onclick="check(this, true)">Загальні факти про історію України</button>
    <button class="quiz-btn" onclick="check(this, false)">Медичні діагнози</button>
  </div>

  <div class="quiz-item" style="margin-bottom: 2rem; padding: 1.5rem; border-bottom: 1px solid var(--border);">
    <p><strong>10. Основна мета використання ШІ у праці майбутнього — це:</strong></p>
    <button class="quiz-btn" onclick="check(this, false)">Повна заміна людини машиною</button>
    <button class="quiz-btn" onclick="check(this, true)">Аугментація (підсилення можливостей людини)</button>
    <button class="quiz-btn" onclick="check(this, false)">Відмова від складної інтелектуальної праці</button>
  </div>
</div>

<style>
  .quiz-btn {
    display: block;
    width: 100%;
    text-align: left;
    padding: 1rem;
    margin-top: 0.5rem;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s;
  }
  .quiz-btn:hover { border-color: var(--accent); background: rgba(0, 212, 255, 0.05); }
  .correct { border-color: #10b981 !important; background: rgba(16, 185, 129, 0.1) !important; color: #10b981; }
  .incorrect { border-color: #ef4444 !important; background: rgba(239, 68, 68, 0.1) !important; color: #ef4444; }
</style>

<script>
  function check(btn, isCorrect) {
    const parent = btn.parentElement;
    const buttons = parent.querySelectorAll('.quiz-btn');
    buttons.forEach(b => b.disabled = true);
    
    if(isCorrect) {
      btn.classList.add('correct');
    } else {
      btn.classList.add('incorrect');
    }
  }
</script>
