Atno_to_Symbol = { 1:'H', 2:'He', 3:'Li', 4:'Be', 5:'B', 6:'C' }
class atom(object):
    def __init__(self, atno, x, y, z):
        self.atno = atno
        # access as self.atno within the class definition
        self.position = (x, y, z)
    def symbol(self):
        return Atno_to_Symbol[self.atno]
    def __str__(self):
        return '%d %10.4f %10.4f %10.4f' %\
        (self.atno, self.position[0], self.position[1], self.position[2])
class molecule(object):
    def __init__(self, name = 'Generic'):
        self.name = name
        self.atomlist = []
    def addatom(self,atom):
        self.atomlist.append(atom)
    def __str__(self):
        s = 'This is a molecule named %s\n' % self.name
        s = s + 'It has %d atom\n' % len(self.atomlist)
        for atom in self.atomlist:
            s = s + str(atom) +'\n'
        return s

at = atom(6, 0.0, 1.0, 2.0)
print at.atno
# access as at.atno outside class
print at.symbol()
s = molecule()
s.addatom(1)
print s.name
print s.atomlist
print s
