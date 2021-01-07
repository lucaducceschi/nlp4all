# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.html
import wx.html2
import os
import os.path
from shutil import copyfile
import bs4
# from bs4 import BeautifulSoup

FileFilter2 =    "Html files (*.html)|*.html|" \
                "All files (*.*)|*.*"
FileFilter =    "Css files (*.css)|*.css|" \
                "All files (*.*)|*.*"

#--------------------------------------------------------------
class AddCssToHtml:
  
  def getHtmlPath(self,htmlPath):
    self.htmlPath = htmlPath
    return htmlPath
  def getCssPath(self,cssPath):
    self.cssPath = cssPath
    return cssPath

  def createLink(self,htmlPath):
    with open(self.htmlPath) as inf:
     txt = inf.read()
     soup = bs4.BeautifulSoup(txt,features="html.parser")
    new_link = soup.new_tag("link", rel="stylesheet", type="text/css", href=self.cssPath)
    soup.head.append(new_link)
    with open(self.htmlPath, "w") as outf:
      outf.write(str(soup))

css = AddCssToHtml()
#---------------------------------------------------------------

###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 675,570 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
        
        self.currentDirectory = os.getcwd()

        vbox = wx.BoxSizer( wx.VERTICAL )
        
        hbox1 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.label1 = wx.StaticText( self, wx.ID_ANY, u"Welcome!", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label1.Wrap( -1 )
        hbox1.Add( self.label1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        vbox.Add( hbox1, 0, wx.EXPAND, 5 )
        
        hbox2 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.label2 = wx.StaticText( self, wx.ID_ANY, u"Please choose a CSS file: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label2.Wrap( -1 )
        hbox2.Add( self.label2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.buttonCSS = wx.Button( self, wx.ID_ANY, u"Choose file", wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox2.Add( self.buttonCSS, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        vbox.Add( hbox2, 0, wx.EXPAND, 5 )
        
        hbox3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.label3 = wx.StaticText( self, wx.ID_ANY, u"Please choose the HTML file: ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label3.Wrap( -1 )
        hbox3.Add( self.label3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.buttonHTML = wx.Button( self, wx.ID_ANY, u"Choose file", wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox3.Add( self.buttonHTML, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        vbox.Add( hbox3, 0, wx.EXPAND, 5 )
        
        hbox3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.label4 = wx.StaticText( self, wx.ID_ANY, u"Click this button to see the result:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.label4.Wrap( -1 )
        hbox3.Add( self.label4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        self.buttonResult = wx.Button( self, wx.ID_ANY, u"Show result", wx.DefaultPosition, wx.DefaultSize, 0 )
        hbox3.Add( self.buttonResult, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        vbox.Add( hbox3, 0, wx.EXPAND, 5 )
        
        
        #self.m_htmlWin11 = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
        #vbox.Add( self.m_htmlWin11, 0, wx.ALL, 5 )
        
        #self.htmlwin = wx.html.HtmlWindow(self, -1)
        #self.htmlwin.SetForegroundColour( wx.Colour( 208, 208, 208 ) )
        #self.htmlwin.SetBackgroundColour( wx.Colour( 240, 240, 128 ) )
        self.htmlwin2=wx.html2.WebView.New(self)
       # self.htmlwin2.LoadURL("E:\\pythonGUI\\newtest.html")
 
        vbox.Add(self.htmlwin2, 1, wx.LEFT | wx.TOP | wx.GROW)
        
        self.SetSizer( vbox )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.buttonCSS.Bind( wx.EVT_BUTTON, self.buttonCSSOnButtonClick )
        self.buttonHTML.Bind( wx.EVT_BUTTON, self.buttonHTMLOnButtonClick )
        self.buttonResult.Bind( wx.EVT_BUTTON, self.buttonResultOnButtonClick )
    
    def __del__( self ):
        pass
    
    
    # Virtual event handlers, overide them in your derived class
    def buttonCSSOnButtonClick( self, event ):
        # todo:mod this to load a json
        dlg = wx.FileDialog(
            self, 
            message = "Choose a file",
            defaultDir = self.currentDirectory, 
            defaultFile = "",
            wildcard = FileFilter,
            style = wx.FD_OPEN | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            cssFilePath = dlg.GetPath() 
            css.getCssPath(cssFilePath)
            self.htmlwin2.LoadURL(cssFilePath)
            
        dlg.Destroy()
    
    def buttonHTMLOnButtonClick( self, event ):
        dlg2 = wx.FileDialog(
            self, 
            message = "Choose a file",
            defaultDir = self.currentDirectory, 
            defaultFile = "",
            wildcard = FileFilter2,
            style = wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        ## If the user selects a file, open it in the Html File Viewer
        if dlg2.ShowModal() == wx.ID_OK:
            htmlFilePath = dlg2.GetPath()
            print(htmlFilePath)
            self.htmlwin2.LoadURL(htmlFilePath)
            #copy the html file into a new file
            htmlDirectory, filename = os.path.split(htmlFilePath)
            newfilename = "new" + filename
            newHtmlFilePath = os.path.join(htmlDirectory, newfilename)
            copyfile(htmlFilePath, newHtmlFilePath)
            #add css to the html file
            css.getHtmlPath(newHtmlFilePath)
            css.createLink(newHtmlFilePath)
            
        dlg2.Destroy()
    
    def buttonResultOnButtonClick( self, event ):
        dlg3 = wx.FileDialog(
            self, 
            message = "Choose a file",
            defaultDir = self.currentDirectory, 
            defaultFile = "",
            wildcard = FileFilter2,
            style = wx.FD_OPEN | wx.FD_CHANGE_DIR
        )

        ## If the user selects a file, open it in the Html File Viewer
        if dlg3.ShowModal() == wx.ID_OK:
            htmlFilePath2 = dlg3.GetPath()
            self.htmlwin2.LoadURL(htmlFilePath2)
        dlg3.Destroy()
     

# Run the program !
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame4(None)
    frame.Show()
    app.MainLoop()
    

