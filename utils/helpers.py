"""
Helper utilities.

This module contains helper functions for various tasks.
"""

from typing import Dict, Any, Tuple, Iterable
from models.quiz_engine import QuizEngine


def performance_message(score_percentage: float) -> Tuple[str, str]:
    """
    Get performance message based on score using functional approach.

    Args:
        score_percentage: Score as percentage

    Returns:
        Tuple of (message, emoji/icon)
    """
    performance_ranges = [
        (80, "¡Excelente! 🌟", "success"),
        (60, "Bien 👍", "warning"),
        (0, "Puedes mejorar 💪", "error"),
    ]

    # Use filter and next to find the appropriate range
    result = next(
        filter(lambda x: score_percentage >= x[0], performance_ranges),
        ("", "", "info"),  # Default if all fitered
    )

    return result[1], result[2]


def format_question_results(quiz_engine: QuizEngine) -> Iterable[Dict[str, Any]]:
    """
    Format question results for display using functional programming.

    Args:
        questions: List of Question objects
        user_answers: Dictionary mapping question text to user answers

    Returns:
        List of dictionaries with formatted question data
    """

    quiz_questions = quiz_engine.questions
    user_answers = quiz_engine.user_answers

    return map(
        lambda item: {
            "index": item[0] + 1,
            "user_answer": user_answers.get(item[0], ""),
            "is_correct": item[1].is_correct(user_answers.get(item[0], "")),
            "correct_answer": item[1].correct_answer,
            "question_text": item[1].question_text,
        },
        enumerate(quiz_questions),
    )
