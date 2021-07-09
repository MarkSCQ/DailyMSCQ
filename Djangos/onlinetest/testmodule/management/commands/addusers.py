#  --------------------------------------------------
# * Thanks for the blog from CSDN and official tutorial
# ! Based on
# ! 1. https://blog.csdn.net/wangfan741/article/details/109964718
# ! https://docs.djangoproject.com/zh-hans/3.1/howto/custom-management-commands/


# * Description: This file is used to generated random users using Faker lib
#  

from django.core.management.base import BaseCommand, CommandError
from testmodule.models import Profile
from django.contrib.auth.hashers import make_password
# using faker to fake some data
from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num', nargs='+', type=int)

    def handle(self, *args, **options):
        # print(options.get('num'))
        number = options.get('num')[0]   # notice: options.get('num') is a list
        if number is None:
            number = 5
        password = make_password('123456')
        # faker = Faker(locale="zh_CN") locale: language settings
        faker = Faker()
        for _ in range(int(number)):
            data = {
                'username': faker.name_male(),
                'password': password,
            }
            print(type(data["username"]))
            print(data["username"])
            print(data["password"])
            try:
                pp = Profile.objects.create(
                    **data
                )
                # pp.save()
            except:
                CommandError('fail')
            self.stdout.write(self.style.SUCCESS(
                'Successfully create user "%s"' % faker.name_male()))
