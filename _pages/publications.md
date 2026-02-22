---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

See my [up-to-date publication list in NASA ADS](https://ui.adsabs.harvard.edu/search/q=%20author%3A%22susobhanan%2C%20abhimanyu%22&sort=date%20desc%2C%20bibcode%20desc&p_=0).

You can find my popular articles [here](/popular-articles/)

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
