#!/usr/bin/env python

#Copyright (C) 2011-2012  A. Felipe Cabargas M. <felipe.cabargas@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, WebKit
import os, sys

UI_FILE = "centaurus.ui"

class Navegador:
	def __init__(self):
		self.builder = Gtk.Builder()
        	self.builder.add_from_file(UI_FILE)
	        self.builder.connect_signals(self)
	
        	self.back = self.builder.get_object("back")
        	self.forward = self.builder.get_object("next")
        	self.url = self.builder.get_object("url")
     	
        	self.webview = WebKit.WebView()
        	scrolled_window = self.builder.get_object("scrolledwindow")
        	scrolled_window.add(self.webview)
	
			#self.webview.connect("titulo-cambiado", self.on_title_changed)
			#self.webview.connect("icono-cambiado", self.on_icon_loaded)
			#self.webview.connect("carga-finalizada", self.on_load_finished)

        	self.window = self.builder.get_object("window")
        	self.window.show_all()

	def on_direccion_activate(self, widget):
		url = widget.get_text()
		if not "http://" in url:
			url = "http://" + url
		self.webview.load_uri(url)

	def destroy(self, window):
		Gtk.main_quit()

def main():
    app = Navegador()
    Gtk.main()

if __name__ == "__main__":
    main()