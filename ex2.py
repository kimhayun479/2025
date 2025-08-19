import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="질병 증상별 권장 행동 가이드", layout="wide")

# 제목 및 소개
st.title("질병 증상별 권장 행동 가이드")
st.write("증상을 선택하면 도움이 되는 행동과 그 효과를 알려드립니다.")

# 증상 데이터베이스 생성 (실제 앱에서는 더 많은 증상과 정보 추가 가능)
symptoms_data = {
    "두통": {
        "actions": [
            {"action": "충분한 수분 섭취", "effect": "탈수로 인한 두통 완화에 도움"},
            {"action": "어두운 곳에서 휴식", "effect": "빛 자극으로 인한 두통 감소"},
            {"action": "목과 어깨 스트레칭", "effect": "긴장성 두통 완화에 효과적"},
            {"action": "카페인 섭취 줄이기", "effect": "혈관성 두통 예방에 도움"}
        ],
        "avoid": ["장시간 스크린 노출", "스트레스 상황", "수면 부족"]
    },
    "감기/독감 증상": {
        "actions": [
            {"action": "충분한 휴식", "effect": "면역 체계 회복 촉진"},
            {"action": "따뜻한 수분 섭취", "effect": "탈수 방지 및 점액 완화"},
            {"action": "따뜻한 소금물로 가글", "effect": "인후통 완화 및 세균 감소"},
            {"action": "실내 습도 유지", "effect": "호흡기 점막 보호"}
        ],
        "avoid": ["과도한 신체 활동", "알코올 섭취", "담배"]
    },
    "소화불량": {
        "actions": [
            {"action": "소량씩 자주 먹기", "effect": "소화기관 부담 감소"},
            {"action": "천천히 식사하기", "effect": "공기 흡입 감소 및 소화 촉진"},
            {"action": "생강차 마시기", "effect": "위장 운동 촉진 및 구역감 완화"},
            {"action": "식후 가벼운 산책", "effect": "소화 촉진 및 위산 역류 방지"}
        ],
        "avoid": ["기름진 음식", "카페인", "과식"]
    },
    "근육통": {
        "actions": [
            {"action": "온찜질", "effect": "혈액순환 촉진 및 통증 완화"},
            {"action": "가벼운 스트레칭", "effect": "근육 긴장 완화 및 유연성 증가"},
            {"action": "충분한 수분 섭취", "effect": "근육 경련 예방 및 독소 배출"},
            {"action": "마그네슘이 풍부한 음식 섭취", "effect": "근육 기능 개선"}
        ],
        "avoid": ["격렬한 운동", "장시간 같은 자세 유지"]
    },
    "불면증": {
        "actions": [
            {"action": "규칙적인 수면 일정 유지", "effect": "생체 시계 조절 및 수면의 질 향상"},
            {"action": "취침 전 카페인 피하기", "effect": "수면 방해 요소 제거"},
            {"action": "취침 전 따뜻한 목욕", "effect": "체온 조절 및 이완 효과"},
            {"action": "침실 환경 최적화 (온도, 소음, 빛)", "effect": "수면에 적합한 환경 조성"}
        ],
        "avoid": ["취침 전 전자기기 사용", "낮잠", "취침 전 과식"]
    },
    "알레르기": {
        "actions": [
            {"action": "정기적인 실내 청소", "effect": "알레르기 유발 물질 감소"},
            {"action": "공기 청정기 사용", "effect": "실내 공기 질 개선"},
            {"action": "비염 세척", "effect": "코 점막의 알레르기 물질 제거"},
            {"action": "항알레르기 음식 섭취 (오메가-3 등)", "effect": "면역 반응 조절"}
        ],
        "avoid": ["알레르기 유발 식품", "외출 후 즉시 샤워하지 않기", "반려동물과 너무 가까이 지내기"]
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
    st.header(f"{selected_symptom}에 도움이 되는 행동")
    
    # 권장 행동과 효과 표시
    for i, action_info in enumerate(symptoms_data[selected_symptom]["actions"]):
        with st.expander(f"{i+1}. {action_info['action']}"):
            st.write(f"**효과:** {action_info['effect']}")
    
    # 피해야 할 행동 표시
    st.header("피해야 할 행동")
    avoid_list = symptoms_data[selected_symptom]["avoid"]
    for i, avoid in enumerate(avoid_list):
        st.write(f"{i+1}. {avoid}")
    
    # 추가 정보 - 의학적 조언 면책조항
    st.divider()
    st.info("이 정보는 일반적인 참고용이며, 심각한 증상이 있는 경우 반드시 의료 전문가와 상담하세요.")

# 사용자 피드백 섹션
st.sidebar.divider()
st.sidebar.subheader("피드백")
feedback = st.sidebar.radio("이 정보가 도움이 되었나요?", ["", "매우 도움됨", "도움됨", "보통", "도움이 되지 않음"])
if feedback and feedback != "":
    st.sidebar.success("피드백 감사합니다!")

# 새로운 증상 제안 섹션
st.sidebar.divider()
st.sidebar.sub
