## @module basicFrame
#  Documentation for this module.
# 
#  @author  Rodrigo Pedroso Mendes
#  @version V1.0
#  @date    19/04/23 1:37:33
#
#  #LICENSE# 
#    
#  Copyright (c) 2023 Rodrigo Pedroso Mendes
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
#  Basic label frame that is used along the boardui program. It organizes  all
#  the widgets in a row using the grid layout.
#
################################################################################

#-------------------------------------------------------------------------------
# Libraries to import
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk

#-------------------------------------------------------------------------------
# basic frame class
#-------------------------------------------------------------------------------
class basicFrame(ttk.Labelframe):

    #---------------------------------------------------------------------------
    # Constructor
    #---------------------------------------------------------------------------
    def __init__(self, 
                 parent, 
                 title, 
                 row = 0, 
                 column = 0, 
                 rowspan = 1, 
                 columnspan = 1):
        #Call the label frame contructor and grid
        ttk.Labelframe.__init__(self, parent, text = title, 
                                padding = "12 12 12 12")
        self.grid(column = column, row = row, rowspan = rowspan, 
                  columnspan = columnspan, sticky = (N, W))
        #Start current row and colomun
        self.row    = 1
        self.column = 1

    #---------------------------------------------------------------------------
    # Increment the column counter
    #---------------------------------------------------------------------------
    def addRow(self):
        self.row = self.row + 1
        self.column = 1

    #---------------------------------------------------------------------------
    # Increment the column counter
    #---------------------------------------------------------------------------
    def addColumn(self):
        self.column = self.column + 1

    #---------------------------------------------------------------------------
    # Add a combo box to the panel
    #---------------------------------------------------------------------------
    def addCombo(self, 
                 dictionary, 
                 width, 
                 textvariable, 
                 callback = None,
                 padx = 5,
                 pady = 1):
        #Prepare the options as the keys of the dictionary
        options = list(dictionary.keys())
        options.sort()

        #Create the combobox
        combo = ttk.Combobox(self, width = width, textvariable = textvariable,
                             values = options )
        combo.grid(column = self.column, row = self.row, padx = padx,
                   pady = pady, sticky = (W, E))  
        #If a callback functions was passed, bind it to the combobox  
        if (callback != None):
            combo.bind("<<ComboboxSelected>>", callback)
        #Increment the column counter
        self.addColumn()

        return combo

    #---------------------------------------------------------------------------
    # Add a label to the panel
    #---------------------------------------------------------------------------
    def addLabel(self,
                 text,
                 columnspan = 1,
                 isvariable = False,
                 padx = 10,
                 pady = 1):       
        #Create a label that has its text as text variable
        if (isvariable):    
            label = ttk.Label(self, textvariable = text)
        #Create a static label
        else:
            label = ttk.Label(self, text = text)
        
        label.grid(column = self.column, row = self.row, padx = padx, 
                   pady = pady, columnspan = columnspan, sticky = (W, E))

        #Increment the column counter
        self.addColumn()

        return label
        

    #---------------------------------------------------------------------------
    # Add a button to the panel
    #---------------------------------------------------------------------------
    def addButton(self,
                  text,
                  callback,
                  padx = 10,
                  pady = 1):       
        #Create the button
        button = ttk.Button(self, text = text, command = callback)
        button.grid(column = self.column, row = self.row, padx = padx, 
                    pady = pady, sticky = (W, E)) 
        #Increment the column counter
        self.addColumn()
    
        return button

    #---------------------------------------------------------------------------
    # Add a radio button to the panel
    #---------------------------------------------------------------------------
    def addRadio(self,
                 text,
                 textvariable,
                 value,
                 callback = None,
                 padx = 10,
                 pady = 1):       
        #Create a radio button with callback
        if (callback == None):
            radio = ttk.Radiobutton(self, text = text, value = value, 
                                    variable = textvariable)
        #Create a radio button without callback
        else:
            radio = ttk.Radiobutton(self, text = text, value = value,
                                    variable = textvariable,
                                    command = callback)
        radio.grid(column = self.column, row = self.row, padx = padx, 
                   pady = pady, sticky = (W, E)) 
        #Increment the column counter
        self.addColumn()

        return radio

    #---------------------------------------------------------------------------
    # Add a Horizontal separator to the panel
    #---------------------------------------------------------------------------
    def addHSep(self,
                size = 1,
                padx = 1,
                pady = 2): 
        #Create a Horizontal separator
        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(column = self.column, row = self.row, columnspan = size,
                 padx = padx, pady = pady, sticky = (W, E))
        #Increment the column counter
        self.addColumn()

        return sep

    #---------------------------------------------------------------------------
    # Add a Vertical separator to the panel
    #---------------------------------------------------------------------------
    def addVSep(self,
                size = 1,
                padx = 2,
                pady = 1): 
        #Create a Vertical separator
        sep = ttk.Separator(self, orient = VERTICAL)
        sep.grid(column = self.column, row = self.row, rowspan = size, 
                 padx = padx, pady = pady, sticky = (N, S))
        #Increment the column counter
        self.addColumn()

        return sep

    #---------------------------------------------------------------------------
    # Add a text entry to the panel
    #---------------------------------------------------------------------------
    def addEntry(self, 
                 size, 
                 textvariable, 
                 callback = None, 
                 padx = 1, 
                 pady = 1): 
        #Create a text entry
        entry = ttk.Entry(self, width = size, textvariable = textvariable)
        #If a callback functions was passed, bind it to Key-Return and FocusOut 
        #Events 
        if (callback != None):
            entry.bind('<Key-Return>', callback)
            entry.bind('<FocusOut>', callback)
        entry.grid(column = self.column, row = self.row, sticky = (W, E))
        #Increment the column counter
        self.addColumn()

        return entry

