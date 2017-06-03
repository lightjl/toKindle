#!usr/bin/env
# -*-coding:utf-8 -*-
import os
import codecs


class saveToFile():
    def __init__(self, fold):
        self.sub_folder = os.path.join(os.getcwd(), "/saveFile/" + fold + "/")
        if not os.path.exists(self.sub_folder):
            os.mkdir(self.sub_folder)

    def save(self, filename, text):
        self.__filename = self.sub_folder + filename + ".txt"
        #print(self.__filename)
        f = codecs.open(self.__filename, "a", "utf-8")
        f.write(text)
        f.close()

    def isDownloaded(self, filename):
        filename2 = self.sub_folder + filename + ".txt"
        #print(filename2)
        return os.path.isfile(self.sub_folder + filename + ".txt")  # 如果不存在就返回False
        pass
