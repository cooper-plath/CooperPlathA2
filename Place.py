class Place:
    def __init__(self, name, country, priority, visited):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def is_visited(self):
        return self.visited == "v"

    def __str__(self):
        return