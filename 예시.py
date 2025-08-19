# 영화 데이터베이스 (더 많은 작품 추가 및 배우 정보 포함)
def get_movies_database():
    movies_db = {
        "액션": [
            {"title": "어벤져스: 엔드게임", "year": 2019, "rating": 8.4, "director": "루소 형제", 
             "actors": "로버트 다우니 주니어, 크리스 에반스, 크리스 헴스워스, 스칼렛 요한슨",
             "description": "인피니티 워 이후 절반만 남은 우주에서 살아남은 어벤져스가 마지막 희망을 걸고 모든 것을 바꾸기 위한 최후의 전쟁을 준비한다.",
             "ott": ["디즈니+", "왓챠"], "origin": "해외"},
            {"title": "존 윅 4", "year": 2023, "rating": 7.8, "director": "채드 스타헬스키", 
             "actors": "키아누 리브스, 도니 예인, 이안 맥쉐인",
             "description": "죽을 위기에서 살아난 존 윅은 하이 테이블을 향해 복수의 칼날을 휘두른다.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"},
            {"title": "범죄도시2", "year": 2022, "rating": 7.1, "director": "이상용", 
             "actors": "마동석, 손석구, 최귀화, 박지환",
             "description": "베트남으로 도주한 용의자를 잡기 위해 한국과 베트남 형사들이 힘을 합치는 이야기.",
             "ott": ["티빙", "웨이브"], "origin": "국내"},
            {"title": "탑건: 매버릭", "year": 2022, "rating": 8.3, "director": "조셉 코신스키", 
             "actors": "톰 크루즈, 마일즈 텔러, 제니퍼 코넬리",
             "description": "최고의 파일럿이자 전설적인 인물 매버릭이 자신이 졸업한 훈련학교 교관으로 발탁되면서 벌어지는 이야기.",
             "ott": ["넷플릭스", "웨이브"], "origin": "해외"},
            {"title": "헌트", "year": 2022, "rating": 7.9, "director": "이정재", 
             "actors": "이정재, 정우성, 전혜진",
             "description": "1980년대를 배경으로 안기부 요원들이 조직 내부의 스파이를 색출하는 이야기.",
             "ott": ["티빙", "넷플릭스"], "origin": "국내"},
            {"title": "007 노 타임 투 다이", "year": 2021, "rating": 7.3, "director": "캐리 후쿠나가", 
             "actors": "다니엘 크레이그, 라미 말렉, 레아 세이두",
             "description": "MI6를 떠난 제임스 본드가 CIA 요원의 요청으로 납치된 과학자를 구출하기 위한 임무에 복귀한다.",
             "ott": ["왓챠", "넷플릭스"], "origin": "해외"},
            {"title": "다크 나이트", "year": 2008, "rating": 9.0, "director": "크리스토퍼 놀란", 
             "actors": "크리스찬 베일, 히스 레저, 게리 올드만",
             "description": "배트맨과 조커의 대결을 그린 명작.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"}
        ],
        "코미디": [
            {"title": "극한직업", "year": 2019, "rating": 8.3, "director": "이병헌", 
             "actors": "류승룡, 이하늬, 진선규",
             "description": "불법 거래 현장을 감시하던 마약반 형사들이 치킨집을 위장 창업하게 되면서 벌어지는 이야기.",
             "ott": ["넷플릭스", "티빙"], "origin": "국내"},
            {"title": "나의 소중한 사람", "year": 2023, "rating": 7.9, "director": "윤제균", 
             "actors": "정유미, 강동원, 유해진",
             "description": "특별한 능력을 가진 두 사람이 과거로 돌아가 소중한 사람을 지키기 위해 벌이는 좌충우돌 코미디.",
             "ott": ["티빙", "쿠팡플레이"], "origin": "국내"},
            {"title": "더 메뉴", "year": 2022, "rating": 7.2, "director": "마크 마일로드", 
             "actors": "랄프 파인즈, 안야 테일러조이, 니콜라스 홀트",
             "description": "외딴섬 미슐랭 레스토랑에서 벌어지는 블랙 코미디 스릴러.",
             "ott": ["디즈니+", "웨이브"], "origin": "해외"},
            {"title": "육사오", "year": 2022, "rating": 6.9, "director": "박규태", 
             "actors": "고경표, 이이경, 음문석",
             "description": "우연히 1등 당첨 로또를 주운 말년 병장과 이를 노리는 다양한 인물들 사이에서 벌어지는 코미디.",
             "ott": ["넷플릭스", "왓챠"], "origin": "국내"},
            {"title": "바빌론", "year": 2022, "rating": 7.2, "director": "데미언 셔젤", 
             "actors": "브래드 피트, 마고 로비, 디에고 칼바",
             "description": "1920년대 할리우드의 황금기와 쇠퇴기를 그린 블랙 코미디.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"},
            {"title": "스파이 코드명 포춘", "year": 2023, "rating": 6.5, "director": "가이 리치", 
             "actors": "제이슨 스타뎀, 휴 그랜트, 오브리 플라자", 
             "description": "뛰어난 스파이 요원과 행운의 여신이 함께 세계 평화를 지키기 위한 미션을 수행한다.",
             "ott": ["애플TV+", "왓챠"], "origin": "해외"}
        ],
        "로맨스": [
            {"title": "어바웃 타임", "year": 2013, "rating": 8.0, "director": "리처드 커티스", 
             "actors": "도널 글리슨, 레이첼 맥아담스, 빌 나이",
             "description": "시간을 되돌릴 수 있는 능력을 가진 남자가 사랑하는 여인과 완벽한 순간을 만들기 위해 노력하는 이야기.",
             "ott": ["넷플릭스", "웨이브"], "origin": "해외"},
            {"title": "라라랜드", "year": 2016, "rating": 8.0, "director": "데이미언 셔젤", 
             "actors": "라이언 고슬링, 엠마 스톤, 존 레전드",
             "description": "꿈을 좇는 두 남녀의 만남과 사랑, 그리고 선택의 이야기.",
             "ott": ["넷플릭스", "티빙"], "origin": "해외"},
            {"title": "너의 이름은", "year": 2016, "rating": 8.4, "director": "신카이 마코토", 
             "actors": "카미키 류노스케 (목소리), 카미시라이시 모네 (목소리)",
             "description": "서로 다른 공간에 있는 소년과 소녀가 몸이 바뀌면서 시작되는 기적 같은 사랑 이야기.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"},
            {"title": "헤어질 결심", "year": 2022, "rating": 7.3, "director": "박찬욱", 
             "actors": "박해일, 탕웨이, 이정현",
             "description": "산에서 추락한 한 남자의 변사 사건을 수사하는 형사와 그의 아내 사이에서 벌어지는 미스터리한 이야기.",
             "ott": ["왓챠", "티빙"], "origin": "국내"},
            {"title": "타이타닉", "year": 1997, "rating": 8.9, "director": "제임스 카메론", 
             "actors": "레오나르도 디카프리오, 케이트 윈슬렛",
             "description": "서로 다른 계급의 남녀가 타이타닉호에서 나누는 운명적인 사랑 이야기.",
             "ott": ["디즈니+", "넷플릭스"], "origin": "해외"}
        ],
        "스릴러": [
            {"title": "올드보이", "year": 2003, "rating": 8.4, "director": "박찬욱", 
             "actors": "최민식, 유지태, 강혜정",
             "description": "15년간 이유도 모른 채 감금되었다가 갑자기 풀려난 남자의 복수극.",
             "ott": ["넷플릭스", "왓챠"], "origin": "국내"},
            {"title": "기생충", "year": 2019, "rating": 8.6, "director": "봉준호", 
             "actors": "송강호, 최우식, 박소담, 조여정",
             "description": "전원백수인 기택네 가족은 어느 날 장남 기우가 박사장네 고액 과외 선생으로 취직하면서 두 가족의 운명이 얽히게 된다.",
             "ott": ["티빙", "웨이브"], "origin": "국내"},
            {"title": "조커", "year": 2019, "rating": 8.4, "director": "토드 필립스",
             "actors": "호아킨 피닉스, 로버트 드 니로, 재지 비츠",
             "description": "실패한 코미디언이 광기와 혼돈의 길로 빠져들며 조커가 되어가는 과정.",
             "ott": ["넷플릭스", "웨이브"], "origin": "해외"},
            {"title": "침묵", "year": 2017, "rating": 7.5, "director": "장재현",
             "actors": "최민식, 박신혜, 류준열",
             "description": "연쇄 살인 사건을 추적하는 형사와 청각장애인 소녀의 이야기.",
             "ott": ["티빙", "왓챠"], "origin": "국내"},
            {"title": "나를 찾아줘", "year": 2014, "rating": 7.8, "director": "데이빗 핀처",
             "actors": "벤 애플렉, 로자먼드 파이크, 닐 패트릭 해리스",
             "description": "결혼 5주년 기념일, 갑자기 사라진 아내를 찾아 나선 남편의 이야기.",
             "ott": ["넷플릭스", "디즈니+"], "origin": "해외"}
        ],
        "공포": [
            {"title": "곤지암", "year": 2018, "rating": 6.8, "director": "정범식", 
             "actors": "위하준, 박지현, 오아연",
             "description": "유튜브 공포 체험을 위해 곤지암 정신병원에 들어간 이들의 이야기.",
             "ott": ["티빙", "웨이브"], "origin": "국내"},
            {"title": "컨저링", "year": 2013, "rating": 7.5, "director": "제임스 완", 
             "actors": "베라 파미가, 패트릭 윌슨, 릴리 테일러",
             "description": "실화를 바탕으로 한 가장 무서운 심령 영화.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"},
            {"title": "장화, 홍련", "year": 2003, "rating": 7.9, "director": "김지운", 
             "actors": "임수정, 문근영, 염정아, 김갑수",
             "description": "어머니를 잃고 새엄마와 살게 된 두 자매에게 벌어지는 기이한 사건들.",
             "ott": ["웨이브", "왓챠"], "origin": "국내"},
            {"title": "미드소마", "year": 2019, "rating": 7.1, "director": "아리 애스터",
             "actors": "플로렌스 퓨, 잭 레이너, 윌리엄 잭슨 하퍼",
             "description": "스웨덴의 한 마을에서 90년에 한 번 열리는 하지 축제에 참가한 대학생들에게 일어나는 기이한 일들.",
             "ott": ["넷플릭스", "티빙"], "origin": "해외"}
        ],
        "SF": [
            {"title": "인터스텔라", "year": 2014, "rating": 8.6, "director": "크리스토퍼 놀란", 
             "actors": "매튜 맥커너히, 앤 해서웨이, 제시카 차스테인",
             "description": "지구 종말 시대에 우주 비행사들이 웜홀을 통해 인류의 새로운 보금자리를 찾아 떠나는 이야기.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"},
            {"title": "매트릭스", "year": 1999, "rating": 8.7, "director": "워쇼스키 형제", 
             "actors": "키아누 리브스, 로렌스 피시번, 캐리 앤 모스",
             "description": "컴퓨터 프로그래머인 네오가 모피어스를 만나 진실의 세계를 알게 되면서 벌어지는 이야기.",
             "ott": ["웨이브", "티빙"], "origin": "해외"},
            {"title": "듄", "year": 2021, "rating": 8.0, "director": "드니 빌뇌브", 
             "actors": "티모시 샬라메, 레베카 퍼거슨, 오스카 아이삭",
             "description": "우주에서 가장 귀중한 자원이 있는 아라키스 행성을 중심으로 벌어지는 대서사시.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"},
            {"title": "승리호", "year": 2021, "rating": 6.5, "director": "조성희",
             "actors": "송중기, 김태리, 진선규",
             "description": "우주 쓰레기를 수거하는 청소선 승리호의 선원들이 인류 멸망 위기에 맞서는 이야기.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "블레이드 러너 2049", "year": 2017, "rating": 8.0, "director": "드니 빌뇌브",
             "actors": "라이언 고슬링, 해리슨 포드, 아나 디 아르마스",
             "description": "복제인간 블레이드 러너가 인류의 미래를 바꿀 비밀을 발견하는 이야기.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"}
        ],
        "판타지": [
            {"title": "신과함께-죄와 벌", "year": 2017, "rating": 7.8, "director": "김용화",
             "actors": "하정우, 차태현, 주지훈, 김향기",
             "description": "인간의 죽음 이후 저승에서 벌어지는 7번의 재판과 7개의 지옥을 무사히 통과해야 하는 이야기.",
             "ott": ["티빙", "넷플릭스"], "origin": "국내"},
            {"title": "해리 포터와 마법사의 돌", "year": 2001, "rating": 8.1, "director": "크리스 콜럼버스",
             "actors": "다니엘 래드클리프, 루퍼트 그린트, 엠마 왓슨",
             "description": "마법 세계에 입문한 소년 해리 포터의 모험 이야기.",
             "ott": ["왓챠", "넷플릭스"], "origin": "해외"},
            {"title": "반지의 제왕: 반지원정대", "year": 2001, "rating": 8.8, "director": "피터 잭슨",
             "actors": "일라이저 우드, 이안 맥켈런, 비고 모텐슨",
             "description": "평화를 지키기 위해 절대 반지를 파괴하러 떠나는 원정대의 이야기.",
             "ott": ["웨이브", "왓챠"], "origin": "해외"},
            {"title": "판의 미로: 오필리아와 세 개의 열쇠", "year": 2006, "rating": 8.2, "director": "기예르모 델 토로",
             "actors": "이바나 바케로, 서지 로페즈, 마리벨 베르두",
             "description": "스페인 내전을 배경으로 소녀가 환상의 세계로 들어가는 이야기.",
             "ott": ["넷플릭스", "왓챠"], "origin": "해외"}
        ]
    }
    return movies_db

