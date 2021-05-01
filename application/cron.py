def application_crontab():
    print('application crontab')
    f = open('/home/pyth/reception/django_cron.txt', 'w')
    f.writelines('cronjob')
    f.close()