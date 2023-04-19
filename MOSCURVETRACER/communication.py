## @module communication
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
#  Comunication frame
#
################################################################################

#-------------------------------------------------------------------------------
# Import
#-------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
import basicFrame
from tkinter.messagebox import showerror
from pysmu import *
import time 
import matplotlib.pyplot as plt


#-------------------------------------------------------------------------------
# communication panel class
#-------------------------------------------------------------------------------
class communicationPanel(ttk.Panedwindow):


    #---------------------------------------------------------------------------
    # Receive button event
    #---------------------------------------------------------------------------
    def trace_start(self):
        vgs_step  = float(self.vgs_step_text.get())
        vgs_start = float(self.vgs_start_text.get())
        vgs_stop  = float(self.vgs_stop_text.get())
        vds_step  = float(self.vds_step_text.get())
        vds_start = float(self.vds_start_text.get())
        vds_stop  = float(self.vds_stop_text.get())
        csv_file  = self.csf_file.get()
        
        
        vgs = vgs_start           
        vgs_list = []
        vds_list = []
        first = True
        ans = []
        #Clean-up
        self.devx.channels['A'].constant(0)
        self.devx.channels['B'].constant(0)
        if not self.session.continuous:
            self.session.flush()
            self.session.start(0)
        time.sleep(0.2)
        #Loop start
        ADsignal1 = self.devx.read(4000, -1, True)
        while vgs <= vgs_stop:
            vgs_list.append(vgs)
            self.devx.channels['A'].constant(vgs)
            idlist = []
            vds = vds_start
            while vds <= vds_stop:
                if first:
                    vds_list.append(vds)
                print('Working on vgs = ' + str(vgs) + ' and vds = ' + str(vds))
                self.devx.channels['B'].constant(vds)
                time.sleep(0.1)
                #get_samples returns a list of [sample][channel][v/i] for voltage [0] and current [1]
                ADsignal1 = self.devx.read(4000, -1, True) # get 400 readings [sample][cha/chb][v/i]
                idlist.append(sum([(sample[1][1] + vds/20e3 + 2.5e-6) for sample in ADsignal1[3000:4000]])/1000)
                vds = vds + vds_step
            ans.append(idlist)
            vgs = vgs + vgs_step
            first = False

        labels = []
        f = open(csv_file, "w")
        f.write("Vgs↓ Vds→," + ",".join([str(vds) for vds in vds_list]))
        for i in range(0, len(vgs_list)):
            plt.plot(vds_list, ans[i])
            labels.append("Vgs = " + str(vgs_list[i]))
            f.write('\n' + str(vgs_list[i]) + "," + ",".join([str(ids) for ids in ans[i]]))
        f.close()
        plt.title("Mos curve")
        plt.legend(labels)
        plt.xlabel('Vds (V)')
        plt.ylabel('Id (A)')
        plt.show() 

    #---------------------------------------------------------------------------
    # Constructor
    #---------------------------------------------------------------------------
    def __init__(self, parent, session):
        #Call ttk.Panedwindow constructor
        ttk.Panedwindow.__init__(self, parent, orient=VERTICAL)
        self.grid(column = 0, row = 0, sticky = (N, W))   
        
        self.session = session
        self.devx = session.devices[0]
        #self.devx = None
        self.devx.channels['A'].mode = Mode.SVMI
        self.devx.channels['B'].mode = Mode.SVMI
        
        #Frame
        frame1 = ttk.Frame(self, padding = "12 12 12 12")   

        #Frame labeled 
        bframe1 = basicFrame.basicFrame(frame1, "Vds (CHB)", 0, 0)
        
        self.vds_step_text  = StringVar()
        self.vds_step_text.set('0.1')
        self.vds_start_text = StringVar()
        self.vds_start_text.set('0.0')
        self.vds_stop_text  = StringVar()
        self.vds_stop_text.set('5.0')

        #Adress label, entry, and combobox
        bframe1.addLabel("Step")
        bframe1.addEntry(7, self.vds_step_text)
        bframe1.addRow()
        
        bframe1.addLabel("Start")
        bframe1.addEntry(7, self.vds_start_text)
        bframe1.addRow()
        
        bframe1.addLabel("Stop")
        bframe1.addEntry(7, self.vds_stop_text)
       

        #Frame labeled 
        bframe2 = basicFrame.basicFrame(frame1, "Vgs (CHA)", 0, 1)
        
        self.vgs_step_text  = StringVar()
        self.vgs_step_text.set('1.0')
        self.vgs_start_text = StringVar()
        self.vgs_start_text.set('1.0')
        self.vgs_stop_text  = StringVar()
        self.vgs_stop_text.set('3.0')

        #Adress label, entry, and combobox
        bframe2.addLabel("Step")
        bframe2.addEntry(7, self.vgs_step_text)
        bframe2.addRow()
        
        bframe2.addLabel("Start")
        bframe2.addEntry(7, self.vgs_start_text)
        bframe2.addRow()
        
        bframe2.addLabel("Stop")
        bframe2.addEntry(7, self.vgs_stop_text)

        #Frame labeled 
        bframe3 = basicFrame.basicFrame(frame1, "Output CSV file and trace", 0, 2)
        
        self.csf_file = StringVar()
        self.csf_file.set('output.csv')
             
        #bframe3.addLabel("CSV file name")
        bframe3.addEntry(20, self.csf_file)
        bframe3.addRow()
        bframe3.addButton("Start Tracing", self.trace_start)

        #Add frame to panel
        self.add(frame1)

