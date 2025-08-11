"""
Welcome page component.
"""

import streamlit as st


def welcome_page() -> None:
    """Render of the welcome page"""

    st.markdown(
        """
    ### 👋 ¡Bienvenido a QuizIA!
    
    Para comenzar:
    1. **Ingresa un tema** en la barra lateral
    2. **Configura** la dificultad y número de preguntas
    3. **Haz clic** en "Generar cuestionario"
    
    El cuestionario aparecerá aquí una vez generado.
    """
    )

    # Example topics
    st.markdown("#### 💡 Ejemplos de temas:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📖 **Académicos**\n- Historia Mundial\n- Matemáticas\n- Ciencias")
    with col2:
        st.info("💻 **Tecnología**\n- Python\n- JavaScript\n- Bases de datos")
    with col3:
        st.info("🌍 **Generales**\n- Geografía\n- Cultura general\n- Deportes")

    st.markdown("---")
    with st.expander("💡 Consejos para mejores resultados"):
        st.markdown(
            """
        - **Sé específico**: En lugar de "Historia", prueba "Guerra de Independencia de México"
        - **Usa términos técnicos**: Para temas especializados, incluye vocabulario específico
        - **Ajusta la dificultad**: Comienza con "Fácil" para temas nuevos
        """
        )
