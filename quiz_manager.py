"""
Модуль quiz_manager.py
Містить функції для обробки результатів тестування користувачів.
"""

def calculate_score(correct_answers: int, total_questions: int) -> float:
    if total_questions <= 0:
        raise ValueError("Загальна кількість питань має бути більшою за нуль.")
    if correct_answers < 0:
        raise ValueError("Кількість правильних відповідей не може бути від'ємною.")
    if correct_answers > total_questions:
        raise ValueError("Кількість правильних відповідей перевищує загальну кількість.")
    return round((correct_answers / total_questions) * 100, 2)


def get_verdict(percentage: float) -> str:
    if not (0.0 <= percentage <= 100.0):
        raise ValueError("Відсоток має бути в діапазоні від 0 до 100.")
    if percentage >= 90.0:
        return "Відмінно"
    elif percentage >= 75.0:
        return "Добре"
    elif percentage >= 60.0:
        return "Задовільно"
    else:
        return "Потрібно повторити матеріал"


def format_feedback(is_correct: bool, message: str) -> dict:
    if not isinstance(is_correct, bool):
        raise TypeError("Параметр is_correct має бути булевим значенням.")
    return {
        "status": "success" if is_correct else "fail",
        "badge": "✅ Вірно" if is_correct else "❌ Неправильно",
        "explanation": message.strip()
    }


def is_quiz_passed(percentage: float, passing_threshold: float = 60.0) -> bool:
    if not (0.0 <= percentage <= 100.0) or not (0.0 <= passing_threshold <= 100.0):
        raise ValueError("Значення мають бути в межах від 0 до 100.")
    return percentage >= passing_threshold
