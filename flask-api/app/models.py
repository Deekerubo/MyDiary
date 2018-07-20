class Models(object):
    

    def __init__(self):
        self.Entries = []

    def add(self, title, content):
        self.title = title
        self.content = content
        number_of_entries = 0
        for i in range(len(self.Entries)):
            number_of_entries += 1
        an_entry = {}
        an_entry['id'] = number_of_entries
        an_entry['title'] = self.title
        an_entry['content'] = self.content

        self.Entries.append(an_entry)

    def all_entries(self):
        return self.Entries