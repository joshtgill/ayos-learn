from data.adapters.data_adapter import DataAdapter
from datetime import datetime
import random
import calendar


class DateAdapter(DataAdapter):

    def __init__(self, res_path):
        super().__init__(res_path)


    def sample_line(self):
        FORMATS = [
            '%m/%d/%Y',
            '%B %d, %Y'
        ]

        year = random.randint(1300, 2100)
        month = random.randint(1, 12)
        date = datetime(
            year,
            month,
            random.randint(1, calendar.monthrange(year, month)[1])
        )

        return date.strftime(random.choice(FORMATS))
