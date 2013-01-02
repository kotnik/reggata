import unittest
import tests_context
import os
import shutil
from data.repo_mgr import RepoMgr
from data.db_schema import DataRef
import helpers
from data.commands import GetExpungedItemCommand, UpdateExistingItemCommand


class AbstractTestCaseWithRepo(unittest.TestCase):
    
    def setUp(self):
        self.repoBasePath = tests_context.TEST_REPO_BASE_PATH
        self.copyOfRepoBasePath = tests_context.COPY_OF_TEST_REPO_BASE_PATH
        
        if (os.path.exists(self.copyOfRepoBasePath)):
            shutil.rmtree(self.copyOfRepoBasePath)
        shutil.copytree(self.repoBasePath, self.copyOfRepoBasePath)
        
        self.repo = RepoMgr(self.copyOfRepoBasePath)

    def tearDown(self):
        self.repo = None
        shutil.rmtree(self.copyOfRepoBasePath)
    
    def getExistingItem(self, id):
        try:
            uow = self.repo.createUnitOfWork()
            item = uow.executeCommand(GetExpungedItemCommand(id))
            self.assertIsNotNone(item)
        finally:
            uow.close()
        return item
    
    def getDataRef(self, url):
        # In the case when this DataRef is a file, url should be a relative path
        try:
            uow = self.repo.createUnitOfWork()
            dataRef = uow._session.query(DataRef) \
                    .filter(DataRef.url_raw==helpers.to_db_format(url)).first()
            self.assertIsNotNone(dataRef)
        finally:
            uow.close()
        return dataRef
    
    def getDataRefById(self, id):
        '''
            Returns a DataRef object with given id or None, if DataRef object not found.
        '''
        try:
            uow = self.repo.createUnitOfWork()
            dataRef = uow._session.query(DataRef).filter(DataRef.id==id).first()
        finally:
            uow.close()
        return dataRef
    
    def updateExistingItem(self, detachedItem, user_login):
        item = None
        try:
            uow = self.repo.createUnitOfWork()
            cmd = UpdateExistingItemCommand(detachedItem, user_login)
            item = uow.executeCommand(cmd)
        finally:
            uow.close()
        return item
        


class AbstractTestCaseWithRepoAndSingleUOW(unittest.TestCase):
    
    def setUp(self):
        self.repoBasePath = tests_context.TEST_REPO_BASE_PATH
        self.copyOfRepoBasePath = tests_context.COPY_OF_TEST_REPO_BASE_PATH
        
        if (os.path.exists(self.copyOfRepoBasePath)):
            shutil.rmtree(self.copyOfRepoBasePath)
        shutil.copytree(self.repoBasePath, self.copyOfRepoBasePath)
        
        self.repo = RepoMgr(self.copyOfRepoBasePath)
        self.uow = self.repo.createUnitOfWork()

    def tearDown(self):
        self.uow.close()
        self.uow = None
        self.repo = None
        shutil.rmtree(self.copyOfRepoBasePath)
