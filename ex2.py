import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="질병 증상별 권장 행동, 음식 및 약 가이드", layout="wide")

# 제목 및 소개
st.title("질병 증상별 권장 행동, 음식 및 약 가이드")
st.write("증상을 선택하면 도움이 되는 행동과 음식, 그리고 한국 약국에서 구할 수 있는 의약품 정보를 알려드립니다.")

# 증상 데이터베이스 생성
symptoms_data = {
    "두통": {
        "actions": [
            {"action": "충분한 수분 섭취", "effect": "탈수로 인한 두통 완화에 도움"},
            {"action": "어두운 곳에서 휴식", "effect": "빛 자극으로 인한 두통 감소"},
            {"action": "목과 어깨 스트레칭", "effect": "긴장성 두통 완화에 효과적"},
            {"action": "카페인 섭취 줄이기", "effect": "혈관성 두통 예방에 도움"}
        ],
        "foods": [
            {"food": "생강차", "benefit": "혈관 확장 및 염증 감소 효과"},
            {"food": "마그네슘이 풍부한 음식(아몬드, 시금치)", "benefit": "근육 이완 및 혈관 확장 효과"},
            {"food": "오메가-3 지방산(연어, 고등어)", "benefit": "염증 감소 효과"}
        ],
        "medications": [
            {"name": "해열진통제", "ingredients": "아세트아미노펜 (예: 타이레놀, 게보린)", "use": "통증 완화 및 해열"},
            {"name": "소염진통제", "ingredients": "이부프로펜, 덱시부프로펜 (예: 부루펜, 이지엔6)", "use": "염증성 통증 완화"}
        ],
        "avoid": ["장시간 스크린 노출", "스트레스 상황", "수면 부족", "초콜릿, 치즈, 와인(편두통 유발 가능성)"]
    },
    "감기/독감 증상": {
        "actions": [
            {"action": "충분한 휴식", "effect": "면역 체계 회복 촉진"},
            {"action": "따뜻한 수분 섭취", "effect": "탈수 방지 및 점액 완화"},
            {"action": "따뜻한 소금물로 가글", "effect": "인후통 완화 및 세균 감소"},
            {"action": "실내 습도 유지", "effect": "호흡기 점막 보호"}
        ],
        "foods": [
            {"food": "닭고기 수프", "benefit": "항염증 효과 및 수분 공급"},
            {"food": "생강, 꿀 차", "benefit": "인후통 완화 및 항염증 효과"},
            {"food": "마늘", "benefit": "항균, 항바이러스 효과"},
            {"food": "오렌지, 키위 등 비타민 C 풍부한 과일", "benefit": "면역력 강화 및 감기 기간 단축"}
        ],
        "medications": [
            {"name": "종합감기약", "ingredients": "복합 성분", "use": "발열, 두통, 콧물, 코막힘 등 여러 증상 동시 완화"},
            {"name": "기침/가래약", "ingredients": "진해거담제", "use": "기침 억제 및 가래 배출 도움"},
            {"name": "목감기약/스프레이", "ingredients": "소염 성분, 살균 성분", "use": "인후통 완화"},
            {"name": "코감기약", "ingredients": "항히스타민, 비충혈제거제", "use": "콧물, 코막힘 완화"}
        ],
        "avoid": ["과도한 신체 활동", "알코올 섭취", "담배", "유제품(점액 증가)"]
    },
    "소화불량": {
        "actions": [
            {"action": "소량씩 자주 먹기", "effect": "소화기관 부담 감소"},
            {"action": "천천히 식사하기", "effect": "공기 흡입 감소 및 소화 촉진"},
            {"action": "생강차 마시기", "effect": "위장 운동 촉진 및 구역감 완화"},
            {"action": "식후 가벼운 산책", "effect": "소화 촉진 및 위산 역류 방지"}
        ],
        "foods": [
            {"food": "바나나", "benefit": "위 점막 보호 및 소화 촉진"},
            {"food": "요구르트, 케피어 등 프로바이오틱스", "benefit": "장내 유익균 증가 및 소화 개선"},
            {"food": "파파야", "benefit": "소화 효소 함유로 소화 촉진"}
        ],
        "medications": [
            {"name": "제산제", "ingredients": "탄산칼슘, 수산화마그네슘 등", "use": "과도한 위산 중화 및 속쓰림 완화"},
            {"name": "소화제", "ingredients": "소화 효소제", "use": "음식물 소화 도움"},
            {"name": "정장제", "ingredients": "유산균 (프로바이오틱스)", "use": "장 건강 개선 및 소화 기능 도움"}
        ],
        "avoid": ["기름진 음식", "카페인", "과식", "매운 음식, 튀긴 음식"]
    },
    "근육통": {
        "actions": [
            {"action": "온찜질", "effect": "혈액순환 촉진 및 통증 완화"},
            {"action": "가벼운 스트레칭", "effect": "근육 긴장 완화 및 유연성 증가"},
            {"action": "충분한 수분 섭취", "effect": "근육 경련 예방 및 독소 배출"}
        ],
        "foods": [
            {"food": "연어, 참치 등 오메가-3 풍부한 생선", "benefit": "염증 감소 및 근육 회복 촉진"},
            {"food": "체리, 블루베리 등 항산화물질 풍부한 과일", "benefit": "염증 감소 및 근육 손상 회복"},
            {"food": "바나나, 감자 등 칼륨 풍부한 식품", "benefit": "근육 기능 개선 및 경련 방지"}
        ],
        "medications": [
            {"name": "근육통 완화 연고/파스", "ingredients": "살리실산메틸, 멘톨 등", "use": "국소 부위 통증 완화 및 염증 감소"},
            {"name": "경구 소염진통제", "ingredients": "이부프로펜, 나프록센 등", "use": "전신적인 근육통 및 염증 완화"}
        ],
        "avoid": ["격렬한 운동", "장시간 같은 자세 유지", "과도한 카페인 섭취", "알코올"]
    },
    "불면증": {
        "actions": [
            {"action": "규칙적인 수면 일정 유지", "effect": "생체 시계 조절 및 수면의 질 향상"},
            {"action": "취침 전 카페인 피하기", "effect": "수면 방해 요소 제거"},
            {"action": "취침 전 따뜻한 목욕", "effect": "체온 조절 및 이완 효과"}
        ],
        "foods": [
            {"food": "따뜻한 우유", "benefit": "트립토판 함유로 수면 유도 호르몬 생성 도움"},
            {"food": "체리", "benefit": "멜라토닌 함유로 수면 사이클 조절에 도움"},
            {"food": "호두, 아몬드", "benefit": "마그네슘, 멜라토닌 함유로 수면의 질 향상"}
        ],
        "medications": [
            {"name": "수면 유도제", "ingredients": "디펜히드라민, 독실아민 (일시적 불면증)", "use": "수면 유도 및 진정 효과 (지속 사용은 전문가와 상담)"}
        ],
        "avoid": ["취침 전 전자기기 사용", "낮잠", "취침 전 과식", "취침 전 음주 및 흡연"]
    },
    "알레르기": {
        "actions": [
            {"action": "정기적인 실내 청소", "effect": "알레르기 유발 물질 감소"},
            {"action": "공기 청정기 사용", "effect": "실내 공기 질 개선"},
            {"action": "비염 세척", "effect": "코 점막의 알레르기 물질 제거"}
        ],
        "foods": [
            {"food": "오메가-3 지방산(고등어, 들기름)", "benefit": "염증 반응 억제"},
            {"food": "사과, 양파 등 퀘르세틴 함유 식품", "benefit": "항히스타민 작용 및 염증 감소"},
            {"food": "유산균 (프로바이오틱스)", "benefit": "장 건강 개선 및 면역 조절"}
        ],
        "medications": [
            {"name": "항히스타민제", "ingredients": "세티리진, 로라타딘, 펙소페나딘 (예: 지르텍, 클라리틴, 알레그라)", "use": "알레르기 증상 (콧물, 재채기, 가려움 등) 완화"}
        ],
        "avoid": ["알레르기 유발 식품/물질 노출", "외출 후 손발 씻지 않기", "건조한 환경"]
    }
}

