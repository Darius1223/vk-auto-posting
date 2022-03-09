class VKPost:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.from_id = kwargs.get("from_id")
        self.owner_id = kwargs.get("owner_id")
        self.date = kwargs.get("date")
        self.marked_as_ads = kwargs.get("marked_as_ads")
        self.post_type = kwargs.get("post_type")
        self.text = kwargs.get("text")
        self.can_edit = kwargs.get("can_edit")
        self.created_by = kwargs.get("created_by")
        self.can_delete = kwargs.get("can_delete")
        self.attachments = kwargs.get("attachments")
        self.event_id = kwargs.get("event_id")
