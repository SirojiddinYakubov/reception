from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from user.models import Section


# @receiver(m2m_changed, sender=Section.district.through)
# def district_changed(sender, **kwargs):
#     if kwargs['action'] == 'post_add':
#         instance = kwargs['instance']
#         print(instance.district.all())
#         instance.save()


# m2m_changed.connect(district_changed, sender=Section.district.through)
