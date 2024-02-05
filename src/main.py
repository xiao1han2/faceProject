"""
author: Ruan Maoliang
datetime: 2023/12/29 17:31
desc: 功能实现
"""

import sys
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from PyQt5 import QtWidgets

sys.path.append(os.path.dirname(__file__) + '/ui')
from src.ui.ui import UI
from config import *


def load_cnn_model():
    """
    载入CNN模型
    :return:
    """
    from model import CNN3
    model = CNN3()
    model.load_weights(MODEL_CK)
    return model


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QMainWindow()
    model = load_cnn_model()
    ui = UI(form, model)
    form.show()
    sys.exit(app.exec_())
