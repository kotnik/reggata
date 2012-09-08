'''
Created on 07.09.2012
@author: vlkv
'''
from user_config import UserConfig
from data.commands import LoginUserCommand
from errors import MsgException

class AbstractMainWindowModel(object):
    '''
        This is a declarative base class for MainWindowModel, 
    just to be able to quickly find all it's descendants.
    '''
    pass


class MainWindowModel(AbstractMainWindowModel):
    
    def __init__(self, mainWindow, repo, user):
        self._repo = repo
        self._user = user
        self._mainWindow = mainWindow
        self._tools = []
    
    
    def addTool(self, tool):
        self._tools.append(tool)
        
    def tools(self):
        return self._tools
    
    def toolById(self, toolId):
        foundTools = [tool for tool in self._tools if tool.id() == toolId]
        
        if len(foundTools) == 0:
            return None
        
        assert len(foundTools) == 1, "Tool id=%s is not unique!" % str(toolId)
        return foundTools[0]
    
    
    def __get_repo(self):
        return self._repo
    
    def __set_repo(self, repo):
        self._repo = repo
        self._mainWindow.onCurrentRepoChanged()
        for tool in self._tools:
            tool.setRepo(repo)
    
    repo = property(fget=__get_repo, fset=__set_repo)
        
        
    def __get_user(self):
        return self._user
    
    def __set_user(self, user):
        self._user = user
        self._mainWindow.onCurrentUserChanged()
        for tool in self._tools:
            tool.setUser(user)
    
    user = property(fget=__get_user, fset=__set_user)
    
    
    def loginRecentUser(self):
        login = UserConfig().get("recent_user.login")
        password = UserConfig().get("recent_user.password")
        self.loginUser(login, password)
        
        
    def loginUser(self, login, password):
        self.checkActiveRepoIsNotNone()
        
        uow = self._repo.createUnitOfWork()
        try:
            user = uow.executeCommand(LoginUserCommand(login, password))
            self.user = user
        finally:
            uow.close()


    def checkActiveRepoIsNotNone(self):
        if self._repo is None:
            raise MsgException(self.tr("Open a repository first."))
    
            
    def checkActiveUserIsNotNone(self):
        if self._user is None:
            raise MsgException(self.tr("Login to a repository first."))
        
    
    def restoreRecentState(self):
        
        #TODO: here we should restore recent user and recent repo
    
        for tool in self._tools:
            tool.restoreRecentState()
        