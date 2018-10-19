import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')


class TagOverlay(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Tag Overlay")
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_resizable(False)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        # Labels
        mainLabel = Gtk.Label("Tag Overlay")
        labelTagName = Gtk.Label("Tag Name")
        labelTaggedField = Gtk.Label("Tagged Field")
        labelTagDescription = Gtk.Label("Tag Description")
        blankTag = Gtk.Label(" ")

        # entries
        entryTagName = Gtk.Entry()
        entryTagName.set_placeholder_text("Tag Name")
        entryTaggedField = Gtk.Entry()
        entryTaggedField.set_placeholder_text("Tagged Field Name")
        entryTagDescription = Gtk.Entry()
        entryTagDescription.set_placeholder_text("Tag Description")
        entryTagDescription.set_max_length(500)



        buttonSave = Gtk.Button("Save")
        buttonCancel = Gtk.Button("Cancel")
        buttonCancel.connect("clicked", self.on_destroy)

        grid.attach(mainLabel, 15, 0, 1, 1)
        grid.attach(labelTagName, 0, 1, 1, 1)
        grid.attach(labelTaggedField, 0, 2, 1, 1)
        grid.attach(labelTagDescription, 0, 3, 1, 1)

        grid.attach(blankTag, 0, 4, 1, 1)

        grid.attach(entryTagName, 1, 1, 20, 1)
        grid.attach(entryTaggedField, 1, 2, 20, 1)
        grid.attach(entryTagDescription, 1, 3, 20, 1)
        grid.attach(buttonSave, 19, 4, 1, 1)
        grid.attach(buttonCancel, 20, 4, 1, 1)

    def on_destroy(self, widget):
        self.destroy()


win = TagOverlay()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()