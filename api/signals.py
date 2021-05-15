import os.path
import shutil
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import Product


def image_delete(filename):
    image_path = os.path.abspath(os.path.join(filename.path, '../..'))
    shutil.rmtree(image_path)


@receiver(post_delete, sender=Product)
def delete_file_on_product_delete(sender, instance, **kwargs):
    image = instance.image
    if image:
        image_delete(image)
