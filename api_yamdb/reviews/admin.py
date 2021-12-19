from django.contrib.admin import ModelAdmin, register
from reviews.models import Comment, Review

from api_yamdb.settings import EMPTY_STRING_FOR_ADMIN_PY

ModelAdmin.empty_value_display = EMPTY_STRING_FOR_ADMIN_PY


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = (
        'id', 'review', 'author', 'text', 'pub_date')
    search_fields = ('review', 'author',)
    list_filter = ('review', 'author',)


@register(Review)
class ReviewAdmin(ModelAdmin):
    list_display = (
        'id', 'title', 'author', 'text', 'score', 'pub_date')
    search_fields = ('title',)
    list_filter = ('title', 'author')
