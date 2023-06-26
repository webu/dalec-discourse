# dalec-discourse

Django Aggregate a Lot of External Content -- Discourse

Aggregate last discourse post from a given discourse instance.

Plugin of [dalec](https://github.com/webu/dalec).

## Installation

Install the module:

```
pip install dalec_discourse
```

In django settings `INSTALLED_APPS`, add:

```
INSTALLED_APPS = [
    ...
    "dalec",
    "dalec_prime",
    "dalec_discourse",
    ...
    ]
```


## Usage

General usage:
```django
{% load dalec %}

{% dalec "discourse" content_type [channel=None] [channel_object=None] [template=None] %}
```

Real examples:

### Topics

Retrieves latest topics:
```django
{% dalec "discourse" "topic" %}
```

Retrieves latest topics from a category:
```django
{% dalec "discourse" "topic" channel="category" channel_object="15" %}
```

### Categories

Retrieves discourse categories:
```django
{% dalec "discourse" "category" %}
```

### User topics and replies

Retrieves user topics and replies:

```django
{% dalec "discourse" "user_topic_and_reply" channel="user" channel_object="zorro" %}
```


## Settings

Django settings must define:

  - `DALEC_DISCOURSE_BASE_URL` : discourse instance url (ex: `https://discourse.org/`)
  - `DALEC_DISCOURSE_API_USERNAME` : discourse username (ex: `admin`)
  - `DALEC_DISCOURSE_API_TOKEN` : discourse api token (ex: `azeazeaezdfqsmlkrjzr`)

It could also define the login/password attribute, and then this auth method will be used
(may be usefull for htaccess access for instance):

  - `DISCOURSE_AUTH_USERNAME`
  - `DISCOURSE_AUTH_PASSWORD`


