from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


# Реализация связи между таблицей и классом
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # Автозаполнение слага
    save_as = True  # Кнопка "Сохранить как новый объект"
    save_on_top = True  # Кнопки сохранения наверху страницы
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')  # Столбцы в таблице
    list_display_links = ('id', 'title')  # Кликабельные ссылки
    search_fields = ('title',)  # Поле для поиска
    list_filter = ('category',)  # Фильтр по категориям
    readonly_fields = ('views', 'created_at', 'get_photo')  # Только для чтения
    fields = (
        'title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'views', 'created_at')  # Порядок полей

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="40" height="40" style="object-fit: cover;" />')
        return "Нет фото"

    get_photo.short_description = 'Фото'  # Заголовок для столбца
