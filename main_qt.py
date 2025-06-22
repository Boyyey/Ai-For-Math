from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QMessageBox, QHBoxLayout, QFrame
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from solver import solve_equation
from explain import explain_solution
from extract_equation import extract_equation
from qt_style import STYLE
import sys

class MathSolverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AI Math Solver')
        self.setGeometry(100, 100, 600, 520)
        self.setWindowIcon(QIcon())
        self.setStyleSheet(STYLE)
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(10)

        self.title = QLabel('AI Math Solver')
        self.title.setObjectName('TitleLabel')
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.subtitle = QLabel('Enter your math problem or question:')
        self.subtitle.setObjectName('SubtitleLabel')
        self.subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.subtitle)

        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("e.g., x**2 - 5*x + 6 = 0 or 'Solve x squared minus 5x plus 6 equals 0'")
        layout.addWidget(self.text_input)

        self.solve_button = QPushButton('Solve')
        self.solve_button.clicked.connect(self.solve_math)
        layout.addWidget(self.solve_button)

        self.solution_label = QLabel('')
        self.solution_label.setObjectName('SolutionLabel')
        self.solution_label.setWordWrap(True)
        layout.addWidget(self.solution_label)

        self.explanation_label = QLabel('')
        self.explanation_label.setObjectName('ExplanationLabel')
        self.explanation_label.setWordWrap(True)
        layout.addWidget(self.explanation_label)

        self.setLayout(layout)

    def solve_math(self):
        equation_input = self.text_input.toPlainText().strip()
        if not equation_input:
            QMessageBox.warning(self, 'Input Error', 'Please enter a math problem.')
            return
        eq = extract_equation(equation_input)
        if not eq:
            QMessageBox.warning(self, 'Input Error', 'Could not extract a valid equation. Please enter a clear math expression or equation.')
            return
        try:
            solution = solve_equation(eq)
            self.solution_label.setText(f'<b>Solution:</b> {solution}')
            explanation = explain_solution(eq)
            self.explanation_label.setText(f'<b>Explanation:</b> {explanation}')
        except Exception as e:
            QMessageBox.critical(self, 'Solve Error', f'Could not solve: {e}')

def main():
    app = QApplication(sys.argv)
    window = MathSolverApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
