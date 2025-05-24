{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello 
{% endblock %}

{% block body %}
<h4><a href="http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{token}}">click to verify!</a></h4>
{% endblock %}

{% block html %}

{% endblock %}