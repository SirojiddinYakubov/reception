import codecs
import io
import json
import os
from pathlib import Path

from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.serializers import serialize
from django.utils import timezone

from reception import settings
from django.db import connection

from django.core.serializers.json import DjangoJSONEncoder

from service.models import Service
from user.models import Region


class Command(BaseCommand):
    help = 'Displays current time'

    def iter_json(self, file):
        """ Iterates dumpdata dson file and yields a model name / field dict pairs.

        e.g.
            model = 'common.sitesettings'
            fields = {'name': 'ACME Products', 'timezone': 'Africa/Johannesburg'}
        """
        with open(file, "r") as f:
            data = json.loads(f.read())
        for obj in data:
            yield obj['model'], obj['pk'], obj['fields']

    def iter_data(self, file):
        """ Iterates dumpdata dson file and yields model instances.

        The downside to this approach is that one requires the code for the models,
        which is not neccessarily the case when migrating data/
        e.g.
            model_instance = <SiteSettings: ACNE Products ()>
        """
        with open(file, "r") as f:
            data_str = f.read()
        for item in serializers.deserialize("json", data_str):
            # item.save() would save it (unconfirmed)
            model_instance = item.object
            yield model_instance

    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            type=str,
            help='Location of the manage.py dumpdata backup file',
        )

    def handle(self, **options):
        file = options['file']
        if not Path(file).is_file():
            print(f"File '${file}' does not exist. EXIT.")
            return

        print(f"START - Customised loaddata")
        for model, id, fields in self.iter_json(file):
            app_label = model.split('.')[0]
            model_name = model.split('.')[1]
            if ContentType.objects.get(app_label=app_label, model=model_name):
                Service.objects.create(long_title=fields['title'], short_title=fields['title'], key=fields['key'],
                                       desc=fields['desc'],photo=fields['photo'], deadline=fields['deadline'],instruction=fields['instruction'])

            print(model, id, fields)
        # for instance in self.iter_data(file):
        #     print(instance)
        print(f"COMPLETE.")

# def dumpload():
#     json_filename = 'region.json'
#
#     json_filepath = os.path.join(settings.BASE_DIR, json_filename)
#
#     # with open(json_filepath, 'w') as f:
#     #     call_command('dumpdata', model, stdout=f, database='default')
#     print(json_filename)
#
#     with open(json_filepath, "r") as f:
#         data_str = f.read()
#     for item in serializers.deserialize("json", data_str):
#         model_instance = item.object
#         print(model_instance)
#         yield model_instance
#
#     # for obj in data:
#     #     yield obj['model'], obj['fields']
#
#     # with connection.cursor() as cursor:
#     #     print(cursor)
#
#     # call_command('loaddata', json_filepath, database='default')
#
#
# class Command(BaseCommand):
#     help = 'Displays current time'
#
#     def iter_json(self, file):
#         """ Iterates dumpdata dson file and yields a model name / field dict pairs.
#
#         e.g.
#             model = 'common.sitesettings'
#             fields = {'name': 'ACME Products', 'timezone': 'Africa/Johannesburg'}
#         """
#         with open(file,'rb') as f:
#             print(f.read().decode('utf-8').replace("'", '"'))
#
#             data = json.loads(f.read())
#             print(data)
#         for obj in data:
#             yield obj['model'], obj['pk'], obj['fields']
#
#     def iter_data(self, file):
#         """ Iterates dumpdata dson file and yields model instances.
#
#         The downside to this approach is that one requires the code for the models,
#         which is not neccessarily the case when migrating data/
#         e.g.
#             model_instance = <SiteSettings: ACNE Products ()>
#         """
#         # data = self.parse_json(file)
#         with open(file, "r") as f:
#             data_str = f.read()
#         for item in serializers.deserialize("json", data_str):
#             # item.save() would save it (unconfirmed)
#             model_instance = item.object
#             yield model_instance
#
#     def add_arguments(self, parser):
#         parser.add_argument(
#             'file',
#             type=str,
#             help='Location of the manage.py dumpdata backup file',
#         )
#
#     def handle(self, **options):
#         file = options['file']
#
#         if not Path(file).is_file():
#             print(f"File '${file}' does not exist. EXIT.")
#             return
#
#         # with io.open(file,encoding="utf8", errors='ignore') as f:
#         #     print(f.read())
#         # item = serializers.serialize("json", f.read())
#         # print(item)
#         # model_instance = item.object
#         # yield model_instance
#
#         print(f"START - Customised loaddata")
#         for model, pk, fields in self.iter_json(file):
#             print(86, model, pk, fields)
#         for instance in self.iter_data(file):
#             print(instance)
#         print(f"COMPLETE.")

# def handle(self, *args, **kwargs):
#     # time = timezone.now().strftime('%X')
#     self.stdout.write("It's now %s" % dumpload())

# self.stdout.write(self.style.ERROR('error - A major error.'))
# self.stdout.write(self.style.NOTICE('notice - A minor error.'))
# self.stdout.write(self.style.SUCCESS('success - A success.'))
# self.stdout.write(self.style.WARNING('warning - A warning.'))
# self.stdout.write(self.style.SQL_FIELD('sql_field - The name of a model field in SQL.'))
# self.stdout.write(self.style.SQL_COLTYPE('sql_coltype - The type of a model field in SQL.'))
# self.stdout.write(self.style.SQL_KEYWORD('sql_keyword - An SQL keyword.'))
# self.stdout.write(self.style.SQL_TABLE('sql_table - The name of a model in SQL.'))
# self.stdout.write(self.style.HTTP_INFO('http_info - A 1XX HTTP Informational server response.'))
# self.stdout.write(self.style.HTTP_SUCCESS('http_success - A 2XX HTTP Success server response.'))
# self.stdout.write(self.style.HTTP_NOT_MODIFIED('http_not_modified - A 304 HTTP Not Modified server response.'))
# self.stdout.write(
#     self.style.HTTP_REDIRECT('http_redirect - A 3XX HTTP Redirect server response other than 304.'))
# self.stdout.write(self.style.HTTP_NOT_FOUND('http_not_found - A 404 HTTP Not Found server response.'))
# self.stdout.write(
#     self.style.HTTP_BAD_REQUEST('http_bad_request - A 4XX HTTP Bad Request server response other than 404.'))
# self.stdout.write(self.style.HTTP_SERVER_ERROR('http_server_error - A 5XX HTTP Server Error response.'))
# self.stdout.write(self.style.MIGRATE_HEADING('migrate_heading - A heading in a migrations management command.'))
# self.stdout.write(self.style.MIGRATE_LABEL('migrate_label - A migration name.'))
