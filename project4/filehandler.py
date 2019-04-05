class Filehandler:
    def __init__(self):
        self.filename = self.get_filename()
        self.file = self.open_file()
        self.data = self.parse_data()

    def get_filename(self):
        filename = input('Which file would you like to use? ')
        return filename

    def open_file(self):
        try:
            file = open(self.filename, 'r')
            return file
        except FileNotFoundError as error:
            print(error)
            exit()

    def parse_data(self):
        data = []
        for lines in self.file.readlines():
            line = lines.strip().split(',')
            data.append(line)
        return data

    def __repr__(self):
        return"File: {0}".format(self.filename)
