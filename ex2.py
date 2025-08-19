import streamlit as st
import pandas as pd
import random
from PIL import Image
import requests
from io import BytesIO

# 페이지 설정
st.set_page_config(page_title="음악 추천 프로그램", layout="wide")

# 제목 및 소개
st.title("🎵 나만의 음악 추천 프로그램")
st.markdown("### 취향, 기분, 분위기에 맞는 음악을 추천해 드립니다!")

# 사이드바 - 사용자 정보
with st.sidebar:
    st.header("나의 음악 취향 설정")
    user_name = st.text_input("이름", "김하윤")
    
    # 취향 설정
    st.subheader("기본 취향 설정")
    preferred_genres = st.multiselect(
        "선호하는 장르를 선택하세요",
        ["팝", "K-POP", "록/메탈", "힙합", "R&B", "재즈", "클래식", "일렉트로닉", "인디", "발라드"],
        default=["K-POP", "팝"]
    )
    
    language_preference = st.selectbox(
        "주로 듣는 언어",
        ["한국어", "영어", "일본어", "중국어", "상관없음"],
        index=0
    )
    
    energy_preference = st.slider("선호하는 에너지 레벨", 1, 10, 5)
    
    st.info("💡 팁: 기분과 분위기를 선택하면 더 정확한 추천을 받을 수 있어요!")

# 메인 화면 - 현재 상태 입력
col1, col2 = st.columns(2)

with col1:
    st.header("현재 상태")
    
    current_mood = st.selectbox(
        "현재 기분을 선택하세요",
        ["행복함", "우울함", "차분함", "에너지 넘침", "로맨틱함", "집중하고 싶음", "스트레스 받음", "편안함", "외로움", "신남"]
    )
    
    current_activity = st.selectbox(
        "현재 하고 있는 활동",
        ["휴식", "공부/일", "운동", "산책", "출퇴근/등하교", "파티/모임", "독서", "명상", "요리", "청소"]
    )
    
    weather = st.selectbox(
        "현재 날씨는 어떤가요?",
        ["맑음", "비/흐림", "눈", "더움", "추움", "상관없음"]
    )

with col2:
    st.header("분위기 설정")
    
    desired_atmosphere = st.select_slider(
        "원하는 분위기",
        options=["아주 조용한", "차분한", "보통", "활기찬", "매우 신나는"],
        value="보통"
    )
    
    tempo_preference = st.slider("원하는 템포 (BPM)", 60, 180, 120)
    
    discovery_level = st.select_slider(
        "새로운 음악 발견 정도",
        options=["익숙한 노래만", "주로 익숙한 노래", "균형있게", "주로 새로운 노래", "완전히 새로운 노래"],
        value="균형있게"
    )
    
    era_preference = st.multiselect(
        "선호하는 시대",
        ["1970년대", "1980년대", "1990년대", "2000년대", "2010년대", "2020년대 이후"],
        default=["2010년대", "2020년대 이후"]
    )

