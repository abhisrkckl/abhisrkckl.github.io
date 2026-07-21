---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

See a list of my [selected publications in NASA ADS](https://ui.adsabs.harvard.edu/search/q=docs(library%2FIfGigYrbQvyqn94YRYC7Xw)&sort=date%20desc%2C%20bibcode%20desc&p_=0).

You can find my popular articles [here](/popular-articles/)

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
