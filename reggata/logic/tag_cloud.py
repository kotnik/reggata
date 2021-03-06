'''
Created on 08.09.2012
@author: vlkv
'''
from PyQt4 import QtCore
from reggata.logic.abstract_tool import AbstractTool
from reggata.logic.handler_signals import HandlerSignals
from reggata.gui.tag_cloud_gui import TagCloudGui


class TagCloud(AbstractTool):

    TOOL_ID = "TagCloudTool"

    def __init__(self):
        super(TagCloud, self).__init__()

        self._repo = None

        self._gui = None


    def id(self):
        return TagCloud.TOOL_ID


    def title(self):
        return self.tr("Tag Cloud")


    def createGui(self, guiParent):
        self._gui = TagCloudGui(parent=guiParent, repo=self._repo)
        return self._gui


    def __getGui(self):
        return self._gui

    gui = property(fget=__getGui)


    def handlerSignals(self):
        return [([HandlerSignals.ITEM_CHANGED,
                  HandlerSignals.ITEM_CREATED,
                  HandlerSignals.ITEM_DELETED], self._gui.refresh)]


    def setRepo(self, repo):
        self._repo = repo
        self._gui.repo = repo


    def relatedToolIds(self):
        return ["ItemsTableTool"] # Cannot reference to ItemsTable.TOOL_ID because of recursive imports...


    def connectRelatedTool(self, relatedTool):
        assert relatedTool is not None
        assert relatedTool.id() == "ItemsTableTool"

        self._connectItemsTableTool(relatedTool)


    def _connectItemsTableTool(self, itemsTable):
        self.connect(self._gui, QtCore.SIGNAL("selectedKeywordAll"),
                     itemsTable.gui.selectedKeywordAll)
        self.connect(self._gui, QtCore.SIGNAL("selectedTagsChanged"),
                     itemsTable.gui.selected_tags_changed)
        self.connect(itemsTable.gui, QtCore.SIGNAL("queryTextResetted"),
                     self._gui.reset)
