from django.db import models
from django.utils.translation import gettext_lazy as _ 

class Category(models.Model):
    parent = models.ForeignKey('self' , verbose_name=_('parent') ,blank=True , null=True , on_delete=models.CASCADE)
    title = models.CharField(_('title') , max_length=50)
    description = models.TextField(_("description") , blank=True)
    avatar = models.ImageField(_("avatar"),blank=True ,upload_to='categories/',) 
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now_add=True)

    class Meta :
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('categories')

class Product(models.Model):
    title = models.CharField(_('title') , max_length=50)
    description = models.TextField(_("description") , blank=True)
    avatar = models.ImageField(_("avatar"),blank=True ,upload_to='Product/',)
    categories = models.ManyToManyField('Category', verbose_name=_('categories')) 
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now_add=True)

class File(models.Model):
    product = models.ForeignKey('Product' , verbose_name=_('product') ,blank=True , null=True , on_delete=models.CASCADE)
    title = models.CharField(_('title') , max_length=50)
    file = models.ImageField(_("file"),blank=True ,upload_to='files/%y/%m/%d/',) 
    is_enable = models.BooleanField(_('is_enable'),default=True)
    created_time = models.DateTimeField(_('created time'),auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'),auto_now_add=True)
