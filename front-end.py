# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.lib.sized_controls as sc
import wx.xrc
import wx.html
import wx.html2
import os
import os.path
from shutil import copyfile
import bs4
from bs4 import BeautifulSoup
from array import *
import functools

FileFilter3 =    "Json files (*.json)|*.json|" \
                "All files (*.*)|*.*"

FileFilter2 =    "Html files (*.html)|*.html|" \
                "All files (*.*)|*.*"
FileFilter =    "Css files (*.css)|*.css|" \
                "All files (*.*)|*.*"
        
#####################################################################################################################################################
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000, 700), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        #menu bar
        self.menuBar = wx.MenuBar()
        self.fileMenu = wx.Menu()
        self.exitMenuItem = self.fileMenu.Append(wx.NewId(), "open",
                                       "choose JSON file")
        self.menuBar.Append(self.fileMenu, "&File")
        self.Bind(wx.EVT_MENU, self.open_json, self.exitMenuItem)
        self.SetMenuBar(self.menuBar)
      
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
        
    def OnQuit(self, e):
        self.Close()

    def sentence_button_onClick( self, event ): 
        self.n += 1
        self.add = wx.Button( self, id = self.n, label = "+", size = (15,15) )
        self.button_dict[self.n] = self.add
        
        self.n += 1
        self.sentence_inst = wx.Button( self, id = self.n, label = "sentence", size = wx.DefaultSize )
        self.button_dict[self.n] = self.sentence_inst
        
        self.bagSizer1.Add(self.add, pos=(self.row , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer1.Add(self.sentence_inst, pos=(self.row , 1 ), flag=wx.ALL, border=5)
        
        func = functools.partial(self.add_onClick, row = self.row)
        self.add.Bind( wx.EVT_BUTTON, func )
        
        self.sentence_inst.Bind( wx.EVT_BUTTON, self.sent_inst_onClick )
        
        func2 = functools.partial(self.sent_inst_rightClick , id = self.n)
        self.sentence_inst.Bind(wx.EVT_RIGHT_DOWN, func2)
        
        self.row +=1
        self.Layout() #to update frame
    
    def add_onClick(self, event, row): 
        
        print('%s clicked' % row)
        self.add_row = row
        self.add_column += 1
        self.normal_case = False
    
    def sent_inst_onClick( self, event):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Show()
        
        # row 1
        self.text1 = wx.StaticText(self, wx.ID_ANY, "Main type")
        
        self.m_button1 = wx.ToggleButton( self, wx.ID_ANY, label = "Declarative")
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( self, wx.ID_ANY, u"Interrogative")
        self.m_button2.SetValue(True)
        
        self.m_button3 = wx.ToggleButton( self, wx.ID_ANY, u"Exclamative" )
        self.m_button3.SetValue(True)
        
        # row 2
        self.text2 = wx.StaticText(self, wx.ID_ANY, "Relative sentences")

        self.m_button4 = wx.ToggleButton( self, wx.ID_ANY, u"has relative sentences")
        self.m_button4.SetValue(True)
        
        self.m_button5 = wx.ToggleButton( self, wx.ID_ANY, u"has conncetors" )
        self.m_button5.SetValue(True)
        
        # row 3
        self.text3 = wx.StaticText(self, wx.ID_ANY, "Number of words")
        self.box1= wx.TextCtrl(self, size=(60, -1))
        
        # row 4
        self.text4 = wx.StaticText(self, wx.ID_ANY, "Number of content words")
        self.box2 = wx.TextCtrl(self, size=(60, -1))
        
        #ADD TO BAG SIZER
        self.bagSizer2.Add(self.text1, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button1, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button2, pos=(0 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button3, pos=(0 , 3 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.text2, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button4, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button5, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.text3, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.box1, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.text4, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.box2, pos=(3 , 1 ), flag=wx.ALL, border= 5)
        
        #line
        self.line3.Show()
        
        #lens
        self.text = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.text, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.FontBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.bgcolorBtn, pos=(3 , 1 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        
        self.Layout()
    
    
    def sent_inst_rightClick( self, event, id ):

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
            self.bagSizer1.Add(self.verb_inst, pos=(self.row , 1 ), flag=wx.ALL, border=5)
            self.row +=1
            
        else:
            self.bagSizer1.Add(self.verb_inst, pos=(self.add_row , 2), flag=wx.ALL, border=5)

        self.button_dict[self.n] = self.verb_inst
        self.verb_inst.Bind( wx.EVT_BUTTON, self.verb_inst_onClick )
        func = functools.partial(self.verb_inst_rightClick , id = self.n)
        self.verb_inst.Bind(wx.EVT_RIGHT_DOWN, func)
        
        self.normal_case = True
        self.Layout() #to update frame

    def verb_inst_onClick( self, event ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Show()
        
        # row 1
        self.text1 = wx.StaticText(self, -1, "Lemma")
        self.textCtrl = wx.TextCtrl(self)
        
        #row2
        self.text2 = wx.StaticText(self, -1, "Number")
        
        self.m_button1 = wx.ToggleButton( self, wx.ID_ANY, u"Singular")
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( self, wx.ID_ANY, u"Plural")
        self.m_button2.SetValue(True)
       
        #textCtrl.SetSizerProps(expand=True)
        
        # row 3
        self.text3= wx.StaticText(self, -1, "Person")
        
        self.m_button3 = wx.ToggleButton( self, wx.ID_ANY, u"First" )
        self.m_button3.SetValue(True)
        
        self.m_button4 = wx.ToggleButton( self, wx.ID_ANY, u"Second" )
        self.m_button4.SetValue(True)
        
        self.m_button5 = wx.ToggleButton( self, wx.ID_ANY, u"Third" )
        self.m_button5.SetValue(True)
        
        # row 4
        self.text4 = wx.StaticText(self, -1, "Tense")
        
        self.m_button6 = wx.ToggleButton( self, wx.ID_ANY, u"Past" )
        self.m_button6.SetValue(True)
        
        self.m_button7 = wx.ToggleButton( self, wx.ID_ANY, u"Present" )
        self.m_button7.SetValue(True)
        
        self.m_button8 = wx.ToggleButton( self, wx.ID_ANY, u"Future" )
        self.m_button8.SetValue(True)
        
        # row 5
        self.text5 = wx.StaticText(self, -1, "Form")
        
        self.m_button9 = wx.ToggleButton( self, wx.ID_ANY, u"Fin" )
        self.m_button9.SetValue(True)
        
        self.m_button10 = wx.ToggleButton( self, wx.ID_ANY, u"Part")
        self.m_button10.SetValue(True)
        
        self.m_button11 = wx.ToggleButton( self, wx.ID_ANY, u"Inf")
        self.m_button11.SetValue(True)
        
        self.m_button12 = wx.ToggleButton( self, wx.ID_ANY, u"Ger")
        self.m_button12.SetValue(True)
        
        #row 6
        self.text6 = wx.StaticText(self, -1, "Mood")
        
        self.m_button13 = wx.ToggleButton( self, wx.ID_ANY, u"Ind")
        self.m_button13.SetValue(True)
        
        self.m_button14 = wx.ToggleButton( self, wx.ID_ANY, u"Cnd")
        self.m_button14.SetValue(True)
        
        self.m_button15 = wx.ToggleButton( self, wx.ID_ANY, u"Sub")
        self.m_button15.SetValue(True)
        
        self.m_button16 = wx.ToggleButton( self, wx.ID_ANY, u"Imp")
        self.m_button16.SetValue(True)
        
        #row 7
        self.text7 = wx.StaticText(self, -1, "Gender")
        
        self.m_button17 = wx.ToggleButton( self, wx.ID_ANY, u"Feminin")
        self.m_button17.SetValue(True)
        
        self.m_button18 = wx.ToggleButton( self, wx.ID_ANY, u"Mascular")
        self.m_button18.SetValue(True)
        
        
        self.bagSizer2.Add(self.text1, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.textCtrl, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text2, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button1, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button2, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text3, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button3, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button4, pos=(2 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button5, pos=(2 , 3 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text4, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button6, pos=(3 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button7, pos=(3 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button8, pos=(3 , 3 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text5, pos=(4 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button9, pos=(4 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button10, pos=(4 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button11, pos=(4 , 3 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button12, pos=(4 , 4 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text6, pos=(5 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button13, pos=(5 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button14, pos=(5 , 2 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button15, pos=(5 , 3 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button16, pos=(5 , 4 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text7, pos=(6 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button17, pos=(6 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button18, pos=(6 , 2 ), flag=wx.ALL, border= 5)
        
         #line
        self.line3.Show()
        
        #lens
        self.text = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.text, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.FontBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.bgcolorBtn, pos=(3 , 1 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)

        self.Layout()

    def verb_inst_rightClick( self, event, id ):
        
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
            
            if col1 == 1:
                self.row -=1
            self.normal_case = True

    def noun_button_onClick( self, event ):
        
        self.n += 1
        self.noun_inst = wx.Button( self, id = self.n, label = "noun", size = wx.DefaultSize )
        if self.normal_case:
            self.bagSizer1.Add(self.noun_inst, pos=(self.row , 1 ), flag=wx.ALL, border=5)
            self.row +=1
            
        else:
            self.bagSizer1.Add(self.noun_inst, pos=(self.add_row , 2), flag=wx.ALL, border=5)

        self.button_dict[self.n] = self.noun_inst
        self.noun_inst.Bind( wx.EVT_BUTTON, self.noun_inst_onClick )
        func = functools.partial(self.noun_inst_rightClick , id = self.n)
        self.noun_inst.Bind(wx.EVT_RIGHT_DOWN, func)
        
        self.normal_case = True
        self.Layout() #to update frame
    
    def noun_inst_onClick( self, event ):
        self.bagSizer2.Clear(True)
        self.bagSizer3.Clear(True)
        
        self.line2.Show()
        
        # row 1
        self.text1 = wx.StaticText(self, -1, "Gender")
        
        self.m_button1 = wx.ToggleButton( self, wx.ID_ANY, u"Feminine")
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( self, wx.ID_ANY, u"Mascular")
        self.m_button2.SetValue(True)
        
        
        # row 2
        self.text2 = wx.StaticText(self, -1, "Number")
        
        self.m_button3 = wx.ToggleButton( self, wx.ID_ANY, u"Singular")
        self.m_button3.SetValue(True)
        
        self.m_button4 = wx.ToggleButton( self, wx.ID_ANY, u"Plural")
        self.m_button4.SetValue(True)
        
        # row 3
        self.text3 = wx.StaticText(self, -1, "Foreign")
        self.m_button5 = wx.ToggleButton( self, wx.ID_ANY, u"yes")
        self.m_button5.SetValue(True)
        
        self.bagSizer2.Add(self.text1, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button1, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button2, pos=(0 , 2 ), flag=wx.ALL, border= 5)
      
        self.bagSizer2.Add(self.text2, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button3, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button4, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text3, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button5, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        
         #line
        self.line3.Show()
        
        #lens
        self.text = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.text, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.FontBtn, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.SizeBtn, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.BoldBtn, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.ItalicBtn, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.colorBtn, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer3.Add(self.bgcolorBtn, pos=(3 , 1 ), flag=wx.ALL, border= 5)

        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.Layout()
    
    def noun_inst_rightClick( self, event, id ):
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
            if col1 == 1:
                self.row -=1
            self.normal_case = True
        """if id in self.button_dict:
          self.button_dict[id].Destroy()"""

    def adj_button_onClick( self, event ):
        self.n += 1
        self.adj_inst = wx.Button( self, id = self.n, label = "adjective", size = wx.DefaultSize )
        if self.normal_case:
            self.bagSizer1.Add(self.adj_inst, pos=(self.row , 1 ), flag=wx.ALL, border=5)
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
        self.text1 = wx.StaticText(self, -1, "Gender")
        
        self.m_button1 = wx.ToggleButton( self, wx.ID_ANY, u"Feminine")
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( self, wx.ID_ANY, u"Mascular")
        self.m_button2.SetValue(True)

        # row 2
        self.text2= wx.StaticText(self, -1, "Number")
        
        self.m_button3 = wx.ToggleButton( self, wx.ID_ANY, u"Singular")
        self.m_button3.SetValue(True)
        
        self.m_button4 = wx.ToggleButton( self, wx.ID_ANY, u"Plural")
        self.m_button4.SetValue(True)
        
        # row 3
        self.text3= wx.StaticText(self, -1, "Degree")
        
        self.m_button5 = wx.ToggleButton( self, wx.ID_ANY, u"Cmp")
        self.m_button5.SetValue(True)
        
        self.m_button6 = wx.ToggleButton( self, wx.ID_ANY, u"Abs")
        self.m_button6.SetValue(True)    
        
        # row 4
        self.text4 = wx.StaticText(self, -1, "Foreign")
        self.m_button7 = wx.ToggleButton( self, wx.ID_ANY, u"yes" )
        self.m_button7.SetValue(True)
        
        self.bagSizer2.Add(self.text1, pos=(0 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button1, pos=(0 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button2, pos=(0 , 2 ), flag=wx.ALL, border= 5)
      
        self.bagSizer2.Add(self.text2, pos=(1 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button3, pos=(1 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button4, pos=(1 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text3, pos=(2 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button5, pos=(2 , 1 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button6, pos=(2 , 2 ), flag=wx.ALL, border= 5)
        
        self.bagSizer2.Add(self.text4, pos=(3 , 0 ), flag=wx.ALL, border= 5)
        self.bagSizer2.Add(self.m_button7, pos=(3 , 1 ), flag=wx.ALL, border= 5)
        
         #line
        self.line3.Show()
        
        #lens
        self.text = wx.StaticText(self, wx.ID_ANY, "lens")
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        
        fonts_size = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts_size, size = (60,25))

        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        
        #ADD TO BAG SIZER
        self.bagSizer3.Add(self.text, pos=(0 , 0 ), flag=wx.ALL, border= 5)
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
            if col1 == 1:
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

    
    def open_json( self, event ):
        dlg3 = wx.FileDialog(
            self, 
            message = "Choose a file",
            #defaultDir = self.currentDirectory, 
            defaultFile = "",
            wildcard = FileFilter3,
            style = wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        if dlg3.ShowModal() == wx.ID_OK:
            htmlFilePath2 = dlg3.GetPath()
            self.htmlwin2.LoadURL(htmlFilePath2)
        dlg3.Destroy()

#--------------------------------------------------------------------------------------------------------------------------
# Run the program !
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()