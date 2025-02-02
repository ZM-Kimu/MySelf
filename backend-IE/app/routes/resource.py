from app import api
from app.controllers.resource import GetImageStream

api.add_resource(GetImageStream, "/img/<string:conversation_uuid>")
