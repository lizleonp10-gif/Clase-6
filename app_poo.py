import streamlit as st
import statistics

# Clase para manejar información de una persona
class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludar(self):
        return f"Hola, me llamo {self.nombre}. ¡Mucho gusto en conocerte!"

    def obtener_edad(self):
        return f"Tengo {self.edad} años."

    def obtener_profesion(self):
        return f"Soy {self.profesion}."

# Clase para manejar cálculos con listas
class CalculadoraListas:
    def __init__(self):
        self.lista = []

    def agregar_numero(self, numero):
        self.lista.append(numero)
        st.success(f"✅ Número {numero} agregado a la lista.")
        st.write(f"📋 Lista actual: {self.lista}")  # Mostrar la lista actualizada

    def calcular_suma(self):
        return sum(self.lista)

    def calcular_promedio(self):
        return sum(self.lista) / len(self.lista) if self.lista else 0

    def calcular_maximo(self):
        return max(self.lista) if self.lista else None

    def calcular_minimo(self):
        return min(self.lista) if self.lista else None

    def calcular_desviacion_estandar(self):
        if len(self.lista) > 1:
            return round(statistics.stdev(self.lista), 3)
        return None

    def mostrar_estadisticas(self):
        if not self.lista:
            return "La lista está vacía."
        return f"""
        📊 **Estadísticas Descriptivas:**
        - **Suma:** {self.calcular_suma()}
        - **Promedio:** {self.calcular_promedio():.2f}
        - **Máximo:** {self.calcular_maximo()}
        - **Mínimo:** {self.calcular_minimo()}
        - **Desviación Estándar:** {self.calcular_desviacion_estandar() if self.calcular_desviacion_estandar() is not None else 'N/A'}
        """

# Interfaz de Streamlit
st.title("📊 Calculadora de Listas y Persona")

# Selección de página
pagina = st.sidebar.selectbox("Selecciona una página:", ["🏠 Home", "📋 Ejemplos"])

if pagina == "🏠 Home":
    st.header("🏠 Bienvenido a la Aplicación")
    st.write("Esta aplicación está construida con **Streamlit**, una herramienta poderosa para crear aplicaciones web interactivas con Python.")
    st.write("En este ejemplo, aprenderás cómo funcionan las clases en Python a través de dos casos prácticos:")
    st.markdown("1️⃣ **Clase Persona**: Para manejar información personal (nombre, edad, profesión).")
    st.markdown("2️⃣ **Clase Calculadora de Listas**: Para realizar cálculos estadísticos básicos sobre listas de números.")
    st.write("Selecciona una opción en el menú desplegable para explorar cada uno de los ejemplos.")
    st.write("Elaborado por Lizbeth León")

elif pagina == "📋 Ejemplos":
    tabs = st.tabs(["👤 Ejemplo de Persona", "📋 Ejemplo de Calculadora de Listas"])

    with tabs[0]:
        st.header("👤 Información de la Persona")
        nombre = st.text_input("Introduce tu nombre:")
        edad = st.number_input("Introduce tu edad:", min_value=0, step=1)
        profesion = st.text_input("Introduce tu profesión:")

        if st.button("Guardar Persona"):
            persona = Persona(nombre, edad, profesion)
            st.success(persona.saludar())
            st.info(persona.obtener_edad())
            st.info(persona.obtener_profesion())

    with tabs[1]:
        st.header("📋 Calculadora de Listas")

        if 'calculadora' not in st.session_state:
            st.session_state.calculadora = CalculadoraListas()

        numero = st.number_input("Introduce un número para agregar a la lista:", step=1.0)

        if st.button("Agregar número"):
            st.session_state.calculadora.agregar_numero(numero)

        if st.button("Mostrar estadísticas"):
            estadisticas = st.session_state.calculadora.mostrar_estadisticas()
            st.write(estadisticas)

        if st.button("Limpiar lista"):
            st.session_state.calculadora.lista = []
            st.info("🗑️ Lista limpiada con éxito.")



