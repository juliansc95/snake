import pygame,random                                                                                                        #Import pygame library and random    
from pygame.math import Vector2                                                                                             #Import vector2

class FRUIT:                                                                                                                #Define class fruit
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : init
//
// Method parameters    :  self,cell_number
//
// Method return        :  none
//
// Synopsis             :  This allow to use the random function to show the fruit
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
    def __init__(self,cell_number):
        self.randomize(cell_number)                                                                                         #call the randomize function
        
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : draw_fruit
//
// Method parameters    :  self,screen, cell_size,fruit_sprite
//
// Method return        :  none
//
// Synopsis             :  This allow to draw the fruit on the screen
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''    
    def draw_fruit(self,screen, cell_size,fruit_sprite):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size) ,int(self.pos.y * cell_size),cell_size,cell_size)              #Make a rectangle to upload the fruit
        screen.blit(fruit_sprite,fruit_rect)                                                                                #Blit the fruit on the screen

    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : randomize
//
// Method parameters    :  self,cell_number
//
// Method return        :  none
//
// Synopsis             :  This allow to make a random method to locate the fruit on the screen
// References           :random — Generate pseudo-random numbers. (n.d.). Python Documentation. https://docs.python.org/3/library/random.html
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''    
    def randomize(self,cell_number):
        self.x = random.randint(0,cell_number-1)                                                                            #Make a random position in x
        self.y = random.randint(0,cell_number-1)                                                                            #Make a random position in y            
        self.pos = Vector2(self.x,self.y)                                                                                   #Store the vector with x and y position
        