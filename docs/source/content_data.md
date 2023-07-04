# Content returned by dalec_discourse

Every dalec save in database object with the following attributes:

 - `last_update_dt` 
 - `creation_dt` 
 - `app` 
 - `content_type` 
 - `channel` 
 - `channel_object` 
 - `dj_channel_content_type_id`
 - `dj_channel_id`
 - `dj_content_content_type_id`
 - `dj_content_id`
 - `content_id`
 - `content_data`

See [the main dalec](https://github.com/webu/dalec) repository for more information.
Hereafter are detailed the `content_data`, specific to the `discourse` content type.

## Topic

```json
{
  // generic field from the `latest.json` (entire forum or for a given category)
  "slug": "ext-er-min-ate",
  "liked": null,
  "title": "Ext-er-min-ate",
  "views": 37,
  "bumped": true,
  "closed": false,
  "pinned": false,
  "unseen": false,
  "posters": [
    {
      "extras": null,
      "user_id": 768,
      "description": "Cr\\u00e9ateur du sujet",
      "primary_group_id": null
    },
    {
      "extras": null,
      "user_id": 12,
      "description": "Auteur fr\\u00e9quent",
      "primary_group_id": null
    },
    {
      "extras": "latest",
      "user_id": 152,
      "description": "Auteur le plus r\\u00e9cent",
      "primary_group_id": null
    }
  ],
  "visible": true,
  "archived": false,
  "unpinned": null,
  "archetype": "regular",
  "bumped_at": "2022-01-10T08:29:34.892Z",
  "image_url": null,
  "bookmarked": null,
  "created_at": "2021-12-31T10:54:59.152Z",
  "like_count": 2,
  "category_id": 37,
  "fancy_title": "Exterminate :slight_smile:",
  "has_summary": false,
  "posts_count": 3,
  "reply_count": 1,
  "featured_link": null,
  "last_posted_at": "2022-01-10T08:29:34.892Z",
  "pinned_globally": false,
  "highest_post_number": 3,
  "last_poster_username": "dalec"
  // Added by the dalec
  "name": "Dalec",
  "base_url": "https://forum.dalec.org",
  "post_url": "https://forum.dalec.org/t/ext-er-min-ate/2379",
  "category": {
    "id": 37,
    "name": "Universe",
    "slug": "universe"
  },
  "id": "2379",
  "creation_dt": "2021-12-31T10:54:59.152Z",
  "last_update_dt": "2022-04-13T12:13:18.746Z",
}
```


## User topic and reply

List of user action filtered by topic and reply type (`4` and `5` filter in the `user_actions.json` endpoint)

```json
{
  // generic field from the `user_actions.json` endpoint
  "name": "Dalec",
  "slug": "ext-er-min-ate",
  "title": "Ext-er-min-ate",
  "closed": false,
  "hidden": null,
  "deleted": false,
  "excerpt": "To the galaxy, \\nI will soon destroy you",
  "post_id": null,
  "user_id": 386,
  "archived": false,
  "topic_id": 1608,
  "username": "dalec",
  "post_type": null,
  "created_at": "2020-09-29T22:21:18.735Z",
  "acting_name": "Dalec",
  "action_code": null,
  "action_type": 4,
  "category_id": 59,
  "post_number": 1,
  "target_name": "Dalec",
  "acting_user_id": 386,
  "target_user_id": 386,
  "acting_username": "dalec",
  "avatar_template": "/user_avatar/forum.dalec.org/dalec/{size}/601_2.png",
  "target_username": "dalec",
  "acting_avatar_template": "/user_avatar/forum.dalec.org/dalec/{size}/601_2.png"
  // Added by the dalec
  "id": "4-None",
  "category": {
    "id": "59",
    "name": "Universe conquest",
    "slug": "universe-conquest"
  },
  "post_url": "https://forum.dalec.org/t/ext-er-min-ate/1608",
  "creation_dt": "2020-09-29T22:21:18.735Z",
  "last_update_dt": "2022-04-20T19:13:41.957Z",
}
```

## Category

```json
{
  // generic field from the `categories.json` endpoint
  "name": "string",
  "color": "string",
  "text_color": "string",
  "slug": "string",
  "topic_count": 0,
  "post_count": 0,
  "position": 0,
  "description": "string",
  "description_text": "string",
  "description_excerpt": "string",
  "topic_url": "string",
  "read_restricted": true,
  "permission": 0,
  "notification_level": 0,
  "can_edit": true,
  "topic_template": "string",
  "has_children": true,
  "sort_order": "string",
  "sort_ascending": "string",
  "show_subcategory_list": true,
  "num_featured_topics": 0,
  "default_view": "string",
  "subcategory_list_style": "string",
  "default_top_period": "string",
  "default_list_filter": "string",
  "minimum_required_tags": 0,
  "navigate_to_first_post_after_read": true,
  "topics_day": 0,
  "topics_week": 0,
  "topics_month": 0,
  "topics_year": 0,
  "topics_all_time": 0,
  "is_uncategorized": true,
  "subcategory_ids": [
    null
  ],
  "subcategory_list": [
    null
  ],
  "uploaded_logo": "string",
  "uploaded_logo_dark": "string",
  "uploaded_background": "string",
  // Added by the dalec
  "id": "string",
  "base_url": "string",
  "last_update_dt": "string",
  "creation_dt": "string",
}
```
