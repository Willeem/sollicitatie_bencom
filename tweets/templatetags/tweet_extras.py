import re 

from django import template 
from django.utils.safestring import mark_safe


register = template.Library()

@register.simple_tag
def add_italics_and_bold(text, most_freq):
    """
    Adds italics to the most frequent letter in a tweet and makes the word(s) 
    that contain the most frequent letter bold.
    """
    text = text.replace(most_freq,"<i>"+most_freq+"</i>")
    max_sum = 0
    words = []
    for word in text.split():
        count = sum(most_freq in s for s in word)
        if count > max_sum:
            words = []
            max_sum = count
            words.append((word, "<b>"+word+"</b>"))
        elif count == max_sum:
            words.append((word, "<b>"+word+"</b>"))
    for word, bold in words:
        text = text.replace(word, bold)
    return mark_safe(text)

