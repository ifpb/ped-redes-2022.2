from datetime import datetime

class DateUtils:

    FORMATO_DATA = "%d/%m/%Y"

    @classmethod
    def converter_string_p_data(cls, data_string):
        return datetime.strptime(data_string, cls.FORMATO_DATA)