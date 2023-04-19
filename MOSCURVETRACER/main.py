## @module mos curve
#  Documentation for this module.
# 
#  @author  Rodrigo Pedroso Mendes
#  @version V1.0
#  @date    19/04/23 1:37:33
#
#  #LICENSE# 
#    
#  Copyright (c) 2018 Rodrigo Pedroso Mendes
#
#  Permission is hereby granted, free of charge, to any  person   obtaining  a 
#  copy of this software and associated  documentation files (the "Software"), 
#  to deal in the Software without restriction, including  without  limitation 
#  the rights to use, copy, modify,  merge,  publish,  distribute, sublicense, 
#  and/or sell copies of the Software, and  to  permit  persons  to  whom  the 
#  Software is furnished to do so, subject to the following conditions:        
#   
#  The above copyright notice and this permission notice shall be included  in 
#  all copies or substantial portions of the Software.                         
#   
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  EXPRESS OR 
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE  WARRANTIES  OF  MERCHANTABILITY, 
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
#  AUTHORS OR COPYRIGHT HOLDERS BE  LIABLE FOR ANY  CLAIM,  DAMAGES  OR  OTHER 
#  LIABILITY, WHETHER IN AN ACTION OF  CONTRACT, TORT  OR  OTHERWISE,  ARISING 
#  FROM, OUT OF OR IN CONNECTION  WITH  THE  SOFTWARE  OR  THE  USE  OR  OTHER  
#  DEALINGS IN THE SOFTWARE. 
#    
#  #DESCRIPTION#
#
################################################################################

#-------------------------------------------------------------------------------
# Libraries to Import
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import communication


#-------------------------------------------------------------------------------
# board user interface class
#-------------------------------------------------------------------------------
class boardui(Tk):
   
    #---------------------------------------------------------------------------
    # Constructor
    #---------------------------------------------------------------------------
    def __init__(self):
        Tk.__init__(self)
        # a fix for running on OSX - to center the title text vertically
        if self.tk.call('tk', 'windowingsystem') == 'aqua':
            s = ttk.Style()
            s.configure('TNotebook.Tab', padding=(12, 8, 12, 0)) 
   
        #Main Window notebook, title and properties 
        #self.notebook  = ttk.Notebook(self)
        #self.notebook.grid(column = 0, row = 0, sticky = (N, W))
        self.title("Mos Curve Tracer")
        self.resizable(False, False)


        #Create panels
        commPanel = communication.communicationPanel(self)

        #Add panels to the notebook
        #self.notebook.add(commPanel, text = "Mos")           

    #---------------------------------------------------------------------------
    # Overwrite exception callback
    #---------------------------------------------------------------------------
    def report_callback_exception(self, exc, val, tb):
        print("Fatal Error\n:" + str(val))
        #showerror("Error", message = str(val))
        exit(0)

    #---------------------------------------------------------------------------
    # Tk Main loop
    #---------------------------------------------------------------------------
    def  mainloop(self):
        Tk.mainloop(self)

#-------------------------------------------------------------------------------
# Start    
#-------------------------------------------------------------------------------

#---------------------------------------------------------------------------
# try to run the program and exit it if an error occur    
#---------------------------------------------------------------------------
try:
    ui = boardui() 
    ui.mainloop()
except Exception as e:
    print('An error occurred: {}'.format(e))
    exit(0)

