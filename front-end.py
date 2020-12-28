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
###########################################################################
class Button:
    def create_button(self, parent, id, label, row, column, size, name):
        self.parent = parent
        self.id = id
        self.label = label
        self.row = row
        self.column = column
        self.size = size
        self.name = name
        return wx.Button(parent, id = id, label = label, pos = (row,column), size = size, name = name)
    
    def get_row(self):
      return self.row
    def get_column(self):
        return self.column
    

###########################################################################
## Class sentence
###########################################################################
class Sentence(sc.SizedDialog):

    def __init__(self):
        sc.SizedDialog.__init__(self, None, title="Sentence", size=(450,210))
        
        panel = self.GetContentsPane()
        panel.SetSizerType("form")
        
        # row 1
        wx.StaticText(panel, -1, "Main type")
        
        buttonPane = sc.SizedPanel(panel, -1)
        buttonPane.SetSizerType("horizontal")
        
        self.m_button1 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Declarative", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Interrogative", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetValue(True)
        
        self.m_button3 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Exclamative", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button3.SetValue(True)
        #textCtrl.SetSizerProps(expand=True)
        
        # row 2
        wx.StaticText(panel, -1, "Relative sentences")
        
        buttonPane2 = sc.SizedPanel(panel, -1)
        buttonPane2.SetSizerType("horizontal")
        
        self.m_button4 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"has relative sentences", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetValue(True)
        
        self.m_button5 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"has conncetors", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button5.SetValue(True)
        
        # row 3
        wx.StaticText(panel, -1, "Number of words")
        wx.TextCtrl(panel, size=(60, -1))
        
        # row 4
        wx.StaticText(panel, -1, "Number of content words")
        wx.TextCtrl(panel, size=(60, -1)) # two chars for state
        
        # row 5
        wx.StaticText(panel, -1, "")
        self.m_button21 = wx.Button( panel, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button21.SetSizerProps(halign='right') 
        self.m_button21.Bind( wx.EVT_BUTTON, self.Ok_onClick )
    
        
        self.Layout()
        self.Centre( wx.BOTH )
        
    def Ok_onClick(self,event):
        self.Destroy()


#####################################################################################################################################################
# class verb
class VerbDialog(sc.SizedDialog):
    def __init__(self):
        """Constructor"""
        sc.SizedDialog.__init__(self, None, title="Verb",
                                size=(450,300))
        
        panel = self.GetContentsPane()
        panel.SetSizerType("form")
        
        
        # row 1
        wx.StaticText(panel, -1, "Lemma")
        textCtrl = wx.TextCtrl(panel)
        textCtrl.SetSizerProps(expand=True)
        
        #row2
        wx.StaticText(panel, -1, "Number")
        buttonPane = sc.SizedPanel(panel, -1)
        buttonPane.SetSizerType("horizontal")
        
        self.m_button1 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Singular", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Plural", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetValue(True)
       
        #textCtrl.SetSizerProps(expand=True)
        
        # row 3
        wx.StaticText(panel, -1, "Person")
        
        buttonPane2 = sc.SizedPanel(panel, -1)
        buttonPane2.SetSizerType("horizontal")
        
        self.m_button3 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"First", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button3.SetValue(True)
        
        self.m_button4 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Second", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetValue(True)
        
        self.m_button5 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Third", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button5.SetValue(True)
        
        # row 4
        wx.StaticText(panel, -1, "Tense")
        buttonPane3 = sc.SizedPanel(panel, -1)
        buttonPane3.SetSizerType("horizontal")
        
        self.m_button6 = wx.ToggleButton( buttonPane3, wx.ID_ANY, u"Past", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button6.SetValue(True)
        
        self.m_button7 = wx.ToggleButton( buttonPane3, wx.ID_ANY, u"Present", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button7.SetValue(True)
        
        self.m_button8 = wx.ToggleButton( buttonPane3, wx.ID_ANY, u"Future", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button8.SetValue(True)
        
        # row 4
        wx.StaticText(panel, -1, "Form")
        buttonPane4 = sc.SizedPanel(panel, -1)
        buttonPane4.SetSizerType("horizontal")
        
        self.m_button9 = wx.ToggleButton( buttonPane4, wx.ID_ANY, u"Fin", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button9.SetValue(True)
        
        self.m_button10 = wx.ToggleButton( buttonPane4, wx.ID_ANY, u"Part", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button10.SetValue(True)
        
        self.m_button11 = wx.ToggleButton( buttonPane4, wx.ID_ANY, u"Inf", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button11.SetValue(True)
        
        self.m_button12 = wx.ToggleButton( buttonPane4, wx.ID_ANY, u"Ger", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button12.SetValue(True)
        
        #row 5
        wx.StaticText(panel, -1, "Mood")
        buttonPane5 = sc.SizedPanel(panel, -1)
        buttonPane5.SetSizerType("horizontal")
        
        self.m_button9 = wx.ToggleButton( buttonPane5, wx.ID_ANY, u"Ind", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button9.SetValue(True)
        
        self.m_button10 = wx.ToggleButton( buttonPane5, wx.ID_ANY, u"Cnd", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button10.SetValue(True)
        
        self.m_button11 = wx.ToggleButton( buttonPane5, wx.ID_ANY, u"Sub", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button11.SetValue(True)
        
        self.m_button12 = wx.ToggleButton( buttonPane5, wx.ID_ANY, u"Imp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button12.SetValue(True)
        
        #row 6
        wx.StaticText(panel, -1, "Gender")
        buttonPane6 = sc.SizedPanel(panel, -1)
        buttonPane6.SetSizerType("horizontal")
        
        self.m_button13 = wx.ToggleButton( buttonPane6, wx.ID_ANY, u"Feminin", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button13.SetValue(True)
        
        self.m_button14 = wx.ToggleButton( buttonPane6, wx.ID_ANY, u"Mascular", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button14.SetValue(True)
        
        
        # row 7
        wx.StaticText(panel, -1, "")
        self.m_button15 = wx.Button( panel, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button15.SetSizerProps(halign='right')
        self.m_button15.Bind( wx.EVT_BUTTON, self.Ok_onClick )
        
        self.Layout()
        self.Centre( wx.BOTH )

#########################################################################################################################
class NounDialog(sc.SizedDialog):

    def __init__(self):
        """Constructor"""
        sc.SizedDialog.__init__(self, None, title="Noun",
                                size=(250,175))
        
        panel = self.GetContentsPane()
        panel.SetSizerType("form")
        
        # row 1
        wx.StaticText(panel, -1, "Gender")
        
        buttonPane = sc.SizedPanel(panel, -1)
        buttonPane.SetSizerType("horizontal")
        
        self.m_button1 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Feminine", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Mascular", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetValue(True)
        
        
        # row 2
        wx.StaticText(panel, -1, "Number")
        
        buttonPane2 = sc.SizedPanel(panel, -1)
        buttonPane2.SetSizerType("horizontal")
        
        self.m_button4 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Singular", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetValue(True)
        
        self.m_button5 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Plural", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button5.SetValue(True)
        
        # row 3
        wx.StaticText(panel, -1, "Foreign")
        self.m_button6 = wx.ToggleButton( panel, wx.ID_ANY, u"yes", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button6.SetValue(True)
     
        
        # row 4
        wx.StaticText(panel, -1, "")
        self.m_button7 = wx.Button( panel, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button7.SetSizerProps(halign='right')
        self.m_button7.Bind( wx.EVT_BUTTON, self.Ok_onClick )
        
        self.Layout()
        self.Centre( wx.BOTH )
        
########################################################################################################################
class AdjDialog(sc.SizedDialog):

    def __init__(self):
        """Constructor"""
        sc.SizedDialog.__init__(self, None, title="Adjective",
                                size=(250,210))
        
        panel = self.GetContentsPane()
        panel.SetSizerType("form")
        
        # row 1
        wx.StaticText(panel, -1, "Gender")
        
        buttonPane = sc.SizedPanel(panel, -1)
        buttonPane.SetSizerType("horizontal")
        
        self.m_button1 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Feminine", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button1.SetValue(True)
        
        self.m_button2 = wx.ToggleButton( buttonPane, wx.ID_ANY, u"Mascular", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button2.SetValue(True)
        
        
        # row 2
        wx.StaticText(panel, -1, "Number")
        
        buttonPane2 = sc.SizedPanel(panel, -1)
        buttonPane2.SetSizerType("horizontal")
        
        self.m_button4 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Singular", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetValue(True)
        
        self.m_button5 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Plural", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button5.SetValue(True)
        
        # row 3
        wx.StaticText(panel, -1, "Degree")
        
        buttonPane2 = sc.SizedPanel(panel, -1)
        buttonPane2.SetSizerType("horizontal")
        
        self.m_button4 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Cmp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button4.SetValue(True)
        
        self.m_button5 = wx.ToggleButton( buttonPane2, wx.ID_ANY, u"Abs", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button5.SetValue(True)
        
        
        # row 4
        wx.StaticText(panel, -1, "Foreign")
        self.m_button6 = wx.ToggleButton( panel, wx.ID_ANY, u"yes", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button6.SetValue(True)
     
        
        # row 5
        wx.StaticText(panel, -1, "")
        self.m_button7 = wx.Button( panel, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button7.SetSizerProps(halign='right')
        self.m_button7.Bind( wx.EVT_BUTTON, self.Ok_onClick )
        
        
        
        self.Layout()
        self.Centre( wx.BOTH )
        
    def Ok_onClick(self, event):
        self.Close()

##################################################################################################################
class LensDlg(wx.Frame):
 
    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Lens", size=(260,180))
        self.colourData = None
        
        vbox = wx.BoxSizer( wx.VERTICAL )     
        hbox1 = wx.BoxSizer( wx.HORIZONTAL )
        
        fonts = ['Arial','Calibri', 'Times New Roman'] 
        self.FontBtn = wx.ComboBox(self,choices = fonts, size = (180,25))
        hbox1.Add( self.FontBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        fonts = ['6','7','8','9','10','11', '12', '13', '14', '15', '16','17','18','19', '20','28','36','48', '72']
        self.SizeBtn = wx.ComboBox(self,choices = fonts, size = (60,25))
        hbox1.Add( self.SizeBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        vbox.Add( hbox1, 0, wx.EXPAND, 5 )
        
        hbox2 = wx.BoxSizer( wx.HORIZONTAL )
        self.colorBtn = wx.Button(self, label="Font color", size = (120,25))
        hbox2.Add( self.colorBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.bgcolorBtn = wx.Button(self, label="Background color", size = (120,25))
        hbox2.Add( self.bgcolorBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        vbox.Add( hbox2, 0, wx.EXPAND, 5 )
        
        hbox3 = wx.BoxSizer( wx.HORIZONTAL )
        self.BoldBtn = wx.ToggleButton(self, label="Bold", size = (120,25))
        hbox3.Add( self.BoldBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.ItalicBtn = wx.ToggleButton(self, label="Italic", size = (120,25))
        hbox3.Add( self.ItalicBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        vbox.Add( hbox3, 0, wx.EXPAND, 5 )
        
        hbox4 = wx.BoxSizer( wx.HORIZONTAL )
        
        hbox4.Add(130,10)
        self.resetBtn = wx.Button(self, label="reset", size = (55,25))
        hbox4.Add( self.resetBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL,1 )
        self.resetBtn.SetBackgroundColour((255, 0, 0, 0))
        
        self.okBtn = wx.Button(self, label="ok", size = (55,25))
        hbox4.Add( self.okBtn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 1)
        self.okBtn.SetBackgroundColour((0, 0, 255, 0))
        
        vbox.Add( hbox4, 0, wx.EXPAND, 5 )
        
        self.SetSizer( vbox )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        self.colorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        self.bgcolorBtn.Bind(wx.EVT_BUTTON, self.onColorDlg)
        
       
        
    #----------------------------------------------------------------------
    def onColorDlg(self, event):
        """
        This is mostly from the wxPython Demo!
        """
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)

        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetColourData()
            print ('You selected: %s\n' % str(data.GetColour().Get()))
            
        dlg.Destroy()
        
#####################################################################################################################################################
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000, 700), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.m_menubar1 = wx.MenuBar( 0 )
        self.fileMenu = wx.Menu()
        self.fileItem = self.fileMenu.Append(wx.ID_EXIT, 'open', 'choose HTML file')
        self.m_menubar1.Append(self.fileMenu, '&File')
        self.SetMenuBar( self.m_menubar1 )
        
        self.sentence_button = wx.Button( self, wx.ID_ANY, u"Sentence", pos = (10,10), size = wx.DefaultSize )

        self.verb_button = wx.Button( self, wx.ID_ANY, u"Verb", pos = (90,10), size = wx.DefaultSize )
 
        self.noun_button = wx.Button( self, wx.ID_ANY, u"Noun", pos = (170,10), size = wx.DefaultSize)
        
        self.adj_button = wx.Button( self, wx.ID_ANY, u"Adjective", pos = (250,10), size = wx.DefaultSize)
        
        self.lens_button = wx.Button( self, wx.ID_ANY, u"Lens", pos = (510,10), size = wx.DefaultSize )

        self.htmlwin2=wx.html2.WebView.New(self, pos=(10,40), size=(490,590))

        self.sentence_button.Bind( wx.EVT_BUTTON, self.sentence_button_onClick )
        self.verb_button.Bind( wx.EVT_BUTTON, self.verb_button_onClick )
        self.noun_button.Bind( wx.EVT_BUTTON, self.noun_button_onClick )
        self.adj_button.Bind( wx.EVT_BUTTON, self.adj_button_onClick )
        self.lens_button.Bind( wx.EVT_BUTTON, self.lens_button_onClick )

        self.row = 0
        self.lens_row= 0
        self.number_of_rows = 0
        self.sent_inst_1_Clicked = False
        self.normal_case = True
        self.first_colum = 530
        self.second_colum = 610
        self.third_colum = 690
        
        self.Layout()
        self.Centre( wx.BOTH )
        
    def OnQuit(self, e):
        self.Close()

    def sentence_button_onClick( self, event ):  
        self.row = self.row + 40
        self.sentence_row = self.row
        self.number_of_rows += 1
        btn = Button()
        #btn.create_button(self.panel, wx.ID_ANY, "click me", 10,10,(70,30), "btn1")
        self.add = wx.Button( self, wx.ID_ANY, u"+", pos = (510 ,self.row), size = (15,15) )
        self.sentence_inst_1 = wx.Button( self, wx.ID_ANY, u"sentence", pos = (530 ,self.row), size = wx.DefaultSize )
        self.add.Bind( wx.EVT_BUTTON, self.add_onClick )
        self.sentence_inst_1.Bind( wx.EVT_BUTTON, self.sent_inst_1_onClick )
        #self.normal_case = True
    
    def add_onClick(self, event): 
        #self.add.Destroy()
        self.normal_case = False
        self.add_row = self.sentence_row
        #self.remove = wx.Button( self, wx.ID_ANY, u"-", pos = (510 ,self.add_row), size = (15,15) )
        #self.box = wx.StaticBox(self, wx.ID_ANY, label="", pos = (610 ,self.add_row-7), size=(80,32))
        #self.remove.Bind( wx.EVT_BUTTON, self.remove_onClick )
    
    def remove_onClick(self, event):
        self.remove.Destroy()
        self.box.Destroy()
        self.normal_case = True
        self.add = wx.Button( self, wx.ID_ANY, u"+", pos = (510 ,self.add_row), size = (15,15) )
        self.add.Bind( wx.EVT_BUTTON, self.add_onClick )
        
    def sent_inst_1_onClick( self, event ):
        self.sent_inst_1_Clicked = True
        Sentence().Show()
        return self.sent_inst_1_Clicked

    def verb_button_onClick( self, event ):
        self.number_of_rows += 1
        if self.normal_case:
            self.x = self.first_colum
            self.row = self.row + 40
            self.verb_inst_1 = wx.Button( self, wx.ID_ANY, u"verb", pos = (self.x ,self.row), size = wx.DefaultSize )
        else:
            self.x = self.second_colum
            #self.box.Destroy()
            self.verb_inst_1 = wx.Button( self, wx.ID_ANY, u"verb", pos = (self.x ,self.add_row), size = wx.DefaultSize )
        self.verb_inst_1.Bind( wx.EVT_BUTTON, self.verb_inst_1_onClick )
        self.normal_case = True

    def verb_inst_1_onClick( self, event ):
        self.sent_inst_1_Clicked = True
        VerbDialog().Show()
        #return self.sent_inst_1_Clicked

    def noun_button_onClick( self, event ):
        self.number_of_rows +=1
        if self.normal_case:
            self.x = self.first_colum
            self.row = self.row + 40
        else:
            self.x = self.second_colum
            self.box.Destroy()
        self.noun_inst_1 = wx.Button( self, wx.ID_ANY, u"noun", pos = (self.x ,self.row), size = wx.DefaultSize )
        self.noun_inst_1.Bind( wx.EVT_BUTTON, self.noun_inst_1_onClick )
        self.normal_case = True
    
    def noun_inst_1_onClick( self, event ):
        NounDialog().Show()

    def adj_button_onClick( self, event ):
        self.number_of_rows +=1
        if self.normal_case:
            self.x = self.first_colum
            self.row = self.row + 40
        else:
            self.x = self.second_colum
            self.box.Destroy()
        self.adj_inst_1 = wx.Button( self, wx.ID_ANY, u"adjective", pos = (self.x ,self.row), size = wx.DefaultSize )
        self.adj_inst_1.Bind( wx.EVT_BUTTON, self.adj_inst_1_onClick )
        self.normal_case = True
    
    def adj_inst_1_onClick( self, event ):
        AdjDialog().Show()

    def lens_button_onClick( self, event ):
        self.lens_row = self.lens_row + 40
        self.lens_inst_1 = wx.Button( self, wx.ID_ANY, u"lens", pos = (610 ,self.lens_row), size = wx.DefaultSize )
        self.lens_inst_1.Bind( wx.EVT_BUTTON, self.lens_inst_1_onClick )
        
    def lens_inst_1_onClick( self, event ):
        LensDlg().Show()

    def combine_button_onClick( self, event ):
        pass

    def do_something1(self, event):
        box = event.GetEventObject()
        setting = box.GetValue()
        if setting:
            self.combine_button = wx.Button( self, wx.ID_ANY, u"Combine filters", pos = (590,10), size = wx.DefaultSize )
        event.Skip()

    
    def __del__( self ):
        pass
    


# Run the program !
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()