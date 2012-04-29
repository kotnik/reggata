import unittest
import tests_context
import os
import shutil
from repo_mgr import RepoMgr, UnitOfWork


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
        
    def getItemsMostRecentHistoryRec(self, item):
        historyRec = None
        try:
            uow = self.repo.create_unit_of_work()
            historyRec = UnitOfWork._find_item_latest_history_rec(uow.session, item)
            self.assertIsNotNone(historyRec)
        finally:
            uow.close()
        return historyRec
    
    def getExistingItem(self, id):
        try:
            uow = self.repo.create_unit_of_work()
            item = uow.getExpungedItem(id)
            self.assertIsNotNone(item)
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
        self.uow = self.repo.create_unit_of_work()

    def tearDown(self):
        self.uow.close()
        self.uow = None
        self.repo = None
        shutil.rmtree(self.copyOfRepoBasePath)

