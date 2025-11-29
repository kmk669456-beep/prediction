import streamlit as st
import pickle
import numpy as np

# ==============================
# 1) 모델 불러오기
# ==============================
model = pickle.load(open("model.pkl", "rb"))

st.title("올림픽공원 입장객 예측 서비스 (날씨 + 이벤트 기반)")

st.write("아래 변수들을 입력하면, 해당 시점의 올림픽공원 예상 입장객 수를 예측합니다.")

# ==============================
# 2) 사용자 입력값
# ==============================

show_cnt = st.number_input("공연 건수", 0, 50, 0)

max_temp = st.number_input("최고기온(℃)", -20.0, 45.0, 20.0)
wind_avg = st.number_input("평균풍속(m/s)", 0.0, 50.0, 2.0)
temp_max_avg = st.number_input("평균최고기온(℃)", -20.0, 45.0, 15.0)
temp_avg = st.number_input("평균기온(℃)", -20.0, 40.0, 10.0)
temp_min_avg = st.number_input("평균최저기온(℃)", -30.0, 35.0, 5.0)
wind_max = st.number_input("최대풍속(m/s)", 0.0, 60.0, 5.0)
temp_min = st.number_input("최저기온(℃)", -30.0, 35.0, 0.0)
holiday = st.number_input("공휴일 수", 0, 10, 0)

# ==============================
# 3) 예측 실행
# ==============================

if st.button("예측하기"):
    
    # 입력 순서 = 모델 학습 순서 그대로
    features = np.array([[ 
        show_cnt,
        max_temp,
        wind_avg,
        temp_max_avg,
        temp_avg,
        temp_min_avg,
        wind_max,
        temp_min,
        holiday
    ]])

    result = model.predict(features)
    pred_value = int(result[0])

    st.success(f"예측된 올림픽공원 입장객 수: **{pred_value:,}명**")
