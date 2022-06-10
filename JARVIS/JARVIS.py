from logging import root
import math
import time
import os
import tkinter
import boot.tool.Load_Bar
import tkinter as tk
from openimages.download import download_dataset


class create_dir():
    def nowdir(path_txt):
        path = os.path.dirname(__file__)+path_txt
        os.makedirs(path, exist_ok=True)
        return 'dir create '+path

    def newdir(path_txt):
        os.makedirs(path_txt, exist_ok=True)
        return 'dir create '+path_txt

class Jarvis_system():
    def creat():
        boot.tool.Load_Bar.Load.now(create_dir.nowdir('\\boot'), create_dir.nowdir('\\boot\\tool'), create_dir.nowdir('\\boot\\ai'), create_dir.nowdir(
            '\\boot\\bitfleyr'), create_dir.nowdir('\\boot\\coincheck'), create_dir.nowdir('\\data'), create_dir.nowdir('\\data\\download'), create_dir.nowdir('\\data\\ai'), create_dir.nowdir('\\data\\ai\\model'))

class test():
    def window():

        frm = tkinter.Tk()
        frm.attributes('-fullscreen', True) 
        frm.title('JARVIS')
        frm.configure(bg='black')
        # 画面をそのまま表示
        frm.mainloop()

class ai_model():
    def test():
        loc = os.path.dirname(__file__) +"\\data\\ai\\model"
        labels = ["Woodpecker","Blue jay","Ostrich","Penguin","Raven","Chicken","Eagle","Owl","Duck","Canary","Goose","Swan","Falcon","Parrot","Sparrow","Turkey","Tick","Centipede","Starfish","Isopod","Squid","Jellyfish","Shrimp","Bee","Beetle","Ladybug","Ant","Caterpillar","Butterfly","Dragonfly","Scorpion","Worm","Spider","Snail","Bat (Animal)","Brown bear","Panda","Polar bear","Teddy bear","Cat","Fox","Jaguar (Animal)","Lynx","Red panda","Tiger","Lion","Dog","Leopard","Cheetah","Otter","Raccoon","Camel","Cattle","Giraffe","Rhinoceros","Goat","Horse","Hamster","Kangaroo","Koala","Mouse","Pig","Rabbit","Squirrel","Sheep","Zebra","Monkey","Hippopotamus","Deer","Elephant","Porcupine","Hedgehog","Bull","Antelope","Mule","Dolphin","Whale","Sea lion","Harbor seal","Skunk","Alpaca","Armadillo","Dinosaur","Lizard","Snake","Turtle","Tortoise","Sea turtle","Crocodile","Frog","Goldfish","Shark","Rays and skates","Seahorse","Shellfish","Oyster","Lobster","Shrimp","Crab","Person"]
        labels.sort()
        download_dataset(loc,labels, annotation_format="darknet")
    def get(model):
        loc = os.path.dirname(__file__) + "\\data\\ai\\model"
        download_dataset(loc, model, annotation_format="darknet")
        print('System Complete')

class boot:
    print('System Boot')
    print('System Diagnostics')
    Jarvis_system.creat()
    ai_model.get(["Hammer", "Gun", ])
