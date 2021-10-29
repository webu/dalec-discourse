from datetime import timedelta
from typing import Dict
import requests

from django.utils.dateparse import parse_datetime
from django.utils.timezone import now
from django.conf import settings

from dalec.proxy import Proxy

from pydiscourse import DiscourseClient

client = DiscourseClient(
        settings.DALEC_DISCOURSE_BASE_URL,
        api_username=settings.DALEC_GITLAB_API_USERNAME,
        api_key=settings.DALEC_GITLAB_API_KEY,
        )


class DiscourseProxy(Proxy):
    """
    Discourse dalec proxy to fetch the last messages.
    """

    app = "discourse"

    def _fetch(
        self, nb: int, content_type: str, channel: str, channel_object: str
    ) -> Dict[str, dict]:
        # TODO

        raise ValueError("Invalid content_type %s" % content_type)

