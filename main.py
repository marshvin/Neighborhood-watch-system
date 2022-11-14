#Neighborhood watch management system
from functools import partial
from tkinter import *
from tkinter import messagebox
import pymysql
import custom as dt
import pepinfo as pep

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Parklands Neighborhood watch")
        self.window.geometry("880x800")
        self.window.config(bg = "white")
        