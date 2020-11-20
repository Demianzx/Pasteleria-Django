from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    sub_category = models.ForeignKey('self', null= True, related_name='general', verbose_name='Sub-Categoria')


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return "Categoria: {} - {}".format(self.name, self.sub_category)

class Product(models.Model):
    title= models.CharField(max_length=400, verbose_name='Titulo')
    description= models.TextField(verbose_name='Descripción')
    img_link= models.CharField(max_length=400, verbose_name='Link de Imagen')
    category= models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title
    