# 드라마 데이터베이스 (더 많은 작품 추가 및 배우 정보 포함)
def get_dramas_database():
    dramas_db = {
        "액션": [
            {"title": "D.P.", "year": 2021, "rating": 8.2, "director": "한준희", 
             "actors": "정해인, 구교환, 김성균, 손석구",
             "description": "탈영병을 체포하는 군사경찰대의 이야기를 그린 넷플릭스 오리지널 시리즈.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "모범택시", "year": 2021, "rating": 7.9, "director": "박준우", 
             "actors": "이제훈, 이솜, 김의성",
             "description": "택시회사를 운영하며 복수 대행 서비스를 제공하는 주인공의 이야기.",
             "ott": ["웨이브", "티빙"], "origin": "국내"},
            {"title": "빈센조", "year": 2021, "rating": 8.5, "director": "김희원", 
             "actors": "송중기, 전여빈, 옥택연",
             "description": "이탈리아 마피아 변호사가 한국에 와서 악당들을 그들의 방식으로 응징하는 이야기.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "더 보이즈", "year": 2019, "rating": 8.7, "director": "필립 스그리시아",
             "actors": "칼 어번, 잭 퀘이드, 안토니 스타",
             "description": "슈퍼히어로들의 어두운 이면과 그들에 맞서는 사람들의 이야기.",
             "ott": ["아마존 프라임"], "origin": "해외"},
            {"title": "워킹 데드", "year": 2010, "rating": 8.2, "director": "프랭크 다라본트",
             "actors": "앤드류 링컨, 노만 리더스, 멜리사 맥브라이드",
             "description": "좀비 아포칼립스 세계에서 생존자들이 겪는 이야기.",
             "ott": ["넷플릭스", "디즈니+"], "origin": "해외"}
        ],
        "코미디": [
            {"title": "슬기로운 의사생활", "year": 2020, "rating": 9.0, "director": "신원호", 
             "actors": "조정석, 유연석, 정경호, 김대명, 전미도",
             "description": "의대 동기 다섯 명이 한 병원에서 근무하며 겪는 일상과 사랑을 그린 드라마.",
             "ott": ["넷플릭스", "티빙"], "origin": "국내"},
            {"title": "이상한 변호사 우영우", "year": 2022, "rating": 8.8, "director": "유인식", 
             "actors": "박은빈, 강태오, 강기영",
             "description": "자폐 스펙트럼 장애를 가진 천재 변호사의 법정 활약을 그린 드라마.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "웬즈데이", "year": 2022, "rating": 8.2, "director": "팀 버튼", 
             "actors": "제나 오르테가, 그웬돌린 크리스티, 제이미 맥셰인",
             "description": "아담스 패밀리의 딸 웬즈데이가 네버모어 아카데미에서 겪는 미스터리한 사건들.",
             "ott": ["넷플릭스"], "origin": "해외"},
            {"title": "김비서가 왜 그럴까", "year": 2018, "rating": 8.0, "director": "박준화",
             "actors": "박서준, 박민영, 이태환",
             "description": "재력, 얼굴, 수완까지 모든 것을 다 갖췄지만 자기애로 똘똘 뭉친 나르시시스트 부회장과 그를 완벽하게 보좌해온 비서의 퇴사 밀당 로맨스.",
             "ott": ["티빙", "넷플릭스"], "origin": "국내"}
        ],
        "로맨스": [
            {"title": "사랑의 불시착", "year": 2019, "rating": 8.9, "director": "이정효", 
             "actors": "현빈, 손예진, 서지혜, 김정현",
             "description": "패러글라이딩 사고로 북한에 불시착한 재벌 상속녀와 북한 장교의 운명적인 사랑.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "스물다섯 스물하나", "year": 2022, "rating": 8.7, "director": "정지현", 
             "actors": "김태리, 남주혁, 김지연",
             "description": "IMF 시대를 배경으로 펜싱 선수와 신문사 만화 작가 지망생의 성장과 사랑을 그린 드라마.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "그 해 우리는", "year": 2021, "rating": 8.5, "director": "김윤진", 
             "actors": "최우식, 김다미, 김성철",
             "description": "첫사랑 커플의 10년에 걸친 사랑과 이별, 그리고 다시 만남을 그린 드라마.",
             "ott": ["넷플릭스", "티빙"], "origin": "국내"},
            {"title": "별에서 온 그대", "year": 2013, "rating": 8.9, "director": "장태유",
             "actors": "전지현, 김수현, 박해진",
             "description": "400년 전 지구에 떨어진 외계인 도민준과 한류 톱스타 천송이의 로맨스.",
             "ott": ["웨이브", "티빙"], "origin": "국내"}
        ],
        "스릴러": [
            {"title": "오징어 게임", "year": 2021, "rating": 8.0, "director": "황동혁", 
             "actors": "이정재, 박해수, 정호연",
             "description": "456억의 상금이 걸린 의문의 서바이벌 게임에 참가한 사람들의 이야기.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "마이 네임", "year": 2021, "rating": 7.8, "director": "김진민", 
             "actors": "한소희, 박희순, 안보현",
             "description": "아버지의 죽음을 목격한 딸이 복수를 위해 조직에 들어가 경찰로 위장 잠입하는 이야기.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "지금 우리 학교는", "year": 2022, "rating": 7.6, "director": "이재규", 
             "actors": "박지후, 윤찬영, 조이현",
             "description": "고등학교에서 좀비 바이러스가 퍼지면서 생존을 위해 고군분투하는 학생들의 이야기.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "시그널", "year": 2016, "rating": 9.1, "director": "김원석",
             "actors": "이제훈, 김혜수, 조진웅",
             "description": "과거로부터 걸려온 무전으로 현재와 과거의 형사들이 미제 사건들을 해결해나가는 이야기.",
             "ott": ["티빙", "웨이브"], "origin": "국내"}
        ],
        "공포": [
            {"title": "스위트홈", "year": 2020, "rating": 7.4, "director": "이응복",
             "actors": "송강, 이진욱, 이시영",
             "description": "괴물로 변한 세상에서 살아남기 위한 주민들의 사투.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "킹덤", "year": 2019, "rating": 8.1, "director": "김성훈",
             "actors": "주지훈, 배두나, 류승룡",
             "description": "조선 시대 배경의 좀비 스릴러.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "타인은 지옥이다", "year": 2019, "rating": 7.5, "director": "이창희",
             "actors": "임시완, 이동욱, 이정은",
             "description": "서울로 상경한 청년이 낯선 고시원에서 타인들이 만들어내는 지옥을 경험하는 이야기.",
             "ott": ["티빙", "웨이브"], "origin": "국내"}
        ],
        "SF": [
            {"title": "고요의 바다", "year": 2021, "rating": 6.9, "director": "최항용",
             "actors": "배두나, 공유, 이준",
             "description": "필수 자원 고갈로 황폐해진 미래 지구를 배경으로, 달에 버려진 연구 기지에 대한 이야기.",
             "ott": ["넷플릭스"], "origin": "국내"},
            {"title": "블랙미러", "year": 2011, "rating": 8.8, "director": "찰리 브루커",
             "actors": "다양",
             "description": "기술이 인간의 삶에 미치는 어두운 영향을 다룬 앤솔로지 시리즈.",
             "ott": ["넷플릭스"], "origin": "해외"},
            {"title": "스트레인저 씽스", "year": 2016, "rating": 8.7, "director": "더퍼 브라더스",
             "actors": "밀리 바비 브라운, 핀 울프하드, 게이튼 마타라조",
             "description": "80년대를 배경으로 초자연적 현상과 정부 음모를 파헤치는 아이들의 이야기.",
             "ott": ["넷플릭스"], "origin": "해외"}
        ],
        "판타지": [
            {"title": "도깨비", "year": 2016, "rating": 9.1, "director": "이응복",
             "actors": "공유, 김고은, 이동욱, 유인나",
             "description": "불멸의 삶을 끝내기 위해 인간 신부가 필요한 도깨비와 저승사자의 이야기.",
             "ott": ["티빙", "웨이브"], "origin": "국내"},
            {"title": "호텔 델루나", "year": 2019, "rating": 8.8, "director": "오충환",
             "actors": "아이유, 여진구, 신정근",
             "description": "엘리트 호텔리어와 까칠한 사장 귀신이 운영하는 호텔 델루나에서 벌어지는 이야기.",
             "ott": ["티빙", "웨이브"], "origin": "국내"},
            {"title": "왕좌의 게임", "year": 2011, "rating": 9.2, "director": "데이비드 베니오프",
             "actors": "피터 딘클리지, 레나 헤디, 에밀리아 클라크",
             "description": "일곱 왕국을 차지하기 위한 권력 다툼과 겨울이 오는 공포를 그린 대서사시.",
             "ott": ["웨이브", "디즈니+"], "origin": "해외"}
        ],
        "애니메이션": [
            {"title": "아케인", "year": 2021, "rating": 8.7, "director": "파스칼 샤르몽, 아르노 들렁",
             "actors": "엘라 퍼넬 (목소리), 헤일리 스타인펠드 (목소리)",
             "description": "리그 오브 레전드 세계관을 배경으로 한 애니메이션 시리즈.",
             "ott": ["넷플릭스"], "origin": "해외"}
        ],
        "다큐멘터리": [
            {"title": "나는 신이다: 신이 배신한 사람들", "year": 2023, "rating": 7.0, "director": "조성현",
             "actors": "다큐멘터리 출연진",
             "description": "현대 한국 사회의 여러 종교 관련 사건들을 다룬 다큐멘터리.",
             "ott": ["넷플릭스"], "origin": "국내"}
        ]
    }
    return dramas_db

