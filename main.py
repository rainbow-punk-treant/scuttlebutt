import os
import sys
import pygame
import subprocess

from distutils.core import setup



class Joystick():
   
    pygame.init()
    pygame.joystick.init()
    def detectButton(self, stick):
        if stick.get_init():
            for event in pygame.event.get():
                if event.type == pygame.JOYBUTTONDOWN:
                    for button in range(stick.get_numbuttons()):
                        butt = stick.get_button(button)
                        # if butt == 1:
                            # print("button"+str(button)+" down")
                        
                if event.type == pygame.JOYBUTTONUP:
                    for button in range(stick.get_numbuttons()):
                        butt = stick.get_button(button)
                        
                        # print("button"+str(button)+" up")
                        if butt == 0 and button == 0:
                            subprocess.run('/usr/bin/yell')
                            print("\x1b[48;2;20;50;20mRAWR\x1b[0m")
                            #sys.exit(1) 
        else:
            sys.exit(1)               

    def showButtons(self):

        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        for stick in joysticks:
            uid = stick.get_guid()
            # print(uid)
            
                # stick.init()
                # print("NUMBER OF BUTTONS::"+str(stick.get_numbuttons()))
                # #print(stick.get_name())
                # print("NUMBER OF hats::"+str(stick.get_numhats()))

                # print("number ")
                # # for event in pygame.event.get():
                # # if event.type == pygame.JOYBUTTONDOWN:
            return stick
joy = Joystick()

stick = joy.showButtons()
while True:
    joy.detectButton(stick)
