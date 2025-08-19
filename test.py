import streamlit as st
import random
import requests
from io import BytesIO
from PIL import Image

# 페이지 설정
st.set_page_config(
    page_title="영화 & 드라마 추천 프로그램",
    page_icon="🎬",
    layout="wide"
)

# 제목과 소개
st.title("🎬 취향별 영화 & 드라마 추천 프로그램")
st.markdown("### 당신의 취향에 맞는 작품을 찾아보세요!")

# 사이드바 생성
st.sidebar.header("필터 옵션")

# OTT 플랫폼 선택
ott_platforms = st.sidebar.multiselect(
    "선호하는 OTT 플랫폼을 선택하세요",
    ["넷플릭스", "티빙", "웨이브", "디즈니+", "왓챠", "쿠팡플레이", "애플TV+"]
)

# 영화/드라마 선택
content_type = st.sidebar.radio(
    "어떤 콘텐츠를 찾고 계신가요?",
    ["영화", "드라마", "둘 다"]
)

# 장르 선택 (다중 선택 가능)
genres = st.sidebar.multiselect(
    "선호하는 장르를 선택하세요",
    ["액션", "코미디", "로맨스", "스릴러", "공포", "SF", "판타지", "애니메이션", "다큐멘터리", "드라마"]
)

# 연도 범위 선택
year_range = st.sidebar.slider(
    "개봉/방영 연도 범위",
    2000, 2025, (2010, 2025)
)

# 평점 범위 선택
rating_range = st.sidebar.slider(
    "최소 평점",
    0.0, 10.0, 7.0, 0.1
)

