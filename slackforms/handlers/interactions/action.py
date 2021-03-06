from .base import InteractionBase


class ActionHandler(InteractionBase):
    """
    Handler for message actions. The argument prop is found in the data's
    "text" property.
    """

    def get_id(self):
        return self.data.get("message", {}).get("text", "")
