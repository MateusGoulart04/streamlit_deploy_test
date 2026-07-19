#Yfinance = pega dados de mercado do yahoo e conecta com o python - biblioteca
## data.news -> pega várias notícias em relação aos dados da empresa
## data.major_holders -> mostra os maiores detentores de ações e as porcentagens que eles tem do total de ações
## ticker = st.session_state.tickercode -> para um imput na streamlit view entrar como ticker no código python

import yfinance as yf
import pandas as pd
import streamlit as st
from datetime import datetime

st.markdown('# Analisando empresas')

st.text_input('Ticker Code',key= 'tickercode',value= 'GOOG')

ticker = st.session_state.tickercode

data = yf.Ticker(ticker)

data_news = data.news
### print(data_news)

# Transformando o data.news em um df com título da notícia e o link
df_data_news = pd.DataFrame(data.news)

#Expandindo as informações da coluna 'content'
df_data_news_expanded = df_data_news['content'].apply(pd.Series)

### print(df_data_news_expanded.columns)

st.markdown(f'## Últimas Notícias: {st.session_state.tickercode}')

df_data_news_expanded2 = df_data_news_expanded[['title','pubDate','canonicalUrl']]
st.dataframe(df_data_news_expanded2)

end_date = datetime.now().strftime('%Y-%m-%d')
data_hist = data.history(period = 'max',start = '2022-01-01',end = end_date,interval = '5d')
data_hist = data_hist.reset_index()

### print(data_hist)

#data_hist é um dataframe em pandas

st.markdown('# Construa seu gráfico:')

eixo_y = st.selectbox('Eixo Y:',data_hist.columns)
eixo_x = st.selectbox('Eixo X:',data_hist.columns)

st.markdown(f'## Gráfico de {eixo_y} X {eixo_x}')
st.line_chart(data_hist,x= eixo_x,y= eixo_y)