# 사이드바 - 증상 선택
st.sidebar.header("증상 선택")
selected_symptom = st.sidebar.selectbox(
    "어떤 증상에 대한 정보가 필요하신가요?",
    options=list(symptoms_data.keys())
)

# 메인 화면 - 선택된 증상에 대한 정보 표시
if selected_symptom:
    st.header(f"{selected_symptom}에 도움이 되는 정보")
    
    # 권장 행동과 효과 표시
    st.subheader("✅ 권장 행동")
    for i, action_info in enumerate(symptoms_data[selected_symptom]["actions"]):
        with st.expander(f"{i+1}. {action_info['action']}"):
            st.write(f"**효과:** {action_info['effect']}")
            
    # 권장 음식과 효능 표시
    st.subheader("🥕 권장 음식")
    for i, food_info in enumerate(symptoms_data[selected_symptom]["foods"]):
        with st.expander(f"{i+1}. {food_info['food']}"):
            st.write(f"**효능:** {food_info['benefit']}")

    # 권장 의약품 정보 표시
    st.subheader("💊 약국 의약품")
    for i, med_info in enumerate(symptoms_data[selected_symptom]["medications"]):
        with st.expander(f"{i+1}. {med_info['name']}"):
            st.write(f"**주요 성분 (예시):** {med_info['ingredients']}")
            st.write(f"**주요 용도:** {med_info['use']}")
    
    # 피해야 할 행동/음식 표시
    st.subheader("⚠️ 피해야 할 행동/음식")
    avoid_list = symptoms_data[selected_symptom]["avoid"]
    for i, avoid in enumerate(avoid_list):
        st.write(f"• {avoid}")
    
    # 추가 정보 - 의학적 조언 면책조항
    st.divider()
    st.info("이 정보는 일반적인 참고용이며, 개인의 건강 상태 및 증상에 따라 차이가 있을 수 있습니다. 심각한 증상이 있거나 의약품 복용 전에는 반드시 의사 또는 약사와 상담하세요.")

# 사용자 피드백 섹션
st.sidebar.divider()
st.sidebar.subheader("피드백")
feedback = st.sidebar.radio("이 정보가 도움이 되었나요?", ["", "매우 도움됨", "도움됨", "보통", "도움이 되지 않음"])
if feedback and feedback != "":
    st.sidebar.success("피드백 감사합니다!")

# 새로운 증상 제안 섹션
st.sidebar.divider()
st.sidebar.subheader("새로운 증상 제안")
new_symptom_suggestion = st.sidebar.text_area("추가하고 싶은 증상이나 정보가 있다면 알려주세요.")
if st.sidebar.button("제안하기"):
    if new_symptom_suggestion:
        st.sidebar.success(f"'{new_symptom_suggestion}' 증상 추가 제안 감사합니다! 다음 업데이트 시 참고하겠습니다.")
    else:
        st.sidebar.warning("제안할 증상을 입력해주세요.")

