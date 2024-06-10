import pygame                                                                                                      #Import pygame library                       
from pygame.math import Vector2                                                                                    #Import vector2     

class SNAKE:
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : init
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to make a snake
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''   
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]                                                       #Make the body of the snake with  an array of vector, start with size 3
        self.direction = Vector2(1,0)                                                                                 #Set the direcction of the snake- the head is pointed to the right side   
        self.new_block = False                                                                                        #New block variable to add when the snake eat a fruit  
                                                                                                                      
        self.head_up = pygame.image.load("sprites/head_up.png").convert_alpha()                                       #Sprite when the snake head is pointing up  
        self.head_down = pygame.image.load("sprites/head_down.png").convert_alpha()                                   #Sprite when the snake head is pointing down              
        self.head_right = pygame.image.load("sprites/head_right.png").convert_alpha()                                 #Sprite when the snake head is pointing right  
        self.head_left = pygame.image.load("sprites/head_left.png").convert_alpha()                                   #Sprite when the snake head is pointing left      
                                                                                                
        self.tail_up = pygame.image.load("sprites/tail_up.png").convert_alpha()                                       #Sprite when tail is pointing up          
        self.tail_down = pygame.image.load("sprites/tail_down.png").convert_alpha()                                   #Sprite when tail is pointing down      
        self.tail_right = pygame.image.load("sprites/tail_right.png").convert_alpha()                                 #Sprite when tail is pointing right  
        self.tail_left = pygame.image.load("sprites/tail_left.png").convert_alpha()                                   #Sprite when tail is pointing left  
        
        self.body_vertical =  pygame.image.load("sprites/body_vertical.png").convert_alpha()                          #Sprite when the snake is in a vertical position  
        self.body_horizontal =  pygame.image.load("sprites/body_horizontal.png").convert_alpha()                      #Sprite when the snake is in an horizontal position      

        self.body_tr =  pygame.image.load("sprites/body_topright.png").convert_alpha()                                #Sprite at the edge top right  
        self.body_tl =  pygame.image.load("sprites/body_topleft.png").convert_alpha()                                 #Sprite at the edge top left  
        self.body_br =  pygame.image.load("sprites/body_bottomright.png").convert_alpha()                             #Sprite at the edge bottom right  
        self.body_bl =  pygame.image.load("sprites/body_bottomleft.png").convert_alpha()                              #Sprite at the edge bottom left  

    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : draw_snake
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to make a snake
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''' 
    def draw_snake(self,screen,cell_size):
        self.update_head_sprites()                                                                                                  #Call the method to update the head sprites
        self.update_tail_sprites()                                                                                                  #Call the method to update the tail sprites
        for index,block in enumerate(self.body):                                                                                    #Iterarte through the body of the snake
            x_pos = (block.x * cell_size)                                                                                           #Get the x position    
            y_pos = (block.y * cell_size)                                                                                           #Get the y position
            block_rect = pygame.Rect(int(x_pos),int(y_pos),cell_size,cell_size)                                                     #Define a rectangle to store the block of the snake
            tail_index =len(self.body)-1                                                                                            #Get the index of the tail                                                                                            
           
            if index == 0:                                                                                                          #Check if the index is 0
                screen.blit(self.head,block_rect)                                                                                   #Blit the head    
            elif index == tail_index:                                                                                               #if the index is the tail    
                screen.blit(self.tail,block_rect)                                                                                   #Blit the tail    
            else:                                                                                                                   #In other case
                previous_position = self.body[index+1]-block                                                                        #store the previous position
                next_position = self.body[index-1]-block                                                                            #store the next position
                if previous_position.x == next_position.x:                                                                          #Check if the position in x is the same
                    screen.blit(self.body_vertical,block_rect)                                                                      #blit a vertical block
                elif previous_position.y == next_position.y:                                                                        #in case that the position is the same in y 
                    screen.blit(self.body_horizontal,block_rect)                                                                    #blit a horizontal block
                else:                                                                                                               #In other case check the edges        
                    if previous_position.x == -1 and next_position.y == -1 or previous_position.y == -1 and next_position.x == -1:  #Check if the snake is turning left to up
                        screen.blit(self.body_tl,block_rect)                                                                        #Blit the body top left sprite
                    elif previous_position.x == -1 and next_position.y == 1 or previous_position.y == 1 and next_position.x == -1:  #Check if the snake is turning left to down
                        screen.blit(self.body_bl,block_rect)                                                                        #Blit the body bottom left sprite
                    elif previous_position.x == 1 and next_position.y == -1 or previous_position.y == -1 and next_position.x == 1:  #Check if the snake is turning right to top
                        screen.blit(self.body_tr,block_rect)                                                                        #Blit the body bottom left sprite
                    elif previous_position.x == 1 and next_position.y == 1 or previous_position.y == 1 and next_position.x == 1:    #Check if the snake is turning right to top
                        screen.blit(self.body_br,block_rect)                                                                        #Blit the body bottom right sprite
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : move_snake
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to move the snake
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''' 
    def move_snake(self):
        if self.new_block == True:                                                                                                  #If the snake eat a fruit and add a new block
            body_copy = self.body[:]                                                                                                #save a copy of the body
            body_copy.insert(0, body_copy[0]+ self.direction)                                                                       #Add the direcction vector
            self.body = body_copy[:]                                                                                                #Overwrite the body 
            self.new_block = False                                                                                                  #Set new block to false
        else:                                                                                                                       #In other case
            body_copy = self.body[:-1]                                                                                              #save a copy of the body      
            body_copy.insert(0, body_copy[0]+ self.direction)                                                                       #Add the direcction to the copy
            self.body = body_copy[:]                                                                                                #Overwrite the body
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : add_block
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to add a new block
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''     
    def add_block(self):
        self.new_block = True                                                                                                       #Set new block to true
    
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : update_head_sprites
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to update the head sprites depends of the position
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''    
    
    def update_head_sprites(self):
        head_direction = self.body[1] -  self.body[0]                                                                              #Get the head direction
        if head_direction == Vector2(1,0):                                                                                         #Check if the head is pointing to left 
            self.head = self.head_left                                                                                             #Set the head left sprite 
        elif head_direction == Vector2(-1,0):                                                                                      #Check if the head is pointing to right 
            self.head = self.head_right                                                                                            #Set the head right sprite 
        elif head_direction == Vector2(0,1):                                                                                       #Check if the head is pointing up
            self.head = self.head_up                                                                                               #Set the head up sprite 
        elif head_direction == Vector2(0,-1):                                                                                      #Check if the head is pointing down 
            self.head = self.head_down                                                                                             #Set the head down sprite 
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : update_tail_sprites
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to update the tail sprites depends of the position
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-05      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''        
    def update_tail_sprites(self):
        tail_direction = self.body[-2] -  self.body[-1]                                                                            #Get tail direction 
        if tail_direction == Vector2(1,0):                                                                                         #Check if tail is pointing left 
            self.tail = self.tail_left                                                                                             #Set the tail left sprite 
        elif tail_direction == Vector2(-1,0):                                                                                      #Check if tail is pointing right  
            self.tail = self.tail_right                                                                                            #Set the tail right sprite 
        elif tail_direction == Vector2(0,1):                                                                                       #Check if tail is pointing up  
            self.tail = self.tail_up                                                                                               #Set the tail up sprite             
        elif tail_direction == Vector2(0,-1):                                                                                      #Check if tail is pointing down     
            self.tail = self.tail_down                                                                                             #Set the tail down sprite   
            