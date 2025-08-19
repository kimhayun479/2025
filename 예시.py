import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import json
import os
from matplotlib import font_manager, rc

# 한글 폰트 설정 (윈도우 기준)
try:
    font_path = "C:/Windows/Fonts/malgun.ttf"  # 맑은 고딕
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)
except:
    st.write("한글 폰트가 제대로 설정되지 않았습니다. 영문으로 표시됩니다.")

# 데이터 파일 경로
DATA_FILE = "study_planner_data.json"

# 초기 데이터 로드 또는 생성
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "subjects": [],
            "tasks": [],
            "study_logs": [],
            "goals": []
        }

# 데이터 저장
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 앱 메인 함수
def main():
    st.set_page_config(page_title="김하윤님의 학습 플래너", layout="wide")
    
    # 데이터 로드
    data = load_data()
    
    # 사이드바 메뉴
    menu = st.sidebar.selectbox(
        "메뉴 선택",
        ["📚 대시보드", "📝 과목 관리", "✅ 할 일 관리", "⏱️ 학습 기록", "🎯 목표 설정"]
    )
    
    if menu == "📚 대시보드":
        show_dashboard(data)
    elif menu == "📝 과목 관리":
        manage_subjects(data)
    elif menu == "✅ 할 일 관리":
        manage_tasks(data)
    elif menu == "⏱️ 학습 기록":
        manage_study_logs(data)
    elif menu == "🎯 목표 설정":
        manage_goals(data)

# 대시보드 화면
def show_dashboard(data):
    st.title("📚 김하윤님의 학습 플래너 대시보드")
    
    # 현재 날짜 표시
    today = datetime.datetime.now()
    st.subheader(f"오늘 날짜: {today.strftime('%Y년 %m월 %d일')}")
    
    col1, col2 = st.columns(2)
    
    # 오늘의 할 일
    with col1:
        st.subheader("📌 오늘의 할 일")
        today_str = today.strftime("%Y-%m-%d")
        today_tasks = [task for task in data["tasks"] 
                      if task["due_date"] == today_str and task["completed"] == False]
        
        if today_tasks:
            for i, task in enumerate(today_tasks):
                st.markdown(f"- {task['subject']}: **{task['title']}**")
        else:
            st.info("오늘의 할 일이 없습니다.")
    
    # D-day 카운터
    with col2:
        st.subheader("⏰ 중요 일정")
        goals = data["goals"]
        if goals:
            for goal in goals:
                goal_date = datetime.datetime.strptime(goal["target_date"], "%Y-%m-%d")
                days_left = (goal_date - today).days
                
                if days_left >= 0:
                    st.markdown(f"- **{goal['title']}**: D-{days_left}")
                else:
                    st.markdown(f"- ~~{goal['title']}~~: 종료됨")
        else:
            st.info("설정된 목표가 없습니다.")
    
    # 과목별 학습 시간 그래프
    st.subheader("📊 과목별 학습 시간 (최근 7일)")
    
    # 최근 7일간의 로그 필터링
    seven_days_ago = today - datetime.timedelta(days=7)
    recent_logs = [log for log in data["study_logs"] 
                  if datetime.datetime.strptime(log["date"], "%Y-%m-%d") >= seven_days_ago]
    
    # 과목별 시간 계산
    subject_times = {}
    for log in recent_logs:
        if log["subject"] in subject_times:
            subject_times[log["subject"]] += log["duration"]
        else:
            subject_times[log["subject"]] = log["duration"]
    
    if subject_times:
        fig, ax = plt.subplots(figsize=(10, 5))
        subjects = list(subject_times.keys())
        times = list(subject_times.values())
        ax.bar(subjects, times, color='skyblue')
        ax.set_ylabel('학습 시간 (분)')
        ax.set_title('최근 7일간 과목별 학습 시간')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("최근 7일간의 학습 기록이 없습니다.")
    
    # 진도율 표시
    st.subheader("📈 과목별 진도율")
    
    if data["subjects"]:
        progress_df = pd.DataFrame(data["subjects"])
        for idx, subject in enumerate(progress_df["name"]):
            progress = progress_df["progress"][idx]
            st.markdown(f"**{subject}**")
            st.progress(progress / 100)
            st.write(f"{progress}% 완료")
    else:
        st.info("등록된 과목이 없습니다.")

