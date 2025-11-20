import unittest
from unittest.mock import patch, MagicMock
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
import tkinter.messagebox
import cv2
import os
from main import Face_Recognition_System
class TestFaceRecognitionSystem(unittest.TestCase):

    @patch('tkinter.Tk')
    def setUp(self, mock_tk):
        self.root = mock_tk()
        self.app = Face_Recognition_System(self.root)

    @patch('tkinter.Toplevel')
    @patch('student.student')
    def test_student_details(self, mock_student, mock_toplevel):
        self.app.student_detials()
        mock_toplevel.assert_called_with(self.root)
        mock_student.assert_called_with(mock_toplevel.return_value)

    @patch('os.startfile')
    def test_open_img(self, mock_startfile):
        self.app.open_img()
        mock_startfile.assert_called_with("data")

    @patch('tkinter.Toplevel')
    @patch('train.Train')
    def test_train_data(self, mock_train, mock_toplevel):
        self.app.train_data()
        mock_toplevel.assert_called_with(self.root)
        mock_train.assert_called_with(mock_toplevel.return_value)

    @patch('tkinter.Toplevel')
    @patch('face_recognition.Face_recognition')
    def test_face_data(self, mock_face_recognition, mock_toplevel):
        self.app.face_data()
        mock_toplevel.assert_called_with(self.root)
        mock_face_recognition.assert_called_with(mock_toplevel.return_value)

    @patch('tkinter.Toplevel')
    @patch('attendance.Attendance')
    def test_attendance_data(self, mock_attendance, mock_toplevel):
        self.app.attendance_data()
        mock_toplevel.assert_called_with(self.root)
        mock_attendance.assert_called_with(mock_toplevel.return_value)

    @patch('tkinter.messagebox.askyesno')
    def test_iExit_yes(self, mock_askyesno):
        mock_askyesno.return_value = True
        with patch.object(self.root, 'destroy') as mock_destroy:
            self.app.iExit()
            mock_destroy.assert_called_once()

    @patch('tkinter.messagebox.askyesno')
    def test_iExit_no(self, mock_askyesno):
        mock_askyesno.return_value = False
        with patch.object(self.root, 'destroy') as mock_destroy:
            self.app.iExit()
            mock_destroy.assert_not_called()

    def tearDown(self):
        del self.app

if __name__ == '__main__':
    unittest.main()