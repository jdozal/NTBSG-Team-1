import gi
import PDMLview
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

code = [("Frame 718: frame, eth, ip, tcp", 74),
        ("   Frame 718: 74 bytes on wire (592 bits), 74 bytes captured (592 bits) on interface 0", 20),
        ("   Ethernet II, Src: Elitegro_dd:12:cd (00:19:21:dd:12:cd), Dst: Broadcom_de:ad:05 (00:10:18:de:ad:05)", 25),
        ("   Internet Control Message Protocol", 25),
        ("   Transmission Control Protocol, Src Port: 55394 (55394), Dst Port: 80, Seq: 0, Len: 0", 25),
        ("Frame 767: frame, eth, ip, tcp", 0),
        ("Frame 768: frame, eth, ip, tcp", 0),
        ("Frame 769: frame, eth, ip, tcp, http", 0)]

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
        #
        # Stack
        # stack = Gtk.Stack()
        # stack.set_transition_type(Gtk.StackTransitionType.SLIDE_DOWN)
        # stack.set_transition_duration(1000)
        #
        # state1 = Gtk.Button(label="State 1")
        # stack.add_titled(state1, "s1", "State1")
        #
        # state2 = Gtk.Button(label="State 2")
        # stack.add_titled(state2, "s2", "State2")
        #
        # # switcher
        # switcher = Gtk.StackSwitcher()
        # switcher.set_stack(stack)
        #
        workspaceLabel = Gtk.Label("Workspace X")
        # grid.add(workspaceLabel)
        # # state1Btn = Gtk.Button(label="State 1")
        # # state2Btn = Gtk.Button(label="State 2")
        #
        # grid.attach_next_to(switcher, workspaceLabel, Gtk.PositionType.BOTTOM, 1, 1)
        # grid.attach_next_to(stack, switcher, Gtk.PositionType.BOTTOM, 1, 1)


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

<<<<<<< HEAD
=======
    def pdmlDesign(self):
        pdmlViewCol = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        thisListBox = Gtk.ListBox()
        pdmlViewCol.add(thisListBox)

        # title "PDML View" area
        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        labelPDML = Gtk.Label("PDML View")
        titleBox.add(labelPDML)
        titleBox.set_child_packing(labelPDML, 1, 1, 350, 0)

        # pdml view header
        headerTab = self.pdmlHeader()

        # filter area
        filterTab = self.filterArea()

        # packet area
        packetTab = self.packetArea()

        # bottom pdml view
        #bottomTab = self.bottomArea()

        thisListBox.add(titleBox)
        thisListBox.add(headerTab)
        thisListBox.add(filterTab)
        thisListBox.add(packetTab)
        #thisListBox.add(bottomTab)

        return pdmlViewCol

    def pdmlHeader(self):
        header = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        # TODO fix spacing

        # text boxes
        newStateNameEntry = Gtk.Entry()
        renameCurrentEntry = Gtk.Entry()

        # buttons
        saveNewBtn = Gtk.Button(label="Save as New\nPDML State")
        saveCurrentBtn = Gtk.Button(label="Save Current\nPDML State")
        closeCurrentBtn = Gtk.Button(label="Close Current\nPDML State")
        deleteCurrentBtn = Gtk.Button(label="Delete Current\nPDML State")
        renameCurrentBtn = Gtk.Button(label="Rename Current\nPDML State")

        header.add(newStateNameEntry)
        header.add(saveNewBtn)
        header.add(saveCurrentBtn)
        header.add(closeCurrentBtn)
        header.add(deleteCurrentBtn)
        header.add(renameCurrentEntry)
        header.add(renameCurrentBtn)

        return header

    def filterArea(self):
        filterTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        grid = Gtk.Grid()
        filterTab.add(grid)
        lineBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        # labels
        nameLabel = Gtk.Label()
        nameLabel.set_markup("<u>Filter Area</u>")
        # nameLabel.set_justify(Gtk.Justification.LEFT)
        filterLabel = Gtk.Label("Filter")

        # buttons
        applyNewBtn = Gtk.Button("Apply")
        clearBtn = Gtk.Button("Clear")
        saveBtn = Gtk.Button("Save")
        applyFilterBtn = Gtk.Button("Apply")

        # text box (entry)
        newFilter = Gtk.Entry()

        # drop down
        # TODO HAVE TO ESTABLISH THE filters saved OF THE DROPDOWN
        savedFilters = Gtk.ComboBox()

        # adding second line into box
        lineBox.add(filterLabel)
        lineBox.pack_start(newFilter, True, True, 5)
        lineBox.pack_start(applyNewBtn, True, True, 5)
        lineBox.pack_start(clearBtn, True, True, 5)
        lineBox.pack_start(saveBtn, True, True, 5)
        lineBox.pack_start(savedFilters, True, True, 5)
        lineBox.pack_start(applyFilterBtn, True, True, 5)

        # adding to grid
        grid.add(nameLabel)
        grid.attach_next_to(lineBox, nameLabel, Gtk.PositionType.BOTTOM, 1, 1)

        return filterTab

    def packetArea(self):
        packetTab = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        grid = Gtk.Grid()
        packetTab.add(grid)

        # name of area
        nameLabel = Gtk.Label()
        nameLabel.set_markup("<u>Packet Area</u>")
        grid.add(nameLabel)

        # initializing box where packet will be
        panelGrid = Gtk.Grid()
        grid.attach_next_to(panelGrid, nameLabel, Gtk.PositionType.BOTTOM,1, 1)

        # left hand side where packet code is
        codeBox = Gtk.Box()
        panelGrid.add(codeBox)

        # Convert data to liststore (to display on treeviews)
        code_list = Gtk.ListStore(str, int)
        for item in code:
            code_list.append(list(item))

        # TreeView
        code_tree = Gtk.TreeView(code_list)

        for i, col_title in enumerate(["Frame", "Size"]):
            # how to draw the data
            renderer = Gtk.CellRendererText()

            # create columns
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # add columns
            code_tree.append_column(column)

        # add treeview
        codeBox.add(code_tree)


        # right hand side buttons
        btnBox = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        panelGrid.attach_next_to(btnBox, codeBox, Gtk.PositionType.RIGHT, 1, 1)

        removeBtn = Gtk.Button(label="Remove")
        clearBtn = Gtk.Button(label="Clear")
        btnBox.pack_end(clearBtn, True, True, 1)
        btnBox.pack_end(removeBtn, True, True, 1)


        return packetTab

>>>>>>> 4cf03bf15933f7e8b8d9c066dea8b490c6e42f09
window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()