# 과목 관리 화면
def manage_subjects(data):
    st.title("📝 과목 관리")
    
    # 새 과목 추가
    st.subheader("새 과목 추가")
    col1, col2 = st.columns(2)
    with col1:
        new_subject = st.text_input("과목명")
    with col2:
        new_progress = st.slider("현재 진도율 (%)", 0, 100, 0)
    
    if st.button("과목 추가"):
        if new_subject:
            data["subjects"].append({
                "name": new_subject,
                "progress": new_progress,
                "created_at": datetime.datetime.now().strftime("%Y-%m-%d")
            })
            save_data(data)
            st.success(f"'{new_subject}' 과목이 추가되었습니다!")
        else:
            st.error("과목명을 입력해주세요.")
    
    # 과목 목록 및 진도 업데이트
        # 과목 목록 및 진도 업데이트
    st.subheader("과목 목록 및 진도 관리")
    
    if data["subjects"]:
        for i, subject in enumerate(data["subjects"]):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"**{subject['name']}** (현재 진도: {subject['progress']}%)")
            
            with col2:
                new_progress = st.slider(f"진도 업데이트: {subject['name']}", 
                                        0, 100, int(subject['progress']), key=f"prog_{i}")
                if new_progress != subject['progress']:
                    data["subjects"][i]["progress"] = new_progress
                    save_data(data)
                    st.success(f"{subject['name']} 진도가 업데이트되었습니다!")
            
            with col3:
                if st.button(f"삭제", key=f"del_subj_{i}"):
                    data["subjects"].pop(i)
                    save_data(data)
                    st.experimental_rerun()
    else:
        st.info("등록된 과목이 없습니다. 위에서 새 과목을 추가해보세요!")

# 할 일 관리 화면
def manage_tasks(data):
    st.title("✅ 할 일 관리")
    
    # 새 할 일 추가
    st.subheader("새 할 일 추가")
    
    # 과목 목록이 있는 경우에만 드롭다운 표시
    if data["subjects"]:
        subject_names = [subject["name"] for subject in data["subjects"]]
        subject_names.append("기타")  # 기타 옵션 추가
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            task_subject = st.selectbox("과목", subject_names)
        
        with col2:
            task_title = st.text_input("할 일 제목")
        
        with col3:
            task_due = st.date_input("마감일", datetime.datetime.now())
            
        task_desc = st.text_area("상세 설명 (선택사항)")
        
        if st.button("할 일 추가"):
            if task_title:
                data["tasks"].append({
                    "subject": task_subject,
                    "title": task_title,
                    "description": task_desc,
                    "due_date": task_due.strftime("%Y-%m-%d"),
                    "completed": False,
                    "created_at": datetime.datetime.now().strftime("%Y-%m-%d")
                })
                save_data(data)
                st.success("새 할 일이 추가되었습니다!")
            else:
                st.error("할 일 제목을 입력해주세요.")
    else:
        st.warning("할 일을 추가하려면 먼저 과목을 등록해주세요.")
    
    # 할 일 목록
    st.subheader("할 일 목록")
    
    # 필터 옵션
    filter_options = ["모든 할 일", "완료된 할 일", "미완료 할 일"]
    filter_choice = st.radio("필터", filter_options, horizontal=True)
    
    if data["tasks"]:
        # 할 일 정렬 (마감일 기준)
        sorted_tasks = sorted(data["tasks"], 
                             key=lambda x: x["due_date"])
        
        # 필터 적용
        if filter_choice == "완료된 할 일":
            sorted_tasks = [task for task in sorted_tasks if task["completed"]]
        elif filter_choice == "미완료 할 일":
            sorted_tasks = [task for task in sorted_tasks if not task["completed"]]
        
        for i, task in enumerate(sorted_tasks):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # 완료 여부에 따른 스타일 변경
                if task["completed"]:
                    st.markdown(f"~~**{task['subject']}**: {task['title']}~~")
                else:
                    due_date = datetime.datetime.strptime(task["due_date"], "%Y-%m-%d")
                    today = datetime.datetime.now()
                    
                    # 마감일이 지났으면 빨간색으로 표시
                    if due_date.date() < today.date() and not task["completed"]:
                        st.markdown(f"🚨 **{task['subject']}**: {task['title']} (마감일: {task['due_date']})")
                    else:
                        st.markdown(f"**{task['subject']}**: {task['title']} (마감일: {task['due_date']})")
                
                if task["description"]:
                    st.markdown(f"> {task['description']}")
            
            with col2:
                col2_1, col2_2 = st.columns(2)
                
                with col2_1:
                    if st.button("✓" if not task["completed"] else "↩️", key=f"comp_{i}"):
                        data["tasks"][data["tasks"].index(task)]["completed"] = not task["completed"]
                        save_data(data)
                        st.experimental_rerun()
                
                with col2_2:
                    if st.button("🗑️", key=f"del_task_{i}"):
                        data["tasks"].remove(task)
                        save_data(data)
                        st.experimental_rerun()
            
            st.markdown("---")
    else:
        st.info("등록된 할 일이 없습니다.")

