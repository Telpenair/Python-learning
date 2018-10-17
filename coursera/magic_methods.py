import os
import tempfile

class File:
    def __init__(self, path=None):
        self.path = path or []
        if not os.path.exists(self.path):
            open(self.path, 'w').close()
        
    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, obj):
        new_path = os.path.join(tempfile.gettempdir(), 'sum_file.txt')

        new_file = type(self)(new_path)
        new_file.write(self.read() +  self.read())

        return new_file
    
    def __iter__(self):
        self.iter_lines = []
        self.iter_count = 0
        self.iter_stop = 0
        with open(self.path, 'r') as f:
            for line in f:
                self.iter_lines.append(line)
                self.iter_stop += 1
        return self
    
    def __next__(self):
        if (self.iter_count >= self.iter_stop):
            raise StopIteration
        
        result = self.iter_lines[self.iter_count]
        self.iter_count += 1
        return result
    
    def __str__(self):
        return self.path