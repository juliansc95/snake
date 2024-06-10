import pygame,os,sys                                                                                            #Import pygame library             
from pygame.math import Vector2                                                                                 #Import vector2     
import snake
import fruit
                                                                                                                #Create some managing variables
begin = True                                                                                                    #Begin bool variable to control the first screen
BLACK = (0, 0, 0)                                                                                               #Black screen
FONT_SIZE = 20                                                                                                  #Font size constant
input_text = ''                                                                                                 #Input text string variable
error_text =''                                                                                                  #Error text string variable    
endGame = True                                                                                                  #End game boolean control
write_score = True                                                                                              #Write score boolean control

class MAIN:
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : init
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to build a snake and fruit on the game
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''  
    def __init__(self):
        self.snake = snake.SNAKE()                                                                              #Create snake object
        self.fruit = fruit.FRUIT(cell_number)                                                                   #Create fruit object            

    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : update
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to use the methods for the update cycle of the game
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''  
    def update(self):
        self.snake.move_snake()                                                                                 #Call the move snake method
        self.check_collision()                                                                                  #Call check collision method
        self.check_fail()                                                                                       #Call check fail method
    
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : draw_elements
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to use the methods for the update cycle of the game
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''      
    def draw_elements(self):
        self.draw_sand()                                                                                        #Call the draw sand method
        self.fruit.draw_fruit(screen, cell_size,apple)                                                          #Draw the fruit
        self.snake.draw_snake(screen,cell_size)                                                                 #Draw the snake        
        self.draw_score()                                                                                       #Draw the score on the game screen
    
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : draw_initial_screen
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to set the initial screen of the game
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''      
    def draw_initial_screen(self):
        initial_text = "Please enter your Initials(3 chars) and press enter key"                                           #Initial text for the user at the top of the screen
        initial_surface =  font.render(initial_text, True, BLACK)                                                               #Create a surface to pass the string        
        screen.blit(initial_surface, (0,200))                                                                                  #Blit the message on the screen
        global input_text                                                                                                       #Use the string control variables
        global error_text                                                                                                       #Use the string control variable
        text_surface = font.render(input_text, True, BLACK)                                                                     #Use a surface to render the input text on the screen
        screen.blit(text_surface, (800 // 2 - text_surface.get_width() // 2, 800 // 2 - text_surface.get_height() // 2))        #Blit the input text at the middle of the screen
        error_surface =  font.render(error_text, True, BLACK)                                                                   #Create a surface to show the error message    
        screen.blit(error_surface, (200,600))                                                                                   #Blit the error message at the down part of the screen        
    
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : handle_input
//
// Method parameters    :  self,event
//
// Method return        :  none
//
// Synopsis             :  This allow to manage the input initials of the user
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
    def handle_input(self,event):
        global input_text                                                                                                       #call the input text variable             
        global error_text                                                                                                       #call the error text variable
        global begin                                                                                                            #call the begin control boolean variable
        if event.type == pygame.KEYDOWN:                                                                                        #Check if the user use the keyboard
            if event.key == pygame.K_RETURN  and len(input_text) == 3 :                                                         #In case the user complete the 3 letters initial and press enter        
                begin = False                                                                                                   #Set begin false because the user change to game screen
            elif event.key == pygame.K_BACKSPACE:                                                                               #If the user delete a character
                input_text = input_text[:-1]                                                                                    #Erase from the chain of characters
            elif event.unicode and len(input_text) < 3 and  event.unicode != ' '  and event.unicode != '\r' and event.unicode != '\n': #Avoid blank spaces and new lines while the user typing also as much 3 characters to type
                input_text += event.unicode
            else:
                error_text ="You must type 3 letters of your initials"                                                          #In other case show a mistake message to the user    
             
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : draw_HighScore
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to draw the high score screen
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
                
    def draw_HighScore(self):
        font = pygame.font.Font(None, FONT_SIZE)                                                                                    #Set a predifine font size 20 of the constant FONT SIZE 
        score_text = "HIGH SCORE TABLE"                                                                                             #Store the string of title of the screen                                        
        score = font.render(score_text, True, BLACK)                                                                                #Render the text
        screen.blit(score,(300,100))                                                                                                #Blit the score title
        names = self.ReadScore()                                                                                                    #Store the matrix with initials and scores of the users
        for i,(name,score) in enumerate(names):                                                                                     #Iterate through the matrix    
            if i < 5:                                                                                                               #Only get the top 5 scores
                text = font.render(f"{name} {score}", True, BLACK)                                                                  #Render on the screen the name means the initials and the score
                screen.blit(text, (350,200 + i * (FONT_SIZE + 20)))                                                                 #Move up to down ordered bigger to smaller
        exit_message = "Please press ESC to close"                                                                                  #Store the string of exit message                                        
        exitR = font.render(exit_message, True, BLACK)                                                                              #Render the text
        screen.blit(exitR,(300,600))                                                                                                #Blit the exit message        
    
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : ReadScore
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to read the score file and store in a matrix ordered by score(Bigger to smaller)
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''                
    def ReadScore(self):                                                                                                             #Call the read score control variable 
        global write_score                                                                                                              
        if write_score:                                                                                                              #Check if the new score has already saved               
            self.WriteScore()                                                                                                        #In the case that is not saved - save   
            write_score = False                                                                                                      #Set the control variable to false   
        names = []                                                                                                                   #Create an empty local array variable
        if os.path.isfile("score.txt"):                                                                                              #Check the file   
            file = open("score.txt", "r")                                                                                            #Open the file and read   
            for line in file:                                                                                                        #Iterate every line of the file
                name, score = line.strip().split()                                                                                   #Store in a matrix the name and score of every player
                score = int(score)                                                                                                   #Cast the score to integer value   
                names.append([name,score])                                                                                           #Append each pair of values in the matrix  
            return sorted(names, key=lambda x: x[1], reverse= True)                                                                  #Return the array ordered
            file.close()                                                                                                             #Close the file   

    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : WriteScore
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to write a new score register for the current player
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''  
    def WriteScore(self):
        file = open("score.txt", "a")                                                                                                 #Open the file and use the append permission                  
        file.write("\n" +str(input_text)+" "+str(len(self.snake.body) - 3))                                                           #Store the initials of the player and the score      
        file.close()                                                                                                                  #Close the file                                                                                                                  
    
        
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : check_collision
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to check when the snake eat a fruit
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''          
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:                                                                                      #Check if the snake head is at the same postion of fruit
            self.fruit.randomize(cell_number)                                                                                         #In that case generate a new fruit  
            self.snake.add_block()                                                                                                    #And increase the length of the snake  
    
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : check_fail
//
// Method parameters    :  self
//
// Method return        :  boolean
//
// Synopsis             :  This allow to check when the snake crashed with the edges of the screen or by itself
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
''' 
    def check_fail(self):
        global endGame                                                                                                                 #Call the endgame control variable                  
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:                                 #Check if the snake touches the edges of the screen 
            endGame = False                                                                                                            #Set the end game control variable to false 
        for block in self.snake.body[1:]:                                                                                              #Iterate through the body of the snake 
            if block == self.snake.body[0]:                                                                                            #Check if the head of the snake crash with any other part of its body                                                                                         #Check if the snake crashes by itself 
                endGame = False                                                                                                        #Set the control variable to false 
        return endGame                                                                                                                 #Return the control variable value     
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : draw_sand
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to draw a sand pattern on the background game screen. It is like a chess board
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''   
    def draw_sand(self):
        sand_color = (194, 178, 128)                                                                                                    #Set the sand color
        for row in range(cell_number):                                                                                                  #Iterate through the rows of the screen
            if row % 2 == 0 :                                                                                                           #Conditioning to do the things in even rows only
                for column in range(cell_number):                                                                                       #Iterate through the columns of the screen
                    if column % 2 == 0 :                                                                                                #Conditioning to do the things in even columns only
                        sand_rect = pygame.Rect(column*cell_size,row*cell_size,cell_size,cell_size)                                     #Make a rectangle    
                        pygame.draw.rect(screen, sand_color, sand_rect)                                                                 #Draw the sand rectangle
            else:                                                                                                                       #In the other case
                for column in range(cell_number):                                                                                       #Iterate through the columns            
                    
                    if column % 2 != 0 :                                                                                                #Check the odd columns
                        sand_rect = pygame.Rect(column*cell_size,row*cell_size,cell_size,cell_size)                                     #Make a rectangle
                        pygame.draw.rect(screen, sand_color, sand_rect)                                                                 #Draw a sand rectangle
    '''
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// Method                : draw_score
//
// Method parameters    :  self
//
// Method return        :  none
//
// Synopsis             :  This allow to draw the score on the game screen
//
// Modifications        :
//                            Date            Developer                Notes
//                            ----            ---------                -----
//                            2023-12-06      Julian Silva            
//
// =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''   

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)                                                                                     #Calculate the score according the length of the snake -3 because the snake starts with size 3                 
        score = font.render(score_text, False, (56,74,12))                                                                             #Render the score 
        score_x = int(cell_size*cell_number - 60)                                                                                      #Set the score x position on the screen 
        score_y = int(cell_size*cell_number - 740)                                                                                     #Set the score y position on the screen 
        score_rect = score.get_rect(center = (score_x,score_y))                                                                        #Build a score rectangle 
        apple_rect = apple.get_rect(midright = (score_rect.left,score_rect.centery))                                                   #Build a fruit rectangle that shows the number of fruits that snake has eaten             
        
        background_rect = pygame.Rect(apple_rect.left,apple_rect.top,apple_rect.width + score_rect.width,apple_rect.height)            #Make a rectangle to enclosed the score and the fruit 
        
        pygame.draw.rect(screen,(194, 178, 128),background_rect)                                                                       #Draw the background rectangle
        screen.blit(score,score_rect)                                                                                                  #Blit the score number 
        screen.blit(apple,apple_rect)                                                                                                  #Blit the fruit 
        pygame.draw.rect(screen,(56,74,12),background_rect,2)                                                                          #Draw the background rectangle 
        
        
        
pygame.init()                                                                                                                          #Start the pygame
cell_size =40                                                                                                                          #Define the cell size  
cell_number=20                                                                                                                         #Define the number of cells 
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))                                                   #Build the screen 
clock = pygame.time.Clock()                                                                                                            #Start a timer 
done = True                                                                                                                            #Set the done control variable to true 
apple = pygame.image.load('sprites/apple.png').convert_alpha()                                                                         #Load the fruit 
font = pygame.font.Font('font/Orange-Style.ttf',25)                                                                                    #Load the font 