# filter_content 함수는 배우 정보가 추가되어도 동작에는 변경 없음
# 메인 앱 로직 (배우 정보 출력 부분 추가)
if st.button("추천 받기", help="클릭할 때마다 새로운 작품을 추천해줍니다!"):
    st.subheader("EMOJI_0 당신을 위한 추천 작품 EMOJI_1")

    movies_db = get_movies_database()
    dramas_db = get_dramas_database()

    all_recommendations = []

    if content_type in ["영화", "둘 다"]:
        filtered_movies = filter_content(movies_db, genres, year_range, rating_range, ott_platforms, origin)
        for movie in filtered_movies:
            movie['type'] = '영화'
            all_recommendations.append(movie)

    if content_type in ["드라마", "둘 다"]:
        filtered_dramas = filter_content(dramas_db, genres, year_range, rating_range, ott_platforms, origin)
        for drama in filtered_dramas:
            drama['type'] = '드라마'
            all_recommendations.append(drama)

    if all_recommendations:
        random.shuffle(all_recommendations)
        
        # 상위 5개 추천 (개수 조절 가능)
        display_count = min(5, len(all_recommendations))
        
        for i in range(display_count):
            item = all_recommendations[i]
            st.markdown(f"### {i+1}. {item['title']} ({item['type']})")
            st.markdown(f"**감독:** {item['director']}")
            st.markdown(f"**주연 배우:** {item['actors']}") # 배우 정보 출력
            st.markdown(f"**개봉/방영:** {item['year']}년")
            st.markdown(f"**평점:** ⭐ {item['rating']} / 10")
            st.markdown(f"**OTT:** {', '.join(item['ott'])}")
            st.markdown(f"**국내/해외:** {item['origin']}")
            
            with st.expander("줄거리 보기"):
                st.write(item['description'])
            
            st.markdown("---") # 구분선
    else:
        st.warning("선택하신 조건에 맞는 작품을 찾을 수 없습니다. 필터 옵션을 조정해보세요!")

    # 추가 추천 버튼 (기존 코드와 동일)
    if st.button("다른 작품도 추천받기", key="more_recommendations"):
        st.experimental_rerun()

# 사이드바에 추가 정보 (기존 코드와 동일)
st.sidebar.markdown("---")
st.sidebar.info("EMOJI_2 이 프로그램은 영화/드라마 추천을 돕기 위해 제작되었습니다.")
st.sidebar.info("EMOJI_3 팁: 다양한 필터 옵션을 조합해보세요!")

# 프로그램 실행 방법 안내 (기존 코드와 동일)
if __name__ == "__main__":
    pass
