from tornado.web import RequestHandler
import json
import traceback
from utils import JSONEncoder


class BaseHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.set_header('Content-Type', 'text/json')
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            lines = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                lines.append(line)
            self.finish(json.dumps({
                'error': self._reason,
                'code': status_code,
                'traceback': lines,

            }))
        else:
            self.finish(json.dumps({
                'error': self._reason,
                'code': status_code,
            }))

    def render_json(self, status_code, reason, data={}, renderer=JSONEncoder):
        self.set_header("Content-Type", "application/json")
        self.set_status(status_code, reason)
        self.write(renderer().encode(data))

    def data_received(self, chunk):
        """
        Implement this method to handle streamed request data.
        Requires the `.stream_request_body` decorator.
        """
        pass
