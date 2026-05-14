---
layout: default
title: Підсумковий іспит
---

# 🎓 Підсумковий іспит (12-бальна система)

Будь ласка, відповідайте уважно. Кожне питання супроводжується поясненням. Ваш фінальний бал буде розраховано за 12-бальною шкалою.

<div id="quiz-wrapper">
  <div class="content-block" style="padding: 1rem; text-align: center; border-color: var(--accent);">
    <h3 id="progress-text">Питання: 1 з 25</h3>
    <div style="width: 100%; background: var(--border); height: 8px; border-radius: 4px; margin-top: 8px;">
      <div id="progress-bar" style="width: 4%; background: var(--accent); height: 100%; border-radius: 4px; transition: 0.3s;"></div>
    </div>
  </div>

  <div id="questions-container">
    </div>

  <div id="final-result" class="content-block" style="display: none; text-align: center; border: 2px solid var(--accent);">
    <h2 style="color: var(--accent);">Іспит завершено!</h2>
    <div style="font-size: 3rem; font-weight: 800; margin: 1rem 0;" id="grade-12">0</div>
    <p style="font-size: 1.2rem;" id="score-raw">Ви набрали 0 балів з 25</p>
    <p id="grade-comment" style="color: var(--muted); margin-bottom: 2rem;"></p>
    <button onclick="window.location.reload()" class="quiz-btn" style="width: auto; margin: 0 auto; background: var(--accent); color: var(--bg); font-weight: bold; padding: 1rem 2rem;">Спробувати ще раз</button>
  </div>
</div>

