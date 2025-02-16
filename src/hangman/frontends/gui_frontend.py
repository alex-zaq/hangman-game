import pygame

from ..backend import MAX_WRONG_LETTERS_COUNT, GameStatus
from .stages import hangman_stages


class GuiFrontend():


    def show_start_menu(self):
        pygame.init()
        
        WIDTH, HEIGHT = 600, 480
        WHITE = (255, 255, 255)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font(None, 36)


        text = self.font.render("Wrong guesses:", True, (0, 0, 0))
        self.screen.blit(text, (10, 240))
        self.screen.fill(WHITE)

        width, height = pygame.display.get_surface().get_size()
        self._draw_button("New Game", x = 40, y = height - 100)
        self._draw_button("Exit", x = width - 250 , y = height - 100)
        pygame.display.flip()


    def set_state(self, state):
        self.state = state


    def read_keys_menu(self):
        key = ""
        while key not in ("n", "q"):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 10 <= event.pos[0] <= 210 and 400 <= event.pos[1] <= 450:
                        key =  "n" 
                    elif 350 <= event.pos[0] <= 350 + 200 and 380 <= event.pos[1] <= 380 + 50:
                        key = "q"
                        
        return key
                        
    
    
    def read_keys(self):
        key = ""
        
        while key == "":
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = event.unicode.lower()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 10 <= event.pos[0] <= 210 and 400 <= event.pos[1] <= 450:
                        key = "n" 
                    elif 350 <= event.pos[0] <= 350 + 200 and 380 <= event.pos[1] <= 380 + 50:
                        key = "q"
                        
        return key
    
    
    def _draw_hangman(self,stage):
        rect = pygame.Rect(10 + 170, 10, 200, 200)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        
        lines = hangman_stages[stage].split('\n')
        for i, line in enumerate(lines):
            text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(text, (170, 10 + i * 20))
        pygame.display.flip()
    
    
    def _draw_button(self,text, x, y):
        button_rect = pygame.Rect(x, y, 200, 50) 
        pygame.draw.rect(self.screen, (0, 0, 255), button_rect)
        text = self.font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect(center=button_rect.center)  
        self.screen.blit(text, text_rect.topleft)
        pygame.display.flip()


    def _get_str_words(self):
        orig_word = self.state.chosen_word
        res = [orig_letter if letter == "+" else "_" for orig_letter, letter in zip(orig_word, self.state.word_lst)]
               
        if self.state.game_status in (GameStatus.LOSE, GameStatus.WIN):
            res = [orig_letter for orig_letter in orig_word]
            
        return " ".join(res)


    def draw(self):
        self._draw_hangman(self.state.wrong_letters_count)
        
        
        rect = pygame.Rect(0, 220, 600, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        res = self._get_str_words()
        text = self.font.render(res, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(text, text_rect.topleft)
        pygame.display.flip() 
        
   
        rect = pygame.Rect(0, 270, 600, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        res = f"Wrong guesses: {self.state.wrong_letters_count} / {MAX_WRONG_LETTERS_COUNT}"
        text = self.font.render(res, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery + 60))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        
        
        rect = pygame.Rect(0, 330, 600, 50)
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        res = self._get_str_game_over()
        text = self.font.render(res, True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_rect().centerx, self.screen.get_rect().centery + 110))
        self.screen.blit(text, text_rect)
        pygame.display.flip()
        
        
        
    def _get_str_game_over(self):
        match self.state.game_status:
            case GameStatus.LOSE:
                return "".join("You lose!")
            case GameStatus.WIN:
                return "".join("You win!")
            case GameStatus.IN_PROGRESS:
                return ""

    def stop(self):
        pygame.quit()
