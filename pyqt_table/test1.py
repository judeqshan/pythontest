import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSlot

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PyQt Table Example')

        # Create a QTableWidget instance
        tableWidget = QTableWidget()

        # Set the row and column count
        tableWidget.setRowCount(5)
        tableWidget.setColumnCount(3)

        # Set horizontal header labels
        tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        # Set vertical header labels
        tableWidget.setVerticalHeaderLabels(['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        # Populate the table with data
        for i in range(5):
            for j in range(3):
                item = QTableWidgetItem(f'Row {i+1}, Column {j+1}')
                tableWidget.setItem(i, j, item)

        # Connect the itemClicked signal to a custom slot
        tableWidget.itemClicked.connect(self.on_item_clicked)

        # Create a layout and add the table to it
        layout = QVBoxLayout()
        layout.addWidget(tableWidget)

        # Create a central widget and set the layout
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    @pyqtSlot(QTableWidgetItem)
    def on_item_clicked(self, item):
        print(f'Item clicked: {item.text()}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableExample()
    window.show()
    sys.exit(app.exec_())