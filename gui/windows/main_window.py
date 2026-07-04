from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("OscilloAI")

        self.resize(1400, 900)

        self.build_ui()

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        central.setLayout(layout)

        title = QLabel("OscilloAI")

        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title.setStyleSheet("""

            font-size:30px;

            font-weight:bold;

            padding:20px;

        """)

        layout.addWidget(title)

        info = QLabel(

            "AI Oscilloscope Waveform Analyzer"

        )

        info.setAlignment(Qt.AlignmentFlag.AlignCenter)

        info.setStyleSheet(

            "font-size:16px;"

        )

        layout.addWidget(info)

        self.status = QStatusBar()

        self.status.showMessage("Ready")

        self.setStatusBar(self.status)