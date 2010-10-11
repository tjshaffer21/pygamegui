"""Object_Container holds GUI objects. It is used to check if an event is
interacting with a widget.
"""
class Object_Container:
    _objects = None
    
    def __init__(self):
        self._objects = []
    
    def add_object(self,object):
        """pygamegui.Object_Container.add_object(self,object)"""
        self._objects.append(object)
        
    def remove_object(self,object):
        """pygamegui.Object_Container.remove_object(self,object): return bool"""
        for i in self._objects:
            if i == object:
                self._objects.remove(object)
                return True
                
        return False
        
    def contains(self,object):
        """pygamegui.Object_Container.contains(self,object): return bool"""
        for i in self._objects:
            if i == object:
                return True
                
        return False
        
    def check_objects(self, position, event):
        """pygamegui.Object_Container.check_objects(self, position, event)"""
        for i in self._objects:
            if i.check_position(position):
                if i.check_event(event):
                    return i.handle_event(event)
                    
        return False