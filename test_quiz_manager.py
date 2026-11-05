import unittest
from quiz_manager import (
    calculate_score,
    get_verdict,
    format_feedback,
    is_quiz_passed
)


class TestQuizManager(unittest.TestCase):

    def test_calculate_score_success(self):
        self.assertEqual(calculate_score(15, 15), 100.0)
        self.assertEqual(calculate_score(10, 15), 66.67)
        self.assertEqual(calculate_score(0, 15), 0.0)

    def test_calculate_score_exceptions(self):
        with self.assertRaises(ValueError):
            calculate_score(5, 0)
        with self.assertRaises(ValueError):
            calculate_score(-1, 10)
        with self.assertRaises(ValueError):
            calculate_score(12, 10)

    def test_get_verdict_categories(self):
        self.assertEqual(get_verdict(95.0), "Відмінно")
        self.assertEqual(get_verdict(80.0), "Добре")
        self.assertEqual(get_verdict(65.0), "Задовільно")
        self.assertEqual(get_verdict(45.0), "Потрібно повторити матеріал")

    def test_get_verdict_invalid_percentage(self):
        with self.assertRaises(ValueError):
            get_verdict(-5.0)
        with self.assertRaises(ValueError):
            get_verdict(105.0)

    def test_format_feedback_correct(self):
        res = format_feedback(True, "  ANI — це вузький ШІ.  ")
        self.assertEqual(res["status"], "success")
        self.assertEqual(res["badge"], "✅ Вірно")
        self.assertEqual(res["explanation"], "ANI — це вузький ШІ.")

    def test_format_feedback_incorrect(self):
        res = format_feedback(False, "AGI ще не існує.")
        self.assertEqual(res["status"], "fail")
        self.assertEqual(res["badge"], "❌ Неправильно")

    def test_format_feedback_type_error(self):
        with self.assertRaises(TypeError):
            format_feedback("True", "Невірний тип параметра")

    def test_is_quiz_passed(self):
        self.assertTrue(is_quiz_passed(75.0, 60.0))
        self.assertTrue(is_quiz_passed(60.0, 60.0))
        self.assertFalse(is_quiz_passed(59.9, 60.0))


if __name__ == "__main__":
    unittest.main()
