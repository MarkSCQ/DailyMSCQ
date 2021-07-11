Django insert data:
1. How to make custom command
   1. https://blog.csdn.net/wangfan741/article/details/109964718
   2. https://docs.djangoproject.com/zh-hans/3.1/howto/custom-management-commands/
2. load json file to Django
   1. Foreign key: using pk value to make a reference
   2. if the target model has primary, using primary key value as instead of using pk value. In the example Json code below, the uuid is functioned as the primariy key value of the foreign key. Normally, when there is no primary key, using pk value, if primary key value exists, use primary key value

            Example
            {
            "model": "testmodule.Choices",
            "pk": 1,
            "fields": {
                "ChoiceQues": "ef0a23d5-ef36-4017-8392-89c2182b0459",
                "ChoiceAnswerA": "Choice Answer A",
                "ChoiceAnswerB": "Choice Answer B",
                "ChoiceAnswerC": "Choice Answer C",
                "ChoiceAnswerD": "Choice Answer D",
                "ChoiceCorrect": "A",
                "ChoiceExplanation": "Explanation of this Question"
            }
        } 


Make Mirgration and Migrate；
1. Each time want to remvoe all dataset and migrations, remember removing the sqlite file
2. If the project has many different types of users, using inhritance maybe a good choice
    reference ：https://stackoverflow.com/questions/33554401/setting-up-foreignkeys-in-loaddata-for-django

        class Profile(AbstractUser):
            def __str__(self):
                return self.username

            class Meta:
                verbose_name = "User Profile"
                verbose_name_plural = verbose_name
