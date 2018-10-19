import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class WorkspaceLauncher(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER_ALWAYS)
        self.set_resizable(False)

        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_row_spacing(10)
        self.add(grid)

        # Labels
        mainLabel = Gtk.Label("Select a directory as workspace: NTBSG uses the workspace \n"
                              " directory to store sessions")
        labelWorkspace = Gtk.Label("Workspace")
        labelDestName = Gtk.Label("Destination Folder Name")
        labelDestPath = Gtk.Label("Destination Folder Path")

        # entries
        entryWorkspace = Gtk.Entry()
        entryWorkspace.set_placeholder_text("Workspace Directory Path")
        entryDestName = Gtk.Entry()
        entryDestName.set_placeholder_text("Destination Folder Name")
        entryDestPath = Gtk.Entry()
        entryDestPath.set_placeholder_text("Destination Folder Path")

        # buttons
        buttonBrowse1 = Gtk.Button("Browse")
        buttonBrowse2 = Gtk.Button("Browse")
        buttonCancel = Gtk.Button("Cancel")
        buttonLaunch = Gtk.Button("Launch")

        grid.attach(mainLabel, 2, 0, 1, 1)
        grid.attach(labelWorkspace, 0, 1, 1, 1)
        grid.attach(labelDestName, 0, 2, 1, 1)
        grid.attach(labelDestPath, 0, 3, 1, 1)
        grid.attach(entryWorkspace, 1, 1, 5, 1)
        grid.attach(entryDestName, 1, 2, 5, 1)
        grid.attach(entryDestPath, 1, 3, 5, 1)
        grid.attach(buttonBrowse1, 7, 1, 1, 1)
        grid.attach(buttonBrowse2, 7, 3, 1, 1)
        grid.attach(buttonLaunch, 5, 4, 1, 1)
        grid.attach(buttonCancel, 7, 4, 1, 1)


        buttonCancel.connect("clicked", self.on_destroy)
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

    # filters file options
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

win = WorkspaceLauncher()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
