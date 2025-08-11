from models.question import QuestionStore


class QuizEngine:
    """A class to manage a quiz session.

    Attributes
    ----------
    questions : QuestionStore
    """

    def __init__(self, questions: QuestionStore):
        self.questions = questions.store
        self.user_answers = {i: "" for i in range(len(questions.store))}

    def update_answer(self, question_index: int, answer: str) -> None:
        """Update the user's answer for a specific question.

        Parameters
        ----------
        question_index : int
            The index of the question to update.
        answer : str
            The user's answer to the question.
        """

        if 0 <= question_index < len(self.questions):
            self.user_answers[question_index] = answer

    def evaluate(self) -> tuple[list[bool], int]:
        """Evaluate the user's answers.

        Returns
        -------
        list[bool]
            A list indicating whether each answer is correct (True) or incorrect (False).
        int
            The number of correct answers provided by the user.
        """

        results = list(
            map(
                lambda q: q[0].is_correct(q[1]),
                zip(self.questions, self.user_answers.values()),
            )
        )
        score = sum(results)

        return results, score

    def is_all_answered(self) -> bool:
        """Check if all questions have been answered.

        Returns
        -------
        bool
            True if all questions are answered, False otherwise.
        """

        return all(answer.strip() for answer in self.user_answers.values())

    def reset_answers(self) -> None:
        """Reset all user answers to empty strings."""

        self.user_answers = {i: "" for i in range(len(self.questions))}
