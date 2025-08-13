import streamlit as st

# 학과별 이모지 매핑 정의 (지난번 코드에 몇 가지 더 추가했어요!)
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
    "화학과": "🧪", "생명과학과": "🧬", "지구과학과": "🌎",
    "도시공학과": "🏙️", "조경학과": "🌳", "환경공학과": "🌿",
    "에너지공학과": "⚡", "식품영양학과": "🥗", "의학과": "🏥",
    "수의학과": "🐾", "약학과": "💊", "경영정보학과": "📊"
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

st.title("🎓 나의 성격에 딱 맞는 학과는?")
st.write("MBTI의 4가지 지표를 직접 선택하여 나에게 어울리는 학과를 찾아보세요!")
st.write("❗ **이 추천은 참고용이며, 개인의 적성과 흥미가 가장 중요합니다!**")

st.markdown("---")
st.subheader("1. 에너지 방향 (어떤 곳에서 에너지를 얻나요?)")
selected_ei = st.radio(
    " ", # 라디오 버튼 위 불필요한 레이블 제거
    ["E (외향: 넓고 활동적인 관계를 선호)", "I (내향: 깊고 신중한 관계를 선호)"],
    index=None
)

st.subheader("2. 인식 기능 (어떤 방식으로 정보를 인지하나요?)")
selected_sn = st.radio(
    " ",
    ["S (감각: 오감으로 실제 경험을 중요시)", "N (직관: 영감과 미래 가능성을 중요시)"],
    index=None
)

st.subheader("3. 판단 기능 (어떤 방식으로 결정을 내리나요?)")
selected_tf = st.radio(
    " ",
    ["T (사고: 논리적이고 분석적으로 판단)", "F (감정: 사람과의 관계, 가치를 중요시 판단)"],
    index=None
)

st.subheader("4. 생활 양식 (어떤 방식으로 삶을 계획하나요?)")
selected_jp = st.radio(
    " ",
    ["J (판단: 체계적이고 계획적으로 행동)", "P (인식: 유연하고 상황에 맞춰 행동)"],
    index=None
)

st.markdown("---")

# 모든 선택이 완료되었는지 확인
if all([selected_ei, selected_sn, selected_tf, selected_jp]):
    # 선택된 값에서 첫 글자(MBTI 지표)만 추출하여 조합
    final_mbti = selected_ei[0] + selected_sn[0] + selected_tf[0] + selected_jp[0]

    # MBTI 추천 정보 가져오기
    if final_mbti in mbti_major_recommendations:
        full_recommendation_string = mbti_major_recommendations[final_mbti]
        
        # 추천 문자열을 학과 리스트 부분과 설명 부분으로 분리
        parts = full_recommendation_string.split('(')
        major_list_string = parts[0].strip()
        description_part = f"({parts[1]}" if len(parts) > 1 else ""

        # 개별 학과 이름 추출 및 이모지 추가
        individual_majors = [m.strip() for m in major_list_string.split(',')]
        
        formatted_majors_with_emojis = []
        for major in individual_majors:
            emoji = major_emojis.get(major, "❓") # major_emojis에 없는 학과는 '?'로 표시
            formatted_majors_with_emojis.append(f"{emoji} {major}")
        
        # 이모지가 추가된 학과 리스트를 하나의 문자열로 결합
        display_string = ", ".join(formatted_majors_with_emojis)
        
        st.markdown(f"### 🎉 당신의 MBTI는 **{final_mbti}** 이군요!")
        st.markdown(f"**{final_mbti}** 유형에게 추천하는 학과는 다음과 같습니다:")
        st.info(f"**{display_string.strip()}**")
        
        # 설명 부분은 따로 표시
        if description_part:
            st.markdown("---")
            clean_description = description_part.strip('() ')
            st.write(f"💡 **{final_mbti}** 유형은 주로 **{clean_description}** 특성을 가집니다.")
        
        st.success("😊 진로 탐색은 흥미로운 여정이에요! 자신의 강점과 관심사를 찾아보세요.")
    else:
        st.warning(f"아직 **{final_mbti}** 유형에 대한 추천 정보가 없습니다. 관리자에게 문의해주세요!")
else:
    st.info("⬆️ 위 4가지 질문에 모두 답변해주세요! 😊")

st.markdown("---")
st.caption("진로에 대한 고민은 언제든지 함께 나눌 수 있어요! 힘내세요, 김하윤님! 💪")
