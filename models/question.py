from pydantic import BaseModel, Field


class Question(BaseModel):
    """A class representing a quiz question.

    Attributes
    ----------
    prompt : str
        The text of the question.
    options : list[str]
        A list of possible answer options.
    correct_answer : str
        The correct answer to the question.
    """

    question_text: str = Field(..., description="The text of the question")
    options: list[str] = Field(
        ..., min_length=2, description="A list of possible answer options"
    )
    correct_answer: str = Field(..., description="The correct answer to the question")

    def is_correct(self, answer: str) -> bool:
        """Check if the provided answer is correct.

        Parameters
        ----------
        answer : str
            The answer to check against the correct answer.

        Returns
        -------
        bool
            True if the answer is correct, False otherwise.
        """
        return answer.strip().lower() == self.correct_answer.strip().lower()


class QuestionStore(BaseModel):
    """A class representing a collection of quiz questions.

    Attributes
    ----------
    questions : list[Question]
        A list of Question objects.
    """

    store: list[Question] = Field(
        default_factory=list, description="A list of quiz questions"
    )
