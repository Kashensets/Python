class Song:
    def __init__(self, title='', author='', lyrics=()):
        self.title = title
        self.author=author
        self.lyrics=lyrics
    
    def display(self):
        print(f"New Song made: {self.title} - {self.author}")
        # return self

    def sing(self, r=-1):
       i=1
       print(f"{self.title} - {self.author}::") 
       for ly in self.lyrics:
            if(r>0 and i>r):
                break
            print(ly)
            i += 1

    def yell(self, r=-1):
       i=1
       print(f"{self.title} - {self.author}::") 
       for ly in self.lyrics:
            if(r>0 and i>r):
                break
            print(ly.upper())
            i += 1

class Rap(Song):
 
    def break_it(self, max_lines, drop="yeah"):
        i=1
        drop = ' '+drop+' '
        for ly in self.lyrics:
            if(i>max_lines):
                break
            print(f"{ly.replace(' ',drop)}{drop}")
            i += 1


# ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu,",
#                                                "Garu, tālu ceļu veicu.",
#                                                "Lēni un par vēlu nācu,", 
#                                                "Meklējot šo ziemeļmalu."])
# ziemelmeita.display()
# ziemelmeita.sing(3)
# ziemelmeita.yell(2)

zrap = Rap("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu,",
                                        "Garu, tālu ceļu veicu.",
                                        "Lēni un par vēlu nācu,", 
                                        "Meklējot šo ziemeļmalu."])

zrap.break_it(3, "Yo")