SCREEN_UPDATE = pygame.USEREVENT                                                                                                       #Define an user event variable
pygame.time.set_timer(SCREEN_UPDATE, 150)                                                                                              #Refresh the timer every 150 millisenconds 

main_game = MAIN()                                                                                                                     #Define a main object 


while done:                                                                                                                            #Game loop 
    #draw all elements
    for event in pygame.event.get():                                                                                                   #Check pygame events  
        if event.type == pygame.QUIT:                                                                                                  #If the user quit the game 
            done = False                                                                                                               #Set the control variable to false 
        if event.type == SCREEN_UPDATE and begin == False:                                                                             #Check the update method of the game 
            main_game.update()                                                                                                         #Call the game update 
        if event.type == pygame.KEYDOWN:                                                                                               #Check key events 
            if event.key == pygame.K_ESCAPE:                                                                                           #Check if the user press escape key
                pygame.quit()                                                                                                          #Quit pygame 
                sys.exit()                                                                                                             #Close the window 
            main_game.handle_input(event)                                                                                              #Manage the input initials of the player 
            if event.key == pygame.K_UP:                                                                                               #Check if the user press up key  
                if main_game.snake.direction.y != 1:                                                                                   #If the snake is not pointing up     
                    main_game.snake.direction = Vector2(0,-1)                                                                          #Send up     
            if event.key == pygame.K_DOWN:                                                                                             #Check if the user press down key 
                if main_game.snake.direction.y != -1:                                                                                  #If the snake is not pointing down      
                    main_game.snake.direction = Vector2(0,1)                                                                           #Send down 
            if event.key == pygame.K_LEFT:                                                                                             #Check if the user press left key  
                if main_game.snake.direction.x != 1:                                                                                   #If the snake is not pointing left     
                    main_game.snake.direction = Vector2(-1,0)                                                                          #Sent left 
            if event.key == pygame.K_RIGHT:                                                                                            #Check if the user press right key 
                if main_game.snake.direction.x != -1:                                                                                  #If the snake is not pointing right     
                    main_game.snake.direction = Vector2(1,0)                                                                           #Sent right  
    screen.fill((195,185,154))                                                                                                         #Fill the screen with rgb color                  
                                
    if(begin):                                                                                                                         #Screen changing, check if it is the first screen 
        main_game.draw_initial_screen()                                                                                                #Draw the initial screen 
    elif(main_game.check_fail() and  begin == False):                                                                                  #Check if it is not on the initial screen and the snake is alive 
        main_game.draw_elements()                                                                                                      #Draw the main game screen  
    else:                                                                                                                              #In other case 
        main_game.draw_HighScore()                                                                                                     #Go to highscore screen 
        
    pygame.display.update()                                                                                                            #update the screen 
    clock.tick(60)                                                                                                                     #Start the clock 