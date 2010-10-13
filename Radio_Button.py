import pygame
import Label
class Radio_Button:
    _button_loc = None
    _location   = None
    _size       = [0,0]
    _caption    = ""
    _font       = [16, "Times New Romans", [0,0,0]]
    _color      = [255,255,255]
    _button_clr = [0,0,0]
    _radius     = 5
    _event_array = []

    
    def __init__(self, caption, x, y, width=100, height=100, radius=5):
        """pygamegui.Radio_Button.__init__(self, caption, x, y, width=100, 
           height=100, radius=5)"""
        self._location = [x,y]
        self._size     = [width, height]
        self._caption  = caption
        self.add_event( "on_click", "_on_click" )
    
    
    def draw(self, surface):
        """pygamegui.Radio_Button.draw(self, surface)
        
        Will adjust the size.
        """  

        pygame.draw.circle( surface, (self._button_clr[0],self._button_clr[1], \
            self._button_clr[2]), (self._location[0], self._location[1]), \
            self._radius, 0)

        button_label = Label.Label(self._caption, self._location[0]+ \
            (self._radius*2), self._location[1]-(self._radius), \
            self._size[0]-5, self._size[1]-5)
        button_label.set_font(self._font[0], (self._font[2][0], \
            self._font[2][1], self._font[2][2]), self._font[1])
        button_label.set_background(self._color[0], self._color[1], \
            self._color[2])
        button_label.draw(surface)

        
    def set_location(self, x, y):
        """pygamegui.Radio_Button.set_location(self, x, y)"""
        self._location[0] = x
        self._location[1] = y

        
    def set_size(self, width, height):
        """pygamegui.Radio_Button.set_size(self, width, height)"""
        self._size[0] = width
        self._size[1] = height
        
        
    def set_caption(self, caption):
        """pygamegui.Radio_Button.set_caption(self,caption)"""
        self._caption = caption

        
    def set_button_color(self,r=255,g=255,b=255):
        """pygamegui.Radio_Button.set_button_color(self, r, g, b)"""
        self._button_clr[0] = r
        self._button_clr[1] = g
        self._button_clr[2] = b
        
        
    def set_font(self, size=16, (r,g,b)=(255,255,255), font_type="Times New Romans"):
        """pygamegui.Radio_Button.set_font(self, size, font_type)"""
        self._font[0] = size
        self._font[1] = font_type
        self._font[2] = [r,g,b]
        
        
    def add_event(self, event, handler):
        """pygamegui.Radio_Button.add_event(self,event,handler)"""
        self._event_array.append([event,handler])
        
        
    def get_location(self):
        """pygamegui.Radio_Button.get_location(self):return array"""
        return self._location
        
        
    def get_size(self):
        """pygamegui.Radio_Button.get_size(self):return array"""
        return self._size
        
        
    def get_caption(self):
        """pygamegui.Radio_Button.get_caption(self):return string"""
        return self._caption
        
        
    def get_color(self):
        """pygamegui.Radio_Button.get_color(self):return array"""
        return self._color
        
        
    def get_events(self):
        """pygamegui.Radio_Button.get_events(self):return array"""
        return self._event_array
        
        
    def check_position(self, position):
        """pygamegui.Radio_Button.check_position(self,position):return bool"""
        loc = self.get_location()
        
        if (position[0] >= loc[0] and position[0] <= self._size[0]) and \
           (position[1] >= loc[1] and position[1] <= self._size[1]):
            return True
            
        return False
        
        
    def check_event(self, event):
        """pygamegui.Radio_Button.check_event(self,event):return bool"""
        for i in self._event_array:
            if i[0] == event:
                if i[0] == "on_click":
                    getattr(self, _on_click)()
                else:
                    return True
                
        return False

        
    def handle_event(self, event):
        """pygamegui.Radio_Button.handle_event(self,event)"""
        for i in self._event_array:
            if i[0] == event:
                return i[1]
            
        return False
        
    def _on_click(self):
        j = 0
        for i in self._button_clr:
            if i > 100:
                color[j] = 0
            else:
                color[j] = 255
            
            j += 1
            
        pygame.draw.circle( surface, (color[0],color[1], color[2]), \
            (self._location[0], self._location[1]), \
            self._radius, 0)