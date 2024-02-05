"""
author: Ruan Maoliang
datetime: 2024/1/15 17:36
desc: 简易的ui设计，实现功能
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")
import sys
sys.path.append('../')
from src.recognition import *
from src.recognition_camera import Camera
from src.recognition_video import Video



class UI(object):
    def __init__(self, form, model):
        self.setup_ui(form)
        self.model = model

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(1200, 800)
        # 原图无图时显示的label
        self.label_raw_pic = QtWidgets.QLabel(form)
        self.label_raw_pic.setGeometry(QtCore.QRect(10, 30, 320, 240))
        self.label_raw_pic.setStyleSheet("background-color:#bbbbbb;")
        self.label_raw_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_raw_pic.setObjectName("label_raw_pic")
        # 原图右方垂直分割线
        self.line1 = QtWidgets.QFrame(form)
        self.line1.setGeometry(QtCore.QRect(340, 30, 20, 670))
        self.line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        # 原图下方水平分割线
        self.line3 = QtWidgets.QFrame(form)
        self.line3.setGeometry(QtCore.QRect(10, 300, 320, 20))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        # 作者说明label
        self.label_designer = QtWidgets.QLabel(form)
        self.label_designer.setGeometry(QtCore.QRect(20, 700, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_designer.setFont(font)
        self.label_designer.setObjectName("label_designer")

        # 结果布局设置
        self.layout_widget = QtWidgets.QWidget(form)
        self.layout_widget.setGeometry(QtCore.QRect(10, 310, 320, 240))
        self.layout_widget.setObjectName("layoutWidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.layout_widget)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("verticalLayout")
        # 右侧水平线
        self.line2 = QtWidgets.QFrame(self.layout_widget)
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.vertical_layout.addWidget(self.line2)
        # 图片选择按钮
        self.pushButton_select_img = QtWidgets.QPushButton(form)
        self.pushButton_select_img.setGeometry(QtCore.QRect(10, 380, 320, 30))
        self.pushButton_select_img.setObjectName("pushButton_2")
        # 摄像头选择按钮
        self.pushButton_select_camera = QtWidgets.QPushButton(form)
        self.pushButton_select_camera.setGeometry(QtCore.QRect(10, 420, 320, 30))
        self.pushButton_select_camera.setObjectName("pushButton_3")
        # 视频选择按钮
        self.pushButton_select_video = QtWidgets.QPushButton(form)
        self.pushButton_select_video.setGeometry(QtCore.QRect(10, 460, 320, 30))
        self.pushButton_select_video.setObjectName("pushButton_3")
        # 其他布局
        self.graphicsView = QtWidgets.QGraphicsView(form)
        self.graphicsView.setGeometry(QtCore.QRect(360, 210, 800, 500))
        self.graphicsView.setObjectName("graphicsView")
        self.label_result = QtWidgets.QLabel(form)
        self.label_result.setGeometry(QtCore.QRect(361, 21, 71, 16))
        self.label_result.setObjectName("label_result")
        self.label_emotion = QtWidgets.QLabel(form)
        self.label_emotion.setGeometry(QtCore.QRect(715, 21, 71, 16))
        self.label_emotion.setObjectName("label_emotion")
        self.label_emotion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bar = QtWidgets.QLabel(form)
        self.label_bar.setGeometry(QtCore.QRect(720, 170, 80, 180))
        self.label_bar.setObjectName("label_bar")
        self.line = QtWidgets.QFrame(form)
        self.line.setGeometry(QtCore.QRect(361, 150, 800, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_rst = QtWidgets.QLabel(form)
        self.label_rst.setGeometry(QtCore.QRect(700, 50, 100, 100))
        self.label_rst.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rst.setObjectName("label_rst")

        # 信号槽
        self.pushButton_select_img.clicked.connect(self.open_file_browser)
        self.pushButton_select_camera.clicked.connect(self.open_camera)
        self.pushButton_select_video.clicked.connect(self.open_video)
        self.retranslate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "faceSystem"))
        self.label_raw_pic.setText(_translate("Form", "O(∩_∩)O"))
        self.label_designer.setText(_translate("Form", "designed by Ruan Maoliang"))
        self.pushButton_select_img.setText(_translate("Form", "选择图片"))
        self.pushButton_select_camera.setText(_translate("Form", "选择摄像头"))
        self.pushButton_select_video.setText(_translate("Form", "选择视频"))
        self.label_result.setText(_translate("Form", "识别结果"))
        self.label_emotion.setText(_translate("Form", "null"))
        self.label_bar.setText(_translate("Form", "概率直方图"))
        self.label_rst.setText(_translate("Form", "Result"))

    def open_camera(self):
        # print("camera")
        Camera(model=self.model).predict_expression()

    def open_video(self):
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(caption="选取视频", directory="../input/video_test/",
                                                                     filter="All Files (*);;Text Files (*.txt)")
        Video(filename=file_name, model=self.model).predict_expression()

    def open_file_browser(self):
        # 加载模型
        file_name, file_type = QtWidgets.QFileDialog.getOpenFileName(caption="选取图片", directory="../input/picture_test/",
                                                                     filter="All Files (*);;Text Files (*.txt)")
        # 显示原图
        if file_name is not None and file_name != "":
            self.show_raw_img(file_name)
            emotion, possibility = predict_expression(file_name, self.model)
            self.show_results(emotion, possibility)

    def show_raw_img(self, filename):
        img = cv2.imread(filename)
        height, width, channels = img.shape
        if width > height:
            height = int(320*height/width)
            width = 320
        elif width < height:
            width = int(240*width/height)
            height = 240
        else:
            width = 320
            height = 240
        frame = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (width, height))
        self.label_raw_pic.setPixmap(QtGui.QPixmap.fromImage(
                    QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], 3 * frame.shape[1],
                                 QtGui.QImage.Format_RGB888)))

    def show_results(self, emotion, possibility):
        # 显示表情名
        self.label_emotion.setText(QtCore.QCoreApplication.translate("Form", emotion))
        # 显示emoji
        if emotion != 'no':
            img = cv2.imread('../assets/icons/' + str(emotion) + '.png')
            frame = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (100, 100))
            self.label_rst.setPixmap(QtGui.QPixmap.fromImage(
                QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], 3 * frame.shape[1],
                             QtGui.QImage.Format_RGB888)))
        else:
            self.label_rst.setText(QtCore.QCoreApplication.translate("Form", "no result"))
        # 显示直方图
        self.show_bars(list(possibility))

    def show_bars(self, possbility):
        dr = MyFigureCanvas()
        dr.draw_(possbility)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addWidget(dr)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()

    def get_faces_from_image(self, img_path):
        """
        获取图片中的人脸
        :param img_path:
        :return:
        """
        img, img_gray, faces = face_detect(img_path, 'blazeface')
        if len(faces) == 0:
            return None
        # 遍历每一个脸
        faces_gray = []
        for (x, y, w, h) in faces:
            face_img_gray = img_gray[y:y + h + 10, x:x + w + 10]
            face_img_gray = cv2.resize(face_img_gray, (48, 48))
            faces_gray.append(face_img_gray)
        return faces_gray


class MyFigureCanvas(FigureCanvas):

    def __init__(self, parent=None, width=8, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.axes = fig.add_subplot(111)

    def draw_(self, possibility):
        x = ['anger', 'disgust', 'fear', 'happy', 'sad', 'surprised', 'neutral', 'contempt']
        self.axes.bar(x, possibility, align='center')
