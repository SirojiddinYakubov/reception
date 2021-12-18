from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    def handle(self, *args, **options):
        print('ok')
        # for poll_id in options['poll_ids']:
        # try:
        #     poll = Application.objects.last()
        # except Application.DoesNotExist:
        #     raise CommandError('Poll "%s" does not exist' % 123)
        #
        # # poll.opened = False
        # # poll.save()
        #
        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % 123))