# 영화 데이터베이스
def get_movies_database():
    movies_db = {
        "액션": [
            {"title": "어벤져스: 엔드게임", "year": 2019, "rating": 8.4, "director": "루소 형제", 
             "description": "인피니티 워 이후 절반만 남은 우주에서 살아남은 어벤져스가 마지막 희망을 걸고 모든 것을 바꾸기 위한 최후의 전쟁을 준비한다.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/2/24/%EC%96%B4%EB%B2%A4%EC%A0%B8%EC%8A%A4_%EC%97%94%EB%93%9C%EA%B2%8C%EC%9E%84_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["디즈니+", "왓챠"]},
            {"title": "존 윅 4", "year": 2023, "rating": 7.8, "director": "채드 스타헬스키", 
             "description": "죽을 위기에서 살아난 존 윅은 하이 테이블을 향해 복수의 칼날을 휘두른다.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/d/d2/%EC%A1%B4_%EC%9C%85_4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "왓챠"]},
            {"title": "미션 임파서블: 데드 레코닝", "year": 2023, "rating": 7.7, "director": "크리스토퍼 맥쿼리", 
             "description": "모든 것을 파괴할 새로운 무기를 추적하는 이단 헌트와 IMF팀의 가장 위험한 미션.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/2/2c/%EB%AF%B8%EC%85%98_%EC%9E%84%ED%8C%8C%EC%84%9C%EB%B8%94_%EB%8D%B0%EB%93%9C_%EB%A0%88%EC%BD%94%EB%8B%9D_PART_1_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["티빙", "넷플릭스"]},
            {"title": "분노의 질주: 라이드 오어 다이", "year": 2023, "rating": 6.0, "director": "루이스 리터리어", 
             "description": "돔과 그의 패밀리 앞에 나타난 운명의 적과의 마지막 대결이 펼쳐진다.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/4/44/%EB%B6%84%EB%85%B8%EC%9D%98_%EC%A7%88%EC%A3%BC_%EB%9D%BC%EC%9D%B4%EB%93%9C_%EC%98%A4%EC%96%B4_%EB%8B%A4%EC%9D%B4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["웨이브", "티빙"]},
            {"title": "탑건: 매버릭", "year": 2022, "rating": 8.3, "director": "조셉 코신스키", 
             "description": "최고의 파일럿이자 전설적인 인물 매버릭이 자신이 졸업한 훈련학교 교관으로 발탁되면서 벌어지는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/d/d4/%ED%83%91%EA%B1%B4_%EB%A7%A4%EB%B2%84%EB%A6%AD_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "웨이브"]},
                       {"title": "킹스맨: 퍼스트 에이전트", "year": 2021, "rating": 6.3, "director": "매튜 본", 
             "description": "역사상 최악의 폭군들과 범죄자들이 모여 수백만 명의 생명을 위협하는 전쟁을 모의하는 가운데, 한 남자가 그들을 막기 위한 여정을 시작한다.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/f/f8/%ED%82%B9%EC%8A%A4%EB%A7%A8_%ED%8D%BC%EC%8A%A4%ED%8A%B8_%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["디즈니+", "웨이브"]}
        ],
        "코미디": [
            {"title": "극한직업", "year": 2019, "rating": 8.3, "director": "이병헌", 
             "description": "불법 거래 현장을 감시하던 마약반 형사들이 치킨집을 위장 창업하게 되면서 벌어지는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/c/c9/%EA%B7%B9%ED%95%9C%EC%A7%81%EC%97%85_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "티빙"]},
            {"title": "나의 소중한 사람", "year": 2023, "rating": 7.9, "director": "윤제균", 
             "description": "특별한 능력을 가진 두 사람이 과거로 돌아가 소중한 사람을 지키기 위해 벌이는 좌충우돌 코미디.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/e/ed/%EB%82%98%EC%9D%98_%EC%86%8C%EC%A4%91%ED%95%9C_%EC%82%AC%EB%9E%8C_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["티빙", "쿠팡플레이"]},
            {"title": "더 메뉴", "year": 2022, "rating": 7.2, "director": "마크 마일로드", 
             "description": "외딴섬 미슐랭 레스토랑에서 벌어지는 블랙 코미디 스릴러.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/e/ed/%EB%8D%94_%EB%A9%94%EB%89%B4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["디즈니+", "웨이브"]},
            {"title": "스파이 코드명 포춘", "year": 2023, "rating": 6.5, "director": "가이 리치", 
             "description": "뛰어난 스파이 요원과 행운의 여신이 함께 세계 평화를 지키기 위한 미션을 수행한다.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/7/7a/%EC%8A%A4%ED%8C%8C%EC%9D%B4_%EC%BD%94%EB%93%9C%EB%AA%85_%ED%8F%AC%EC%B6%98_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["애플TV+", "왓챠"]},
            {"title": "육사오", "year": 2022, "rating": 6.9, "director": "박규태", 
             "description": "우연히 1등 당첨 로또를 주운 말년 병장과 이를 노리는 다양한 인물들 사이에서 벌어지는 코미디.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/4/4c/%EC%9C%A1%EC%82%AC%EC%98%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "왓챠"]}
        ],
        "로맨스": [
            {"title": "어바웃 타임", "year": 2013, "rating": 8.0, "director": "리처드 커티스", 
             "description": "시간을 되돌릴 수 있는 능력을 가진 남자가 사랑하는 여인과 완벽한 순간을 만들기 위해 노력하는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/5/5e/%EC%96%B4%EB%B0%94%EC%9B%83_%ED%83%80%EC%9E%84_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "웨이브"]},
            {"title": "라라랜드", "year": 2016, "rating": 8.0, "director": "데이미언 셔젤", 
             "description": "꿈을 좇는 두 남녀의 만남과 사랑, 그리고 선택의 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/8/8a/%EB%9D%BC%EB%9D%BC%EB%9E%9C%EB%93%9C_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "티빙"]},
            {"title": "너의 이름은", "year": 2016, "rating": 8.4, "director": "신카이 마코토", 
             "description": "서로 다른 공간에 있는 소년과 소녀가 몸이 바뀌면서 시작되는 기적 같은 사랑 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/9/9a/%EB%84%88%EC%9D%98_%EC%9D%B4%EB%A6%84%EC%9D%80_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "왓챠"]},
                        {"title": "헤어질 결심", "year": 2022, "rating": 7.3, "director": "박찬욱", 
             "description": "산에서 추락한 한 남자의 변사 사건을 수사하는 형사와 그의 아내 사이에서 벌어지는 미스터리한 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/f/f5/%ED%97%A4%EC%96%B4%EC%A7%88_%EA%B2%B0%EC%8B%AC_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["왓챠", "티빙"]},
            {"title": "타이타닉", "year": 1997, "rating": 8.9, "director": "제임스 카메론", 
             "description": "서로 다른 계급의 남녀가 타이타닉호에서 나누는 운명적인 사랑 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/1/18/%ED%83%80%EC%9D%B4%ED%83%80%EB%8B%89_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["디즈니+", "넷플릭스"]}
        ],
        "스릴러": [
            {"title": "올드보이", "year": 2003, "rating": 8.4, "director": "박찬욱", 
             "description": "15년간 이유도 모른 채 감금되었다가 갑자기 풀려난 남자의 복수극.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/4/48/%EC%98%AC%EB%93%9C%EB%B3%B4%EC%9D%B4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "왓챠"]},
            {"title": "기생충", "year": 2019, "rating": 8.6, "director": "봉준호", 
             "description": "전원백수인 기택네 가족은 어느 날 장남 기우가 박사장네 고액 과외 선생으로 취직하면서 두 가족의 운명이 얽히게 된다.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/6/60/%EA%B8%B0%EC%83%9D%EC%B6%A9_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["티빙", "웨이브"]},
            {"title": "7번방의 선물", "year": 2013, "rating": 8.8, "director": "이환경", 
             "description": "6살 지능을 가진 아빠와 그의 딸이 함께 7번 교도소 방에서 겪는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/a/ae/7%EB%B2%88%EB%B0%A9%EC%9D%98%EC%84%A0%EB%AC%BC.jpg",
             "ott": ["넷플릭스", "티빙"]}
        ],
        "SF": [
            {"title": "인터스텔라", "year": 2014, "rating": 8.6, "director": "크리스토퍼 놀란", 
             "description": "지구 종말 시대에 우주 비행사들이 웜홀을 통해 인류의 새로운 보금자리를 찾아 떠나는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/e/e0/%EC%9D%B8%ED%84%B0%EC%8A%A4%ED%85%94%EB%9D%BC_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "왓챠"]},
            {"title": "매트릭스", "year": 1999, "rating": 8.7, "director": "워쇼스키 형제", 
             "description": "컴퓨터 프로그래머인 네오가 모피어스를 만나 진실의 세계를 알게 되면서 벌어지는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/4/40/%EB%A7%A4%ED%8A%B8%EB%A6%AD%EC%8A%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["웨이브", "티빙"]},
            {"title": "듄", "year": 2021, "rating": 8.0, "director": "드니 빌뇌브", 
             "description": "우주에서 가장 귀중한 자원이 있는 아라키스 행성을 중심으로 벌어지는 대서사시.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/2/26/%EB%93%84_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "왓챠"]}
        ]
    }
    return movies_db

# 드라마 데이터베이스
def get_dramas_database():
    dramas_db = {
        "액션": [
            {"title": "D.P.", "year": 2021, "rating": 8.2, "director": "한준희", 
             "description": "탈영병을 체포하는 군사경찰대의 이야기를 그린 넷플릭스 오리지널 시리즈.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/d/dd/D.P_%EB%84%B7%ED%94%8C%EB%A6%AD%EC%8A%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "모범택시", "year": 2021, "rating": 7.9, "director": "박준우", 
             "description": "택시회사를 운영하며 복수 대행 서비스를 제공하는 주인공의 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/e/e3/%EB%AA%A8%EB%B2%94%ED%83%9D%EC%8B%9C_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["웨이브", "티빙"]},
                        {"title": "빈센조", "year": 2021, "rating": 8.5, "director": "김희원", 
             "description": "이탈리아 마피아 변호사가 한국에 와서 악당들을 그들의 방식으로 응징하는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/1/17/%EB%B9%88%EC%84%BC%EC%A1%B0_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]}
        ],
        "코미디": [
            {"title": "슬기로운 의사생활", "year": 2020, "rating": 9.0, "director": "신원호", 
             "description": "의대 동기 다섯 명이 한 병원에서 근무하며 겪는 일상과 사랑을 그린 드라마.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/6/6e/%EC%8A%AC%EA%B8%B0%EB%A1%9C%EC%9A%B4_%EC%9D%98%EC%82%AC%EC%83%9D%ED%99%9C_%EC%8B%9C%EC%A6%8C1_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "티빙"]},
            {"title": "이상한 변호사 우영우", "year": 2022, "rating": 8.8, "director": "유인식", 
             "description": "자폐 스펙트럼 장애를 가진 천재 변호사의 법정 활약을 그린 드라마.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/f/f5/%EC%9D%B4%EC%83%81%ED%95%9C_%EB%B3%80%ED%98%B8%EC%82%AC_%EC%9A%B0%EC%98%81%EC%9A%B0_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "웬즈데이", "year": 2022, "rating": 8.2, "director": "팀 버튼", 
             "description": "아담스 패밀리의 딸 웬즈데이가 네버모어 아카데미에서 겪는 미스터리한 사건들.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/6/67/%EC%9B%AC%EC%A6%88%EB%8D%B0%EC%9D%B4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]}
        ],
        "로맨스": [
            {"title": "사랑의 불시착", "year": 2019, "rating": 8.9, "director": "이정효", 
             "description": "패러글라이딩 사고로 북한에 불시착한 재벌 상속녀와 북한 장교의 운명적인 사랑.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/6/64/%EC%82%AC%EB%9E%91%EC%9D%98_%EB%B6%88%EC%8B%9C%EC%B0%A9_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "스물다섯 스물하나", "year": 2022, "rating": 8.7, "director": "정지현", 
             "description": "IMF 시대를 배경으로 펜싱 선수와 신문사 만화 작가 지망생의 성장과 사랑을 그린 드라마.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/9/9d/%EC%8A%A4%EB%AC%BC%EB%8B%A4%EC%84%AF_%EC%8A%A4%EB%AC%BC%ED%95%98%EB%82%98_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "그 해 우리는", "year": 2021, "rating": 8.5, "director": "김윤진", 
             "description": "첫사랑 커플의 10년에 걸친 사랑과 이별, 그리고 다시 만남을 그린 드라마.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/0/00/%EA%B7%B8_%ED%95%B4_%EC%9A%B0%EB%A6%AC%EB%8A%94_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "티빙"]}
        ],
        "스릴러": [
            {"title": "오징어 게임", "year": 2021, "rating": 8.0, "director": "황동혁", 
             "description": "456억의 상금이 걸린 의문의 서바이벌 게임에 참가한 사람들의 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/f/f1/%EC%98%A4%EC%A7%95%EC%96%B4_%EA%B2%8C%EC%9E%84_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "마이 네임", "year": 2021, "rating": 7.8, "director": "김진민", 
             "description": "아버지의 죽음을 목격한 딸이 복수를 위해 조직에 들어가 경찰로 위장 잠입하는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/7/7c/%EB%A7%88%EC%9D%B4_%EB%84%A4%EC%9E%84_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "지금 우리 학교는", "year": 2022, "rating": 7.6, "director": "이재규", 
             "description": "고등학교에서 좀비 바이러스가 퍼지면서 생존을 위해 고군분투하는 학생들의 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/e/e9/%EC%A7%80%EA%B8%88_%EC%9A%B0%EB%A6%AC_%ED%95%99%EA%B5%90%EB%8A%94_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]}
        ],
        "공포": [
            {"title": "스위트홈", "year": 2020, "rating": 7.4, "director": "이응복",
             "description": "괴물로 변한 세상에서 살아남기 위한 주민들의 사투.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/1/10/%EC%8A%A4%EC%9C%84%ED%8A%B8%ED%99%88_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "킹덤", "year": 2019, "rating": 8.1, "director": "김성훈",
             "description": "조선 시대 배경의 좀비 스릴러.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/5/53/%ED%82%B9%EB%8D%A4_%EB%84%B7%ED%94%8C%EB%A6%AD%EC%8A%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "타인은 지옥이다", "year": 2019, "rating": 7.5, "director": "이창희",
             "description": "서울로 상경한 청년이 낯선 고시원에서 타인들이 만들어내는 지옥을 경험하는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/a/a2/%ED%83%80%EC%9D%B8%EC%9D%80_%EC%A7%80%EC%98%A5%EC%9D%B4%EB%8B%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["티빙", "웨이브"]}
        ],
        "SF": [
            {"title": "고요의 바다", "year": 2021, "rating": 6.9, "director": "최항용",
             "description": "필수 자원 고갈로 황폐해진 미래 지구를 배경으로, 달에 버려진 연구 기지에 대한 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/d/de/%EA%B3%A0%EC%9A%94%EC%9D%98_%EB%B0%94%EB%8B%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "루카스", "year": 2021, "rating": 7.0, "director": "조진호",
             "description": "가상 현실 게임 속에서 펼쳐지는 SF 스릴러.",
             "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzExMDJfMTY0%2FM_SVG%2FM_2bf5e85501dc6c57f2023b3f2e46e273.jpeg", # 예시 이미지 URL
             "ott": ["왓챠", "쿠팡플레이"]}
        ],
        "판타지": [
            {"title": "도깨비", "year": 2016, "rating": 9.1, "director": "이응복",
             "description": "불멸의 삶을 끝내기 위해 인간 신부가 필요한 도깨비와 저승사자의 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/f/f3/%EB%8F%84%EA%B9%A8%EB%B9%84_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["티빙", "웨이브"]},
            {"title": "호텔 델루나", "year": 2019, "rating": 8.8, "director": "오충환",
             "description": "엘리트 호텔리어와 까칠한 사장 귀신이 운영하는 호텔 델루나에서 벌어지는 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/4/4b/%ED%98%B8%ED%85%94_%EB%8D%B8%EB%A3%A8%EB%82%98_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["티빙", "웨이브"]},
        ],
        "애니메이션": [
            {"title": "아케인", "year": 2021, "rating": 8.7, "director": "파스칼 샤르몽, 아르노 들렁",
             "description": "리그 오브 레전드 세계관을 배경으로 한 애니메이션 시리즈.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/0/02/%EC%95%84%EC%BC%80%EC%9D%B8_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "극장판 귀멸의 칼날: 무한열차편", "year": 2020, "rating": 8.0, "director": "소토자키 하루오",
             "description": "귀살대 최강의 검사 염주 렌고쿠와 함께 임무를 수행하는 탄지로 일행의 이야기.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/0/01/%EA%B7%B9%EC%9E%A5%ED%8C%90_%EA%B7%80%EB%A9%B8%EC%9D%98_%EC%B9%BC%EB%82%A0_%EB%AC%B4%ED%95%9C%EC%97%B4%EC%B0%A8%ED%8E%B8_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스", "왓챠"]}
        ],
        "다큐멘터리": [
            {"title": "나는 신이다: 신이 배신한 사람들", "year": 2023, "rating": 7.0, "director": "조성현",
             "description": "현대 한국 사회의 여러 종교 관련 사건들을 다룬 다큐멘터리.",
             "image_url": "https://upload.wikimedia.org/wikipedia/ko/4/4b/%EB%82%98%EB%8A%94_%EC%8B%A0%EC%9D%B4%EB%8B%A4_%EC%8B%A0%EC%9D%B4_%EB%B0%B0%EC%8B%A0%ED%95%9C_%EC%82%AC%EB%9E%8C%EB%93%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg",
             "ott": ["넷플릭스"]},
            {"title": "BTS: Burn The Stage", "year": 2018, "rating": 8.5, "director": "박준수",
             "description": "아이돌 그룹 BTS의 월드 투어 과정을 담은 다큐멘터리 영화.",
             "image_url": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTA3MjNfNjgg%2FM_SVG%2FM_KakaoTalk_20190723_103816654.jpg", # 예시 이미지 URL
             "ott": ["유튜브 프리미엄", "넷플릭스"]}
        ]
    }
    return dramas_db

# --- 콘텐츠 필터링 함수 ---
def filter_content(content_db, selected_genres, year_range, rating_min, selected_ott_platforms):
    filtered_list = []
    
    # 1. 장르 필터링
    # 장르 선택이 없으면 모든 장르를 포함
    target_genres = selected_genres if selected_genres else list(content_db.keys())

    for genre in target_genres:
        if genre in content_db:
            for item in content_db[genre]:
                # 연도, 평점, OTT 플랫폼 필터링 조건을 모두 만족하는지 확인
                year_match = year_range[0] <= item['year'] <= year_range[1]
                rating_match = item['rating'] >= rating_min
                
                ott_match = True
                if selected_ott_platforms: # OTT 플랫폼이 선택된 경우에만 필터링 적용
                    # 선택된 OTT 중 하나라도 해당 콘텐츠에 있으면 매치
                    ott_match = any(platform in item['ott'] for platform in selected_ott_platforms)

                if year_match and rating_match and ott_match:
                    # 해당 장르를 만족하는 아이템을 추가 (원본 장르 정보 유지)
                    filtered_list.append(item)
                    
    # 중복 제거 (여러 장르에 걸쳐있을 수 있으므로)
    unique_titles = set()
    deduplicated_list = []
    for item in filtered_list:
        if item['title'] not in unique_titles:
            deduplicated_list.append(item)
            unique_titles.add(item['title'])
            
    return deduplicated_list

# --- 이미지 표시 함수 ---
def display_image_from_url(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status() # HTTP 오류가 발생하면 예외 발생
        image = Image.open(BytesIO(response.content))
        st.image(image, use_column_width=True)
    except requests.exceptions.RequestException as e:
        st.warning(f"이미지를 불러올 수 없습니다. URL 오류 또는 네트워크 문제: {e}")
        st.image("https://via.placeholder.com/200x300.png?text=No+Image", use_column_width=True) # 대체 이미지
    except Exception as e:
        st.warning(f"이미지 처리 중 오류 발생: {e}")
        st.image("https://via.placeholder.com/200x300.png?text=No+Image", use_column_width=True) # 대체 이미지

# --- 메인 앱 로직 ---
if st.button("추천 받기", help="클릭할 때마다 새로운 작품을 추천해줍니다!"):
    st.subheader("🌟 당신을 위한 추천 작품 🌟")

    # 모든 영화/드라마 데이터 불러오기
    movies_db = get_movies_database()
    dramas_db = get_dramas_database()

    all_recommendations = []

    if content_type == "영화" or content_type == "둘 다":
        # 영화 필터링 및 추가
        filtered_movies = filter_content(movies_db, genres, year_range, rating_range, ott_platforms)
        for movie in filtered_movies:
            movie['type'] = '영화'
            all_recommendations.append(movie)

    if content_type == "드라마" or content_type == "둘 다":
        # 드라마 필터링 및 추가
        filtered_dramas = filter_content(dramas_db, genres, year_range, rating_range, ott_platforms)
        for drama in filtered_dramas:
            drama['type'] = '드라마'
            all_recommendations.append(drama)

    if all_recommendations:
        # 무작위로 섞어서 추천 (클릭 시마다 다르게 나오도록)
        random.shuffle(all_recommendations)
        
        # 상위 3개 추천 (개수 조절 가능)
        display_count = min(3, len(all_recommendations))
        
        # 세로로 3개씩 표시
        cols = st.columns(display_count)

        for i in range(display_count):
            item = all_recommendations[i]
            with cols[i]:
                st.markdown(f"#### {item['title']} ({item['type']})")
                display_image_from_url(item['image_url'])
                st.markdown(f"**감독:** {item['director']}")
                st.markdown(f"**개봉/방영:** {item['year']}년")
                st.markdown(f"**평점:** {item['rating']} / 10")
                st.markdown(f"**OTT:** {', '.join(item['ott'])}")
                st.caption(item['description'])
                st.markdown("---") # 구분선
    else:
        st.warning("선택하신 조건에 맞는 작품을 찾을 수 없습니다. 필터 옵션을 조정해보세요!")

st.sidebar.markdown("---")
st.sidebar.info("🎬 이 프로그램은 영화/드라마 추천을 돕기 위해 제작되었습니다.")
