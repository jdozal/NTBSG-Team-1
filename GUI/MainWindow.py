import gi
import PDMLview

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import sys
sys.path.append('../')
from Workspace import Workspace 

class MainWindow(Gtk.Window):

    currentWorkspace = Workspace("","")

    def __init__(self, workspace):
        Gtk.Window.__init__(self, title="NTSBG")
        self.currentWorkspace = workspace
        print("workspace name= " + self.currentWorkspace.name)

        self.set_border_width(10)
        # self.set_default_size(s.get_width(), s.get_height())

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
        views = self.viewsDesign(self.currentWorkspace)
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

        # Connecting buttons
        createBtn.connect("clicked", self.on_new_session_clicked)
        pcapBtn.connect("clicked", self.on_open_pcap_clicked)
        openBtn.connect("clicked", self.on_open_session_clicked)

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

    def viewsDesign(self, currentWorkspace):
        views = Gtk.ListBoxRow()

        sessionsView = self.sessionsDesign(currentWorkspace)
        self.pdml = PDMLview.PDMLview()
        pdmlView = self.pdml.pdmlDesign(currentWorkspace)
        print("THIS IS THE CURRENT LIST ALV")
        self.sessionList = self.pdml.getListSession()
        views.add(sessionsView)
        sessionsView.pack_start(pdmlView, True, True, 0)

        return views

    def sessionsDesign(self, currentWorkspace):
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
        tagAreaTab = self.tagArea(currentWorkspace)

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

        # workspaceLabel = Gtk.Button(label="Workspace X")
        # workspaceLabel.set_sensitive(False)
        # grid.add(workspaceLabel)

        self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.hbox.store = Gtk.TreeStore(str, bool)

        for i in range(len(work)):
            piter = self.hbox.store.append(None, [work[i][0], False])

            j = 1
            while j < len(work[i]):
                self.hbox.store.append(piter, work[i][j])
                j += 1

        self.view = Gtk.TreeView()
        self.view.set_model(self.hbox.store)

        renderer = Gtk.CellRendererToggle()
        column_in_size = Gtk.TreeViewColumn("", renderer, active=1)
        self.view.append_column(column_in_size)

        renderer_frame = Gtk.CellRendererText()
        column_frame = Gtk.TreeViewColumn(self.currentWorkspace.name, renderer_frame, text=0)
        self.view.append_column(column_frame)

        # initializing box where packet will be
        scroll_window = Gtk.ScrolledWindow()
        grid.add(scroll_window)

        scroll_window.add(self.view)

        scroll_window.set_min_content_width(200)
        scroll_window.set_min_content_height(200)

        return sessionsTab

    def tagArea(self, workspace):
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
        self.tagListWorkspace = workspace.tagContainer
        self.tag_store = Gtk.ListStore(str)
        for currTag in self.tagListWorkspace.tagList:
            tagStr = currTag.name
            print(tagStr)
            self.tag_store.append([tagStr])
        self.savedCombo = Gtk.ComboBox().new_with_model(self.tag_store)
        
        renderer_text = Gtk.CellRendererText()
        self.savedCombo.pack_start(renderer_text, True)
        self.savedCombo.add_attribute(renderer_text, "text", 0)

        self.savedCombo.connect("changed", self.on_tag_changed)
        
        # text boxes
        self.nameEntry = Gtk.Entry()
        self.fieldEntry = Gtk.Entry()
        self.descriptionEntry = Gtk.Entry()

        # buttons
        buttonBox = Gtk.Box()
        buttonBox.set_homogeneous(True)
        buttonBox.set_spacing(5)
        updateBtn = Gtk.Button(label="Update")
        cancelBtn = Gtk.Button(label="Cancel")
        buttonBox.pack_end(cancelBtn, True, True, 0)
        buttonBox.add(updateBtn)

        leftBox = Gtk.VBox()
        leftBox.add(savedLabel)
        leftBox.add(nameLabel)
        leftBox.add(fieldLabel)
        leftBox.add(descriptionLabel)

        rightBox = Gtk.VBox()
        rightBox.pack_start(self.savedCombo, True, True, 5)
        rightBox.pack_start(self.nameEntry, True, True, 0)
        rightBox.pack_start(self.fieldEntry, True, True, 0)
        rightBox.pack_start(self.descriptionEntry, True, True, 0)
        rightBox.pack_start(buttonBox, True, True, 0)

        # adding to grid
        grid.add(tagLabel)
        grid.attach_next_to(leftBox, tagLabel, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(rightBox, leftBox, Gtk.PositionType.RIGHT, 1, 1)


        updateBtn.connect("clicked", self.on_tag_update)

        return tagAreaTab

    def on_new_session_clicked(self, widget):
        from NewSession import NewSession
        win = NewSession()
        win.show_all()

    def on_open_pcap_clicked(self, widget):
        from OpenPCAP import OpenPCAP
        win = OpenPCAP()
        win.show_all()

    def on_open_session_clicked(self, widget):
        from OpenSession import OpenSession
        win = OpenSession()
        win.show_all()

    def on_tag_changed(self, widget):
        tree_iter = widget.get_active_iter()
        if tree_iter is not None:
            model = widget.get_model()
            currTag = model[tree_iter][0]
            print("Selected: tag=%s" % currTag)
            taglist = self.currentWorkspace.tagContainer
            self.tagObj = taglist.getTag(currTag)
            self.nameEntry.set_text(self.tagObj.name)
            self.fieldEntry.set_text(self.tagObj.field)
            self.descriptionEntry.set_text(self.tagObj.annotation)
        
    def on_tag_update(self, widget):
        currName = self.nameEntry.get_text()
        currField = self.fieldEntry.get_text()
        currAnnot = self.descriptionEntry.get_text()
        self.tagObj.name = currName
        self.tagObj.field = currField
        self.tagObj.annotation = currAnnot
        self.tag_store.clear()
        for currTag in self.tagListWorkspace.tagList:
            tagStr = currTag.name
            self.tag_store.append([tagStr])
        self.savedCombo = Gtk.ComboBox().new_with_model(self.tag_store)
        self.on_session_update()
        
    def on_session_update(self):
        
        
        work = self.pdml.getListSession()
        self.hbox.store.clear()
        for i in range(len(work)):
            piter = self.hbox.store.append(None, [work[i][0], False])

            j = 1
            while j < len(work[i]):
                self.hbox.store.append(piter, work[i][j])
                j += 1

        self.view = Gtk.TreeView()
        self.view.set_model(self.hbox.store)
    
            
work = [["Session A",
              ["State 1", False],
              ["State 2", False]],
             ["Session B", ["stage", False]],
             ["Session C", ["stage", False]]
             ]

    

# window = MainWindow(workspace)
# window.connect("destroy", Gtk.main_quit)
# window.show_all()
# # Maximize window
# window.maximize()
# Gtk.main()