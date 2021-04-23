# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 22:24:24 2021

@author: sevda
"""

# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
# import wx.lib.sized_controls as sc
import wx.xrc
import wx.html
import wx.html2
import wx.lib.inspection
import cssutils
# import os
# import os.path
# from shutil import copyfile
# import bs4
# from bs4 import BeautifulSoup
# from array import *
import functools
import pickle
# import stanza
# nlp4ll module to deal with json and stanza
from utils import stanza_annotation, generate_d_from_stanza, GetPos, filter_by_pos

FILEFILTER_PKL =    "Json files (*.pkl)|*.pkl|" \
                "All files (*.*)|*.*"
FileFilter3 =    "Json files (*.json)|*.json|" \
                "All files (*.*)|*.*"

FileFilter2 =    "Html files (*.html)|*.html|" \
                "All files (*.*)|*.*"
FileFilter =    "Css files (*.css)|*.css|" \
                "All files (*.*)|*.*"
        
#####################################################################################################################################################
class MainWindow( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, 
                           parent, 
                           id = wx.ID_ANY,
                           # title = wx.EmptyString, 
                           title = "NLP4ALL" ,
                           pos = wx.DefaultPosition, 
                           size = wx.Size( 1000, 700),
                           style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        #menu bar
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.exitMenuItem = self.fileMenu.Append(wx.NewId(), "open")
        self.menuBar.Append(self.fileMenu, "&File")
        #self.Bind(wx.EVT_MENU, self.open_pkl, self.exitMenuItem)
        self.Bind(wx.EVT_MENU, self.open_html, self.exitMenuItem)
        
        self.SetMenuBar(self.menuBar)
        self.Show(True)
      
        # 1st row of widgets
        self.sentence_button = wx.Button( self, wx.ID_ANY, u"Sentence", pos = (10,1), size = wx.DefaultSize )
        self.verb_button = wx.Button( self, wx.ID_ANY, u"Verb", pos = (90,1), size = wx.DefaultSize )
        self.noun_button = wx.Button( self, wx.ID_ANY, u"Noun", pos = (170,1), size = wx.DefaultSize)
        self.adj_button = wx.Button( self, wx.ID_ANY, u"Adjective", pos = (250,1), size = wx.DefaultSize)
        #self.lens_button = wx.Button( self, wx.ID_ANY, u"Lens", pos = (510,1), size = wx.DefaultSize )
        
        #2nd row of widgets
        self.line = wx.StaticLine(self, id=wx.ID_ANY, size=(2000,2), style =wx.LI_VERTICAL)

        #3rd row of widgets
        self.htmlwin2=wx.html2.WebView.New(self, size=(500,1000))
        self.line1 = wx.StaticLine(self, id=wx.ID_ANY, size=(2,600), style =wx.LI_HORIZONTAL)
        self.line2 = wx.StaticLine(self, id=wx.ID_ANY, size=(2,600), style =wx.LI_HORIZONTAL)
        self.line2.Hide()
        
        self.line3 = wx.StaticLine(self, id=wx.ID_ANY, size=(1000,2), style =wx.LI_VERTICAL)
        self.line3.Hide()
        
        #bind buttons
        self.sentence_button.Bind( wx.EVT_BUTTON, self.sentence_button_onClick )
        self.verb_button.Bind( wx.EVT_BUTTON, self.verb_button_onClick )
        self.noun_button.Bind( wx.EVT_BUTTON, self.noun_button_onClick )
        self.adj_button.Bind( wx.EVT_BUTTON, self.adj_button_onClick )
        #self.lens_button.Bind( wx.EVT_BUTTON, self.lens_button_onClick )
        
        # bind filters values toggle buttons
        
        
        # self.noun_button_onClick
        
        # Create the sizers
        self.topSizer = wx.BoxSizer( wx.VERTICAL ) 
        self.bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
        self.lineSizer = wx.BoxSizer( wx.VERTICAL )
        self.bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        self.bSizer2_2 = wx.BoxSizer( wx.VERTICAL)
        self.bagSizer1 = wx.GridBagSizer(hgap=5, vgap=5)
        self.bagSizer2 = wx.GridBagSizer(hgap=5, vgap=5)
        self.bagSizer3 = wx.GridBagSizer(hgap=5, vgap=5)
        
        # Add widgets to sizers
        self.bSizer1.Add( self.sentence_button, 1, wx.ALL, 5 )
        self.bSizer1.Add( self.verb_button, 1, wx.ALL, 5 )
        self.bSizer1.Add( self.noun_button, 1, wx.ALL, 5 )
        self.bSizer1.Add( self.adj_button, 1, wx.ALL, 5 )
        
        self.lineSizer.Add( self.line, 0, wx.EXPAND, 5 )
        
        self.bSizer2.Add( self.htmlwin2, 2, wx.EXPAND, 5 )
        self.bSizer2.Add( self.line1, 0, wx.EXPAND, 5 )
        
        self.bSizer2_2.Add( self.bagSizer2, 0, wx.ALL, 5 )
        self.bSizer2_2.Add( self.line3, 0, wx.ALL, 5 )
        self.bSizer2_2.Add( self.bagSizer3, 0, wx.ALL, 5 )
        
        # Add sub-sizers to topSizer
        self.bSizer2.Add( self.bagSizer1, 1, wx.EXPAND, 5 )
        
        self.bSizer2.Add( self.line2, 0, wx.EXPAND, 5 )
        
        self.bSizer2.Add( self.bSizer2_2, 1, wx.EXPAND, 5 )
        
        self.topSizer.Add( self.bSizer1, 0, wx.ALL, 5 )
        self.topSizer.Add( self.lineSizer, 0, wx.ALL, 5 )
        self.topSizer.Add( self.bSizer2, 0, wx.ALL, 5 )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetSizer( self.topSizer )
        self.Layout()
        self.Centre( wx.BOTH )
        
        #variables
        self.n = -1
        self.row = 0
        self.colum = 0
        self.add_column = 1
        self.button_dict = {}
        self.normal_case = True
        self.docfile = {}   
        
    def OnQuit(self, e):
        self.Close()

    def on_toggle(self, event):
        # GetPos(self.docfile["dfromstanza"])
        print()
        
    def sentence_button_onClick( self, event ): 
        
        self.n += 1
        self.sentence_inst = wx.Button( self, id = self.n, label = "sentence", size = wx.DefaultSize )
        self.button_dict[self.n] = self.sentence_inst
        
        self.n += 1
        self.add = wx.Button( self, id = self.n, label = "+", size = (15,15) )
        self.button_dict[self.n] = self.add
        
        self.bagSizer1.Add(self.sentence_inst, pos=(self.row , 0 ), flag=wx.ALL, border=5)
        self.bagSizer1.Add(self.add, pos=(self.row , 1 ), flag=wx.ALL, border= 5)
        
        func = functools.partial(self.add_onClick, row = self.row)
        self.add.Bind( wx.EVT_BUTTON, func )
        
        self.sentence_inst.Bind( wx.EVT_BUTTON, self.sent_inst_onClick )
        #self.sentence_inst.Bind( wx.EVT_BUTTON, self.creat_sent_css )
        
        func2 = functools.partial(self.sent_inst_rightClick , id = self.n)
        self.sentence_inst.Bind(wx.EVT_RIGHT_DOWN, func2)
        
        self.row +=1
        self.Layout() #to update frame
    
    def add_onClick(self, event, row): 
        
        print('%s clicked' % row)
        self.add_row = row
        self.add_column += 1
        self.normal_case = False
        #self.add.SetLabel("-")
    
    def sent_inst_onClick( self, event):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Show()
        
        # row 1
        self.stextMain = wx.StaticText(self, wx.ID_ANY, "Main type")
        
        self.sbuttonDec = wx.ToggleButton( self, wx.ID_ANY, label = "Declarative")
        self.sbuttonDec.SetValue(True)
        
        self.sbuttonInt = wx.ToggleButton( self, wx.ID_ANY, u"Interrogative")
        self.sbuttonInt.SetValue(True)
        
        self.sbuttonExc = wx.ToggleButton( self, wx.ID_ANY, u"Exclamative" )
        self.sbuttonExc.SetValue(True)
        
        # row 2
        self.stextRelative = wx.StaticText(self, wx.ID_ANY, "Relative sentences")

        self.sbuttonRel = wx.ToggleButton( self, wx.ID_ANY, u"has relative sentences")
        self.sbuttonRel.SetValue(True)
        
        self.sbuttonConn = wx.ToggleButton( self, wx.ID_ANY, u"has conncetors" )
        self.sbuttonConn.SetValue(True)
        
        # row 3
        self.stextWords = wx.StaticText(self, wx.ID_ANY, "Number of words")
        self.sTextCtrlwords= wx.TextCtrl(self, size=(60, -1))
        
        # row 4
        self.stextcontent = wx.StaticText(self, wx.ID_ANY, "Number of content words")
        self.sTextCtrlcontent = wx.TextCtrl(self, size=(60, -1))
        
        #ADD TO BAG SIZER
        self.bagSizer2.Add(self.stextMain, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.sbuttonDec, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.sbuttonInt, pos=(0 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.sbuttonExc, pos=(0 , 3 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.stextRelative, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.sbuttonRel, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.sbuttonConn, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.stextWords, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.sTextCtrlwords, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.stextcontent, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.sTextCtrlcontent, pos=(3 , 1 ), flag=wx.ALL, border= 5)
        
        #line
        self.line3.Show()
        
        #lens
        self.lenslabel = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        self.FontBtn.SetValue("Arial")
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))
        self.SizeBtn.SetValue("11")

        fonts_color = ['black', 'blue', 'red', 'green', 'yellow']
        self.colorBtn = wx.ComboBox(self, choices = fonts_color, size = (120,25))
        self.colorBtn.SetValue("black")
        #self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.lenslabel, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.FontBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.bgcolorBtn, pos=(3 , 1 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg1)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        
        self.BoldBtn.Bind( wx.EVT_TOGGLEBUTTON, self.creat_sent_css )
        #self.SizeBtn.Bind(wx.EVT_COMBOBOX, self.on_fntsize)
        self.colorBtn.Bind(wx.EVT_COMBOBOX, self.on_fntColor)
        self.Layout()
        event.Skip()
    
    def on_fntColor(self, event):
        self.colorBtn_value = self.colorBtn.GetValue()
        if self.colorBtn_value != 'black':
             parser = cssutils.parseFile('sentCsStyle.css')
             for rule in parser.cssRules:
                        try:
                            if rule.selectorText == '.sentence':
                                rule.style.backgroundColor = self.colorBtn_value
                        except AttributeError as e:
                            pass
                 # Write to a new file
             with open('sent-bold.css', 'wb') as f:
                f.write(parser.cssText)
             self.htmlwin2.Reload()
    
    def creat_sent_css(self, event):
        state = event.GetEventObject().GetValue()
        if state == True:
            parser = cssutils.parseFile('sentCsStyle.css')
            for rule in parser.cssRules:
                        try:
                            if rule.selectorText == '.sentence':
                                rule.fontweight = 'bold'
                        except AttributeError as e:
                            pass
                 # Write to a new file
            with open('sent-bold.css', 'wb') as f:
                f.write(parser.cssText)
                
    def onColorDlg1(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)

        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            print ('You selected: %s\n' % str(data.GetColour().Get()))
            
        dlg.Destroy()
        parser = cssutils.parseFile('sentCsStyle.css')
        for rule in parser.cssRules:
                        try:
                            if rule.selectorText == '.sentence':
                                rule.style.color = data
                        except AttributeError as e:
                            pass
                 # Write to a new file
        with open('sentCsStyle.css', 'wb') as f:
                f.write(parser.cssText)
    
    def sent_inst_rightClick( self, event, id ):
        
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Hide()
        self.line3.Hide()

        #print("id is "+str(id))
        add_id = id - 1
        j= -1
        for x in self.button_dict.keys():
            j+=1
            if id == x:
                break
        #print("j  "+ str(j))
        #print("BABIES "+str(len(self.bagSizer1.GetChildren())))

        if self.bagSizer1.GetChildren():
            
            position1 = self.bagSizer1.GetItemPosition(self.button_dict[id])
            print("position is" + str(position1))
            
            sizer_item = self.bagSizer1.GetItem(j)
            widget = sizer_item.GetWindow()
            self.bagSizer1.Hide(widget)
            widget.Destroy()
            
            sizer_item2 = self.bagSizer1.GetItem(j-1)
            widget2 = sizer_item2.GetWindow()
            self.bagSizer1.Hide(widget2)
            widget2.Destroy()
            
           
            """row1 = position1.GetRow()
            col1 = 2
            sizer_item3 = self.bagSizer1.FindItemAtPosition((row1,col1))
            widget3 = sizer_item3.GetWindow()"""

            #self.bagSizer1.Hide(widget3)
            #widget3.Destroy()
            #print(button)
            self.button_dict.pop(id)
            self.button_dict.pop(add_id)
           
            self.Layout()
          #self.button_dict[add_id].Destroy()
          #self.Layout()
            for i in self.button_dict.keys():
              print(i)
              if int(i) < int(id)+1:
                  continue
              
              button=self.button_dict[i]
              self.position = self.bagSizer1.GetItemPosition(button)
              print(self.position)
              self.rows = self.position.GetRow()
              self.cols = self.position.GetCol()
              self.bagSizer1.SetItemPosition(button,pos=(self.rows - 1,self.cols))
              print(self.position)

              self.Layout()
            self.row -=1
            self.normal_case = True
          

    def verb_button_onClick( self, event ):
        self.n += 1
        self.verb_inst = wx.Button( self, id = self.n, label = "verb", size = wx.DefaultSize )
        if self.normal_case:
            self.bagSizer1.Add(self.verb_inst, pos=(self.row , 0 ), flag=wx.ALL, border=5)
            self.row +=1
            
        else:
            self.bagSizer1.Add(self.verb_inst, pos=(self.add_row , 2), flag=wx.ALL, border=5)

        self.button_dict[self.n] = self.verb_inst
        self.verb_inst.Bind( wx.EVT_BUTTON, self.verb_inst_onClick )
        func = functools.partial(self.verb_inst_rightClick , id = self.n)
        self.verb_inst.Bind(wx.EVT_RIGHT_DOWN, func)
        self.verb_inst.Bind(wx.EVT_RIGHT_DOWN, self.verb_inst_onClick2)
        
        self.normal_case = True
        self.Layout() #to update frame
        
    def verb_inst_onClick2(self, event):
        print("gino")
        event.Skip()

    def verb_inst_onClick( self, event ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Show()
        
        # row 1
        self.vtextlemma = wx.StaticText(self, -1, "Lemma")
        self.vtextCtrllemma = wx.TextCtrl(self)
        
        #row2
        self.vtextnum = wx.StaticText(self, -1, "Number")
        
        self.vbuttonsing = wx.ToggleButton( self, wx.ID_ANY, u"Singular")
        self.vbuttonsing.SetValue(True)
        
        self.vbuttonpl = wx.ToggleButton( self, wx.ID_ANY, u"Plural")
        self.vbuttonpl.SetValue(True)
       
        #textCtrl.SetSizerProps(expand=True)
        
        # row 3
        self.vtextpers= wx.StaticText(self, -1, "Person")
        
        self.vbutton1st = wx.ToggleButton( self, wx.ID_ANY, u"First" )
        self.vbutton1st.SetValue(True)
        
        self.vbutton2nd = wx.ToggleButton( self, wx.ID_ANY, u"Second" )
        self.vbutton2nd.SetValue(True)
        
        self.vbutton3rd = wx.ToggleButton( self, wx.ID_ANY, u"Third" )
        self.vbutton3rd.SetValue(True)
        
        # row 4
        self.vtextTense = wx.StaticText(self, -1, "Tense")
        
        self.vbuttonPast = wx.ToggleButton( self, wx.ID_ANY, u"Past" )
        self.vbuttonPast.SetValue(True)
        
        self.vbuttonPres = wx.ToggleButton( self, wx.ID_ANY, u"Present" )
        self.vbuttonPres.SetValue(True)
        
        self.vbuttonFut = wx.ToggleButton( self, wx.ID_ANY, u"Future" )
        self.vbuttonFut.SetValue(True)
        
        # row 5
        self.vtextForm = wx.StaticText(self, -1, "Form")
        
        self.vbuttonFin = wx.ToggleButton( self, wx.ID_ANY, u"Fin" )
        self.vbuttonFin.SetValue(True)
        
        self.vbuttonPart = wx.ToggleButton( self, wx.ID_ANY, u"Part")
        self.vbuttonPart.SetValue(True)
        
        self.vbuttonInf = wx.ToggleButton( self, wx.ID_ANY, u"Inf")
        self.vbuttonInf.SetValue(True)
        
        self.vbuttonGer = wx.ToggleButton( self, wx.ID_ANY, u"Ger")
        self.vbuttonGer.SetValue(True)
        
        #row 6
        self.vtextMood = wx.StaticText(self, -1, "Mood")
        
        self.vbuttonInd = wx.ToggleButton( self, wx.ID_ANY, u"Ind")
        self.vbuttonInd.SetValue(True)
        
        self.vbuttonCnd = wx.ToggleButton( self, wx.ID_ANY, u"Cnd")
        self.vbuttonCnd.SetValue(True)
        
        self.vbuttonSub = wx.ToggleButton( self, wx.ID_ANY, u"Sub")
        self.vbuttonSub.SetValue(True)
        
        self.vbuttonImp = wx.ToggleButton( self, wx.ID_ANY, u"Imp")
        self.vbuttonImp.SetValue(True)
        
        #row 7
        self.vtextGender = wx.StaticText(self, -1, "Gender")
        
        self.vbuttonF = wx.ToggleButton( self, wx.ID_ANY, u"Feminin")
        self.vbuttonF.SetValue(True)
        
        self.vbuttonM = wx.ToggleButton( self, wx.ID_ANY, u"Masculin")
        self.vbuttonM.SetValue(True)
        
        
        self.bagSizer2.Add(self.vtextlemma, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vtextCtrllemma , pos=(0 , 1 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.vtextnum, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonsing, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonpl, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.vtextpers, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbutton1st, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbutton2nd, pos=(2 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbutton3rd, pos=(2 , 3 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.vtextTense, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonPast, pos=(3 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonPres, pos=(3 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonFut, pos=(3 , 3 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.vtextForm, pos=(4 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonFin, pos=(4 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonPart, pos=(4 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonInf, pos=(4 , 3 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonGer, pos=(4 , 4 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.vtextMood, pos=(5 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonInd, pos=(5 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonCnd, pos=(5 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonSub, pos=(5 , 3 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonImp, pos=(5 , 4 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.vtextGender, pos=(6 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonF, pos=(6 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.vbuttonM, pos=(6 , 2 ), flag=wx.ALL, border= 5)
        
         #line
        self.line3.Show()
        
         #lens
        self.lenslabel = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        self.FontBtn.SetValue("Arial")
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))
        self.SizeBtn.SetValue("11")

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.lenslabel, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.FontBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.bgcolorBtn, pos=(3 , 1 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)

        self.Layout()
        event.Skip()    
    
    def verb_inst_rightClick( self, event, id ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Hide()
        self.line3.Hide()
        
        """if id in self.button_dict:
          self.button_dict[id].Destroy()"""
        j= -1
        for x in self.button_dict.keys():
            j+=1
            if id == x:
                break
        
        position1 = self.bagSizer1.GetItemPosition(self.button_dict[id])
        col1 = position1.GetCol()
        if self.bagSizer1.GetChildren():
            sizer_item = self.bagSizer1.GetItem(j)
            widget = sizer_item.GetWindow()
            self.bagSizer1.Hide(widget)
            widget.Destroy()
            
            
            self.button_dict.pop(id)
           
            self.Layout()

            for i in self.button_dict.keys():
              print(i)
              if int(i) < int(id)+1:
                  continue
              
              button=self.button_dict[i]
              self.position = self.bagSizer1.GetItemPosition(button)
              print(self.position)
              self.rows = self.position.GetRow()
              self.cols = self.position.GetCol()
              self.bagSizer1.SetItemPosition(button,pos=(self.rows - 1,self.cols))
              print(self.position)

              self.Layout()
            
            if col1 == 0:
                self.row -=1
            self.normal_case = True

    def noun_button_onClick( self, event ):
        
        self.n += 1
        key = "NOUN"+ str(self.n)
        self.noun_inst = wx.Button( self, id = self.n, label = "noun", size = wx.DefaultSize )
        if self.normal_case:
            self.bagSizer1.Add(self.noun_inst, pos=(self.row , 0 ), flag=wx.ALL, border=5)
            self.row +=1
            
        else:
            self.bagSizer1.Add(self.noun_inst, pos=(self.add_row , 2), flag=wx.ALL, border=5)

        #self.button_dict[key] = self.noun_inst
        self.button_dict[self.n] = self.noun_inst
        self.noun_inst.Bind( wx.EVT_BUTTON, self.noun_inst_onClick )
        func = functools.partial(self.noun_inst_rightClick , id = self.n)
        self.noun_inst.Bind(wx.EVT_RIGHT_DOWN, func)
        func_id = functools.partial(self.noun_handling , id = self.n)
        self.noun_inst.Bind(wx.EVT_BUTTON, func_id)
        self.normal_case = True
        self.Layout() #to update frame
        event.Skip()
    
    def noun_inst_onClick( self, event ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Show()
        
        # row 1
        self.ntextGender = wx.StaticText(self, -1, "Gender")
        
        self.n += 1
        self.nbuttonF = wx.ToggleButton( self, id=self.n, label="Feminine")
        nfid = self.nbuttonF.GetId()
        self.button_dict["feminine" + str(nfid)]  = self.nbuttonF.GetValue()      
        # self.nbuttonF.Bind(wx.EVT_TOGGLEBUTTON, self.noun_handling)
       
        self.nbuttonF.SetValue(True)
        
        self.nbuttonM = wx.ToggleButton( self, wx.ID_ANY, u"Masculine")
        self.nbuttonM.SetValue(True)
        
        
        # row 2
        self.ntextNum = wx.StaticText(self, -1, "Number")
        
        self.nbuttonSin = wx.ToggleButton( self, wx.ID_ANY, u"Singular")
        self.nbuttonSin.SetValue(True)
        
        self.nbuttonPl = wx.ToggleButton( self, wx.ID_ANY, u"Plural")
        self.nbuttonPl.SetValue(True)
        
        # row 3
        self.ntextForeign = wx.StaticText(self, -1, "Foreign")
        self.nbuttonForeign = wx.ToggleButton( self, wx.ID_ANY, u"yes")
        self.nbuttonForeign.SetValue(True)
        
        self.bagSizer2.Add(self.ntextGender, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.nbuttonF, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.nbuttonM, pos=(0 , 2 ), flag=wx.ALL, border= 5)
      
        self.bagSizer2.Add(self.ntextNum, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.nbuttonSin, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.nbuttonPl, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.ntextForeign, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.nbuttonForeign, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        
         #line
        self.line3.Show()
        
         #lens
        self.lenslabel = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        self.FontBtn.SetValue("Arial")
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))
        self.SizeBtn.SetValue("11")

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.lenslabel, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.FontBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.bgcolorBtn, pos=(3 , 1 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        
        self.Layout()
        event.Skip()
        
    def noun_inst_rightClick( self, event, id ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Hide()
        self.line3.Hide()
        
        j= -1
        for x in self.button_dict.keys():
            j+=1
            if id == x:
                break

        position1 = self.bagSizer1.GetItemPosition(self.button_dict[id])
        col1 = position1.GetCol()
        if self.bagSizer1.GetChildren():
            sizer_item = self.bagSizer1.GetItem(j)
            widget = sizer_item.GetWindow()
            self.bagSizer1.Hide(widget)
            widget.Destroy()
            
            
            self.button_dict.pop(id)
           
            self.Layout()

            for i in self.button_dict.keys():
              print(i)
              if int(i) < int(id)+1:
                  continue
              
              button=self.button_dict[i]
              self.position = self.bagSizer1.GetItemPosition(button)
              print(self.position)
              self.rows = self.position.GetRow()
              self.cols = self.position.GetCol()
              self.bagSizer1.SetItemPosition(button,pos=(self.rows - 1,self.cols))
              print(self.position)

              self.Layout()
            if col1 == 0:
                self.row -=1
            self.normal_case = True
        """if id in self.button_dict:
          self.button_dict[id].Destroy()"""

    def adj_button_onClick( self, event ):
        self.n += 1
        self.adj_inst = wx.Button( self, id = self.n, label = "adjective", size = wx.DefaultSize )
        if self.normal_case:
            self.bagSizer1.Add(self.adj_inst, pos=(self.row , 0 ), flag=wx.ALL, border=5)
            self.row +=1
        else:
            self.bagSizer1.Add(self.adj_inst, pos=(self.add_row , 2), flag=wx.ALL, border=5)

        self.button_dict[self.n] = self.adj_inst
        self.adj_inst.Bind( wx.EVT_BUTTON, self.adj_inst_onClick )
        func = functools.partial(self.adj_inst_rightClick , id = self.n)
        self.adj_inst.Bind(wx.EVT_RIGHT_DOWN, func)
        
        self.normal_case = True
        self.Layout() #to update frame
    
    def adj_inst_onClick( self, event ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Show()
        
        # row 1
        self.adjtextGender = wx.StaticText(self, -1, "Gender")
        
        self.adjbuttonF = wx.ToggleButton( self, wx.ID_ANY, u"Feminine")
        self.adjbuttonF.SetValue(True)
        
        self.adjbuttonM = wx.ToggleButton( self, wx.ID_ANY, u"Mascular")
        self.adjbuttonM.SetValue(True)

        # row 2
        self.adjtextNum= wx.StaticText(self, -1, "Number")
        
        self.adjbuttonSin = wx.ToggleButton( self, wx.ID_ANY, u"Singular")
        self.adjbuttonSin.SetValue(True)
        
        self.adjbuttonPl = wx.ToggleButton( self, wx.ID_ANY, u"Plural")
        self.adjbuttonPl.SetValue(True)
        
        # row 3
        self.adjtextDegree= wx.StaticText(self, -1, "Degree")
        
        self.adjbuttonCmp = wx.ToggleButton( self, wx.ID_ANY, u"Cmp")
        self.adjbuttonCmp.SetValue(True)
        
        self.adjbuttonAbs = wx.ToggleButton( self, wx.ID_ANY, u"Abs")
        self.adjbuttonAbs.SetValue(True)    
        
        # row 4
        self.adjtextForeign = wx.StaticText(self, -1, "Foreign")
        self.adjbuttonForeign = wx.ToggleButton( self, wx.ID_ANY, u"yes" )
        self.adjbuttonForeign.SetValue(True)
        
        self.bagSizer2.Add(self.adjtextGender, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.adjbuttonF, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.adjbuttonM, pos=(0 , 2 ), flag=wx.ALL, border= 5)
      
        self.bagSizer2.Add(self.adjtextNum, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.adjbuttonSin, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.adjbuttonPl, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.adjtextDegree, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.adjbuttonCmp, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.adjbuttonAbs, pos=(2 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.adjtextForeign, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.adjbuttonForeign, pos=(3 , 1 ), flag=wx.ALL, border= 5)
        
         #line
        self.line3.Show()
        
        #lens
        self.lenslabel = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        self.FontBtn.SetValue("Arial")
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))
        self.SizeBtn.SetValue("11")

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.lenslabel, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.FontBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.bgcolorBtn, pos=(3 , 1 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        
        self.Layout()

    def adj_inst_rightClick( self, event, id ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Hide()
        self.line3.Hide()
        
        j= -1
        for x in self.button_dict.keys():
            j+=1
            if id == x:
                break

        position1 = self.bagSizer1.GetItemPosition(self.button_dict[id])
        col1 = position1.GetCol()
        if self.bagSizer1.GetChildren():
            sizer_item = self.bagSizer1.GetItem(j)
            widget = sizer_item.GetWindow()
            self.bagSizer1.Hide(widget)
            widget.Destroy()
            
            
            self.button_dict.pop(id)
           
            self.Layout()

            for i in self.button_dict.keys():
              print(i)
              if int(i) < int(id)+1:
                  continue
              
              button=self.button_dict[i]
              self.position = self.bagSizer1.GetItemPosition(button)
              print(self.position)
              self.rows = self.position.GetRow()
              self.cols = self.position.GetCol()
              self.bagSizer1.SetItemPosition(button,pos=(self.rows - 1,self.cols))
              print(self.position)

              self.Layout()
            if col1 == 0:
                self.row -=1
            self.normal_case = True
        """if id in self.button_dict:
          self.button_dict[id].Destroy()"""

    def lens_button_onClick( self, event ):
        if (self.lens_row == 0):
            self.lens_row = self.lens_row + 50
        else:
            self.lens_row = self.lens_row + 30
            
        self.lens_inst_1 = wx.Button( self, wx.ID_ANY, u"lens", pos = (610 ,self.lens_row), size = wx.DefaultSize )
        self.lens_inst_1.Bind( wx.EVT_BUTTON, self.lens_inst_1_onClick )
        
    def lens_inst_onClick( self, event ):
 
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        self.bagSizer3.Add(self.FontBtn, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(1 , 2 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)

    def onColorDlg(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)

        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            print ('You selected: %s\n' % str(data.GetColour().Get()))
            
        dlg.Destroy()

    
    def open_pkl( self, event ):
        dlg3 = wx.FileDialog(
            self, 
            message = "Choose a file",
            #defaultDir = self.currentDirectory, 
            defaultFile = "",
            #wildcard = FILEFILTER_PKL,
            wildcard = FileFilter2,
            style = wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        if dlg3.ShowModal() == wx.ID_OK:
            # GetPath() returns just the path of the file
            filepath = dlg3.GetPath()
            stanzadoc = pickle.load(open(filepath, "rb"))
            self.docfile["pkl"] = stanzadoc
            self.docfile["html"] = stanza_annotation(stanzadoc)
            self.docfile["dfromstanza"] = generate_d_from_stanza(stanzadoc)
            self.htmlwin2.SetPage(self.docfile["html"],"")
            
            
        dlg3.Destroy()
    
    def open_html( self, event ):
        dlg3 = wx.FileDialog(
            self, 
            message = "Choose a file",
            #defaultDir = self.currentDirectory, 
            defaultFile = "",
            wildcard = FileFilter2,
            style = wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        if dlg3.ShowModal() == wx.ID_OK:
            self.htmlFilePath2 = dlg3.GetPath()
            self.htmlwin2.LoadURL(self.htmlFilePath2)
        dlg3.Destroy()
    
    
    def noun_handling(self, event, id):
        event.Skip()
        # nouns = [(key,val) for key,val in self.docfile["dfromstanza"].items()]
        # self.button_dict[id] 
        # d = self.docfile["dfromstanza"]
        # pos = GetPos("NOUN", d)
        # print(pos.words)
        
        # print( self.button_dict.items())
        # print(self.htmlwin2.RunScript("document.write('Hello from wx.Widgets!')"))
        #ids_of_nouns = filter_by_pos(self.docfile["dfromstanza"], "NOUN")
        
        # Todo : take the ids and send them to the javascript function that alters the page look (the lens)
        # print(self.htmlwin2.RunScript("document.write('Hello from wx.Widgets!')"))

        #print(ids_of_nouns)
       # event.Skip()
        # nd = {"fem": [1,2,3,],
        #      "masc": [6,5,8]
        #      "sing" : [78,5,6]}
    
    # def noun_filter(self, event):
    #     if self.nbuttonM.SetValue(True)
    
    def creat_sent_css1(self, event):
        f = open('sentCsStyle.css','w')
        message = """.sentence {
              background-color:white;  /* or rgb(189, 17, 152) */
              color: black;
              font-size: 11px;
              font-style: normal; /* or  italic  */
              font-family: Arial, Helvetica, sans-serif;
              font-weight: normal; /* or bold */
            }"""
        f.write(message)
        f.close()
        event.Skip()
    
    
        

class nlp_app(wx.App):
    def OnInit(self):
        self.frame = MainWindow(parent=None)
        self.frame.Show()
        
        wx.lib.inspection.InspectionTool().Show()
        return True

#--------------------------------------------------------------------------------------------------------------------------
# # Run the program !
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MainWindow(None)
#     frame.Show()
#     app.MainLoop()

app = nlp_app()
app.MainLoop()
