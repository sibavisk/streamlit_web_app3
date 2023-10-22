import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt

with st.form(key='profile_form'):
  #テキストボックス
  name = st.text_input('名前')
  address = st.text_input('住所')

#セレクトボックスにしたい場合は st.selectbox ラジオにしたい場合は、st,radio
  age_category = st.radio(
    '年齢',
    ('子ども(18才未満)', '大人(18才以上)'))
  
  #複数選択
  hobby = st.multiselect(
    '趣味',
    ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理'))

  #ボタン
  submit_btn = st.form_submit_button('送信')
  cancel_btn = st.form_submit_button('キャンセル')
if submit_btn and name and address:  # 送信ボタンが押されて、名前と住所が入力されている場合
    st.text(f'ようこそ！{name}さん！{address}に書籍を送りました！')
    st.text(f'年齢:{age_category}')
    st.text(f'趣味:{", ".join(hobby)}')
elif submit_btn and (not name or not address):  # 送信ボタンが押されて、名前や住所が空の場合
    st.text('内容を入力してください')
elif cancel_btn:
    st.text(f'キャンセルされました')