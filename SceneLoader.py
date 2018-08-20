#-*-coding: utf-8 -*-

import xml.etree.cElementTree as ET

# класс загрузки параметров сцены из xml-файла
class SceneLoader(object):

    def __init__(self, scene_name):
        self.SceneName = scene_name
        tree = ET.ElementTree(file="Sirius-7.xml")
        root = tree.getroot()
        for elem in root:
            if elem.tag=="scene" and elem.attrib['name']==self.SceneName:
                self.SceneNode = elem
                break
    
    def GetQuestText(self):
        for child in self.SceneNode:
            if child.tag=="text":
                return child.text

        text = "Что-то пошло не так"
        return text

    def GetExits(self):
        Exits = []
        for child in self.SceneNode:
            exit = []
            if child.tag == "exit":
                exit.append(child.attrib['next_scene'])
                exit.append(child.text)
                Exits.append(exit)
        return Exits

    def GetBattle(self):
        try:
            if self.SceneNode.attrib['battle']=="1":
                return True
            else:
                return False
        except:
            return False

