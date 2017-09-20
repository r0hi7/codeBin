from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

#getting the list of lexers,languages and the available styles from the Pygments

LEXERS = [lexer for lexer in get_all_lexers() if lexer[1]]
LANGUAGES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLECHOICES = sorted((item,item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100,blank=True,default='')
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGES,default='python',max_length=100)
    style = models.CharField(choices=STYLECHOICES,default='friendly',max_length=100)
    code = models.TextField()

