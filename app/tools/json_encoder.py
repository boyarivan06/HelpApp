from datetime import date

from flask.json import JSONEncoder

from app.models import HelpRequest


class MyJsonEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, date):
            return object.isoformat()
        elif isinstance(object, HelpRequest):
            res = object.__dict__
            del res['_sa_instance_state']
            return res
        return super().default(object)