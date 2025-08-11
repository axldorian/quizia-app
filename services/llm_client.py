from openai import OpenAI
from models.question import QuestionStore
from config import BASE_URL, API_KEY, MODEL_NAME


class LLMClient:
    """A client for interacting with the LLM to generate quiz questions.

    Attributes
    ----------
    api_key : str
        The API key for the LLM service.
    model : str
        The model to use for generating questions.
    temperature : float
    """

    def __init__(
        self, base_url: str, api_key: str, model_name: str, temperature: float = 0.7
    ):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model_name
        self.temperature = temperature

    def generate_questions(
        self, topic: str, difficulty: str, num_questions: int = 5
    ) -> QuestionStore:
        """Generate quiz questions based on a given topic.

        Parameters
        ----------
        topic : str
            The topic for which to generate questions.
        difficulty : str
            The difficulty level of the questions.
        num_questions : int
            The number of questions to generate.

        Returns
        -------
        QuestionStore
            A store containing the generated questions.
        """

        prompt = (
            f'Genera exactamente "{num_questions}" preguntas '
            f'de opción múltiple sobre el tema "{topic}", en español, '
            f'con un nivel de dificultad "{difficulty}".'
        )

        response = self.client.chat.completions.parse(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Eres un generador de cuestionarios que responde en JSON.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            temperature=self.temperature,
            response_format=QuestionStore,
        )

        event = response.choices[0].message.content

        try:
            result = QuestionStore.model_validate_json(event)
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            result = QuestionStore(store=[])

        return result


def create_client() -> LLMClient:
    """Factory function to create an LLMClient instance."""
    return LLMClient(BASE_URL, API_KEY, MODEL_NAME)
