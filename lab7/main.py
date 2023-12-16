import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from clusterization import fcm, normalize, sil

cluster_count = st.sidebar.number_input('Число кластеров', 2, 10)
fuzzy_value = st.sidebar.number_input('Значение фазификации', min_value=1.01, value=2.0)
max_iteration_count = st.sidebar.number_input('Максимальное число итераций', min_value=1, max_value=100, value=10)
eps = st.sidebar.number_input('Параметр сходимости', min_value=0.0001, value=0.1)

prepared_data = [[1.0, 1.2], [1.5, 1.8], [1.2, 1.5], [1.8, 1.2], [1.6, 1.6], [4.0, 4.2], [4.5, 4.8], [4.2, 4.5], [4.8, 4.2],
        [4.6, 4.6], [8.0, 2.0], [8.5, 2.5], [8.2, 2.2], [8.8, 2.8], [8.6, 2.6]]

st.subheader("Входные данные")
with st.expander("Развернуть"):
    raw_data = st.data_editor(prepared_data)
st.divider()

data = normalize(raw_data, 2)

st.subheader("Нормированные данные")
with st.expander("Развернуть"):
    st.table(data)
st.divider()

result = fcm(data, 2, cluster_count, fuzzy_value, max_iteration_count, eps)

st.subheader("Результаты нечеткой кластеризации")
with st.expander("Развернуть"):
    st.table(result)
st.divider()

x_values = np.array(data)[:, 0]
y_values = np.array(data)[:, 1]
colors = ['red', 'green', 'blue', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'brown', 'pink', 'gray', 'lime',
          'olive', 'teal', 'navy', 'salmon', 'indigo', 'gold', 'tomato', 'darkgreen']
cluster_relation = []
cluster_relation_colors = []
for i in range(len(data)):
    el = result[i]
    max_atr_index = el.index(max(el))
    cluster_relation.append(max_atr_index)
    cluster_relation_colors.append(colors[max_atr_index])

fig, ax = plt.subplots()
scatter_plot = ax.scatter(x_values, y_values, color=cluster_relation_colors)
st.subheader("Результаты четкой кластеризации")
with st.expander("Развернуть", True):
    st.pyplot(fig)
st.divider()


norm_data = normalize(data, 2)
for i in range(len(data)):
    st.write(sil(norm_data, i, 2, cluster_relation, cluster_count))
