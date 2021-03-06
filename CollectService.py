from datetime import date
import datetime
import os

class CollectService:
    def __init__(self, first_date, db_path, factory):
        self._first_date = first_date
        self._path = db_path
        self._factory = factory
        self._last_updated = os.path.join(self._path, "._last_updated.txt")

    def _set_last_updated(self, actual_date):
        date_str = "{0:%Y-%m-%d}".format(actual_date)
        with open(self._last_updated, "w") as f:
            f.write(date_str)

    def _get_last_updated(self):
        actual_date = None
        with open(self._last_updated, "r") as f:
            date_str = f.readline().rstrip()
            actual_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        return actual_date.date()

    def execute(self):
        last_updated = self._first_date
        today = datetime.datetime.now().date()
        one_day = datetime.timedelta(days=1)

        if not os.path.exists(self._path):
            os.mkdir(self._path)
            
        if os.path.isfile(self._last_updated):
            last_updated = self._get_last_updated() 

        if last_updated == today:
            return

        start_date = last_updated + one_day
        stop_date = today

        funds = {}
        c = self._factory.create_collector(funds)
        c.execute(start_date, stop_date)

        s = self._factory.create_storer(funds)
        s.execute()

        self._set_last_updated(stop_date)