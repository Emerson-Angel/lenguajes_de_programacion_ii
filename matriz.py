import streamlit as st
import pandas as pd
import numpy as np

class MatrixOperations:
    def __init__(self, file_path):
        self.matrix = pd.read_csv(file_path, header=None).values

    def sum_of_elements(self):
        return np.sum(self.matrix)

    def product_of_elements(self):
        return np.prod(self.matrix)

    def transpose(self):
        return self.matrix.T

    def determinant(self):
        return np.linalg.det(self.matrix)

    def inverse(self):
        det = self.determinant()
        if det == 0:
            return "La matriz es singular y no tiene inversa."
        else:
            return np.linalg.inv(self.matrix)

st.title("Operaciones con Matrices")

# Cargar archivo CSV
uploaded_file = st.file_uploader("Selecciona un archivo CSV", type="csv")

if uploaded_file is not None:
    # Crear instancia de MatrixOperations
    matrix_ops = MatrixOperations(uploaded_file)

    # Mostrar resultados
    st.header("1. Suma de elementos")
    st.write(matrix_ops.sum_of_elements())

    st.header("2. Producto de elementos")
    st.write(matrix_ops.product_of_elements())

    st.header("3. Transpuesta")
    st.write(matrix_ops.transpose())

    st.header("4. Determinante")
    st.write(matrix_ops.determinant())

    st.header("5. Inversa")
    st.write(matrix_ops.inverse())