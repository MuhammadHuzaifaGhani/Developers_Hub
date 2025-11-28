# app.py
# 🌸 Iris Dataset Explorer — Streamlit App
# This app loads, inspects, and visualizes the Iris dataset.

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import sys

st.set_page_config(page_title="Iris Dataset Explorer", page_icon="🌸", layout="wide")

st.title("🌸 Iris Dataset Explorer")
st.write("Load, inspect, and visualize the Iris dataset.")

# ===========================================
# Load Dataset
# ===========================================

st.header("📂 Load Dataset")
iris = sns.load_dataset("iris")
st.success("Dataset loaded successfully!")

# ===========================================
# Basic Information
# ===========================================

st.header("📊 Dataset Information")

st.subheader("🔹 Shape of Dataset")
st.write(iris.shape)

st.subheader("🔹 Column Names")
st.write(iris.columns.tolist())

st.subheader("🔹 Full Dataset")
st.write(iris.__dataframe__())

# info() does not return text normally → capture it
st.subheader("🔹 Dataset Info")
buffer = io.StringIO()
iris.info(buf=buffer)
info_text = buffer.getvalue()
st.text(info_text)

st.subheader("🔹 Summary Statistics (describe())")
st.write(iris.describe())

# ===========================================
# Visualization Section
# ===========================================

st.header("📈 Data Visualizations")

# -------- Scatter Plot --------
st.subheader("🔸 Scatter Plot — Feature Relationship")

x_axis = st.selectbox("Select X-axis feature", iris.columns[:-1])
y_axis = st.selectbox("Select Y-axis feature", iris.columns[:-1])

fig, ax = plt.subplots()
sns.scatterplot(data=iris, x=x_axis, y=y_axis, hue="species", ax=ax)
st.pyplot(fig)

# -------- Histograms --------
st.subheader("🔸 Histograms — Value Distribution")

feature = st.selectbox("Select a feature for histogram", iris.columns[:-1])

fig2, ax2 = plt.subplots()
sns.histplot(iris[feature], kde=True, ax=ax2)
st.pyplot(fig2)

# -------- Box Plot --------
st.subheader("🔸 Box Plot — Outliers Detection")

feature2 = st.selectbox("Select a feature for box plot", iris.columns[:-1])

fig3, ax3 = plt.subplots()
sns.boxplot(data=iris, y=feature2, ax=ax3)
st.pyplot(fig3)

st.success("All tasks completed: data loaded, inspected, and visualized!")
