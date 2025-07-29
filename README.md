
# 📝 Streamlit Task Manager

A simple and efficient task management web app built with [Streamlit](https://streamlit.io/) to help you organize your daily to-dos with priorities and deadlines.

---

## 🚀 Features

- 📋 Add tasks with:
  - Name
  - Description
  - Due date
  - Priority (Low / Medium / High)
- 📊 View task statistics:
  - Total tasks
  - Completed tasks
  - Pending tasks by priority
- ✅ Mark tasks as completed
- ❌ Delete tasks
- 💾 Persistent task storage using `tasks.json`

---

## 📂 File Structure

```bash
├── task2.py           # Main Streamlit application
├── tasks.json         # JSON file used for saving task data (auto-created)
└── README.md          # Project documentation (this file)
```

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/streamlit-task-manager.git
   cd streamlit-task-manager
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install streamlit
   ```

---

## ▶️ Run the App

```bash
streamlit run task2.py
```

This will open a new tab in your browser where you can use the Task Manager app.

---

## 📌 Notes

- The task data is stored locally in a file named `tasks.json`.
- The app automatically refreshes after completing or deleting a task.
- Built-in priority filters and progress bar help you focus on high-priority pending tasks.

---

## 📷 Screenshot

> *(Add your app screenshot here, if available)*

---

## 🧾 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 👤 Author

- **Your Name** – [MITHILESH](https://github.com/MITHILESH-WEB)

---

## 📬 Feedback

Feel free to open an issue or pull request if you have suggestions, bugs, or ideas to improve this project!
