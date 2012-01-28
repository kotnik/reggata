# -*- coding: utf-8 -*-
'''
Copyright 2010 Vitaly Volkov

This file is part of Reggata.

Reggata is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Reggata is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Reggata.  If not, see <http://www.gnu.org/licenses/>.

Created on 15.10.2010

@author: vlkv
'''
import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
from PyQt4.QtCore import Qt
import ui_itemdialog
from db_schema import Item, DataRef, Tag, Item_Tag, Field, Item_Field
from helpers import tr, show_exc_info, DialogMode, index_of, is_none_or_empty, \
                    is_internal
import os
from parsers import definition_parser, definition_tokens
from parsers.util import quote, unquote
import consts
from exceptions import MsgException
import helpers

class ItemDialog(QtGui.QDialog):
    '''
    Диалог для представления одного элемента хранилища
    '''

    def __init__(self, item, parent=None, mode=DialogMode.VIEW, completer=None):
        super(ItemDialog, self).__init__(parent)
        self.ui = ui_itemdialog.Ui_ItemDialog()
        self.ui.setupUi(self)
        
        self.completer = completer
        
        #Adding my custom widgets into design
        self.ui.plainTextEdit_fields = helpers.TextEdit(self, self.completer, completer_end_str=": ")
        self.ui.verticalLayout_text_edit_fields.addWidget(self.ui.plainTextEdit_fields)
        
        self.ui.plainTextEdit_tags = helpers.TextEdit(self, self.completer)
        self.ui.verticalLayout_text_edit_tags.addWidget(self.ui.plainTextEdit_tags)
        
        if type(item) != Item:
            raise TypeError(self.tr("Argument item should be an instance of Item class."))

        #parent обязательно должен быть экземпляром MainWindow
        #потому, что дальше будут обращения к полю parent.active_repo 
        if parent.__class__.__name__ != "MainWindow": 
            raise TypeError(self.tr("Parent must be an instance of MainWindow class."))
                    
        self.parent = parent
        self.mode = mode
        self.item = item        
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("accepted()"), self.button_ok)
        self.connect(self.ui.buttonBox, QtCore.SIGNAL("rejected()"), self.button_cancel)
        self.connect(self.ui.pushButton_add_files, QtCore.SIGNAL("clicked()"), self.button_add_files)
        self.connect(self.ui.pushButton_remove, QtCore.SIGNAL("clicked()"), self.button_remove)
        self.connect(self.ui.pushButton_select_dst_path, QtCore.SIGNAL("clicked()"), self.button_sel_dst_path)
        
        
#        self.ui.action_popup_compl = QtGui.QAction(self)
#        self.ui.action_popup_compl.setShortcut(QtGui.QKeySequence(self.tr("Ctrl+Space")))
#        self.ui.action_popup_compl.setShortcutContext(Qt.WidgetShortcut)
#        self.connect(self.ui.action_popup_compl, QtCore.SIGNAL("triggered()"), self.action_popup_compl)
#        self.ui.plainTextEdit_tags.addAction(self.ui.action_popup_compl)
#        
#        self.ui.text_edit = helpers.TextEdit(self, self.completer)
#        self.ui.verticalLayout_text_edit_tags.addWidget(self.ui.text_edit)
        
        self.read()
        
