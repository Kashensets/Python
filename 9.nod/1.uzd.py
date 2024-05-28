class Song:
  """Klases definīcija dziesmām."""

  def __init__(self, title, author, lyrics, max_lines=-1,):
    """Konstruktors dziesmas izveidei."""
    self.title = title
    self.author = author
    self.lyrics = lyrics
    self.max_lines = max_lines
    print(f"Jauna dziesma izveidota: {title} - {author}")

  def sing(self, max_lines=None):
    """Izdrukā dziesmu pa rindiņai."""
    if self.title and self.author:
      print(f"{self.title} - {self.author}")
    if max_lines is None:
      max_lines = self.max_lines
    for line in self.lyrics[:max_lines]:
      print(line)

  def yell(self, max_lines=None):
    """Izdrukā dziesmu ar lieliem burtiem pa rindiņai."""
    if self.title and self.author:
        print(f"{self.title} - {self.author}")
    if max_lines is None:
        max_lines = self.max_lines
    for line in self.lyrics[:max_lines]:
        words = line.split()
        upper_case_line = ' '.join([word.upper() for word in words])
        print(upper_case_line)

# Piemērs dziesmas izveidei un izdrukai
ziemelmeita = Song("Ziemeļmeita", "Jumprava", ["Gāju meklēt ziemeļmeitu", "Garu, tālu ceļu veicu"])
ziemelmeita.sing(1)  # Izdrukā pirmo rindiņu
ziemelmeita.sing()    # Izdrukā visas rindas
ziemelmeita.yell()   # Izdrukā visu dziesmu ar lieliem burtiem

# Piemērs ar citu dziesmu
meza_meita = Song("Meža meita", "Taurenīte", ["Dzied meža meitiņa", "Pļavās zied zālīte"])
meza_meita.sing(2)   # Izdrukā pirmās divas rindas
meza_meita.yell(1)  # Izdrukā pirmo rindiņu ar lieliem burtiem

