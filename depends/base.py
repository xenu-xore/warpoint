from databases import Database


class BaseCollector:
    def __init__(self, database: Database):
        self.database = database
