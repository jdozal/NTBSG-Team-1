import gi
import PDMLview
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="NTSBG")
        self.set_border_width(10)
        self.set_default_size(1100,200)

        # initialize header bar
        header = self.header()

        # initialize listbox design
        listMain = Gtk.ListBox()
        listMain.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listMain)

        # initialize stages buttons
        stages = self.stagesButtons()
        listMain.add(stages)

        # initialize views
        views = self.viewsDesign()
        listMain.add(views)

    def header(self):
        hb = Gtk.HeaderBar()
        hb.props.title = "Network Traffic Based Software Generation"
        self.set_titlebar(hb)

        # title = Gtk.Label()
        # title.set_markup("Network Traffic Based Software Generation")

        button = Gtk.Button(label="x")
        button.set_relief(Gtk.ReliefStyle.NONE)
        button.connect("clicked", Gtk.main_quit)
        hb.pack_end(button)

        buttonBox = self.menuBox()
        hb.pack_end(buttonBox)

        return hb

    def menuBox(self):
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(buttonBox.get_style_context(), "linked")
        buttonBox.set_spacing(10)

        # init Header Buttons Menu
        createBtn = Gtk.Button(label="Create Session")
        openBtn = Gtk.Button(label="Open Session")
        closeBtn = Gtk.Button(label="Close Session")
        switchBtn = Gtk.Button(label="Switch Workspace")
        pcapBtn = Gtk.Button(label="Open PCAP")
        terminalBtn = Gtk.Button(label="Terminal")

        buttonBox.add(createBtn)
        buttonBox.add(openBtn)
        buttonBox.add(closeBtn)
        buttonBox.add(switchBtn)
        buttonBox.add(pcapBtn)
        buttonBox.add(terminalBtn)

        return buttonBox

    def stagesButtons(self):
        stages = Gtk.ListBoxRow()

        # initialize stages section
        stage1 = Gtk.Button(label="Stage 1: Configuration and Setup")
        stage2 = Gtk.Button(label="Stage 2: Message Analysis")
        stage3 = Gtk.Button(label="Stage 3: Sequencing")
        stage4 = Gtk.Button(label="Stage 4: Code Generation")

        stageBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(stageBox.get_style_context(), "linked")
        stageBox.set_homogeneous(True)
        stageBox.set_spacing(10)

        stageBox.add(stage1)
        stageBox.add(stage2)
        stageBox.add(stage3)
        stageBox.add(stage4)

        stages.add(stageBox)

        return stages

    def viewsDesign(self):
        views = Gtk.ListBoxRow()

        sessionsView = self.sessionsDesign()
        pdmlView = PDMLview.pdmlDesign()

        views.add(sessionsView)
        sessionsView.pack_start(pdmlView, True, True, 0)

        return views

    def sessionsDesign(self):
        sessionsViewCol = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        thisListBox = Gtk.ListBox()
        sessionsViewCol.add(thisListBox)

        # Title "Sessions View" box
        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelSessions = Gtk.Label("Sessions View")
        titleBox.add(labelSessions)
        titleBox.set_child_packing(labelSessions, 1, 1, 80, 0)

        # Sessions View tab
        sessionsTab = self.sessionsArea()

        # Tag Area
        tagAreaTab = self.tagArea()

        thisListBox.add(titleBox)
        thisListBox.add(sessionsTab)
        thisListBox.add(tagAreaTab)

        return sessionsViewCol

    def sessionsArea(self):
        sessionsTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        # TODO DON'T KNOW HOW TO DO SESSIONS HELP

        grid = Gtk.Grid()
        sessionsTab.add(grid)
        grid.set_row_spacing(5)

        workspaceLabel = Gtk.Label("Workspace X")
        sessionA = Gtk.Label("Session A")
        state1 = Gtk.Label("State 1")
        state2 = Gtk.Label("State 2")
        sessionB = Gtk.Label("Session B")
        sessionC = Gtk.Label("Session C")

        grid.add(workspaceLabel)
        grid.attach_next_to(sessionA, workspaceLabel, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(state1, sessionA, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(state2, state1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(sessionB, state2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(sessionC, sessionB, Gtk.PositionType.BOTTOM, 1, 1)

        return sessionsTab

    def tagArea(self):
        tagAreaTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        grid = Gtk.Grid()
        tagAreaTab.add(grid)
        grid.set_column_spacing(10)
        grid.set_row_spacing(5)

        # title
        tagLabel = Gtk.Label()
        tagLabel.set_markup("<u>Tag Area</u>")

        # labels
        savedLabel = Gtk.Label("Saved Tag")
        nameLabel = Gtk.Label("Tag Name")
        fieldLabel = Gtk.Label("Tag Field")
        descriptionLabel = Gtk.Label("Tag Description")

        # drop down menu
        # TODO HAVE TO ESTABLISH THE INSIDE OF THE DROPDOWN
        savedCombo = Gtk.ComboBox()

        # text boxes
        nameEntry = Gtk.Entry()
        fieldEntry = Gtk.Entry()
        descriptionEntry = Gtk.Entry()

        # buttons
        buttonBox = Gtk.Box()
        buttonBox.set_homogeneous(True)
        buttonBox.set_spacing(5)
        updateBtn = Gtk.Button(label="Update")
        cancelBtn = Gtk.Button(label="Cancel")
        buttonBox.pack_end(cancelBtn, True, True, 0)
        buttonBox.add(updateBtn)

        #adding to grid
        grid.add(tagLabel)
        grid.attach_next_to(savedLabel, tagLabel, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(savedCombo, savedLabel, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(nameLabel, savedLabel, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(nameEntry, nameLabel, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(fieldLabel, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(fieldEntry, fieldLabel, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(descriptionLabel, fieldLabel, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(descriptionEntry, descriptionLabel, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(buttonBox, descriptionEntry, Gtk.PositionType.BOTTOM, 1, 1)

        return tagAreaTab

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()