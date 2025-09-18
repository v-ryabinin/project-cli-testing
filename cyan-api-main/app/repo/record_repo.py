from app.db.recordManager import RecordManager


class RecordRepo(RecordManager):
    def __init__(self):
        super().__init__("offers")