# 학습 기록 관리
def manage_study_logs(data):
    st.title("⏱️ 학습 기록")
    
    # 새 학습 기록 추가
    st.subheader("새 학습 기록 추가")
    
    if data["subjects"]:
        subject_names = [subject["name"] for subject in data["subjects"]]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            log_subject = st.selectbox("과목", subject_names)
        
        with col2:
            log_date = st.date_input("학습 날짜", datetime.datetime.now())
        
        with col3:
            log_duration = st.number_input("학습 시간 (분)", min_value=1, value=60)
        
        log_content = st.text_area("학습 내용 (선택사항)")
        
        if st.button("학습 기록 추가"):
            data["study_logs"].append({
                "subject": log_subject,
                "date": log_date.strftime("%Y-%m-%d"),
                "duration": log_duration,
                "content": log_content
            })
            save_data(data)
            st.success("학습 기록이 추가되었습니다!")
    else:
        st.warning("학습 기록을 추가하려면 먼저 과목을 등록해주세요.")
    
           # 학습 기록 목록
    st.subheader("학습 기록 조회")
    
    if data["study_logs"]:
        # 날짜별 필터링 옵션
        col1, col2 = st.columns(2)
        with col1:
            start_date = st.date_input("시작일", 
                                     value=datetime.datetime.now() - datetime.timedelta(days=7))
        with col2:
            end_date = st.date_input("종료일", 
                                   value=datetime.datetime.now())
        
        # 날짜 범위에 맞는 로그 필터링
        filtered_logs = [log for log in data["study_logs"] 
                        if start_date <= datetime.datetime.strptime(log["date"], "%Y-%m-%d").date() <= end_date]
        
        if filtered_logs:
            # 날짜별 정렬
            sorted_logs = sorted(filtered_logs, 
                               key=lambda x: x["date"], reverse=True)
            
            # 총 학습 시간 계산
            total_minutes = sum(log["duration"] for log in sorted_logs)
            st.info(f"선택 기간 총 학습 시간: {total_minutes} 분 ({total_minutes/60:.1f} 시간)")
            
            # 학습 기록 표시
            for i, log in enumerate(sorted_logs):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                with col1:
                    st.markdown(f"**{log['date']} - {log['subject']}** ({log['duration']}분)")
                    if log["content"]:
                        st.markdown(f"> {log['content']}")
                
                with col3:
                    if st.button("🗑️", key=f"del_log_{i}"):
                        data["study_logs"].remove(log)
                        save_data(data)
                        st.experimental_rerun()
                
                st.markdown("---")
            
            # 과목별 학습 시간 파이 차트
            st.subheader("과목별 학습 시간 분포")
            subject_times = {}
            for log in sorted_logs:
                if log["subject"] in subject_times:
                    subject_times[log["subject"]] += log["duration"]
                else:
                    subject_times[log["subject"]] = log["duration"]
            
            fig, ax = plt.subplots()
            ax.pie(subject_times.values(), labels=subject_times.keys(), autopct='%1.1f%%')
            ax.axis('equal')
            st.pyplot(fig)
        else:
            st.info("선택한 기간에 학습 기록이 없습니다.")
    else:
        st.info("등록된 학습 기록이 없습니다.")

# 목표 설정 관리
def manage_goals(data):
    st.title("🎯 목표 설정")
    
    # 새 목표 추가
    st.subheader("새 목표 추가")
    
    col1, col2 = st.columns(2)
    
    with col1:
        goal_title = st.text_input("목표 제목")
    
    with col2:
        goal_date = st.date_input("목표 날짜", 
                                value=datetime.datetime.now() + datetime.timedelta(days=30))
    
    goal_desc = st.text_area("목표 설명 (선택사항)")
    
    if st.button("목표 추가"):
        if goal_title:
            data["goals"].append({
                "title": goal_title,
                "description": goal_desc,
                "target_date": goal_date.strftime("%Y-%m-%d"),
                "created_at": datetime.datetime.now().strftime("%Y-%m-%d")
            })
            save_data(data)
            st.success("새 목표가 추가되었습니다!")
        else:
            st.error("목표 제목을 입력해주세요.")
    
    # 목표 목록
    st.subheader("목표 목록")
    
    if data["goals"]:
        # 날짜순 정렬
        sorted_goals = sorted(data["goals"], 
                             key=lambda x: x["target_date"])
        
        for i, goal in enumerate(sorted_goals):
            target_date = datetime.datetime.strptime(goal["target_date"], "%Y-%m-%d")
            today = datetime.datetime.now()
            days_left = (target_date - today).days
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**{goal['title']}** (목표일: {goal['target_date']})")
                
                if days_left >= 0:
                    st.info(f"D-{days_left}")
                else:
                    st.warning("목표일이 지났습니다.")
                
                if goal["description"]:
                    st.markdown(f"> {goal['description']}")
            
            with col2:
                if st.button("🗑️", key=f"del_goal_{i}"):
                    data["goals"].remove(goal)
                    save_data(data)
                    st.experimental_rerun()
            
            st.markdown("---")
    else:
        st.info("등록된 목표가 없습니다.")

# 앱 실행
if __name__ == "__main__":
    main()
