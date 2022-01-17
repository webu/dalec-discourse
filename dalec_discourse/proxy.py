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

# monkey patch because not yet upstream...
def category_show(category_id, **kwargs):
    response = client._get("/c/{0}/show".format(category_id), **kwargs)
    return response["category"]


client.category_show = category_show

client.auth_username = getattr(settings, "DISCOURSE_AUTH_USERNAME", None)
client.auth_password = getattr(settings, "DISCOURSE_AUTH_PASSWORD", None)


class DiscourseProxy(Proxy):
    """
    Discourse dalec proxy to fetch the last messages.
    """

    app = "discourse"

    def __init__(self):
        self.kwargs = {"override_request_kwargs": {}}

        if client.auth_username and client.auth_password:
            self.kwargs["override_request_kwargs"]["auth"] = (
                client.auth_username,
                client.auth_password,
            )

    def _fetch(
        self, nb: int, content_type: str, channel: str, channel_object: str
    ) -> Dict[str, dict]:

        kwargs = self.kwargs
        kwargs["per_page"] = nb

        if content_type == "topic":
            return self._fetch_latest_topics(nb, channel, channel_object, **kwargs)
        elif content_type == "category":
            return self._fetch_categories(nb, channel, channel_object, **kwargs)
        elif content_type == "user_topic_and_reply":
            return self._fetch_user_topics_and_replies(
                nb, channel, channel_object, **kwargs
            )

        raise ValueError(
            f"""
        Invalid content_type {content_type}. Accepted: topic, category,
                user_topic_and_reply."""
        )

    def _fetch_latest_topics(self, nb, channel=None, channel_object=None, **kwargs):
        """
        Get latest topics from entire forum or category
        """
        kwargs["override_request_kwargs"]["allow_redirects"] = True

        if channel == "category" and channel_object is not None:
            topics = client.category_latest_topics(name=channel_object, **kwargs)[
                "topic_list"
            ]["topics"]
        else:
            topics = client.latest_topics(name=channel_object, **kwargs,)[
                "topic_list"
            ]["topics"]

        contents = {}
        for topic in topics:
            category = client.category_show(topic["category_id"], **kwargs)

            post_url = "{}/t/{}/{}".format(
                settings.DALEC_DISCOURSE_BASE_URL,
                topic["slug"],
                topic["id"],
            )

            topic["id"] = str(topic["id"])
            contents[topic["id"]] = {
                **topic,
                "category": {
                    "id": category["id"],
                    "name": category["name"],
                    "slug": category["slug"],
                },
                "base_url": settings.DALEC_DISCOURSE_BASE_URL,  # to reconstruct different url later
                "post_url": post_url,
                "last_update_dt": now(),
                "creation_dt": topic["created_at"],
            }
        return contents

    def _fetch_categories(self, nb, channel=None, channel_object=None, **kwargs):
        """
        Get categories
        """
        categories = client.categories()

        contents = {}
        for category in categories:
            category["id"] = str(category["id"])
            contents[category["id"]] = {
                **category,
                "base_url": settings.DALEC_DISCOURSE_BASE_URL,  # to reconstruct url later
                "last_update_dt": now(),
                "creation_dt": now(),
            }
        return contents

    def _fetch_user_topics_and_replies(
        self, nb, channel=None, channel_object=None, **kwargs
    ):
        """
        Get latest topics and replies of a given user identified by its username `channel_object`
        """

        if channel != "user":
            raise ValueError(f"channel should be in : user .")
        if not channel_object:
            raise ValueError(f"channel_object must be defined")

        # 4 = topic
        # 5 = reply
        topics_and_replies = client.user_actions(
            username=channel_object, filter="4,5", **kwargs
        )

        contents = {}
        for topic_and_reply in topics_and_replies:
            id = "{}-{}".format(
                topic_and_reply["action_type"], topic_and_reply["post_id"]
            )
            content = {k: v for k, v in topic_and_reply.items()}

            category = client.category_show(topic_and_reply["category_id"], **kwargs)

            post_url = "{}/t/{}/{}{}".format(
                settings.DALEC_DISCOURSE_BASE_URL,
                topic_and_reply["slug"],
                topic_and_reply["topic_id"],
                "/{}".format(topic_and_reply["post_id"])
                if topic_and_reply["post_id"]
                else "",
            )

            content.update(
                {
                    "category": {
                        "id": str(category["id"]),
                        "name": category["name"],
                        "slug": category["slug"],
                    },
                    "post_url": post_url,
                    "id": id,
                    "creation_dt": topic_and_reply["created_at"],
                    "last_update_dt": now(),
                }
            )

            contents[id] = content

        return contents
