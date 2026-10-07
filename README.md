# 🧮 Math 4 Kids

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

#### An interactive, kid-friendly web application built with **_Streamlit_** that makes learning early arithmetic fun, visual, and intuitive. Designed to help young learners build foundational skills and gain confidence in math.

---

## 🌐 Live Demo

Experience the app live in your browser:  
👉 **[Launch Math 4 Kids](https://your-app-name.streamlit.app)**

---

## ✨ Features

- 🏠 **Engaging Landing Page**: Welcome dashboard that framing math as an exciting superpower.
- ➕ **Addition**: Visual concept breakdowns paired with dynamic multiple-choice quizzes.
- ➖ **Subtraction**: Intuitive lessons on taking away/sharing with real-time quiz feedback.
- ✖️ **Multiplication**: Grouping concept explanations and fast-paced arithmetic challenges.
- ➗ **Division**: Fair-sharing visualizations and randomized integer division practice.
- 🔀 **Randomized Quiz Engine**: Generates new numbers on every question with shuffled multiple-choice options.
- ⚡ **Instant Validation**: Immediate visual feedback for correct (`✅`) and incorrect (`❌`) answers.

---

## 🛠️ Tech Stack

- **Language**: Python (>= 3.14)
- **Web Framework**: [Streamlit](https://streamlit.io/)
- **Data Processing**: NumPy, Pandas

---

## 📁 Project Structure

```text
mathforkids/
├── main.py           # Entry point with sidebar navigation configuration
├── home.py           # Landing page content
├── addition.py       # Addition lesson & interactive quiz
├── subtraction.py    # Subtraction lesson & interactive quiz
├── multiplication.py # Multiplication lesson & interactive quiz
├── division.py       # Division lesson & interactive quiz
├── pyproject.toml    # Project metadata & environment configuration
└── .gitignore        # Files ignored by Git control
```

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.14+ installed on your system.

### Installation

1. **Clone the repository:**

```bash
   git clone https://github.com/Maruf39237/math-for-kids-app.git
   cd mathforkids

```

2. **Create and activate a virtual environment:**

```bash
python -m venv .venv

# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate

```

3. **Install dependencies:**

```bash
pip install streamlit numpy pandas

```

_(Or if using `uv`):_

```bash
uv sync

```

---

## 🎮 Running the Application

Launch the app using Streamlit:

```bash
streamlit run main.py

```

Once executed, open your browser and navigate to `http://localhost:8501`.

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.
