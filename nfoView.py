#!/usr/bin/python3

# Copyright 2012 Johannes Hamberg
#
# This file is part of nfoView.
#
# nfoView is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# nfoView is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with nfoView.  If not, see <http://www.gnu.org/licenses/>.


import sys
import os.path
from gi.repository import Gtk





class nfoView():

    # signals from window_main
    def on_window_main_destroy(self, widget, data=None):
        Gtk.main_quit()

    # signals from window_main
    def on_menuitem_open_activate(self, widget, data=None):
        self.window_file.show()

    def on_menuitem_quit_activate(self, widget, data=None):
        Gtk.main_quit()

    def on_menuitem_about_activate(self, widget):
       self.window_about.show()

    # signals from window_file
    def on_file_open_clicked(self, widget, data=None):
        uri = self.window_file.get_filename()
        fil = open(uri, "r")
        self.text_buffer.set_text(fil.read())
        self.text_view.set_buffer(self.text_buffer)
        self.window_file.hide()

    def on_window_file_activated(self, widget, data=None):
        uri = self.window_file.get_filename()
        fil = open(uri, "r")
        self.text_buffer.set_text(fil.read())
        self.text_view.set_buffer(self.text_buffer)
        self.window_file.hide()

    def on_file_cancel_clicked(self, widget, data=None):
        self.window_file.hide()

    def on_window_file_delete_event(self, widget, data=None):
        self.window_file.hide()
        return(True)

    # signals from window_about
    def on_window_about_response(self, widget, data=None):
        self.window_about.hide()

    def on_window_about_delete_event(self, widget, data=None):
        self.window_about.hide()
        return(True)






    def __init__(self):

        # set execution directory to base_uri
        base_uri = os.path.dirname(__file__)

        # make builder object
        self.builder = Gtk.Builder()
        self.builder.add_from_file(base_uri+"/nfoView.glade")

        # get widgets from builder object
        self.window_main = self.builder.get_object("window_main")
        self.window_about = self.builder.get_object("window_about")
        self.window_file = self.builder.get_object("window_file")

        #self.window_about.show()
        self.text_view = self.builder.get_object("text_view")


        # conect signals
        self.builder.connect_signals(self)

        # creats a text buffer object text_buffer
        self.text_buffer = Gtk.TextBuffer()

        # sets the initial text to text_buffer and set the text buffer to text_view
        if len(sys.argv)>=2 and os.path.isfile(sys.argv[1]):
            fil = open(sys.argv[1], "r")
        else:
            fil = open(base_uri+'/start.nfo', "r")
        self.text_buffer.set_text(fil.read())
        fil.close()
        self.text_view.set_buffer(self.text_buffer)

        #   runs the gtk main loop
        Gtk.main()


if __name__ == "__main__":
    # initialises a nfoView object
    app = nfoView()