<script>
  const questionsData = [
    { q: "Хто ввів термін 'Штучний інтелект' у 1956 році?", a: ["Джон Маккарті", "Алан Тюрінг", "Ілон Маск"], c: 0, e: "Саме Джон Маккарті організував Дартмутський семінар, де ШІ було визнано як наукову галузь." },
    { q: "Що таке 'Зима ШІ'?", a: ["Назва суперкомп'ютера", "Період спаду інтересу та фінансування ШІ", "Алгоритм для прогнозу погоди"], c: 1, e: "Зима ШІ стається, коли очікування від технології не справджуються, і інвестори припиняють фінансування." },
    { q: "Який тип ШІ ми використовуємо сьогодні (наприклад, перекладачі)?", a: ["Загальний ШІ (AGI)", "Надзагальний ШІ (ASI)", "Вузький ШІ (ANI)"], c: 2, e: "Вузький ШІ (ANI) спеціалізується на конкретних задачах і не має свідомості." },
    { q: "Яка архітектура дозволила створити сучасні моделі на кшталт ChatGPT?", a: ["Transformer", "Deep Blue", "Binary Tree"], c: 0, e: "Архітектура Transformer (2017) дозволила моделям обробляти весь контекст тексту одночасно." },
    { q: "Як називається процес поділу тексту на дрібні частини для ШІ?", a: ["Дифузія", "Токенізація", "Генерація"], c: 1, e: "Токенізація перетворює слова або склади в числа (токени), які розуміє комп'ютер." },
    { q: "Що таке 'галюцинація' в контексті LLM?", a: ["Впевнене вигадування фактів", "Вірус у програмі", "Збій сервера"], c: 0, e: "ШІ лише передбачає наступне слово за ймовірністю, тому може 'впевнено' помилятися." },
    { q: "Який метод навчання використовує 'винагороду'?", a: ["Навчання з учителем", "Навчання без учителя", "Навчання з підкріпленням"], c: 2, e: "У навчанні з підкріпленням алгоритм отримує 'бали' за кожну правильну дію." },
    { q: "Що таке промпт?", a: ["Текстовий запит до ШІ", "Мова програмування", "Назва моделі"], c: 0, e: "Промпт — це інструкція або питання, яке ми вводимо в інтерфейс ШІ." },
    { q: "Який елемент промпту найкраще допомагає ШІ зрозуміти стиль відповіді?", a: ["Роль (наприклад, 'Ти — юрист')", "Кількість знаків", "Дата запиту"], c: 0, e: "Встановлення ролі (персони) змінює словниковий запас та тон відповіді моделі." },
    { q: "Що означає техніка 'Chain of Thought'?", a: ["Швидка відповідь", "Прохання думати крок за кроком", "Заборона думати"], c: 1, e: "Покрокове роздумування значно зменшує кількість логічних помилок у ШІ." },
    { q: "Яка технологія лежить в основі Midjourney?", a: ["Експертні системи", "Дифузійні моделі", "Таблиці Excel"], c: 1, e: "Дифузійні моделі створюють зображення, поступово прибираючи випадковий шум." },
    { q: "Що таке Deepfake?", a: ["Сховище даних", "Підміна обличчя на відео за допомогою ШІ", "Дуже глибокий код"], c: 1, e: "Дипфейки використовують нейромережі для реалістичного накладання чужого обличчя на відео." },
    { q: "Яка головна проблема авторського права в ШІ?", a: ["Висока ціна", "Навчання на роботах художників без дозволу", "Повільний інтернет"], c: 1, e: "ШІ вчиться на мільярдах картинок з інтернету, часто порушуючи права авторів цих творів." },
    { q: "Що таке Bias (упередженість) ШІ?", a: ["Висока швидкість", "Перенесення людських стереотипів у відповіді", "Точність розрахунків"], c: 1, e: "Якщо навчальні дані містили стереотипи, ШІ буде їх повторювати (наприклад, гендерні чи расові)." },
    { q: "Для чого використовують Teachable Machine?", a: ["Для ігор", "Для швидкого навчання моделей розпізнавання", "Для написання коду"], c: 1, e: "Це інструмент від Google, що дозволяє навчити нейромережу розпізнавати об'єкти за 5 хвилин." },
    { q: "Що таке сильний ШІ (AGI)?", a: ["ШІ людського рівня у всіх сферах", "Швидкий калькулятор", "ШІ в смартфоні"], c: 0, e: "AGI — це гіпотетичний ШІ, який здатний виконати будь-яку інтелектуальну задачу не гірше за людину." },
    { q: "Який рік вважається початком 'сучасного ШІ' (через Transformer)?", a: ["1956", "2017", "1991"], c: 1, e: "Стаття 'Attention Is All You Need' вийшла у 2017 році, запустивши еру великих мовних моделей." },
    { q: "Чи можна вводити паролі в ChatGPT?", a: ["Так, це безпечно", "Ні, дані використовуються для навчання", "Тільки короткі"], c: 1, e: "Все, що ви пишете в ШІ, може бути використано розробниками для покращення моделі." },
    { q: "Що таке 'токен'?", a: ["Одиниця обробки тексту", "Пароль", "Віртуальна валюта"], c: 0, e: "Одне слово може складатися з 1-3 токенів. ШІ 'бачить' світ саме через них." },
    { q: "Хто створив тест для перевірки 'людяності' ШІ?", a: ["Ада Лавлейс", "Алан Тюрінг", "Стів Джобс"], c: 1, e: "Тест Тюрінга перевіряє, чи зможе людина відрізнити відповіді машини від відповідей людини." },
    { q: "Яка компанія створила ChatGPT?", a: ["Google", "OpenAI", "Microsoft"], c: 1, e: "Компанія OpenAI випустила ChatGPT у листопаді 2022 року." },
    { q: "Що таке нейронна мережа?", a: ["Дроти всередині ПК", "Математична модель, натхненна мозком", "Соціальна мережа"], c: 1, e: "Це набір вузлів (нейронів) та зв'язків, які змінюють свою силу під час навчання." },
    { q: "Яка роль GPU в ШІ?", a: ["Виведення картинки", "Швидкі паралельні обчислення для навчання", "Охолодження"], c: 1, e: "Відеокарти (GPU) набагато швидше за звичайні процесори тренують нейромережі." },
    { q: "Що таке мультимодальність?", a: ["Багато користувачів", "Здатність працювати з текстом, фото та звуком одночасно", "Швидкий режим"], c: 1, e: "Мультимодальні моделі (як GPT-4o) можуть бачити, чути і говорити одночасно." },
    { q: "Яка головна мета 'аугментації' праці?", a: ["Замінити людину", "Підсилити людину за допомогою ШІ", "Зменшити зарплату"], c: 1, e: "Аугментація — це співпраця, де ШІ бере на себе рутину, а людина — стратегію." }
  ];

  let currentIdx = 0;
  let score = 0;

  function renderQuestion() {
    if (currentIdx >= questionsData.length) {
      showResult();
      return;
    }

    const data = questionsData[currentIdx];
    const container = document.getElementById('questions-container');
    container.innerHTML = '';

    // Оновлення прогресу
    document.getElementById('progress-text').innerText = `Питання: ${currentIdx + 1} з 25`;
    document.getElementById('progress-bar').style.width = `${((currentIdx + 1) / 25) * 100}%`;

    const block = document.createElement('div');
    block.className = 'content-block';
    block.innerHTML = `<p><strong>${data.q}</strong></p>`;

    // Рендеримо кнопки (варіанти відповіді вже в кожному об'єкті)
    data.a.forEach((text, i) => {
      const btn = document.createElement('button');
      btn.className = 'quiz-btn';
      btn.innerText = text;
      btn.onclick = () => handleChoice(btn, i === data.c, data.e);
      block.appendChild(btn);
    });

    const feedback = document.createElement('p');
    feedback.id = 'feedback-area';
    feedback.className = 'feedback';
    block.appendChild(feedback);

    const nextBtn = document.createElement('button');
    nextBtn.innerText = "Наступне питання →";
    nextBtn.className = 'quiz-btn';
    nextBtn.style.display = 'none';
    nextBtn.style.background = 'var(--accent)';
    nextBtn.style.color = 'var(--bg)';
    nextBtn.onclick = () => { currentIdx++; renderQuestion(); };
    block.appendChild(nextBtn);

    container.appendChild(block);
  }

  function handleChoice(selectedBtn, isCorrect, explanation) {
    const parent = selectedBtn.parentElement;
    const buttons = parent.querySelectorAll('.quiz-btn:not(:last-child)');
    const feedback = parent.querySelector('#feedback-area');
    const nextBtn = parent.querySelector('button:last-child');

    buttons.forEach(b => { b.style.pointerEvents = 'none'; b.style.opacity = '0.5'; });
    selectedBtn.style.opacity = '1';

    if (isCorrect) {
      score++;
      selectedBtn.classList.add('correct');
      feedback.innerHTML = `✅ <strong>Правильно!</strong><br>${explanation}`;
    } else {
      selectedBtn.classList.add('incorrect');
      feedback.innerHTML = `❌ <strong>Помилка.</strong><br>${explanation}`;
      // Підсвітимо правильний варіант
      const correctIdx = questionsData[currentIdx].c;
      buttons[correctIdx].classList.add('correct');
      buttons[correctIdx].style.opacity = '1';
    }

    feedback.style.display = 'block';
    nextBtn.style.display = 'block';
  }

  function showResult() {
    document.getElementById('questions-container').style.display = 'none';
    document.getElementById('progress-text').parentElement.style.display = 'none';
    
    const resBlock = document.getElementById('final-result');
    const gradeDisplay = document.getElementById('grade-12');
    const scoreRaw = document.getElementById('score-raw');
    const comment = document.getElementById('grade-comment');

    // Розрахунок оцінки за 12-бальною системою
    const grade12 = Math.round((score / 25) * 12);
    
    resBlock.style.display = 'block';
    gradeDisplay.innerText = `${grade12} балів`;
    scoreRaw.innerText = `Ви набрали ${score} правильних відповідей з 25`;

    if (grade12 >= 10) comment.innerText = "Відмінний результат! Ви глибоко засвоїли тему штучного інтелекту.";
    else if (grade12 >= 7) comment.innerText = "Добрий результат. Ви добре орієнтуєтесь у сучасних технологіях.";
    else if (grade12 >= 4) comment.innerText = "Задовільно. Рекомендуємо ще раз переглянути складні розділи теорії.";
    else comment.innerText = "Потрібно більше практики. Спробуйте пройти курс ще раз.";
    
    resBlock.scrollIntoView({ behavior: 'smooth' });
  }

  renderQuestion();
</script>
