{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello 
{% endblock %}

{% block body %}
<h4>Your Token is: {{token}}</h4>
{% endblock %}

{% block html %}

{% endblock %}