#    def action_popup_compl(self):
#        
#        cursor = self.ui.plainTextEdit_tags.textCursor()
#        cursor.select(QtGui.QTextCursor.WordUnderCursor)
#        word =  cursor.selectedText()
#        if is_none_or_empty(word):
#            return
#        
#        list = QtGui.QListWidget(self)
#        list.addItem(word)
#        list.addItem("456")
#        list.addItem("656")
#        list.addItem("sdfsdf")
#        list.addItem("1sdf")
#        list.addItem("1234")
#        list.addItem("12")
#        
#        rect = self.ui.plainTextEdit_tags.cursorRect()
#        point = rect.bottomLeft()
#        list.move(self.ui.plainTextEdit_tags.mapToParent(point))
#        list.show()
#        list.setFocus(Qt.PopupFocusReason)
        
    
    def read(self):
        self.ui.lineEdit_id.setText(str(self.item.id))
        self.ui.lineEdit_user_login.setText(self.item.user_login)
        self.ui.lineEdit_title.setText(self.item.title)        
        
        #Добавляем в список единственный файл
        if self.item.data_ref:
            #TODO если файл --- это архив, то на лету распаковать его и вывести в этот список все содержимое архива
            lwitem = QtGui.QListWidgetItem(self.item.data_ref.url)
            self.ui.listWidget_data_refs.addItem(lwitem)        
            #Проверяем, существует ли файл
            test_url = self.item.data_ref.url
            if not os.path.isabs(test_url):
                test_url = self.parent.active_repo.base_path + os.sep + test_url
            if not os.path.exists(test_url):
                lwitem.setTextColor(QtCore.Qt.red)
        
        #Displaying item's list of field-values
        s = ""
        for itf in self.item.item_fields:
            #Processing reserved fields
            if itf.field.name in consts.RESERVED_FIELDS:
                if itf.field.name == consts.NOTES_FIELD:
                    self.ui.plainTextEdit_notes.setPlainText(itf.field_value)
                elif itf.field.name == consts.RATING_FIELD:
                    try:
                        rating = int(itf.field_value)
                    except:
                        rating = 0
                    self.ui.spinBox_rating.setValue(rating)
                else:
                    raise MsgException(self.tr("Unknown reserved field name '{}'").format(itf.field.name))            
            #Processing all other fields
            else:
                name = quote(itf.field.name) if definition_parser.needs_quote(itf.field.name) else itf.field.name
                value = quote(itf.field_value) if definition_parser.needs_quote(itf.field_value) else itf.field_value
                s = s + name + ": " + value + os.linesep
        self.ui.plainTextEdit_fields.setPlainText(s)
        
        #Displaying item's list of tags
        s = ""
        for itg in self.item.item_tags:
            tag_name = itg.tag.name
            s = s + (quote(tag_name) if definition_parser.needs_quote(tag_name) else tag_name) + " "
        self.ui.plainTextEdit_tags.setPlainText(s)
        
        
    
    def write(self):
        '''Запись введенной в элементы gui информации в поля объекта.'''
        self.item.title = self.ui.lineEdit_title.text()
        
        #Создаем объекты Tag
        text = self.ui.plainTextEdit_tags.toPlainText()
        tags, tmp = definition_parser.parse(text)
        for t in tags:
            tag = Tag(name=t)
            item_tag = Item_Tag(tag)
            item_tag.user_login = self.item.user_login
            self.item.item_tags.append(item_tag)
        
        
        #Создаем объекты Field
        text = self.ui.plainTextEdit_fields.toPlainText()
        tmp, fields = definition_parser.parse(text)
        for (f, v) in fields:
            if f in consts.RESERVED_FIELDS:
                raise MsgException(self.tr("Field name '{}' is reserved.").format(f))
            field = Field(name=f)
            item_field = Item_Field(field, v)
            item_field.user_login = self.item.user_login
            self.item.item_fields.append(item_field)
        
        #Creating reserved fields (NOTES and RATING)
        #create NOTES_FIELD
        notes = self.ui.plainTextEdit_notes.toPlainText()
        if not is_none_or_empty(notes):
            field = Field(name=consts.NOTES_FIELD)
            item_field = Item_Field(field, notes)
            item_field.user_login = self.item.user_login
            self.item.item_fields.append(item_field)
        
        #create RATING_FIELD
        rating = self.ui.spinBox_rating.value()
        if rating > 0:
            field = Field(name=consts.RATING_FIELD)
            item_field = Item_Field(field, rating)
            item_field.user_login = self.item.user_login
            self.item.item_fields.append(item_field)
        
    def button_ok(self):
        try:
            if self.mode == DialogMode.VIEW:
                self.accept()
                
            elif self.mode == DialogMode.CREATE:
                #Очищаем коллекции тегов/полей
                #Т.к. возможно уже write() один раз вызывался, но потом check_valid() выкинул исключение
                del self.item.item_tags[:]
                del self.item.item_fields[:]
                
                self.write()
                self.item.check_valid()
                self.accept()
                
            elif self.mode == DialogMode.EDIT:
                #Очищаем коллекции тегов/полей
                del self.item.item_tags[:]
                del self.item.item_fields[:]
                
                #Метод write() создаст все необходимые теги/поля (как бы заново)
                self.write()
                self.item.check_valid()
                self.accept()
                                
        except Exception as ex:
            show_exc_info(self, ex)
    
    def button_cancel(self):
        self.reject()
        
    def button_add_files(self):
        
        #Пока что эта кнопка будет менять текущий DataRef на другой файл.
        #В будущем можно сделать выбор файлов и добавление их в архив, с которым связан данный Item
        
        file = QtGui.QFileDialog.getOpenFileName(self, self.tr("Select file"))
        if is_none_or_empty(file):
            return
        #Если lineEdit для title еще пустой, то предлагаем туда записать имя первого файла
        title = self.ui.lineEdit_title.text()
        if is_none_or_empty(title):
            self.ui.lineEdit_title.setText(os.path.basename(file))
            
        #Создаем DataRef объект и привязываем его к self.item
        data_ref = DataRef(type=DataRef.FILE, url=file)
        data_ref.dst_path = self.ui.lineEdit_dst_path.text()
        self.item.data_ref = data_ref
                        
        #Отображаем в списке файлов диалога
        self.ui.listWidget_data_refs.clear() #Удаляем все файлы, что есть сейчас
        lwitem = QtGui.QListWidgetItem(file) #Создаем и
        self.ui.listWidget_data_refs.addItem(lwitem) #добавляем новый файл в список
        
    
    def button_sel_dst_path(self):
        try:
            if self.item.data_ref is None:
                raise Exception(self.tr("You must define a data reference first."))
            
            dir = QtGui.QFileDialog.getExistingDirectory(self, 
                self.tr("Select destination path within repository"), 
                self.parent.active_repo.base_path)
            if dir:
                if not is_internal(dir, self.parent.active_repo.base_path):
                    #Выбрана директория снаружи хранилища
                    raise Exception(self.tr("Chosen directory is out of active repository."))
                else:
                    new_dst_path = os.path.relpath(dir, self.parent.active_repo.base_path)
                    self.ui.lineEdit_dst_path.setText(new_dst_path)
