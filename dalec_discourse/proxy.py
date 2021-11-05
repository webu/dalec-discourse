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
            return self._fetch_latest_topics(nb, channel, channel_object)
        elif content_type == "category":
            return self._fetch_categories(nb, channel, channel_object)
        elif content_type == "user_topic_and_reply":
            return self._fetch_user_topics_and_replies(nb, channel, channel_object)

        raise ValueError(
            f"""
        Invalid content_type {content_type}. Accepted: topic, category,
                user_topic_and_reply."""
        )

    def _fetch_latest_topics(self, nb, channel=None, channel_object=None):
        """
        Get latest topics from entire forum or category
        """
        options = {"per_page": nb, "override_request_kwargs": {"allow_redirects": True}}

        if channel == "category" and channel_object is not None:
            topics = client.category_latest_topics(name=channel_object, **options)[
                "topic_list"
            ]["topics"]
        else:
            topics = client.latest_topics(name=channel_object, **options,)[
                "topic_list"
            ]["topics"]

        contents = {}
        for topic in topics:
            contents[topic["id"]] = {
                **topic,
                "base_url": settings.DALEC_DISCOURSE_BASE_URL,  # to reconstruct url later
                "last_update_dt": now(),
                "creation_dt": topic["created_at"],
            }
        return contents

    def _fetch_categories(self, nb, channel=None, channel_object=None):
        """
        Get categories
        """
        categories = client.categories()

        contents = {}
        for category in categories:
            contents[category["id"]] = {
                **category,
                "base_url": settings.DALEC_DISCOURSE_BASE_URL,  # to reconstruct url later
                "last_update_dt": now(),
                "creation_dt": now(),
            }
        return contents

    def _fetch_user_topics_and_replies(self, nb, channel=None, channel_object=None):
        """
        Get latest topics and replies of a given user identified by its username `channel_object`
        """

        if channel != "user":
            raise ValueError(f"channel should be in : user .")
        if not channel_object:
            raise ValueError(f"channel_object must be defined")

        # 4 = topic
        # 5 = reply
        topics_and_replies = client.user_actions(username=channel_object, filter="4,5")

        contents = {}
        for topic_and_reply in topics_and_replies:
            id = "{}-{}".format(
                topic_and_reply["action_type"], topic_and_reply["post_id"]
            )
            content = {k: v for k, v in topic_and_reply.items()}

            post_url = "{}/t/{}/{}{}".format(
                    settings.DALEC_DISCOURSE_BASE_URL,
                    topic_and_reply["slug"],
                    topic_and_reply["topic_id"],
                    "/{}".format(topic_and_reply["post_id"]) if topic_and_reply["post_id"] else ""
                    )
            content.update(
                {
                    "post_url": post_url,
                    "id": id,
                    "creation_dt": topic_and_reply["created_at"],
                    "last_update_dt": now(),
                }
            )

            contents[id] = content

        return contents
