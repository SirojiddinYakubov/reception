def crontab_function():
    print('printed from crontab')
    f = open('crontab.txt', 'w')
    f.close()