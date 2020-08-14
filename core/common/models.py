from django.db import models

class TimestampedModel(models.Model):
    # A timestamp for when an object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # A timestamp for last update of object
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        ordering = ["-created_at", "-updated_at"]
