#!/usr/bin/env python
     
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
