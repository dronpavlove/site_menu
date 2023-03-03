from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class PodCategoryMenu(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150)
    category = TreeForeignKey('CategoryMenu', on_delete=models.PROTECT,
                              related_name='posts', verbose_name='Категория меню')
    categori_url = models.TextField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подпункт меню'
        verbose_name_plural = 'Подпункты меню'


class CategoryMenu(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True,
                            blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория меню')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория меню'
        verbose_name_plural = 'Категории меню'

    def get_absolute_url(self):
        return reverse('podcategory-menu', args=[str(self.slug)])

    def __str__(self):
        return self.title
