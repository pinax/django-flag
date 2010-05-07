from django.dispatch import Signal


content_flagged = Signal(providing_args=["flagged_content", "flagged_instance"])