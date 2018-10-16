import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class WorkspaceLauncher(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="NTSBG")
        self.set_border_width(10)
        self.set_default_size(510, 200)

    def pdmlDesign(self):
        labelPDML = Gtk.Label("PDML View")

window = WorkspaceLauncher()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()