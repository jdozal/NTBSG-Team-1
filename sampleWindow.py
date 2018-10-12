import pgi
pgi.require_version("Gtk", "3.0")
from pgi.repository import Gtk

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()