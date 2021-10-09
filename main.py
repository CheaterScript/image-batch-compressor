#!/usr/bin/python3

import os
import sys
import re
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtWinExtras import QWinTaskbarProgress, QWinTaskbarButton
from resUI import Ui_MainWindow
from processer import handle
from multiprocessing import Process, Queue, set_start_method, get_context, freeze_support


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.precent = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.handle)
        self.updateTimer = QTimer(self)
        self.updateTimer.timeout.connect(self.update)
        self.p = None
        self.q = Queue()
        self.inputPath = ''
        self.outputPath = ''
        self.image_width = 512
        self.image_height = 512
        self.max_width = 512
        self.max_height = 512
        self.jpge_quality = 10
        self.png_compression = 9
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_openInput.clicked.connect(self.selectInputDir)
        self.ui.btn_openOutput.clicked.connect(self.selectOutputDir)
        self.ui.btn_start.clicked.connect(self.start)

        self.taskBarButton = QWinTaskbarButton(self)

        # 初始化Input
        self.ui.input_width.setText(str(self.image_width))
        self.ui.input_height.setText(str(self.image_height))
        self.ui.input_maxWidth.setText(str(self.max_width))
        self.ui.input_maxHeight.setText(str(self.max_height))
        self.ui.input_jpgeQuality.setText(str(self.jpge_quality))
        self.ui.input_pngCompression.setText(str(self.png_compression))

    def showProgress(self, value):
        self.taskBarButton.setWindow(self.windowHandle())
        progress = self.taskBarButton.progress()
        progress.setRange(0, 100)
        progress.setVisible(True)
        progress.setValue(value)
        progress.show()

    def hideProgress(self):
        self.taskBarButton.setWindow(self.windowHandle())
        progress = self.taskBarButton.progress()
        progress.setVisible(False)

    def selectInputDir(self):
        self.inputPath = QFileDialog.getExistingDirectory(
            self, "选择输入目录", self.inputPath)
        self.ui.input_input.setText(self.inputPath)

    def selectOutputDir(self):
        self.outputPath = QFileDialog.getExistingDirectory(
            self, "选择输出目录", self.outputPath)
        self.ui.input_output.setText(self.outputPath)

    def log(self, text):
        self.ui.textBrowser.append(text)

    def start(self):
        if self.ui.btn_start.text() == '停 止':
            self.stop()
            return
        # 检查参数
        # 修改窗口状态
        if not self.checkInputs():
            return
        if self.p:
            return
        self.ui.group_setting.setEnabled(False)
        self.ui.btn_start.setText('停 止')
        self.ui.textBrowser.clear()
        self.log('开始处理')
        self.timer.start(100)
        self.updateTimer.start(100)
        self.precent = 0
        self.showProgress(0)

    def update(self):
        self.precent += 1
        if self.precent >= 100:
            self.precent = 0
        self.showProgress(self.precent)
        while not self.q.empty():
            text = self.q.get()
            self.log(text)
        if self.p and not self.p.is_alive():
            self.stop()

    def handle(self):
        self.timer.stop()
        p = Process(target=handle, args=(
            self.q,
            (self.ui.input_input.text()),
            (self.ui.input_output.text()),
            int(self.ui.input_width.text()),
            int(self.ui.input_height.text()),
            int(self.ui.input_maxWidth.text()),
            int(self.ui.input_maxHeight.text()),
            int(self.ui.input_jpgeQuality.text()),
            int(self.ui.input_pngCompression.text()),
        ))
        p.daemon = True
        p.start()
        # p.join()
        self.p = p

    def stop(self):
        self.ui.group_setting.setEnabled(True)
        self.ui.btn_start.setText('开始处理')
        if self.p:
            self.p.terminate()
            self.p.join()
            self.p = None
        self.updateTimer.stop()
        self.hideProgress()

    def checkInputs(self):
        # 检查输入
        if not os.path.exists(self.ui.input_input.text()):
            QMessageBox.critical(self.ui.centralwidget, '参数错误', '输入目录不存在!')
            return False
        pattern = re.compile(
            u'[a-zA-Z]:/((?:[a-zA-Z0-9\u4e00-\u9fa5() ]*/)*).*.')
        if not re.match(pattern, self.ui.input_output.text()):
            QMessageBox.critical(self.ui.centralwidget, '参数错误', '输出目录不存在!')
            return False
        # 检查
        input = self.ui.input_width.text()
        if not input.isnumeric():
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '宽度必须是数字!')
            return False
        if not int(input) > 0:
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '宽度必须是大于零的数字!')
            return False

        if not self.ui.input_height.text().isnumeric():
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '高度必须是数字!')
            return False
        if not self.ui.input_maxWidth.text().isnumeric():
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '宽度阈值必须是数字!')
            return False
        if not self.ui.input_maxHeight.text().isnumeric():
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '高度阈值必须是数字!')
            return False
        if not self.ui.input_jpgeQuality.text().isnumeric():
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', 'JPGE质量必须是数字!')
            return False
        if not self.ui.input_pngCompression.text().isnumeric():
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', 'PNG质量必须是数字!')
            return False

        input = self.ui.input_height.text()
        if not int(input) > 0:
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '高度必须是大于零的数字!')
            return False
        input = self.ui.input_maxWidth.text()
        if not int(input) > 0:
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '宽度阈值必须是大于零的数字!')
            return False
        input = self.ui.input_maxHeight.text()
        if not int(input) > 0:
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', '高度阈值必须是大于零的数字!')
            return False
        input = self.ui.input_jpgeQuality.text()
        if not int(input) > 0 or int(input) > 100:
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', 'JPGE质量必须是0-100的整数!')
            return False
        input = self.ui.input_pngCompression.text()
        if not int(input) > 0 or int(input) > 10:
            QMessageBox.critical(
                self.ui.centralwidget, '参数错误', 'png质量必须是0-10的整数!')
            return False
        return True


if __name__ == '__main__':
    # windows 启动方式
    set_start_method('spawn')
    # 获取上下文
    ctx = get_context('spawn')
    # main()
    freeze_support()
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    window.ui.group_setting.setEnabled(True)
    sys.exit(app.exec_())
