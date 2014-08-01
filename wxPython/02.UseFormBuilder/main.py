# -*- coding: utf-8 -*-

import wx
import noname

app = wx.App()

window = noname.customFrame_list(None)
window.Show()

app.MainLoop()
