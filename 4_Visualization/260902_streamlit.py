# 문항 1. 다양한 시각화 차트 생성
# seaborn의 iris 데이터셋을 활용해 다음의 그래프를 그려보세요.

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

iris = sns.load_dataset('iris')

fig1, ax1 = plt.subplots()
ax1.scatter(iris['sepal_length'], iris['sepal_width'], color='navy')
ax1.set_xlabel('꽃받침 길이 (sepal_length)')
ax1.set_ylabel('꽃받침 너비 (sepal_width)')
ax1.set_title('붓꽃 꽃받침 크기')
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.histplot(data=iris, x='petal_length', bins=20, kde=True, ax=ax2)
ax2.set_title('꽃잎 길이는 몇 개나 있을까?')
st.pyplot(fig2)

fig3, ax3 = plt.subplots()
sns.boxplot(data=iris, x='species', y='petal_length', ax=ax3)
ax3.set_title('꽃 종류별 꽃잎 길이 비교')
st.pyplot(fig3)

fig4 = px.scatter(iris, x='sepal_length', y='sepal_width', color='species',
                   title='마우스로 확대/축소 되는 산점도')
st.plotly_chart(fig4)

fig5 = px.line(iris, x='sepal_length', y='sepal_width', color='species',
               title='선으로 이어본 그래프')
st.plotly_chart(fig5)

# 문항 2. Plotly를 활용한 인터랙티브한 그래프 구현
# update_layout을 활용하여 드롭다운 메뉴로 species를 선택할 수 있도록 대시보드 레이아웃을 구현해보세요.

import streamlit as st
import seaborn as sns
import plotly.express as px

iris = sns.load_dataset('iris')
species_list = iris['species'].unique().tolist() 

fig = px.scatter(iris, x='sepal_length', y='sepal_width', color='species')

buttons = [
    dict(
        label='All',
        method='update',
        args=[{'visible': [True] * len(species_list)}, {'title': 'All Species'}]
    )
]

for i, sp in enumerate(species_list):
    visible_list = [j == i for j in range(len(species_list))]  # 이 종류만 True
    buttons.append(dict(
        label=sp.capitalize(),
        method='update',
        args=[{'visible': visible_list}, {'title': sp.capitalize()}]
    ))

fig.update_layout(
    updatemenus=[dict(buttons=buttons, direction='down', x=0, y=1.15)],
    title='All Species'
)

st.plotly_chart(fig)