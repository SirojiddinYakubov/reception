from django.core.management.base import BaseCommand, CommandError

from reception.api import PaymentByRequisites, SUCCESS
from user.models import Balance


class Command(BaseCommand):
    help = 'Run Crontab command'

    def handle(self, *args, **options):
        # for poll_id in options['poll_ids']:
        # try:
        #     poll = Poll.objects.get(pk=poll_id)
        # except Poll.DoesNotExist:
        #     raise CommandError('Poll "%s" does not exist' % poll_id)
        try:
            #account balansini olish
            account_balance = PaymentByRequisites().account_balance()
            if account_balance['status'] == SUCCESS:
                balance = int(account_balance['result']) / 100
                Balance.objects.create(amount=balance)
            else:
                raise CommandError('cron error account_balance')
        except Exception as e:
            raise CommandError("Command not working: %s" % str(e))


        self.stdout.write(self.style.SUCCESS('Successfully running cron'))