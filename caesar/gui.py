""":mod:`caesar.gui` --- Graphics for Caesar cipher
"""

from PySide import QtCore, QtGui
import metadata
from cipher import caesar

MAX_KEY_LENGTH = 4

class MainWindow(QtGui.QMainWindow):
    """Graphical entry point."""
    def __init__(self, parent=None):
        """Create the main window."""
        super(MainWindow, self).__init__(parent)

        # title
        self.setWindowTitle(metadata.nice_title)

        # menu
        self.menu_bar = QtGui.QMenuBar()
        self.file_menu = self.menu_bar.addMenu('&File')
        self.quit_action = self.file_menu.addAction('&Quit')
        self.quit_action.triggered.connect(self.close)
        self.help_menu = self.menu_bar.addMenu('&Help')
        self.about_action = self.help_menu.addAction('&About')
        self.about_action.triggered.connect(self.about)
        self.setMenuBar(self.menu_bar)

        # window contents
        self.setCentralWidget(QtGui.QWidget(self))
        self.layout = QtGui.QFormLayout(self.centralWidget())
        self.text_field = QtGui.QPlainTextEdit(self.centralWidget())
        self.layout.addRow('Text', self.text_field)
        self.key_field = QtGui.QLineEdit(self.centralWidget())
        self.key_field.setPlaceholderText('Enter key...')
        self.key_field.setMaxLength(MAX_KEY_LENGTH)
        self.int_validator = QtGui.QIntValidator(self.centralWidget())
        self.key_field.setValidator(self.int_validator)
        self.layout.addRow('Key', self.key_field)
        self.button_box = QtGui.QDialogButtonBox(self.centralWidget())
        self.encrypt_button = QtGui.QPushButton('Encrypt', self.centralWidget())
        self.encrypt_button.clicked.connect(self.encrypt)
        self.encrypt_button.setDefault(True)
        self.button_box.addButton(self.encrypt_button,
                                  QtGui.QDialogButtonBox.ActionRole)
        self.decrypt_button = QtGui.QPushButton('Decrypt', self.centralWidget())
        self.decrypt_button.clicked.connect(self.decrypt)
        self.button_box.addButton(self.decrypt_button, 
                                  QtGui.QDialogButtonBox.ActionRole)
        self.layout.addRow(self.button_box)
        self.auto_encrypt_checkbox = QtGui.QCheckBox(self.centralWidget())
        self.auto_encrypt_checkbox.stateChanged.connect(self.auto_encrypt_changed)
        self.layout.addRow('Auto-Encrypt', self.auto_encrypt_checkbox)
        self.output_field = QtGui.QPlainTextEdit(self.centralWidget())
        self.output_field.setReadOnly(True)
        self.layout.addRow('Result', self.output_field)
        self.copy_result_to_text_button = QtGui.QPushButton(
            'Copy result to text', self.centralWidget())
        self.copy_result_to_text_button.clicked.connect(
            self.copy_result_to_text)
        self.layout.addRow(self.copy_result_to_text_button)
        
    @QtCore.Slot()
    def about(self):
        """Create and show the about dialog."""
        AboutDialog(self).exec_()

    @QtCore.Slot()
    def encrypt(self):
        """Encrypt the text in the field. Just calls
        :meth:`self.do_caesar(True)`.

        .. seealso::

           :meth:`do_caesar`"""
        self.do_caesar(True)
        
    @QtCore.Slot()
    def decrypt(self):
        """Decrypt the text in the field. Just calls
        :meth:`self.do_caesar(False)`.
        
        .. seealso::

           :meth:`do_caesar`"""
        self.do_caesar(False)

    def do_caesar(self, encrypt):
        """Peform the Caesar cipher on the text in the field and show the
        results.

        :param encrypt: whether to encrypt or decrypt
        :type encrypt: :class:`bool`
        """
        try:
            key = int(self.key_field.text())
        except ValueError:
            error_dialog = QtGui.QErrorMessage(self)
            error_dialog.showMessage(
                'Please enter a valid integer for the key.')
            return
        if not encrypt:
            key *= -1
        self.output_field.document().setPlainText(
            caesar(self.text_field.toPlainText(), key))

    @QtCore.Slot()
    def auto_encrypt_changed(self, state):
        """Toggle auto-encrypt.

        :param state: whether it is enabled
        :type state: :class:`int`
        """
        if bool(state):
            self.text_field.textChanged.connect(self.encrypt)
        else:
            self.text_field.textChanged.disconnect(self.encrypt)

    @QtCore.Slot()
    def copy_result_to_text(self):
        self.text_field.document().setPlainText(self.output_field.toPlainText())


class AboutDialog(QtGui.QDialog):
    """Shows information about the program."""
    def __init__(self, parent=None):
        """Construct the dialog."""
        super(AboutDialog, self).__init__(parent)
        self.setWindowTitle('About ' + metadata.nice_title)
        self.layout = QtGui.QVBoxLayout(self)
        self.title_label = QtGui.QLabel(metadata.nice_title, self)
        self.layout.addWidget(self.title_label)
        self.version_label = QtGui.QLabel('Version ' + metadata.version, self)
        self.layout.addWidget(self.version_label)
        self.copyright_label = QtGui.QLabel('Copyright (C) ' +
                                            metadata.copyright, self)
        self.layout.addWidget(self.copyright_label)
        self.url_label = QtGui.QLabel(
            '<a href="{0}">{0}</a>'.format(metadata.url), self)
        self.url_label.setOpenExternalLinks(True)
        self.layout.addWidget(self.url_label)
        for i in xrange(self.layout.count()):
            self.layout.itemAt(i).setAlignment(QtCore.Qt.AlignHCenter)
