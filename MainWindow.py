import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="NTSBG")
        self.set_border_width(10)
        #self.set_default_size(400,200)

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
        pdmlView = self.pdmlDesign()

        views.add(sessionsView)
        sessionsView.pack_start(pdmlView, True, True, 0)

        return views

    def sessionsDesign(self):
        sessionsViewCol = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)

        thisListBox = Gtk.ListBox()
        sessionsViewCol.add(thisListBox)

        # Title "Sessions View" box
        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelSessions = Gtk.Label("Sessions View")
        titleBox.add(labelSessions)
        titleBox.set_child_packing(labelSessions, 1, 1, 80, 0)

        # Sessions View tab
        sessionsTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        # Tag Area
        tagAreaTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)


        thisListBox.add(titleBox)
        thisListBox.add(sessionsTab)
        thisListBox.add(tagAreaTab)
        return sessionsViewCol

    def pdmlDesign(self):
        pdmlViewCol = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)

        thisListBox = Gtk.ListBox()
        pdmlViewCol.add(thisListBox)

        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelPDML = Gtk.Label("PDML View")
        titleBox.add(labelPDML)
        titleBox.set_child_packing(labelPDML, 1, 1, 325, 0)

        thisListBox.add(titleBox)

        return pdmlViewCol

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()