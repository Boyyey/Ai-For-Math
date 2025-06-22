# Custom stylesheet for MathSolverApp
STYLE = """
QWidget {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #232526, stop:1 #414345);
    color: #f8f8f2;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-size: 16px;
}
QLabel#TitleLabel {
    font-size: 32px;
    font-weight: bold;
    color: #50fa7b;
    margin-bottom: 20px;
    letter-spacing: 2px;
}
QLabel#SubtitleLabel {
    font-size: 18px;
    color: #8be9fd;
    margin-bottom: 10px;
}
QTextEdit {
    background: #282a36;
    color: #f8f8f2;
    border: 2px solid #44475a;
    border-radius: 10px;
    padding: 10px;
    font-size: 18px;
    min-height: 80px;
}
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #50fa7b, stop:1 #8be9fd);
    color: #282a36;
    border: none;
    border-radius: 10px;
    font-size: 20px;
    font-weight: bold;
    padding: 12px 0;
    margin-top: 10px;
    margin-bottom: 20px;
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
        stop:0 #8be9fd, stop:1 #50fa7b);
}
QLabel#SolutionLabel, QLabel#ExplanationLabel {
    background: #44475a;
    color: #f1fa8c;
    border-radius: 8px;
    padding: 12px;
    font-size: 18px;
    margin-top: 10px;
    margin-bottom: 10px;
}
QScrollBar:vertical {
    background: #282a36;
    width: 12px;
    margin: 0px 0px 0px 0px;
    border-radius: 6px;
}
QScrollBar::handle:vertical {
    background: #50fa7b;
    min-height: 20px;
    border-radius: 6px;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}
"""
