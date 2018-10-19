import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


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
        entryPcapName = Gtk.Entry()
        entryPcapName.set_placeholder_text("PCAP File")
        entryDissectorName = Gtk.Entry()
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

        buttonBrowse1.connect("clicked", self.on_open_clicked)
        buttonBrowse2.connect("clicked", self.on_open_clicked)
        buttonCancel.connect("clicked", self.on_destroy)


    def on_destroy(self, widget):
        self.destroy()

    def on_open_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Select file", self,
                                       Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        dialog.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.add_filters(dialog)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("File selected: " + dialog.get_filename())
            dialog.destroy()

        dialog.destroy()

    # Add filters to the open file directory to show all files
    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)
        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)
        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

win = OpenPCAP()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
