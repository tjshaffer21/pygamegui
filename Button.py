"""Button module allows for the existance of a Button widget within the pygame
environment.
"""

import pygame
class Button:
    _location    = [0, 0]
    _size        = [0, 0]
    _caption     = ""
    _color       = [255, 255, 255]
    _font        = [36, None, [0,0,0]]
    _event_array = []
    
    
    def __init__(self, caption, x, y, width, height):
        """pygamegui.Button.__init__(self, caption, x, y, width, height)"""
        self._location = [x,y]
        self._size     = [width, height]
        self._caption  = caption
    
    
    def draw(self, surface):
        """pygamegui.Button.draw(self, surface)
        
        Will adjust the size.
        """  

        if not pygame.font.get_init():        
            pygame.font.init()
        
        text_font = pygame.font.Font(None, self._font[0])
        ren = text_font.render( self._caption, 0, (self._font[2][0], \
            self._font[2][1], self._font[2][2]))

        # TODO: Scale font instead of resizing box
        w,h = text_font.size(self._caption)
        self._size[0] = w+10
        self._size[1] = h+10

        button = pygame.Rect(self._location[0],self._location[1], \
            self._size[0], self._size[1])
        pygame.draw.rect(surface, (self._color[0], self._color[1], \
            self._color[2]),button)
            
        surface.blit(ren, (self._location[0]+5, self._location[1]+5))
        pygame.display.update()
        pygame.font.quit()

        
    def set_location(self, x, y):
        """pygamegui.Button.set_location(self, x, y)"""
        self._location[0] = x
        self._location[1] = y

        
    def set_size(self, width, height):
        """pygamegui.Button.set_size(self, width, height)"""
        self._size[0] = width
        self._size[1] = height
        
        
    def set_caption(self, caption):
        """pygamegui.Button.set_caption(self,caption)"""
        self._caption = caption

        
    def set_background(self,r,g,b):
        """pygamegui.Button.set_background(self, r, g, b)"""
        self._color[0] = r
        self._color[1] = g
        self._color[2] = b
        
        
    def set_font(self, size, (r,g,b), font_type=None):
        """pygamegui.Button.set_font(self, size, font_type)"""
        self._font[0] = size
        self._font[1] = font_type
        self._font[2] = [r,g,b]
        
        
    def add_event(self, event, handler):
        """pygamegui.Button.add_event(self,event,handler)"""
        self._event_array.append([self,event,handler])
        
        
    def get_location(self):
        """pygamegui.Button.get_location(self):return array"""
        return self._location
        
        
    def get_size(self):
        """pygamegui.Button.get_size(self):return array"""
        return self._size
        
        
    def get_caption(self):
        """pygamegui.Button.get_caption(self):return string"""
        return self._caption
        
        
    def get_color(self):
        """pygamegui.Button.get_color(self):return array"""
        return self._color
        
        
    def get_events(self):
        """pygamegui.Button.get_events(self):return array"""
        return self._event_array
        
        
    def check_position(self, position):
        """pygamegui.Button.check_position(self,position):return bool"""
        loc = self.get_location()
        
        if (position[0] >= self._location[0] and position[0] <= \
            (self._location[0]+self._size[0])) and (position[1] >= \
            self._location[1] and position[1] <= (self._location[1] \
            + self._size[1])):
            return True
            
        return False
        
        
    def check_event(self, event):
        """pygamegui.Button.check_event(self,event):return bool"""
        for i in self._event_array:
            if i[0] == self and i[1] == event:
                return True
                
        return False

        
    def handle_event(self, event):
        """pygamegui.Button.handle_event(self,event):return bool or event"""
        for i in self._event_array:
            if i[0] == self and i[1] == event:
                return i[2]
            
        return False