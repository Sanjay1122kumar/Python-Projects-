class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, key):
        return sum(ord(char) for char in key)

    def add(self, key, value):
        hashed = self.hash(key)
        if hashed not in self.collection:
            self.collection[hashed] = {}
        self.collection[hashed][key] = value

    def remove(self, key):
        hashed = self.hash(key)
        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]
            if not self.collection[hashed]:
                del self.collection[hashed]

    def lookup(self, key):
        hashed = self.hash(key)
        if hashed in self.collection:
            return self.collection[hashed].get(key)
        return None


# Example usage
if __name__ == "__main__":
    table = HashTable()
    print(table.hash('golf'))         # 424

    table.add('golf', 'sport')
    table.add('dear', 'friend')
    table.add('read', 'book')
    table.add('fcc', 'coding')
    table.add('cfc', 'chemical')
    print(table.collection)

    print(table.lookup('golf'))       # sport
    print(table.lookup('unknown'))    # None

    table.remove('dear')              # 'read' stays at 412
    table.remove('missing')           # no error
    print(table.collection)