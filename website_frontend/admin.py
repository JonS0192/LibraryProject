from django.contrib import admin
from .models import *

admin.site.register(books)
admin.site.register(library_cards)
admin.site.register(checked_out)
