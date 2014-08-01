# -*- coding: utf-8 -*-

import wx,sys

app = wx.App()
param = sys.argv
param_1 = "None"
if len(param) > 1:
	param_1 = param[1]

window_style = wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
window = wx.Frame(None, style=window_style)

panel = wx.Panel(window, wx.ID_ANY)
panel.SetBackgroundColour("#AFAFAF")

label1 = wx.StaticText(panel, wx.ID_ANY, u"テキスト１")
label2 = wx.StaticText(panel, wx.ID_ANY, param_1)

layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(label1)
layout.Add(label2)

panel.SetSizer(layout)

window.Show(True)

app.MainLoop()
