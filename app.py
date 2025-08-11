import streamlit as st

from services.llm_client import create_client
from utils.helpers import performance_message, format_question_results

import utils.session_state as ss_utils
from components.welcome import welcome_page
from models.quiz_engine import QuizEngine


def main():
    # Initialize the LLM client
    client = create_client()

    # ---- Streamlit App ----
    st.title("🧠 QuizIA - Generador de cuestionarios con IA")

    # Initialize session state
    ss_utils.initialize()

    # Sidebar with the quiz configuration
    with st.sidebar:
        st.header("⚙️ Configuración del cuestionario")

        # Topic input
        topic = st.text_input(
            "📚 Tema del cuestionario",
            placeholder="Ej. Historia de México, Polinomios, Programación en Python",
            key="topic_input",
            help="Ingresa el tema sobre el cual quieres generar preguntas",
        )

        # Difficulty level (optional for future implementation)
        difficulty = st.selectbox(
            "🎯 Dificultad",
            ["Fácil", "Medio", "Difícil"],
            key="difficulty_select",
            help="Selecciona el nivel de dificultad",
        )

        # Number of questions
        num_questions = st.number_input(
            "🔢 Número de preguntas",
            min_value=1,
            max_value=10,
            value=3,
            key="num_questions_input",
            help="Cantidad de preguntas a generar (1-10)",
        )

        st.divider()

        # Generate quiz button
        generate_button = st.button(
            "🚀 Generar cuestionario",
            type="primary",
            use_container_width=True,
            disabled=not topic.strip() or st.session_state.quiz_generated,
        )

        # Quiz generation process
        if generate_button and topic.strip():
            with st.spinner("Generando cuestionario..."):
                try:
                    quiz_store = client.generate_questions(
                        topic, difficulty, int(num_questions)
                    )
                    ss_utils.generated_state(QuizEngine(quiz_store))
                    st.success("¡Cuestionario generado exitosamente!")
                except Exception as e:
                    st.error(f"Error al generar el cuestionario: {str(e)}")

    # -- Main content area --
    if not st.session_state.quiz_generated:
        welcome_page()
    else:
        quiz_questions = st.session_state.quiz_engine.questions

        st.markdown(f"### 📝 Cuestionario: {st.session_state.topic_input}")
        st.markdown(
            f"**Dificultad:** {difficulty} | **Preguntas:** {len(quiz_questions)}"
        )

        if not st.session_state.quiz_submitted:
            # Quiz form
            with st.form("quiz_form"):
                st.markdown("---")
                for i, question in enumerate(quiz_questions, 1):
                    st.markdown(f"#### Pregunta {i}")
                    answer = st.radio(
                        question.question_text,
                        options=question.options,
                        key=f"question_{i}",
                        index=None,
                    )
                    if answer:
                        st.session_state.quiz_engine.update_answer(i - 1, answer)

                st.markdown("---")
                submit_button = st.form_submit_button(
                    "📤 Enviar respuestas", type="primary", use_container_width=True
                )

            # On submit
            if submit_button:
                # if all questions are answered
                if st.session_state.quiz_engine.is_all_answered():
                    st.session_state.quiz_submitted = True
                    st.rerun()
                else:
                    st.warning(
                        "⚠️ Por favor responde todas las preguntas antes de enviar."
                    )

        else:
            st.markdown("### 🎉 Resultados del cuestionario")

            evaluation_results, correct_count = st.session_state.quiz_engine.evaluate()
            total_questions = len(evaluation_results)

            # Calculate score percentage
            score_percentage = (
                (correct_count / total_questions * 100) if total_questions > 0 else 0.0
            )

            # Display score
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Respuestas correctas", f"{correct_count}/{total_questions}")
            with col2:
                st.metric("Porcentaje", f"{score_percentage:.1f}%")
            with col3:
                message, status = performance_message(score_percentage)
                getattr(st, status, st.info)(message)

            # -- Detailed review section --
            st.markdown("---")
            st.markdown("#### 📊 Revisión detallada:")

            formatted_results = format_question_results(st.session_state.quiz_engine)

            # display results
            for result in formatted_results:
                with st.expander(
                    f"Pregunta {result['index']} {'✅' if result['is_correct'] else '❌'}"
                ):
                    st.write(f"**Pregunta:** {result['question_text']}")
                    st.write(f"**Tu respuesta:** {result['user_answer']}")
                    st.write(f"**Respuesta correcta:** {result['correct_answer']}")

                    if result["is_correct"]:
                        st.success("¡Correcto!")
                    else:
                        st.error("Incorrecto")

            # Option to retake quiz or start new topic
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Repetir cuestionario", use_container_width=True):
                    st.session_state.quiz_submitted = False
                    st.session_state.quiz_engine.reset_answers()
                    st.rerun()
            with col2:
                if st.button("📝 Nuevo tema", use_container_width=True):
                    ss_utils.reset_all()
                    st.rerun()


if __name__ == "__main__":
    main()
