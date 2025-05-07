{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello 
{% endblock %}

{% block body %}
<h4>http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{token}}</h4>
{% endblock %}

{% block html %}

{% endblock %}