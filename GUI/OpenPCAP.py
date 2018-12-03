import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import FileChooserWindow

import sys
import PCAPtoPDMLController

response = ''

# entries 
entryPcapName = Gtk.Entry()
entryDissectorName = Gtk.Entry()

class OpenPCAP(Gtk.Window):
    

    def __init__(self):
        Gtk.Window.__init__(self, title="PCAP")
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_resizable(False)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        # Labels
        mainLabel = Gtk.Label("Open a PCAP File")
        labelPcapName = Gtk.Label("PCAP Name")
        labelDissectorName = Gtk.Label("Dissector Name")

        # entries
        entryPcapName.set_placeholder_text("PCAP File")
        entryDissectorName.set_placeholder_text("Optional Dissector")

        # buttons
        buttonBrowse1 = Gtk.Button("Browse")
        buttonBrowse2 = Gtk.Button("Browse")
        buttonCancel = Gtk.Button("Cancel")
        buttonConvert = Gtk.Button("Convert to PDML")
        buttonCancel.connect("clicked", self.on_destroy)

        grid.attach(mainLabel, 13, 0, 1, 1)
        grid.attach(labelPcapName, 0, 1, 1, 1)
        grid.attach(labelDissectorName, 0, 2, 1, 1)
        grid.attach(entryPcapName, 1, 1, 15, 1)
        grid.attach(entryDissectorName, 1, 2, 15, 1)
        grid.attach(buttonBrowse1, 18, 1, 1, 1)
        grid.attach(buttonBrowse2, 18, 2, 1, 1)
        grid.attach(buttonConvert, 15, 3, 1, 1)
        grid.attach(buttonCancel, 18, 3, 1, 1)

        buttonBrowse1.connect("clicked", self.on_file_clicked)
        buttonBrowse2.connect("clicked", self.on_file_clicked)
        buttonCancel.connect("clicked", self.on_destroy)
        buttonConvert.connect("clicked", self.on_convert)


    def on_destroy(self, widget):
        self.destroy()

    def on_file_clicked(self,widget):
        response = FileChooserWindow.on_file_clicked(self,widget)
        
        # Trying to have "all files" as default when opening file chooser
        #filefilter = gtk.FileFilter()
        #filefilter.set_name("All Files")


        entryPcapName.set_text(response)
        print("RESPONSE - " + response)
        
    def on_convert(self, widget):
        pathPCAP = entryPcapName.get_text()
        dissector = entryDissectorName.get_text()
        print(pathPCAP)
        if(pathPCAP == '' or pathPCAP == "Missing PCAP File"):
            entryPcapName.set_text("Missing PCAP File")
        else:
            print(pathPCAP)
            print(dissector)
            self.controller = PCAPtoPDMLController.PCAPtoPDMLController()
            self.controller.setPCAP(pathPCAP)
            self.controller.callConversion()
            self.destroy()
            
            
            
        
        
        
win = OpenPCAP()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