# 음악 데이터베이스 (실제 서비스에서는 API나 대형 데이터베이스 사용)
@st.cache_data
def load_music_database():
    # 실제로는 CSV 파일이나 데이터베이스에서 로드
    music_db = {
        # 행복한 분위기의 노래들
        "행복함": {
            "K-POP": [
                {"title": "Dynamite", "artist": "BTS", "album": "Dynamite (DayTime Version)", "year": 2020, "mood": "신남", "energy": 8},
                {"title": "Feel Special", "artist": "TWICE", "album": "Feel Special", "year": 2019, "mood": "행복함", "energy": 7},
                {"title": "에너제틱", "artist": "우주소녀", "album": "HAPPY", "year": 2017, "mood": "행복함", "energy": 9}
            ],
            "팝": [
                {"title": "Happy", "artist": "Pharrell Williams", "album": "G I R L", "year": 2014, "mood": "행복함", "energy": 8},
                {"title": "Can't Stop the Feeling!", "artist": "Justin Timberlake", "album": "Trolls (Original Motion Picture Soundtrack)", "year": 2016, "mood": "행복함", "energy": 7},
                {"title": "Good as Hell", "artist": "Lizzo", "album": "Cuz I Love You", "year": 2019, "mood": "행복함", "energy": 8}
            ]
        },
        
        # 우울한 분위기의 노래들
        "우울함": {
            "K-POP": [
                {"title": "through the night", "artist": "IU", "album": "Palette", "year": 2017, "mood": "차분함", "energy": 3},
                {"title": "비밀의 화원", "artist": "아이유", "album": "Modern Times", "year": 2013, "mood": "우울함", "energy": 4},
                {"title": "사랑했었다", "artist": "이홍기, 유회승", "album": "사랑했었다", "year": 2018, "mood": "우울함", "energy": 3}
            ],
            "팝": [
                {"title": "Someone Like You", "artist": "Adele", "album": "21", "year": 2011, "mood": "우울함", "energy": 3},
                {"title": "Fix You", "artist": "Coldplay", "album": "X&Y", "year": 2005, "mood": "우울함", "energy": 4},
                {"title": "Heather", "artist": "Conan Gray", "album": "Kid Krow", "year": 2020, "mood": "우울함", "energy": 2}
            ]
        },
        
        # 차분한 분위기의 노래들
        "차분함": {
            "K-POP": [
                                {"title": "밤편지", "artist": "아이유", "album": "Palette", "year": 2017, "mood": "차분함", "energy": 3},
                {"title": "너의 의미", "artist": "아이유", "album": "꽃갈피", "year": 2014, "mood": "차분함", "energy": 4},
                {"title": "좋은 날", "artist": "아이유", "album": "Real", "year": 2010, "mood": "차분함", "energy": 6}
            ],
            "팝": [
                {"title": "Glimpse of Us", "artist": "Joji", "album": "Smithereens", "year": 2022, "mood": "차분함", "energy": 3},
                {"title": "All of Me", "artist": "John Legend", "album": "Love In The Future", "year": 2013, "mood": "차분함", "energy": 4},
                {"title": "Say You Won't Let Go", "artist": "James Arthur", "album": "Back from the Edge", "year": 2016, "mood": "차분함", "energy": 4}
            ]
        },
        
        # 다른 기분과 장르에 대한 노래들
        "에너지 넘침": {
            "K-POP": [
                {"title": "ZOOM", "artist": "제시", "album": "ZOOM", "year": 2022, "mood": "에너지 넘침", "energy": 9},
                {"title": "Next Level", "artist": "aespa", "album": "Next Level", "year": 2021, "mood": "에너지 넘침", "energy": 8},
                {"title": "불타오르네", "artist": "BTS", "album": "화양연화 pt.2", "year": 2015, "mood": "에너지 넘침", "energy": 9}
            ],
            "팝": [
                {"title": "Physical", "artist": "Dua Lipa", "album": "Future Nostalgia", "year": 2020, "mood": "에너지 넘침", "energy": 9},
                {"title": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours", "year": 2020, "mood": "에너지 넘침", "energy": 8},
                {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "album": "Uptown Special", "year": 2015, "mood": "에너지 넘침", "energy": 10}
            ]
        }
    }
    return music_db

# 음악 데이터베이스 불러오기
music_db = load_music_database()

# 추천 기능
def get_recommendations(mood, genres, language, energy_level, atmosphere, era_pref, discovery):
    recommendations = []
    
    # 기분에 맞는 음악 필터링
    for genre in genres:
        if genre in music_db.get(mood, {}) and music_db[mood][genre]:
            songs = music_db[mood][genre]
            
            # 에너지 레벨에 따라 필터링
            energy_mapping = {
                "아주 조용한": range(1, 3),
                "차분한": range(3, 5),
                "보통": range(5, 7),
                "활기찬": range(7, 9),
                "매우 신나는": range(9, 11)
            }
            
            # 분위기에 맞는 노래 필터링
            filtered_songs = [song for song in songs if song["energy"] in energy_mapping.get(atmosphere, range(1, 11))]
            
            # 시대 필터링
            if era_pref:
                era_filtered = []
                for song in filtered_songs:
                    for era in era_pref:
                        if era == "1970년대" and 1970 <= song["year"] < 1980:
                            era_filtered.append(song)
                        elif era == "1980년대" and 1980 <= song["year"] < 1990:
                            era_filtered.append(song)
                        elif era == "1990년대" and 1990 <= song["year"] < 2000:
                            era_filtered.append(song)
                        elif era == "2000년대" and 2000 <= song["year"] < 2010:
                            era_filtered.append(song)
                        elif era == "2010년대" and 2010 <= song["year"] < 2020:
                            era_filtered.append(song)
                        elif era == "2020년대 이후" and song["year"] >= 2020:
                            era_filtered.append(song)
                filtered_songs = era_filtered if era_filtered else filtered_songs
            
            recommendations.extend(filtered_songs)
    
    # 결과가 없으면 모든 장르에서 기분에 맞는 노래 추천
    if not recommendations:
        for genre_key, genre_songs in music_db.get(mood, {}).items():
            recommendations.extend(genre_songs)
    
    # 추천 결과가 여전히 없으면 랜덤 추천
    if not recommendations:
        all_songs = []
        for mood_key, genres in music_db.items():
            for genre_key, songs in genres.items():
                all_songs.extend(songs)
        
        if all_songs:
            recommendations = random.sample(all_songs, min(3, len(all_songs)))
    
    # 최대 5개까지 추천
    if recommendations:
        if discovery == "익숙한 노래만":
            # 인기 있는 노래 (2010년 이후, 에너지 높은)
            recommendations = sorted(recommendations, key=lambda x: (x["year"] > 2010, x["energy"]), reverse=True)
        elif discovery == "완전히 새로운 노래":
            # 무작위로 섞어서 새로운 발견 유도
            random.shuffle(recommendations)
    
    return recommendations[:5]

# 버튼 클릭 시 추천 실행
if st.button("🎵 노래 추천 받기"):
    with st.spinner("당신의 취향에 맞는 음악을 찾고 있어요..."):
        recommendations = get_recommendations(
            current_mood, 
            preferred_genres, 
            language_preference, 
            energy_preference,
            desired_atmosphere,
            era_preference,
            discovery_level
        )
        
        if recommendations:
            st.success(f"### {user_name}님을 위한 추천 음악 리스트")
            
            # 추천 결과 표시
            for i, song in enumerate(recommendations):
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    # 앨범 커버 이미지 (실제로는 API에서 가져와야 함)
                    try:
                        # 임시로 랜덤 색상 이미지 생성 (실제로는 앨범 커버 API 사용)
                        st.image(f"https://via.placeholder.com/150/{random.randint(100, 999)}", 
                                caption=f"{song['album']}")
                    except:
                        st.write("🎵")
                
                with col2:
                    st.markdown(f"#### {i+1}. {song['title']}")
                    st.markdown(f"**아티스트**: {song['artist']}")
                                       st.markdown(f"**앨범**: {song['album']}")
                    st.markdown(f"**발매년도**: {song['year']}")
                    
                    # 에너지 레벨 시각화
                    energy = song['energy']
                    energy_bar = "🔋" * energy + "⚪" * (10 - energy)
                    st.markdown(f"**에너지 레벨**: {energy_bar}")
                    
                    # 음악 플레이어 (실제로는 스트리밍 서비스 연동 필요)
                    st.markdown(f"[🎧 들어보기](https://www.youtube.com/results?search_query={song['artist']}+{song['title']})")
            
            # 피드백 섹션
            st.write("---")
            st.subheader("이 추천이 마음에 드셨나요?")
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("👍 좋아요"):
                    st.success("피드백 감사합니다! 더 나은 추천을 위해 활용하겠습니다.")
            with col2:
                if st.button("👎 별로예요"):
                    st.info("피드백 감사합니다. 다음에는 더 나은 추천을 드리겠습니다.")
            with col3:
                if st.button("🔄 다시 추천받기"):
                    st.experimental_rerun()
        else:
            st.error("죄송합니다. 현재 조건에 맞는 노래를 찾을 수 없습니다. 다른 조건으로 시도해보세요.")

# 추가 기능 탭
tab1, tab2, tab3 = st.tabs(["플레이리스트 만들기", "음악 통계", "도움말"])

with tab1:
    st.header("나만의 플레이리스트")
    st.write("마음에 드는 노래를 저장하여 플레이리스트를 만들어보세요.")
    
    # 세션 상태로 플레이리스트 관리 (실제로는 데이터베이스에 저장)
    if 'playlist' not in st.session_state:
        st.session_state.playlist = []
    
    # 플레이리스트에 노래 추가 (예시)
    new_song = st.text_input("노래 제목 입력")
    new_artist = st.text_input("아티스트 입력")
    
    if st.button("플레이리스트에 추가") and new_song and new_artist:
        st.session_state.playlist.append({"title": new_song, "artist": new_artist})
        st.success(f"'{new_song} - {new_artist}'가 플레이리스트에 추가되었습니다!")
    
    # 저장된 플레이리스트 표시
    if st.session_state.playlist:
        st.write("### 내 플레이리스트")
        for i, song in enumerate(st.session_state.playlist):
            st.write(f"{i+1}. {song['title']} - {song['artist']}")
        
        if st.button("플레이리스트 초기화"):
            st.session_state.playlist = []
            st.info("플레이리스트가 초기화되었습니다.")
    else:
        st.info("아직 플레이리스트에 노래가 없습니다. 노래를 추가해보세요!")

with tab2:
    st.header("음악 취향 통계")
    st.write("당신의 음악 취향을 분석한 결과입니다.")
    
    # 차트 예시 (실제로는 사용자 데이터 기반 분석 필요)
    chart_data = pd.DataFrame({
        '장르': ['K-POP', '팝', '록/메탈', '힙합', 'R&B'],
        '선호도': [65, 80, 30, 45, 55]
    })
    
    st.bar_chart(chart_data.set_index('장르'))
    
    # 시간대별 음악 취향 (예시)
    st.write("### 시간대별 음악 취향")
    time_data = pd.DataFrame({
        '시간': ['아침', '오전', '오후', '저녁', '밤'],
        '에너지': [7, 8, 6, 5, 3],
        '템포': [120, 130, 125, 110, 90]
    })
    
    st.line_chart(time_data.set_index('시간'))

with tab3:
    st.header("도움말")
    st.write("""
    ### 음악 추천 프로그램 사용법
    
    1. **취향 설정**: 사이드바에서 기본 음악 취향을 설정하세요.
    2. **현재 상태 입력**: 현재 기분, 활동, 날씨를 선택하세요.
    3. **분위기 설정**: 원하는 음악의 분위기와 템포를 설정하세요.
    4. **추천 받기**: '노래 추천 받기' 버튼을 클릭하면 맞춤 추천을 받을 수 있습니다.
    5. **피드백**: 추천 결과에 대한 피드백을 주시면 더 나은 추천을 제공해 드립니다.
    
    ### 팁
    - 더 정확한 추천을 원하시면 모든 설정을 상세히 입력해주세요.
    - '다시 추천받기' 버튼을 누르면 같은 설정으로 다른 노래를 추천받을 수 있습니다.
    - 플레이리스트 기능을 활용하여 마음에 드는 노래를 저장해보세요.
    """)

# 푸터
st.markdown("---")
st.markdown("© 2025 음악 추천 프로그램 | 김하윤님을 위한 맞춤 서비스")
