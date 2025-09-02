import streamlit as st

# CSS 스타일 적용
st.markdown("""
<style>
    /* 버튼 색상 커스텀 */
    .stButton>button {
        background-color: #4CAF50;  /* 초록색 계열 */
        color: white;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;  /* 호버 시 색상 변경 */
    }
    
    /* 특정 버튼 별도 색상 지정 */
    #video-btn { background-color: #FF5722 !important; }  /* 주황색 */
    #talk-btn { background-color: #2196F3 !important; }   /* 파란색 */
    #ppt-btn { background-color: #9C27B0 !important; }     /* 보라색 */
    
    /* 강조 텍스트 스타일 */
    .highlight {
        font-weight: bold;
        color: #FF5722;  /* 주황색 */
    }
    .note {
        font-size: 14px;
        color: #666;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀
st.write("# 행복에  투자 해라! 👋")

# 설명 텍스트 (bold 및 색상 적용)
st.markdown("""
<span class="highlight">행복은 어디애 있나요,  만들어야 하나요</span>  
여기 Kevin이 맛깔나게  풀어 봅니다.  
<span class="highlight">아래 3편을 의미 있게 보시길</span>  
""", unsafe_allow_html=True)   
   
# # 대화 링크 버튼
st.link_button("대화 를 통해 듣기", "https://youtu.be/5k0ywIUIMCQ")

# Video 링크 버튼
st.link_button("Video 를 통해 보기", "https://youtu.be/Qi89LZ4nwBg")

# # PPT 링크 버튼
st.link_button("PPT 를 통해 보기", "https://kevinoh-happy00.streamlit.app/")
st.caption("화면이 안나오면 (zzz) 클릭하고 기다리면 됩니다, 1-2 분정도")

