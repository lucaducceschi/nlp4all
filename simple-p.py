# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 20:43:13 2020

@author: Sevda
"""
import wx
import wx.xrc
import wx.html
import wx.html2
import os
import os.path
from shutil import copyfile
import stanza
import requests
import re
import bs4
from bs4 import BeautifulSoup
import json

FileFilter2 =    "Html files (*.html)|*.html|" \
                "All files (*.*)|*.*"
FileFilter =    "Css files (*.css)|*.css|" \
                "All files (*.*)|*.*"

nlp_it = stanza.Pipeline("it", processors="tokenize, pos, lemma", verbose = False ) #  , use_gpu=True 
sample_it_url = "https://www.gutenberg.org/cache/epub/18456/pg18456.txt" # Pirandello, Enrico 4
imported_json = json.load(open("/Users/luca/Downloads/nlp4all_data_dec_2020/small_sample_pirandello_25_11_2020.json"))



class VerbClk:
    
    def how_many_pos(self, data, pos):
        out = {}
        for sentid,list_of_ds in data.items():
            out[sentid] = []
            for dict_ in list_of_ds:
              if  dict_["upos"] == pos:
                 out[sentid].append(dict_["id"])
        c = 0
        for listids in out.values():
            c+= len(listids)
        return c, out

verbclk1 = VerbClk()
#=================================================================================================================

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 833,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.OpenFile = wx.Button( self, wx.ID_ANY, u"OpenFile", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.OpenFile, 0, wx.ALL, 5 )
        
        self.Verb = wx.Button( self, wx.ID_ANY, u"Verb", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_colourPicker2 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        bSizer2.Add( self.Verb, 0, wx.ALL, 5 )
        
        self.Lens = wx.Button( self, wx.ID_ANY, u"Lens", wx.DefaultPosition, wx.DefaultSize, 0 )
        #self.m_colourPicker2 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 255, 0, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
        bSizer2.Add( self.Lens, 0, wx.ALL, 5 )
        
        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )
        
        
        
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_htmlWin2 = wx.html2.WebView.New(self)
        #self.m_htmlWin2.LoadURL("E:\\pythonGUI\\small_sample_pirandello_25_11_2020.html")
        #bSizer4.Add( self.m_htmlWin2, 0, wx.ALL, 5 )
        bSizer4.Add(self.m_htmlWin2, 1, wx.LEFT | wx.TOP | wx.GROW)
        
        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )

        self.OpenFile.Bind( wx.EVT_BUTTON, self.OpenFileOnButtonClick )
        self.Verb.Bind( wx.EVT_BUTTON, self.VerbOnButtonClick )
    
    def __del__( self ):
        pass

    def OpenFileOnButtonClick( self, event ):
        dlg3 = wx.FileDialog(
            self, 
            message = "Choose a file",
            #defaultDir = self.currentDirectory, 
            defaultFile = "",
            wildcard = FileFilter2,
            style = wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        ## If the user selects a file, open it in the Html File Viewer
        if dlg3.ShowModal() == wx.ID_OK:
            htmlFilePath2 = dlg3.GetPath()
            self.m_htmlWin2.LoadURL(htmlFilePath2)
        dlg3.Destroy()

    def VerbOnButtonClick( self, event ):
        verbclk1.how_many_pos(imported_json, "VERB")
    # Run the program !
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()