# main.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QTabWidget, QLabel, QFileDialog
)
from automation.file_organizer import organize_files
from automation.pdf_splitter import split_pdf

class AutomationSuite(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Automation Suite")
        self.setGeometry(300, 200, 600, 400)
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.tabs.addTab(self.file_organizer_tab(), "File Organizer")
        self.tabs.addTab(self.pdf_splitter_tab(), "PDF Splitter")

    def file_organizer_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Select a folder to organize files:")
        button = QPushButton("Browse Folder")
        button.clicked.connect(self.browse_and_organize)

        self.status_label = QLabel("Status: Waiting")

        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(self.status_label)
        tab.setLayout(layout)
        return tab

    def browse_and_organize(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            organize_files(folder)
            self.status_label.setText(f"Status: Organized files in {folder}")

    def pdf_splitter_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Select a PDF to split:")
        button = QPushButton("Browse PDF")
        button.clicked.connect(self.browse_and_split_pdf)

        self.pdf_status = QLabel("Status: Waiting")

        layout.addWidget(label)
        layout.addWidget(button)
        layout.addWidget(self.pdf_status)
        tab.setLayout(layout)
        return tab

    def browse_and_split_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select PDF", "", "PDF Files (*.pdf)")
        if file_path:
            split_pdf(file_path)
            self.pdf_status.setText(f"Status: Split PDF: {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutomationSuite()
    window.show()
    sys.exit(app.exec_())
