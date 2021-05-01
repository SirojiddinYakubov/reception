def hi():
    print('iam an cron job')
    f = open('/home/pyth/reception/django_cron.txt', 'w')
    f.writelines('cronjob')
    f.close()