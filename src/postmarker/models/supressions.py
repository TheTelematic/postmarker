from postmarker.models.base import ModelManager, MessageModel


class Suppressions(MessageModel):
    """Suppressions model."""


class SuppresionsManager(ModelManager):
    """Encapsulates logic about suppressions."""

    name = "suppressions"
    model = Suppressions


