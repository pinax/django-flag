from django import template

register = template.Library()

def flag(context, obj):
    return {
        'object_id': obj,
        'request': context['request'],
        'user': context['user'],
    }

register.inclusion_tag('templates/flag_form.html', takes_context=True)(flag)
