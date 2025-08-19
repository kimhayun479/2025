import streamlit as st
import random

def main():
    st.title('나만의 여가 활동 추천 프로그램')
    st.write('기분과 취향에 따라 맞춤형 여가 활동을 추천해드립니다!')
    
    # 사이드바 생성
    st.sidebar.header('선택지를 입력해주세요')
    
    # 기분 선택
    mood = st.sidebar.selectbox(
        '현재 기분이 어떤가요?',
        ['즐거움', '지루함', '피곤함', '스트레스 받음', '차분함', '의욕 넘침']
    )
    
    # 취향 선택 (다중 선택 가능)
    preferences = st.sidebar.multiselect(
        '어떤 활동을 선호하시나요? (여러 개 선택 가능)',
        ['실내 활동', '야외 활동', '창의적인 활동', '신체 활동', '사회적 활동', '혼자 하는 활동', '학습 활동']
    )
    
    # 시간 선택
    available_time = st.sidebar.slider('가능한 시간은 얼마나 되나요? (시간)', 0.5, 5.0, 1.0, 0.5)
    
    # 예산 선택
    budget = st.sidebar.selectbox(
        '예산은 어느 정도인가요?',
        ['무료', '저비용 (1만원 이하)', '중간 (1~5만원)', '고비용 (5만원 이상)']
    )
    
    # 영화/드라마 장르 선택 (영화/드라마 추천을 위한 추가 옵션)
    movie_genres = st.sidebar.multiselect(
        '선호하는 영화/드라마 장르가 있나요?',
        ['액션', '코미디', '로맨스', '스릴러', '공포', 'SF', '판타지', '애니메이션', '다큐멘터리', '드라마', '미스터리', '역사']
    )
    
    # 추천 버튼
    if st.sidebar.button('활동 추천 받기'):
        recommendations = generate_recommendations(mood, preferences, available_time, budget)
        
        st.subheader('추천 여가 활동')
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.info('💭 현재 기분: ' + mood)
            st.info('⏱️ 가능 시간: ' + str(available_time) + '시간')
        
        with col2:
            st.info('❤️ 선호 활동: ' + ', '.join(preferences) if preferences else '선택 없음')
            st.info('💰 예산: ' + budget)
        
        st.markdown('---')
        
        # 추천 활동 표시
        for i, (activity, description) in enumerate(recommendations):
            with st.expander(f"추천 {i+1}: {activity}"):
                st.write(description)
                
                # 영화/드라마 추천 기능 추가
                if '영화' in activity.lower() or '드라마' in activity.lower() or 'OTT' in activity.upper():
                    if movie_genres:
                        if '영화' in activity.lower():
                            movie_recommendations = recommend_movies(movie_genres)
                            st.subheader('🎬 당신의 취향에 맞는 영화 추천')
                            
                            for j, (movie, genre, description) in enumerate(movie_recommendations[:3]):
                                st.markdown(f"**{j+1}. {movie}** ({genre})")
                                st.write(description)
                                st.write("---")
                        
                        if '드라마' in activity.lower() or 'OTT' in activity.upper():
                            drama_recommendations = recommend_dramas(movie_genres)
                            st.subheader('📺 당신의 취향에 맞는 드라마 추천')
                            
                            for j, (drama, genre, description) in enumerate(drama_recommendations[:3]):
                                st.markdown(f"**{j+1}. {drama}** ({genre})")
                                st.write(description)
                                st.write("---")
                    else:
                        st.write("영화/드라마 장르를 선택하시면 맞춤형 콘텐츠를 추천해드립니다!")
                
                # 랜덤 이모지 추가
                emojis = ['✨', '🌟', '🎯', '🎨', '🏃‍♀️', '📚', '🎮', '🎬', '🎵', '🧘‍♀️', '🌿']
                st.write(f"{random.choice(emojis)} 이 활동이 마음에 드시나요?")
        
        # 새로운 추천 버튼
        if st.button('다른 활동도 추천해주세요!'):
            st.experimental_rerun()
    
    # 영화/드라마 추천 전용 섹션
    st.sidebar.markdown('---')
    st.sidebar.subheader('영화/드라마만 추천받기')
    
    col1, col2 = st.sidebar.columns(2)
    
    with col1:
        if st.button('영화 추천'):
            if movie_genres:
                st.subheader('🎬 당신을 위한 영화 추천')
                movie_recommendations = recommend_movies(movie_genres)
                
                for i, (movie, genre, description) in enumerate(movie_recommendations[:5]):
                    with st.expander(f"{movie} ({genre})"):
                        st.write(description)
            else:
                st.warning('영화 장르를 선택해주세요!')
    
    with col2:
        if st.button('드라마 추천'):
            if movie_genres:
                st.subheader('📺 당신을 위한 드라마 추천')
                drama_recommendations = recommend_dramas(movie_genres)
                
                for i, (drama, genre, description) in enumerate(drama_recommendations[:5]):
                    with st.expander(f"{drama} ({genre})"):
                        st.write(description)
            else:
                st.warning('드라마 장르를 선택해주세요!')
    
    # 앱 정보
    st.sidebar.markdown('---')
    st.sidebar.info('이 앱은 여가 시간을 더 즐겁게 보낼 수 있도록 도와드립니다.')

