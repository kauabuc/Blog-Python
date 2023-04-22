import os

from categoria.models import Categoria
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.


class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    autor_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    excerto_post = models.TextField(verbose_name='Excerto')
    conteudo_post = models.TextField(verbose_name='Conteudo')
    categoria_post = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, blank=True, null=True,
        verbose_name='Categoria')
    imagem_post = models.ImageField(
        upload_to='post_img/%Y/%m/%d', blank=True, null=True,
        verbose_name='Foto')
    publicado_post = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self):
        return self.titulo_post

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_image(self.imagem_post.name, 800)

    @staticmethod
    def resize_image(nome_imagem, largura_img):
        if not nome_imagem:
            return
        img_path = os.path.join(settings.MEDIA_ROOT, nome_imagem)
        img = Image.open(img_path)
        width, height = img.size

        if largura_img >= width:
            img.close()
            return

        largura_nova = round((largura_img * height) / width)

        nova_img = img.resize((largura_img, largura_nova), Image.ANTIALIAS)

        nova_img.save(img_path, optimize=True, quality=60)
