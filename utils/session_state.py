import streamlit as st
from models.quiz_engine import QuizEngine

_default_vars = {
    "quiz_generated": False,
    "quiz_engine": None,
    "quiz_submitted": False,
}


def initialize() -> None:
    """Initialize all session state variables."""

    for var, default_value in _default_vars.items():
        if var not in st.session_state:
            st.session_state[var] = default_value


def generated_state(quiz_engine: QuizEngine) -> None:
    """Set the generated quiz state.

    Parameters
    ----------
    quiz_engine: QuizEngine
        The QuizEngine instance containing the generated quiz data.
    """

    st.session_state.quiz_engine = quiz_engine
    st.session_state.quiz_generated = True
    st.session_state.quiz_submitted = False


def reset_all() -> None:
    """Reset all session state variables to default values."""

    for var, default_value in _default_vars.items():
        st.session_state[var] = default_value
