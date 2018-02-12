class FileStructure:

    def __init__(self, filename, location, size):
        self.filename = filename
        self.location = location
        self.size = size

    def get_size(self):
        return self.size

    def get_filename(self):
        return self.filename

    def get_file_location(self):
        return self.location
