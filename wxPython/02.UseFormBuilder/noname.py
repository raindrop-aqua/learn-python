# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.grid

###########################################################################
## Class customFrame_list
###########################################################################

class customFrame_list ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"modo script downloader", pos = wx.DefaultPosition, size = wx.Size( 1000,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_file = wx.Menu()
		self.m_menuItem_close = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Close", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_file.AppendItem( self.m_menuItem_close )
		
		self.m_menubar.Append( self.m_menu_file, u"File" ) 
		
		self.m_menu_view = wx.Menu()
		self.m_menuItem_refresh = wx.MenuItem( self.m_menu_view, wx.ID_ANY, u"Refresh"+ u"\t" + u"F5", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_view.AppendItem( self.m_menuItem_refresh )
		
		self.m_menubar.Append( self.m_menu_view, u"View" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"resrc/arrowleft16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString ) 
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"resrc/arrowright16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString ) 
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"resrc/exchange16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString ) 
		self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"resrc/home16.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString ) 
		self.m_toolBar1.Realize()
		
		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )
		
		self.m_grid_list = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.m_grid_list.CreateGrid( 1, 5 )
		self.m_grid_list.EnableEditing( False )
		self.m_grid_list.EnableGridLines( True )
		self.m_grid_list.SetGridLineColour( wx.Colour( 112, 120, 128 ) )
		self.m_grid_list.EnableDragGridSize( False )
		self.m_grid_list.SetMargins( 0, 0 )
		
		# Columns
		self.m_grid_list.SetColSize( 0, 150 )
		self.m_grid_list.SetColSize( 1, 100 )
		self.m_grid_list.SetColSize( 2, 80 )
		self.m_grid_list.SetColSize( 3, 80 )
		self.m_grid_list.SetColSize( 4, 500 )
		self.m_grid_list.EnableDragColMove( False )
		self.m_grid_list.EnableDragColSize( True )
		self.m_grid_list.SetColLabelSize( 30 )
		self.m_grid_list.SetColLabelValue( 0, u"Name" )
		self.m_grid_list.SetColLabelValue( 1, u"Author" )
		self.m_grid_list.SetColLabelValue( 2, u"Version" )
		self.m_grid_list.SetColLabelValue( 3, u"Rating" )
		self.m_grid_list.SetColLabelValue( 4, u"Description" )
		self.m_grid_list.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.m_grid_list.EnableDragRowSize( False )
		self.m_grid_list.SetRowLabelSize( 0 )
		self.m_grid_list.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		self.m_grid_list.SetLabelBackgroundColour( wx.Colour( 100, 112, 124 ) )
		self.m_grid_list.SetLabelFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 91, False, wx.EmptyString ) )
		self.m_grid_list.SetLabelTextColour( wx.Colour( 180, 192, 204 ) )
		
		# Cell Defaults
		self.m_grid_list.SetDefaultCellBackgroundColour( wx.Colour( 144, 152, 160 ) )
		self.m_grid_list.SetDefaultCellTextColour( wx.Colour( 47, 50, 104 ) )
		self.m_grid_list.SetDefaultCellFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.m_grid_list.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer2.Add( self.m_grid_list, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.menu_close_selection, id = self.m_menuItem_close.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_refresh_selection, id = self.m_menuItem_refresh.GetId() )
		self.Bind( wx.EVT_TOOL, self.m_tool_prev_click, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL, self.m_tool_next_click, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL, self.m_tool_refresh_click, id = wx.ID_ANY )
		self.Bind( wx.EVT_TOOL, self.m_tool_home_click, id = wx.ID_ANY )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def menu_close_selection( self, event ):
		event.Skip()
	
	def menu_refresh_selection( self, event ):
		event.Skip()
	
	def m_tool_prev_click( self, event ):
		event.Skip()
	
	def m_tool_next_click( self, event ):
		event.Skip()
	
	def m_tool_refresh_click( self, event ):
		event.Skip()
	
	def m_tool_home_click( self, event ):
		event.Skip()
	

###########################################################################
## Class customFrame_detail
###########################################################################

class customFrame_detail ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Detail", pos = wx.DefaultPosition, size = wx.Size( 499,425 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.FRAME_NO_TASKBAR|wx.FRAME_TOOL_WINDOW|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer6 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		fgSizer6.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_textCtrl_name = wx.TextCtrl( self, wx.ID_ANY, u"window set script", wx.DefaultPosition, wx.Size( 250,-1 ), wx.TE_READONLY )
		fgSizer6.Add( self.m_textCtrl_name, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Author", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		fgSizer6.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_textCtrl_author = wx.TextCtrl( self, wx.ID_ANY, u"Masahiro Atsumi", wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_READONLY )
		fgSizer6.Add( self.m_textCtrl_author, 0, wx.ALL, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		fgSizer6.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.m_textCtrl_version = wx.TextCtrl( self, wx.ID_ANY, u"1.0.0.1", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_NO_VSCROLL|wx.TE_READONLY )
		fgSizer6.Add( self.m_textCtrl_version, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Rating", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer6.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_textCtrl_rating = wx.TextCtrl( self, wx.ID_ANY, u"★★★★★", wx.DefaultPosition, wx.Size( 100,-1 ), wx.TE_NO_VSCROLL|wx.TE_READONLY )
		fgSizer6.Add( self.m_textCtrl_rating, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer6.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_textCtrl_description = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,200 ), wx.TE_MULTILINE|wx.TE_READONLY )
		fgSizer6.Add( self.m_textCtrl_description, 0, wx.ALL, 5 )
		
		
		fgSizer6.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button_install = wx.Button( self, wx.ID_ANY, u"Install", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button_install, 0, wx.ALL, 5 )
		
		self.m_button_close = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button_close, 0, wx.ALL, 5 )
		
		fgSizer6.Add( bSizer1, 1, wx.EXPAND, 5 )
		
		self.SetSizer( fgSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_install.Bind( wx.EVT_BUTTON, self.m_button_install_click )
		self.m_button_close.Bind( wx.EVT_BUTTON, self.m_button_close_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_button_install_click( self, event ):
		event.Skip()
	
	def m_button_close_click( self, event ):
		event.Skip()
	

