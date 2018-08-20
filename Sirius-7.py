#главный файл игры
#строка для проверки git

#-*-coding: utf-8 -*-

import battle
import SceneLoader as SL
import random
import codecs, sys
outf = codecs.getwriter('utf-8') (sys.stdout, errors = 'replace')
sys.stdout = outf


# класс переключает сцены 
class Engine(object):

    def play(self):
        scene_name = 'first_scene'         
        person = Person()
        while scene_name != 'end':
            scene = Scene(scene_name) 
            scene_name = scene.play(person)


# персонаж и его характеристики (посещённые места, наличие оружия,
# здоровье...)
class Person(object):
    def __init__(self):
        self.Places = []

# сцена (комната). Имеет имя, текстоывй вывод, пользовательский ввод
# и набор выходов (выход - это имя следующей сцены). Также может содержать
# сражение (Battle)
class Scene(object):

    def __init__(self, scene_name):
        self.SceneName = scene_name
        self.sceneloader = SL.SceneLoader(scene_name)
        self.QuestText = self.sceneloader.GetQuestText()
        self.Exits = self.sceneloader.GetExits()
        self.IsBattle = self.sceneloader.GetBattle()

    def play(self, person):
        # вывод текста сцены
        print self.QuestText

        # сражение, если оно есть в сцене
        if self.IsBattle:
            bttl = battle.Battle()
            if bttl.play(person)==False:
                return 'end'        

        # выводим возможные выходы
        print u"\nВаши действия?"
        i=0
        for exit in self.Exits:
            i+=1
            print u"%d - %s" % (i, exit[1])

        # выбор выхода
        while True:
            try:
                action = int(raw_input("-->"))
            except:
                print u"Нельзя совершить такое действие!"
                continue
            try:
                #возвращаем имя следующей сцены
                return self.Exits[action-1][0]     
            except:
                print u"Нет выхода с таким номером!"
                continue


# основная программа
game = Engine()
game.play()
