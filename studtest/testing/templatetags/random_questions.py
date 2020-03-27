from django import template
import random

register = template.Library()


@register.filter
def random_questions(questions, max_questions):
    return random.sample(list(questions), max_questions)
