# 🤖✨ AI Math Solver ✨🧮

AI Math Solver is a user-friendly desktop application that leverages AI and symbolic computation to solve mathematical equations and provide step-by-step explanations. Built with PyQt5, it features a modern GUI for entering math problems in natural language or equation form, and supports OCR for extracting equations from images.

---

## 🚀 Features

- 🧩 **Equation Solving:** Enter algebraic, quadratic, or other equations and get instant solutions.
- 📖 **Step-by-Step Explanations:** Understand the solution process with detailed explanations.
- 💬 **Natural Language Input:** Type math problems in plain English or standard math notation.
- 🖼️ **OCR Support:** Extract equations from images (e.g., handwritten notes, textbooks).
- 🎨 **Beautiful UI:** Modern, clean, and responsive interface.
- 🛠️ **Extensible:** Modular codebase for easy addition of new features (e.g., plotting, calculus, statistics).

---

## 🌟 Potential Applications

- 🎓 **Educational Tool:** Help students learn math by showing solutions and explanations.
- 🏠 **Homework Helper:** Quickly solve and understand homework problems.
- 👩‍🏫 **Math Assistant:** Aid teachers in preparing materials or checking answers.
- ♿ **Accessibility:** Assist users with dyslexia or visual impairments via OCR and explanations.
- 📱 **Mobile/Cloud Expansion:** Adapt the core logic for mobile apps or web/cloud-based math solvers.
- 🔬 **STEM Research:** Integrate with LaTeX or scientific tools for research workflows.

---

## 🛠️ How to Run

### 1. 🧑‍💻 Clone the Repository

```powershell
git clone <your-repo-url>
cd "Math solver"
```

### 2. 🏗️ Set Up a Virtual Environment (Recommended)

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### 3. 📦 Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. 🖥️ Run the Application

For the GUI (recommended):
```powershell
python main_qt.py
```

For the Streamlit web app:
```powershell
streamlit run app.py
```

✨ The application window will open. Enter a math problem or equation and click "Solve" to see the solution and explanation!

---

## 🗂️ File Structure

- `main_qt.py` — Main GUI application
- `solver.py` — Equation solving logic
- `explain.py` — Generates step-by-step explanations
- `extract_equation.py` — Parses and extracts equations from input
- `ocr.py` — OCR utilities for image-to-equation
- `plotter.py` — (Optional) Plotting utilities
- `qt_style.py` — Custom UI styles
- `requirements.txt` — Python dependencies
- `sample_images/` — Example images for OCR

---

## 🤝 Contributing

Pull requests and feature suggestions are welcome! Please open an issue to discuss your ideas. Let's make math magical together! ✨

---

<p align="center"><b>Empower your math journey with AI! 🚀🧮</b></p>
