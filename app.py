import streamlit as st
from services.llm_client import create_client
from functools import reduce


def main():
    # Initialize the LLM client
    client = create_client()

    # ---- Streamlit App ----
    st.title("🧠 QuizIA - Generador de cuestionarios con IA")

    with st.form("quiz_form"):
        topic = st.text_input(
            "Tema del cuestionario",
            placeholder="Ej. Historia de México, Polinomios, Programación en Python",
        )
        # dificultad = st.selectbox("Dificultad", ["Fácil", "Medio", "Difícil"])
        # tipo_pregunta = st.selectbox("Tipo de pregunta", ["Opción múltiple", "Verdadero/Falso"])
        n_questions = st.number_input(
            "Número de preguntas", min_value=1, max_value=10, value=3
        )
        submit = st.form_submit_button("Generar cuestionario")

    if submit and topic:
        # Llamar al modelo para generar preguntas
        quiz_store = client.generate_questions(topic, int(n_questions))
        preguntas = quiz_store.store  # Lista de dicts con pregunta, opciones, respuesta_correcta

        respuestas_usuario = {}

        with st.form("respuestas_form"):
            for p in preguntas:
                respuesta = st.radio(
                    p.pregunta,
                    options=p.opciones,
                    key=p.pregunta
                )
                respuestas_usuario[p.pregunta] = respuesta

            enviar_respuestas = st.form_submit_button("Enviar respuestas")

        if enviar_respuestas:
            # Evaluación funcional
            evaluacion = list(
                map(lambda p: p.respuesta_correcta == respuestas_usuario.get(p.pregunta), preguntas)
            )

            total_correctas = reduce(lambda acc, val: acc + int(val), evaluacion, 0)

            st.success(f"Respondiste correctamente {total_correctas} de {len(preguntas)} preguntas")

            for i, (p, correcto) in enumerate(zip(preguntas, evaluacion)):
                if correcto:
                    st.write(f"✅ {p.pregunta}")
                else:
                    st.write(f"❌ {p.pregunta} (Correcta: {p.respuesta_correcta})")


if __name__ == "__main__":
    main()
