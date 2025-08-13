import streamlit as st

# 학과별 이모지 매핑 정의
# 여기에 더 많은 학과와 어울리는 이모지를 추가해 보세요!
major_emojis = {
    "경영학과": "💼", "컴퓨터공학과": "💻", "회계학과": "💰",
    "간호학과": "👩‍⚕️", "유아교육과": "🧸", "사회복지학과": "🤝",
    "심리학과": "🧠", "교육학과": "🍎", "문예창작학과": "✍️",
    "인공지능학과": "🤖", "통계학과": "📊", "기계공학과": "⚙️",
    "건축학과": "🏗️", "체육학과": "🏃‍♂️", "미술학과": "🎨",
    "디자인학과": "🖌️", "음악학과": "🎶", "철학과": "🤔",
    "수학과": "➕", "물리학과": "⚛️", "스포츠경영학과": "🏆",
    "마케팅학과": "📈", "경찰행정학과": "👮‍♀️", "연극영화학과": "🎭",
    "관광경영학과": "✈️", "실용음악과": "🎤", "광고홍보학과": "📣",
    "상담학과": "🗣️", "창업학과": "💡", "신문방송학과": "📺",
    "법학과": "⚖️", "행정학과": "🏛️", "외교학과": "🌍",
    "국어국문학과": "📚", "영어영문학과": "🇬🇧", "역사학과": "📜",
    "화학과": "🧪", "생명과학과": "🧬", "지구과학과": "🌎", # 김하윤님 활동에 맞춰 지구과학과 추가!
    "도시공학과": "🏙️", "조경학과": "🌳"
}

# MBTI 유형별 추천 학과 정의 (예시)
# 이 부분은 김하윤님이 생각하는 MBTI와 학과의 연관성에 따라 자유롭게 수정하고 추가해 보세요!
mbti_major_recommendations = {
    "ISTJ": "경영학과, 컴퓨터공학과, 회계학과 (실용적이고 체계적인 분야)",
    "ISFJ": "간호학과, 유아교육과, 사회복지학과 (타인을 돕고 돌보는 분야)",
    "INFJ": "심리학과, 교육학과, 문예창작학과 (통찰력과 사람 이해)",
    "INTJ": "컴퓨터공학과, 인공지능학과, 통계학과 (전략적이고 분석적인 분야)",
    "ISTP": "기계공학과, 건축학과, 체육학과 (실용적이고 활동적인 분야)",
    "ISFP": "미술학과, 디자인학과, 음악학과 (예술적이고 자유로운 분야)",
    "INFP": "문예창작학과, 철학과, 심리학과 (이상적이고 창의적인 분야)",
    "INTP": "수학과, 물리학과, 컴퓨터공학과 (논리적이고 이론적인 분야)",
    "ESTP": "스포츠경영학과, 마케팅학과, 경찰행정학과 (활동적이고 현실적인 분야)",
    "ESFP": "연극영화학과, 관광경영학과, 실용음악과 (사교적이고 경험을 중시하는 분야)",
    "ENFP": "광고홍보학과, 심리학과, 상담학과 (열정적이고 관계 지향적인 분야)",
    "ENTP": "창업학과, 신문방송학과, 경영학과 (새로운 아이디어를 탐구하는 분야)",
    "ESTJ": "경영학과, 법학과, 행정학과 (체계적이고 리더십이 요구되는 분야)",
    "ESFJ": "유아교육과, 간호학과, 사회복지학과 (사람들과 함께하고 협력하는 분야)",
    "ENFJ": "교육학과, 외교학과, 상담학과 (타인의 성장을 돕고 이끄는 분야)",
    "ENTJ": "경영학과, 정치외교학과, 법학과 (전략적이고 리더십을 발휘하는 분야)"
}

st.set_page_config(
    page_title="김하윤님의 MBTI 학과 추천 앱",
    page_icon="🎓"
)

st.title("🎓 나의 MBTI는 어떤 학과와 어울릴까?")
st.write("나의 MBTI 유형을 선택하면, 어울리는 학과를 추천해 드릴게요!")
st.write("❗ **이 추천은 참고용이며, 개인의 적성과 흥미가 가장 중요합니다!**")

# MBTI 유형 선택
selected_mbti = st.selectbox(
    "당신의 MBTI 유형은 무엇인가요?",
    list(mbti_major_recommendations.keys()),
    index=None, # 초기 선택 없음
    placeholder="MBTI 유형을 선택해주세요"
)

if selected_mbti:
    full_recommendation_string = mbti_major_recommendations[selected_mbti]
    
    # 추천 문자열을 학과 리스트 부분과 설명 부분으로 분리
    parts = full_recommendation_string.split('(')
    major_list_string = parts[0].strip() # 예: "경영학과, 컴퓨터공학과, 회계학과"
    description_part = f"({parts[1]}" if len(parts) > 1 else "" # 예: "(실용적이고 체계적인 분야)"

    # 개별 학과 이름 추출 및 이모지 추가
    individual_majors = [m.strip() for m in major_list_string.split(',')]
    
    formatted_majors_with_emojis = []
    for major in individual_majors:
        emoji = major_emojis.get(major, "❓") # major_emojis에 없는 학과는 '?'로 표시
        formatted_majors_with_emojis.append(f"{emoji} {major}")
    
    # 이모지가 추가된 학과 리스트를 하나의 문자열로 결합
    display_string = ", ".join(formatted_majors_with_emojis)
    
    st.markdown(f"### 🎉 {selected_mbti} 유형에게 추천하는 학과는 다음과 같습니다:")
    st.info(f"**{display_string.strip()}**")
    
    # 설명 부분은 따로 표시
    if description_part:
        st.markdown(f"---")
        # 괄호를 제거하고 설명만 표시
        clean_description = description_part.strip('() ')
        st.write(f"🤔 **{selected_mbti}** 유형은 주로 **{clean_description}** 특성을 가집니다.")
    
    st.success("😊 진로 탐색은 흥미로운 여정이에요! 자신의 강점과 관심사를 찾아보세요.")

st.markdown("---")
st.caption("궁금한 점이 있다면 언제든지 물어보세요! 😄")

