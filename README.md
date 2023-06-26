# 🗣 dalec-discourse

[![Stable Version](https://img.shields.io/pypi/v/dalec-discourse?color=blue)](https://pypi.org/project/dalec-discourse/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![semver](https://img.shields.io/badge/semver-2.0.0-green)](https://semver.org/)


Django Aggregate a Lot of External Content -- Discourse

Aggregate last discourse post from a given discourse instance.

Plugin of [🤖 dalec](https://github.com/webu/dalec).

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


