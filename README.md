# 🧠 QuizIA - Generador de Cuestionarios con IA

QuizIA es una aplicación web interactiva que utiliza inteligencia artificial para generar cuestionarios personalizados sobre cualquier tema. La aplicación permite a los usuarios crear, realizar y evaluar cuestionarios de manera automática, lo que proporciona una experiencia de aprendizaje interactiva y adaptable.

## ✨ Características

- **Generación Automática de Preguntas**: Mediante modelos de IA (LLMs) se crean preguntas relevantes sobre el tema dado
- **Interfaz Intuitiva**: Diseño limpio y fácil de usar construido con Streamlit
- **Configuración Personalizable**: Permite ajustar varios parámetros del cuestionario
- **Evaluación Inmediata**: Calificación automática una vez finalizado el cuestionario

## 🛠️ Tecnologías Utilizadas

- **Python**: Lenguaje principal de desarrollo
- **Streamlit**: Framework para la interfaz web
- **LLM**: Para la generación de los cuestionarios
- **Pydantic**: Validación y modelado de datos
- **UV**: Gestión de dependencias y entorno virtual

## 📁 Estructura del Proyecto

```
quizia-app/
├── app.py                # Aplicación principal de Streamlit
├── config.py             # Configuración de la aplicación
├── pyproject.toml        # Configuración del proyecto y dependencias
├── components/
│   └── welcome.py        # Página de bienvenida
├── models/
│   ├── question.py       # Modelo para representar preguntas
│   └── quiz_engine.py    # Motor de funcionamiento del cuestionario
├── services/
│   └── llm_client.py     # Cliente para interactuar con el LLM
└── utils/
    ├── helpers.py        # Funciones auxiliares
    └── session_state.py  # Gestión del estado de sesión
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Tener UV instalado
- Un API Key de OpenAI (sí se utilizarán modelos cloud, de forma local no es necesario)

### Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/axldorian/quizia-app.git
   cd quizia-app
   ```

2. **Instala las dependencias usando UV**:
   ```bash
   uv sync
   ```

3. **Configura las variables de entorno**:
   - Crea un archivo `.env` en la raíz del proyecto y agrega los siguientes valores:
   ```text
   BASE_URL=https://api.example.com
   API_KEY=tu_clave_de_api_aquí
   MODEL_NAME=nombre_de_modelo_aquí
   ```

4. **Ejecuta la aplicación**:
   ```bash
   uv run streamlit run app.py
   ```

5. **Accede a la aplicación**:
   Abre tu navegador y ve a `http://localhost:8501`

## 💡 Uso de la Aplicación

1. **Configura tu cuestionario** en la barra lateral:
   - Ingresa el tema sobre el que quieres estudiar
   - Selecciona el nivel de dificultad (Fácil, Medio, Difícil)
   - Elige el número de preguntas (1-10)

2. **Genera el cuestionario** haciendo clic en "🚀 Generar cuestionario"

3. **Responde las preguntas** seleccionando la opción que consideres correcta

4. **Envía tus respuestas** y revisa los resultados

5. **Analiza tu rendimiento** con las métricas y revisión pregunta por pregunta

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Axel García** - [aisaac.gargon@gmail.com](mailto:aisaac.gargon@gmail.com)

## 🔮 Próximas Características

- [ ] Soporte para diferentes tipos de preguntas
- [ ] Exportación de resultados a PDF
- [ ] Historial de cuestionarios realizados