from app import api
from app.controllers.conversation import (
    CreateConversation,
    DeleteConversation,
    GetConversations,
)

api.add_resource(GetConversations, "/get_conversations")
api.add_resource(CreateConversation, "/create_conversation")
api.add_resource(DeleteConversation, "/delete_conversation/<string:conversation_uuid>")
