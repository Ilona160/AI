---
layout: default
title: Підсумковий іспит
---

# 🎓 Підсумковий іспит (Assessment)

Цей тест містить 25 запитань. Наприкінці ви побачите свій загальний бал та відсоток успішності. Кожна правильна відповідь — **1 бал**.

<div id="quiz-container">

  <div class="content-block quiz-item" data-correct="b">
    <p><strong>1. Хто є автором терміну "Штучний інтелект" (1956 рік)?</strong></p>
    <button class="quiz-btn" onclick="processAnswer(this, 'a')">Алан Тюрінг</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'b')">Джон Маккарті</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'c')">Гаррі Каспаров</button>
    <p class="feedback-text"></p>
  </div>

  <div class="content-block quiz-item" data-correct="a">
    <p><strong>2. Як називається період в історії, коли фінансування ШІ було припинено через низькі результати?</strong></p>
    <button class="quiz-btn" onclick="processAnswer(this, 'a')">Зима ШІ</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'b')">Ера застою</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'c')">Технологічна пауза</button>
    <p class="feedback-text"></p>
  </div>

  <div class="content-block quiz-item" data-correct="c">
    <p><strong>3. Що таке "Вузький ШІ" (ANI)?</strong></p>
    <button class="quiz-btn" onclick="processAnswer(this, 'a')">ШІ, що перевершує людину в усьому</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'b')">Проста база даних</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'c')">ШІ, навчений для однієї конкретної задачі</button>
    <p class="feedback-text"></p>
  </div>

  <div class="content-block quiz-item" data-correct="b">
    <p><strong>4. Яка архітектура лежить в основі моделей ChatGPT?</strong></p>
    <button class="quiz-btn" onclick="processAnswer(this, 'a')">Експертна система</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'b')">Transformer</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'c')">Лінійна регресія</button>
    <p class="feedback-text"></p>
  </div>

  <div class="content-block quiz-item" data-correct="a">
    <p><strong>5. Як називається "вигадування" фактів мовною моделлю?</strong></p>
    <button class="quiz-btn" onclick="processAnswer(this, 'a')">Галюцинація</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'b')">Ітерація</button>
    <button class="quiz-btn" onclick="processAnswer(this, 'c')">Дифузія</button>
    <p class="feedback-text"></p>
  </div>

  </div>

<div id="final-result" class="content-block" style="display: none; text-align: center; border: 2px solid var(--accent);">
  <h2 id="score-text" style="color: var(--accent);">Ваш результат: 0 з 25</h2>
  <p id="grade-text"></p>
  <button onclick="window.location.reload()" class="quiz-btn" style="width: auto; margin: 0 auto; background: var(--accent); color: var(--bg); font-weight: bold;">Спробувати ще раз</button>
</div>

<script>
  let totalScore = 0;
  let questionsAnswered = 0;
  const totalQuestions = 5; // Змініть на 25, коли додасте всі питання

  function processAnswer(btn, choice) {
    const parent = btn.parentElement;
    const correctChoice = parent.getAttribute('data-correct');
    const feedback = parent.querySelector('.feedback-text');
    const buttons = parent.querySelectorAll('.quiz-btn');

    // Блокуємо кнопки
    buttons.forEach(b => {
      b.disabled = true;
      b.style.opacity = '0.6';
    });

    btn.style.opacity = '1';

    if (choice === correctChoice) {
      totalScore++;
      btn.classList.add('correct');
      feedback.innerHTML = "✅ Правильно! +1 бал";
      feedback.style.color = "var(--accent3)";
    } else {
      btn.classList.add('wrong');
      feedback.innerHTML = "❌ Неправильно. Правильна відповідь була в іншому варіанті.";
      feedback.style.color = "#ef4444";
      
      // Підсвічуємо правильну кнопку
      buttons.forEach(b => {
        // Ми не знаємо точно яка кнопка була б, але за логікою можемо знайти через аргумент
        // В даному випадку просто покажемо пояснення
      });
    }

    questionsAnswered++;

    // Якщо відповіли на всі — показуємо результат
    if (questionsAnswered === totalQuestions) {
      showFinalScore();
    }
  }

  function showFinalScore() {
    const resultBlock = document.getElementById('final-result');
    const scoreText = document.getElementById('score-text');
    const gradeText = document.getElementById('grade-text');
    
    resultBlock.style.display = 'block';
    scoreText.innerHTML = `Ваш результат: ${totalScore} з ${totalQuestions}`;
    
    const percent = (totalScore / totalQuestions) * 100;
    if (percent >= 80) {
      gradeText.innerHTML = "🌟 Відмінно! Ви справжній експерт у ШІ.";
    } else if (percent >= 50) {
      gradeText.innerHTML = "👍 Добре! Ви маєте солідну базу знань.";
    } else {
      gradeText.innerHTML = "📚 Варто ще раз переглянути теоретичний матеріал.";
    }
    
    // Плавний скрол до результату
    resultBlock.scrollIntoView({ behavior: 'smooth' });
  }
</script>
