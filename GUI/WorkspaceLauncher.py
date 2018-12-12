import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import FileChooserWindow
from OpenPCAP import OpenPCAP
import Workspace

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
        entryDestName.set_text("WorkspaceFolder")
        entryDestPath = Gtk.Entry()
        entryDestPath.set_placeholder_text("Destination Folder Path")
        #print(entryWorkspace)

        # buttons
        buttonBrowse1 = Gtk.Button("Browse")
        #buttonBrowse2 = Gtk.Button("Browse")
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
        #grid.attach(buttonBrowse2, 7, 3, 1, 1)
        grid.attach(buttonLaunch, 5, 4, 1, 1)
        grid.attach(buttonCancel, 7, 4, 1, 1)


        buttonCancel.connect("clicked", self.on_destroy)
        buttonBrowse1.connect("clicked", self.on_folder_clicked, entryWorkspace, entryDestPath)
        #buttonBrowse2.connect("clicked", self.on_folder_clicked, entryDestPath)
        buttonLaunch.connect("clicked", self.on_launch_clicked, entryWorkspace.get_text(), labelWorkspace.get_text())


    def on_destroy(self, widget):
        self.destroy()

    def on_folder_clicked(self, widget, entry1, entry2):
        self.response = FileChooserWindow.on_folder_clicked(self,widget)
        entry1.set_text(self.response)
        entry2.set_text(self.response + "/Conversions")
        print("RESPONSE - " + self.response)

    def on_launch_clicked(self, widget, path, name):
        workspace = Workspace(name, path)
        win = OpenPCAP(workspace)
        win.show_all()

win = WorkspaceLauncher()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
