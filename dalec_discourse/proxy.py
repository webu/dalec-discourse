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
        api_username=settings.DALEC_DISCOURSE_API_USERNAME,
        api_key=settings.DALEC_DISCOURSE_API_KEY,
        )


class DiscourseProxy(Proxy):
    """
    Discourse dalec proxy to fetch the last messages.
    """

    app = "discourse"

    def _fetch(
        self, nb: int, content_type: str, channel: str, channel_object: str
    ) -> Dict[str, dict]:
        if content_type == "topic":
            return self._fetch_topic(nb, channel, channel_object)

        raise ValueError("Invalid content_type %s" % content_type)

    def _fetch_topic(self, nb, channel=None, channel_object=None):
        options = {"per_page": nb}

        topics = client.category_latest_topics(
                name=channel_object,
                parent=channel
                )["topic_list"]["topics"]

        contents = {}
        for topic in topics:
            contents[topic["id"]] = {
                    **topic,
                    "last_update_dt": now(),
                    "creation_dt": topic["created_at"]
                    }
        return contents