#                    #Присваиваем новое значение dst_path объекту DataRef, если он ссылается
#                    #на новый внешний файл (его путь абсолютный и вне хранилища)                
#                    if os.path.isabs(self.item.data_ref.url) and \
#                    not is_internal(self.item.data_ref.url, self.parent.active_repo.base_path):
#                        #Этот файл еще не в хранилище
#                        self.item.data_ref.dst_path = new_dst_path
                    self.item.data_ref.dst_path = new_dst_path
                    #Если файл self.item.data_ref уже в хранилище и в БД, то изменение 
                    #dst_path означает ПЕРЕМЕЩЕНИЕ его в другую поддиректорию внутри хранилища
                    #Если файл self.item.data_ref - новый и в хранилище и БД еще
                    #не сохранен, то dst_path - это директория, куда данный файл
                    #будет СКОПИРОВАН 
        except Exception as ex:
            show_exc_info(self, ex)
    
    def button_remove(self):
        if self.ui.listWidget_data_refs.count() == 0:
            return
        
#        sel_items = self.ui.listWidget_data_refs.selectedItems()
#        for list_item in sel_items:
#            row = self.ui.listWidget_data_refs.row(list_item)
#            self.ui.listWidget_data_refs.takeItem(row)
        self.item.data_ref = None
        self.item.data_ref_id = None
        self.ui.listWidget_data_refs.clear()
        self.ui.lineEdit_dst_path.clear()
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        