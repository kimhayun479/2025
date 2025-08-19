import streamlit as st
import pandas as pd
import datetime
import json
import os

# 데이터 파일 경로
DATA_FILE = "simple_study_planner.json"

# 초기 데이터 로드 또는 생성
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"subjects": [], "tasks": [], "study_logs": []}

# 데이터 저장
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 앱 메인 함수
def main():
    st.title("김하윤님의 간편 학습 관리")
    
    # 데이터 로드
    data = load_data()
    
    tab1, tab2, tab3 = st.tabs(["📚 과목 관리", "✅ 할 일", "⏱️ 학습 기록"])
    
    with tab1:
        manage_subjects(data)
    
    with tab2:
        manage_tasks(data)
    
    with tab3:
        manage_study_logs(data)

# 과목 관리 화면
def manage_subjects(data):
    st.header("📝 과목 관리")
    
    # 새 과목 추가
    col1, col2 = st.columns([3, 1])
    with col1:
        new_subject = st.text_input("과목명")
    with col2:
        if st.button("추가"):
            if new_subject and new_subject not in [s["name"] for s in data["subjects"]]:
                data["subjects"].append({"name": new_subject, "progress": 0})
                save_data(data)
                st.success(f"'{new_subject}' 추가 완료!")
                st.experimental_rerun()
    
    # 과목 목록 표시
    if data["subjects"]:
        for i, subject in enumerate(data["subjects"]):
            col1, col2, col3 = st.columns([2, 2, 1])
            with col1:
                st.write(f"**{subject['name']}**")
            with col2:
                progress = st.slider(f"진도 (%)", 0, 100, subject["progress"], key=f"prog_{i}")
                if progress != subject["progress"]:
                    data["subjects"][i]["progress"] = progress
                    save_data(data)
            with col3:
                if st.button("삭제", key=f"del_{i}"):
                    data["subjects"].pop(i)
                    save_data(data)
                    st.experimental_rerun()
    else:
        st.info("등록된 과목이 없습니다.")

# 할 일 관리 화면
def manage_tasks(data):
    st.header("✅ 할 일 관리")
    
    # 새 할 일 추가
    if data["subjects"]:
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            subject = st.selectbox("과목", [s["name"] for s in data["subjects"]])
        with col2:
            task = st.text_input("할 일")
        with col3:
            if st.button("추가"):
                if task:
                    data["tasks"].append({
                        "subject": subject,
                        "title": task,
                        "completed": False,
                        "date": datetime.datetime.now().strftime("%Y-%m-%d")
                    })
                    save_data(data)
                    st.success("추가 완료!")
                    st.experimental_rerun()
        
        # 할 일 목록 표시
        if data["tasks"]:
            for i, task in enumerate(data["tasks"]):
                col1, col2 = st.columns([4, 1])
                with col1:
                    done = st.checkbox(
                        f"{task['subject']}: {task['title']} ({task['date']})", 
                        value=task["completed"],
                        key=f"task_{i}"
                    )
                    if done != task["completed"]:
                        data["tasks"][i]["completed"] = done
                        save_data(data)
                with col2:
                    if st.button("삭제", key=f"del_task_{i}"):
                        data["tasks"].pop(i)
                        save_data(data)
                        st.experimental_rerun()
        else:
            st.info("등록된 할 일이 없습니다.")
    else:
        st.warning("할 일을 추가하려면 먼저 과목을 등록해주세요.")

# 학습 기록 관리
def manage_study_logs(data):
    st.header("⏱️ 학습 기록")
    
    # 새 학습 기록 추가
    if data["subjects"]:
        col1, col2, col3 = st.columns([2, 1, 1])
        with col1:
            subject = st.selectbox("과목 선택", [s["name"] for s in data["subjects"]])
        with col2:
            duration = st.number_input("학습 시간(분)", min_value=5, step=5, value=30)
        with col3:
            if st.button("기록"):
                data["study_logs"].append({
                    "subject": subject,
                    "duration": duration,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d")
                })
                save_data(data)
                st.success("학습 기록 완료!")
                st.experimental_rerun()
        
        # 학습 기록 요약
        if data["study_logs"]:
            # 오늘 날짜의 학습 기록만 필터링
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            today_logs = [log for log in data["study_logs"] if log["date"] == today]
            
            if today_logs:
                st.subheader("오늘의 학습")
                total_time = sum(log["duration"] for log in today_logs)
                st.info(f"총 학습 시간: {total_time}분 ({total_time/60:.1f}시간)")
                
                # 과목별 학습 시간
                subject_times = {}
                for log in today_logs:
                    if log["subject"] in subject_times:
                        subject_times[log["subject"]] += log["duration"]
                    else:
                        subject_times[log["subject"]] = log["duration"]
                
                for subject, time in subject_times.items():
                    st.write(f"- {subject}: {time}분")
            else:
                st.info("오늘 기록된 학습이 없습니다.")
        else:
            st.info("학습 기록이 없습니다.")
    else:
        st.warning("학습 기록을 추가하려면 먼저 과목을 등록해주세요.")

if __name__ == "__main__":
    main()
