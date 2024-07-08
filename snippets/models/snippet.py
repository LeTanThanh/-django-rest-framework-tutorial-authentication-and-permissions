from django.db.models import (
    BooleanField, CharField, DateTimeField, Model, TextField,
)
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(Model):
    title = CharField(max_length=100, blank=True, default='')
    code = TextField()
    linenos = BooleanField(default=False)
    language = CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
