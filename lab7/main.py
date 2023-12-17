import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

from clusterization import fcm, normalize, clusters_sil

colors_pull = ['aquamarine', 'lightcoral', 'mediumseagreen', 'orchid', 'lightskyblue', 'gold',
               'tomato', 'cornflowerblue', 'palegreen', 'lightpink', 'skyblue', 'palevioletred',
               'lightseagreen', 'lavender', 'lightsteelblue', 'palegoldenrod', 'mediumslateblue',
               'mediumaquamarine', 'thistle']

index_color_dict = {str(index): color for index, color in enumerate(colors_pull)}


cluster_count = st.sidebar.number_input('Число кластеров', 2, 10)
fuzzy_value = st.sidebar.number_input('Значение фазификации', min_value=1.01, value=2.0)
max_iteration_count = st.sidebar.number_input('Максимальное число итераций', min_value=1, max_value=100, value=10)
eps = st.sidebar.number_input('Параметр сходимости', min_value=0.0001, value=0.1)
point_size = st.sidebar.number_input('Размер точки', min_value=10, max_value=50, value=15)

prepared_data = [[1.0, 1.2], [1.5, 1.8], [1.2, 1.5], [1.8, 1.2], [1.6, 1.6], [4.0, 4.2], [4.5, 4.8], [4.2, 4.5],
                 [4.8, 4.2],
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
cluster_relation = []
for i in range(len(data)):
    el = result[i]
    max_atr_index = el.index(max(el))
    cluster_relation.append(max_atr_index)
    
scatter_data = {'x': x_values, 'y': y_values, 'cluster': cluster_relation }
df = pd.DataFrame(scatter_data)
df['cluster'] = df['cluster'].astype(str)
fig = px.scatter(df, x='x', y='y', color='cluster', color_discrete_map=index_color_dict)
fig.update_traces(marker=dict(size=point_size))
st.subheader("Результаты четкой кластеризации")
with st.expander("Развернуть", True):
    st.plotly_chart(fig)
st.divider()

sil, sil_assessments, total_assessment = clusters_sil(data, 2, cluster_relation, cluster_count)

x = []
y = []
i = 0
j = 0
colors = []
for cluster_objects in sil:
    for obj in cluster_objects:
        x.append(obj)
        y.append(i)
        i = i + 1
    colors = colors + [colors_pull[j % len(colors_pull)], ] * len(cluster_objects)
    j = j + 1
x.reverse()
colors.reverse()

fig = go.Figure(data=[go.Bar(
    x=x,
    y=y,
    marker_color=colors,
    orientation='h'
)])

st.subheader("Результаты оценки кластерного силуэта")
with st.expander("Развернуть", True):
    st.plotly_chart(fig)

for i in range(cluster_count):
    color = colors_pull[i % len(colors_pull)]
    text = "Оценка силуэта кластера " + str(i) + " равна " + str(sil_assessments[i])
    st.markdown(f'<span style="color:{color}">{text}</span>', unsafe_allow_html=True)
st.write("Общая силуэтная оценка: " + str(total_assessment))
