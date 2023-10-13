import sys
#from PySide6.QtCore import Qt
#from PySide6.QtWidgets import QApplication, QLabel
import logging
import node

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":

    print (node.node(['metadata','1.json']))    

    logging.info('application run ...')

    # app = QApplication(sys.argv)
    # label = QLabel("Hello World", alignment=Qt.AlignCenter)
    # label.show()
    # label.setMinimumSize(1000,1000)
    # sys.exit(app.exec_())