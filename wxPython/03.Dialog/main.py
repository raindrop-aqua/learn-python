# -*- coding: utf-8 -*-

import wx

class DetailDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, title="modal window")

        button = wx.Button(self, wx.ID_ANY, "Close")
        button.Bind(wx.EVT_BUTTON, self.button_close_click)
        text = wx.TextCtrl(self, wx.ID_ANY)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(text)
        layout.Add(button)
        self.SetSizer(layout)
        self.Layout()
        self.Center(wx.BOTH)

    def button_close_click(self, event):
        yesno_dialog = wx.MessageDialog(self, "close window?",
            "message", wx.YES_NO | wx.ICON_QUESTION)

        try:
            if yesno_dialog.ShowModal() == wx.ID_YES:
                self.Close()
        finally:
            yesno_dialog.Destroy()
        return True

class ParentFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="parent window")

        button = wx.Button(self, wx.ID_ANY, "Show Modal")
        button.Bind(wx.EVT_BUTTON, self.button_open_click)
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(button)
        self.SetSizer(layout)
        self.Layout()
        self.Center(wx.BOTH)

    def button_open_click(self, event):
        dialog = DetailDialog(self)

        try:
            dialog.ShowModal()
        finally:
            dialog.Destroy()
        return True

class App(wx.App):
    def OnInit(self):
        self.frame = ParentFrame(None)
        self.frame.Show()
        return True

app = App()
app.MainLoop()




