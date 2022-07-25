import json
import datetime
from json import JSONEncoder
import dateutil.parser

class DateTimeEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (datetime.date)):
            return obj.isoformat()


def DecodeDateTime(empDict):
   if 'joindate' in empDict:
      empDict["joindate"] = dateutil.parser.parse(empDict["joindate"])
      return empDict