def generate_recommendations(mood, preferences, available_time, budget):
   def generate_recommendations(mood, preferences, available_time, budget):
    # 활동 데이터베이스 (활동명, 설명)
    activities = {
        '즐거움': {
            '실내 활동': [
                ('보드게임 하기', '친구나 가족과 함께 보드게임을 즐겨보세요. 다양한 전략과 협력이 필요한 게임들이 많습니다.'),
                ('영화 감상하기', '좋아하는 장르의 영화를 선택해 감상해보세요. 혼자 또는 친구와 함께 즐길 수 있습니다.'),
                ('베이킹', '맛있는 쿠키나 케이크를 만들어보세요. 창의력을 발휘할 수 있고 결과물도 맛있습니다!')
            ]},
            '야외 활동': [
                ('피크닉', '가까운 공원에서 피크닉을 즐겨보세요. 좋아하는 음식과 음료를 준비해가면 더 즐거워집니다.'),
                ('자전거 타기', '근처 자전거 도로나 공원에서 자전거를 타며 상쾌한 공기를 마셔보세요.'),
                ('물놀이', '더운 날씨에는 수영장이나 계곡에서 물놀이를 즐겨보세요.')
            ],
            '창의적인 활동': [
                ('그림 그리기', '좋아하는 풍경이나 인물을 그려보세요. 미술 실력은 중요하지 않아요, 즐기는 것이 중요합니다.'),
                ('DIY 프로젝트', '집에 있는 물건들을 활용해 새로운 것을 만들어보세요. 유튜브에 많은 아이디어가 있습니다.'),
                ('드라마 시청하기', '인기 드라마나 좋아하는 장르의 드라마를 시청하며 휴식을 취해보세요.')
            ]
        },
        '지루함': {
            '창의적인 활동': [
                ('새로운 취미 배우기', '유튜브 튜토리얼을 통해 드로잉, 뜨개질, 종이접기 등 새로운 취미를 시작해보세요.'),
                ('DIY 프로젝트', '집에 있는 물건들을 활용해 새로운 것을 만들어보세요. 재활용 아이템으로 예술 작품을 만들 수도 있습니다.'),
                ('글쓰기', '짧은 이야기나 시를 써보세요. 자신의 생각과 감정을 표현하는 좋은 방법입니다.')
            ]},
            '학습 활동': [
                ('새로운 언어 배우기', '듀오링고나 다른 언어 학습 앱을 통해 새로운 언어의 기초를 배워보세요.'),
                ('온라인 강의 듣기', '관심 있는 주제의 무료 온라인 강의를 찾아 들어보세요.'),
                ('다큐멘터리 시청', '흥미로운 주제의 다큐멘터리를 시청하며 새로운 지식을 얻어보세요.')
            ],
            '혼자 하는 활동': [
                ('OTT 서비스로 드라마 몰아보기', '넷플릭스, 왓챠 등의 OTT 서비스에서 인기 드라마나 시리즈를 몰아보세요.'),
                ('독서', '미뤄두었던 책을 읽거나 새로운 장르의 책을 탐험해보세요.'),
                ('퍼즐 맞추기', '직소 퍼즐이나 스도쿠 등 두뇌를 자극하는 퍼즐을 풀어보세요.')
            ]
        },
        '피곤함': {
            '혼자 하는 활동': [
                ('명상', '조용한 공간에서 명상을 통해 마음을 진정시키고 에너지를 회복해보세요.'),
                ('가벼운 독서', '부담 없는 소설이나 잡지를 읽으며 휴식을 취해보세요.'),
                ('파워 낮잠', '20-30분의 짧은 낮잠은 에너지를 회복하는 데 도움이 됩니다.')
         ],
            '실내 활동': [
                ('따뜻한 차 마시기', '카모마일이나 라벤더 차와 같은 허브티를 마시며 휴식을 취해보세요.'),
                ('영화 감상', '편안한 분위기에서 좋아하는 영화를 감상하며 휴식을 취해보세요.'),
                ('아로마 테라피', '라벤더나 유칼립투스 오일을 이용한 아로마 테라피로 긴장을 풀어보세요.')
            ],
            '신체 활동': [
                ('가벼운 스트레칭', '간단한 스트레칭으로 굳어있는 근육을 풀어주세요.'),
                ('요가', '초보자용 요가 동작으로 몸과 마음의 긴장을 풀어보세요.'),
                ('느린 산책', '공원이나 한적한 거리를 천천히 걸으며 신선한 공기를 마셔보세요.')
            ]
        },
        '스트레스 받음': {
            '신체 활동': [
                ('달리기', '달리기는 스트레스 호르몬을 줄이고 기분을 좋게 만드는 엔도르핀을 분비합니다.'),
                ('댄스', '좋아하는 음악에 맞춰 자유롭게 춤을 추며 스트레스를 해소해보세요.'),
                ('격렬한 운동', '복싱이나 HIIT와 같은 격렬한 운동으로 스트레스를 발산해보세요.')
            ]},
            '창의적인 활동': [
                ('그림 그리기', '자유롭게 그림을 그리며 감정을 표현해보세요. 미술 실력은 중요하지 않습니다.'),
                ('악기 연주', '좋아하는 악기를 연주하거나 새로운 악기에 도전해보세요.'),
                ('정원 가꾸기', '식물을 돌보는 것 추천해요.')]
