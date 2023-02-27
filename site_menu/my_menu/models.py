from django.utils.translation import gettext_lazy as _
from django.db import models
import mptt

CHOICES_VISIBLE = [
    ('1', _('Yes')),
    ('0', _('No')),
]


class Menu(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name="название пукта меню",
    )
    position = models.CharField(
        max_length=80,
        verbose_name="позиция",
    )
    visible = models.CharField(
        max_length=2,
        verbose_name=_('видимость'),
        choices=CHOICES_VISIBLE,
        default=CHOICES_VISIBLE[0][0],
    )

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню"

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name="название пукта родителя",
        on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        'self',
        verbose_name="родитель",
        related_name=u'child',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=150,
        verbose_name="собственное название",
    )
    uri = models.SlugField(
        verbose_name=_('URL'),
        help_text=_('If you do not want to connect this item to your models, you can specify a URL explicitly'),
        blank=True,
        null=True,
    )
    visible = models.CharField(
        max_length=1,
        verbose_name="видимость",
        choices=CHOICES_VISIBLE,
        default=CHOICES_VISIBLE[0][0],
    )
    css_class = models.CharField(
        max_length=50,
        verbose_name=_('CSS class'),
        help_text=u'',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "подпункт меню"
        verbose_name_plural = "подпункты меню"

    def get_absolute_url(self):
        return '/%s' % self.uri

    # def __unicode__(self):
    #     return self.name

    def __str__(self):
        return self.name


mptt.register(MenuItem, )
