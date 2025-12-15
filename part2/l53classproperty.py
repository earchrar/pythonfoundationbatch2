class classproperty:
    def __init__(self,func): # stored the function 
        self.func = func 
    
    def __get__(self,obj,cls=None): # makes it work like a property ( no () method )
        return self.func(cls)

class Greet: 
    # greeting = "Hello Mandalay!" # work
    _greeting = "Hello Mandalay!"

    @classproperty
    def sayhi(cls):
        return cls._greeting
        # return cls.greeting # work

print(Greet.sayhi)

# Method override in Subclass 

class SocialMedia:
    @classproperty
    def category(cls):
        return "Generic Social Perform"

class Facebook(SocialMedia):
    @classproperty
    def category(cls):
        return "Social Network"

class Youtube(SocialMedia):
    @classproperty
    def category(cls):
        return "Video Sharing"

print(SocialMedia.category) # Generic Social Perform
print(Facebook.category) # Social Network
print(Youtube.category) # Video Sharing