---
layout: default
title: Підсумковий тест з ШІ
---

# 🎓 Підсумковий контроль знань

Це великий іспит, який складається з **25 запитань**. Він охоплює всі теми курсу. Кожна відповідь супроводжується детальним розбором. Успіхів!

<div id="assessment-container">

  <div class="content-block">
    <p><strong>1. Хто є автором терміну "Штучний інтелект" (1956 рік)?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Правильно! Джон Маккарті ввів цей термін на Дартмутському семінарі.')">Джон Маккарті</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Ні, Алан Тюрінг створив тест Тюрінга, але не сам термін.')">Алан Тюрінг</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>2. Як називається період в історії, коли фінансування та інтерес до ШІ різко впали?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Вірно. Це періоди «Зими ШІ» (AI Winters).')">Зима ШІ</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Такого терміну в історії технологій не існує.')">Льодовиковий період ШІ</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>3. Перемога якого комп’ютера над Гаррі Каспаровим у 1997 році стала сенсацією?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так! Deep Blue від IBM вперше переміг чемпіона світу з шахів.')">Deep Blue</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ AlphaGo переміг у грі Го набагато пізніше — у 2016 році.')">AlphaGo</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>4. Що таке «Вузький ШІ» (ANI)?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Правильно. Це ШІ, навчений виконувати одну конкретну задачу.')">ШІ для однієї конкретної задачі</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це опис Загального ШІ (AGI).')">ШІ, що вміє все, що й людина</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>5. Яка технологія дозволяє комп’ютеру вчитися на даних без жорстких правил?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Вірно. Машинне навчання (ML) базується на статистичному аналізі даних.')">Машинне навчання</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це застаріла технологія 80-х років.')">Експертні системи</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>6. Що імітує структуру людського мозку в програмуванні?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. Нейронні мережі побудовані за принципом зв’язків між нейронами.')">Нейронні мережі</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це структури даних, але вони не копіюють мозок.')">Масиви та бази даних</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>7. Який алгоритм навчання використовує «тренер», що вказує ШІ на помилки?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Правильно. Це навчання з учителем (Supervised Learning).')">Навчання з учителем</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Тут ШІ сам шукає групи та кластери.')">Навчання без учителя</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>8. Для чого потрібні GPU (відеокарти) у навчанні ШІ?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. Паралельні обчислення на GPU значно прискорюють роботу нейромереж.')">Для швидкої паралельної обробки даних</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Ні, ШІ не потребує монітора для навчання.')">Щоб виводити зображення на екран</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>9. Що таке «Глибоке навчання» (Deep Learning)?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Правильно. Це використання нейромереж з великою кількістю шарів.')">Використання багатошарових нейромереж</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Глибина навчання не вимірюється часом.')">Довге навчання тривалістю понад рік</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>10. Як ШІ перетворює слова у зрозумілі йому числа?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. Ембеддінг (Embedding) представляє слова як вектори в просторі.')">Через вектори (Embeddings)</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це не пов’язано з кодуванням тексту.')">Через азбуку Морзе</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>11. Яка архітектура зробила революцію в LLM у 2017 році?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Transformer дозволив моделям краще розуміти контекст.')">Transformer</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це старий тип мереж для відео.')">CNN</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>12. Що таке «галюцинація» ШІ?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Вірно. ШІ вигадує факти, бо лише вгадує ймовірні слова.')">Впевнена відповідь фактами, яких не існує</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це технічна помилка доступу.')">Повільне завантаження відповіді</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>13. Який елемент промпту задає ШІ певну особистість?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. Роль (наприклад, «вчитель») змінює тон та стиль ШІ.')">Роль</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Формат лише вказує на вигляд (таблиця, список).')">Формат</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>14. Що робить фраза «думай крок за кроком» у промпті?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Це техніка Chain-of-Thought, що покращує логіку.')">Активує логічний ланцюжок міркувань</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Швидкість навпаки може трохи впасти через деталізацію.')">Прискорює відповідь у 2 рази</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>15. Промпт-інженерія — це навичка:</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. Це вміння ставити завдання мовою, зрозумілою моделі.')">Формулювання ефективних запитів</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це системне адміністрування, а не промптинг.')">Ремонту серверів ШІ</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>16. Як працюють моделі генерації зображень (Stable Diffusion, Midjourney)?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Вірно. Дифузія — це процес перетворення шуму на картинку.')">Видаляють шум із випадкового кадру</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це роблять звичайні колажні редактори.')">Шукають фото в Google і склеюють їх</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>17. Яка модель найкраще підходить для створення фотореалістичних людей?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. DALL-E та Midjourney — лідери візуальної генерації.')">DALL-E / Midjourney</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Claude — це текстова модель.')">Claude</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>18. Що таке Deepfake (дипфейк)?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Правильно. Це небезпечна технологія підміни зовнішності.')">Підміна обличчя чи голосу на відео через ШІ</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це термін з кібербезпеки мереж.')">Дуже складний пароль</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>19. Який сервіс дозволяє вчити власну модель розпізнавання за 5 хвилин?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. Teachable Machine від Google ідеальна для навчання.')">Teachable Machine</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Excel не працює з навчанням нейромереж.')">MS Excel</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>20. Чи має ШІ творчу свідомість під час створення картини?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Правильно. Це складна математична обробка статистики.')">Ні, це лише обробка статистичних ймовірностей</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Наразі ШІ не має душі чи свідомості.')">Так, ШІ відчуває натхнення</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>21. Що таке упередженість (Bias) у ШІ?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. Це відображення людських стереотипів у коді.')">Стереотипи, перейняті ШІ з поганих даних</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Швидкість не впливає на етичність відповіді.')">Занадто швидка відповідь</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>22. Яка головна загроза конфіденційності при роботі з ChatGPT?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Вірно. Ваші дані можуть бути використані для навчання системи.')">Використання ваших запитів для донавчання моделі</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це стара загроза, не пов’язана з ШІ.')">Комп’ютерні віруси в чаті</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>23. Чому виникають суперечки щодо авторського права в ШІ?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Так. ШІ вчиться на роботах живих авторів без їх дозволу.')">ШІ вчився на роботах мільйонів художників без згоди</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Висока ціна не є юридичною проблемою.')">Бо сервіси ШІ занадто дорогі</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>24. Що означає термін «Аугментація праці»?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Вірно. Це партнерство людини та ШІ для кращих результатів.')">Підсилення можливостей людини за допомогою ШІ</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Це автоматизація, а не аугментація.')">Звільнення всіх людей і заміна їх роботами</button>
    <p class="feedback"></p>
  </div>

  <div class="content-block">
    <p><strong>25. Яка навичка стане найважливішою в еру ШІ?</strong></p>
    <button class="quiz-btn" onclick="check(this, true, '✅ Абсолютно! Вміння аналізувати, ставити питання та вчитися — головне.')">Критичне мислення та адаптивність</button>
    <button class="quiz-btn" onclick="check(this, false, '❌ Знання однієї мови вже не буде достатньо.')">Вміння рахувати в умі</button>
    <p class="feedback"></p>
  </div>

</div>
