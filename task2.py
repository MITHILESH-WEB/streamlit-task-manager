import streamlit as st
import json
import os
from datetime import datetime


def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)


def main():
    st.set_page_config(
        page_title="Task Manager",
        page_icon="✅",
        layout="wide"
    )

    st.title("📝 Task Manager")
    st.subheader("Organize your work efficiently")

    
    if 'tasks' not in st.session_state:
        st.session_state.tasks = load_tasks()

    
    with st.sidebar:
        st.header("Add New Task")
        with st.form("task_form"):
            task_name = st.text_input("Task Name")
            task_desc = st.text_area("Description")
            due_date = st.date_input("Due Date")
            priority = st.selectbox(
                "Priority",
                ["Low", "Medium", "High"]
            )
            
            submitted = st.form_submit_button("Add Task")
            if submitted and task_name:
                new_task = {
                    "id": len(st.session_state.tasks) + 1,
                    "name": task_name,
                    "description": task_desc,
                    "due_date": due_date.strftime("%Y-%m-%d"),
                    "priority": priority,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "completed": False
                }
                st.session_state.tasks.append(new_task)
                save_tasks(st.session_state.tasks)
                st.success("Task added successfully!")

    
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader("Your Tasks")
        if not st.session_state.tasks:
            st.info("No tasks found. Add some tasks using the sidebar!")

        for i, task in enumerate(st.session_state.tasks):
            with st.expander(f"{task['name']} - {task['priority']} priority"):
                st.write(f"**Description:** {task['description']}")
                st.write(f"**Due Date:** {task['due_date']}")
                st.write(f"**Created:** {task['created_at']}")
                
                c1, c2, c3 = st.columns(3)
                with c1:
                    if st.button(f"Mark Complete", key=f"complete_{i}"):
                        st.session_state.tasks[i]['completed'] = True
                        save_tasks(st.session_state.tasks)
                        st.rerun()
                with c2:
                    if st.button(f"Delete", key=f"delete_{i}"):
                        del st.session_state.tasks[i]
                        save_tasks(st.session_state.tasks)
                        st.experimental_rerun()

    with col2:
        st.subheader("Statistics")
        if st.session_state.tasks:
            total_tasks = len(st.session_state.tasks)
            completed_tasks = sum(1 for task in st.session_state.tasks if task['completed'])
            progress = completed_tasks / total_tasks
            
            st.metric("Total Tasks", total_tasks)
            st.metric("Completed Tasks", completed_tasks)
            st.progress(progress)
            
            high_priority = sum(1 for task in st.session_state.tasks if task['priority'] == "High" and not task['completed'])
            medium_priority = sum(1 for task in st.session_state.tasks if task['priority'] == "Medium" and not task['completed'])
            low_priority = sum(1 for task in st.session_state.tasks if task['priority'] == "Low" and not task['completed'])
            
            st.write("Pending Tasks by Priority:")
            st.write(f"🔴 High: {high_priority}")
            st.write(f"🟡 Medium: {medium_priority}")
            st.write(f"🟢 Low: {low_priority}")

if __name__ == "__main__":
    main()
