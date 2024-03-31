# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:11:46 2024

@author: hugot
"""

import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title(" Aplicação GUI com Widget Label")
ttk.Label(janela, text="Componente Label").grid(column=0, row=0)
janela.mainloop()