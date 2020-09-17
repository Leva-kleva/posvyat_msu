from django import forms
from .models import Team


class TeamForm(forms.Form):
        TYPESTUDY = (
            ("бак", "бакалавриат"),
            ("спец", "специалитет"),
            ("маг", "магистратура"),
        )
        WHERE = (
            ("Увидел афишу/получил флаер", "Увидел афишу/получил флаер"),
            ("Узнал от друзей", "Узнал от друзей"),
            ("Из группы Профсоюзной организации VK",
             "Из группы Профсоюзной организации VK"),
            ("Из аккаунта Профсоюзной организации в Instagram",
             "Из аккаунта Профсоюзной организации в Instagram"),
            ("Прочитал в Профсоюзном путеводителе для студентов МГУ",
             "Прочитал в Профсоюзном путеводителе для студентов МГУ"),
            ("Узнал на факультете (кураторы/групповоды/...)", "Узнал на факультете (кураторы/групповоды/...)"),
            ("Другое", "Другое"),
        )
        ENTER = (
            ('YES', 'Да'),
            ('NO', 'Нет'),
        )
        FACULTY = (
            ("0", "----"),
            ("1", "Механико–математический факультет"),
            ("2", "Факультет вычислительной математики и кибернетики"),
            ("3", "Физический факультет"),
            ("4", "Химический факультет"),
            ("5", "Факультет наук о материалах"),
            ("6", "Биологический факультет"),
            ("7", "Факультет биоинженерии и биоинформатики"),
            ("8", "Факультет почвоведения"),
            ("9", "Геологический факультет"),
            ("10", "Географический факультет"),
            ("11", "Факультет фундаментальной медицины"),
            ("12", "Факультет фундаментальной физико-химической инженерии"),
            ("13", "Биотехнологический факультет"),
            ("14", "Факультет космических исследований"),
            ("15", "Исторический факультет"),
            ("16", "Филологический факультет"),
            ("17", "Философский факультет"),
            ("18", "Экономический факультет"),
            ("19", "Юридический факультет"),
            ("20", "Факультет журналистики"),
            ("21", "Факультет психологии"),
            ("22", "Институт стран Азии и Африки"),
            ("23", "Социологический факультет"),
            ("24", "Факультет иностранных языков и регионоведения"),
            ("25", "Факультет государственного управления"),
            ("26", "Факультет мировой политики"),
            ("27", "Факультет искусств"),
            ("28", "Факультет глобальных процессов"),
            ("29", "Факультет педагогического образования"),
            ("30", "Факультет политологии"),
            ("31", "Высшая школа бизнеса (факультет)"),
            ("32", "Московская школа экономики(факультет)"),
            ("33", "Высшая школа перевода(факультет)"),
            ("34", "Высшая школа государственного администрирования(факультет)"),
            ("35", "Высшая школа государственного аудита(факультет)"),
            ("36", "Высшая школа управления и инноваций(факультет)"),
            ("37", "Высшая школа инновационного бизнеса(факультет)"),
            ("38", "Высшая школа современных социальных наук(факультет)"),
            ("39", "Высшая школа телевидения(факультет)"),
            ("40", "Высшая школа культурной политики и управления в гуманитарной сфере(факультет)")
        )

        name = forms.CharField(label="Название")
        typestudy = forms.ChoiceField(label="форма обучения", choices=TYPESTUDY)

        secondname0 = forms.CharField(label="Фамилия")
        firstname0 = forms.CharField(label="Имя")
        faculty0 = forms.ChoiceField(label="Факультет", choices=FACULTY)
        mail0 = forms.EmailField(label="Электронная почта")
        #phone0 = forms.RegexField(label="Номер телефона", regex='^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\-]?)?[\d\- ]{7,10}$',
        #                          error_messages={'invalid': 'Номер телефона в формате +7xxxxxxxxxx',
        #                                          'required': 'Введите номер телефона в формате +7xxxxxxxxxx'})
        phone0 = forms.CharField(label="Номер телефона", widget=forms.TextInput({'class': 'phone_mask'}))
        vk0 = forms.CharField(label="Ссылка на страницу в ВК")

        secondname1 = forms.CharField(label="Фамилия")
        firstname1 = forms.CharField(label="Имя")
        faculty1 = forms.ChoiceField(label="Факультет", choices=FACULTY)
        mail1 = forms.EmailField(label="Электронная почта")

        secondname2 = forms.CharField(label="Фамилия")
        firstname2 = forms.CharField(label="Имя")
        faculty2 = forms.ChoiceField(label="Факультет", choices=FACULTY)
        mail2 = forms.EmailField(label="Электронная почта")

        secondname3 = forms.CharField(label="Фамилия")
        firstname3 = forms.CharField(label="Имя")
        faculty3 = forms.ChoiceField(label="Факультет", choices=FACULTY)
        mail3 = forms.EmailField(label="Электронная почта")

        secondname4 = forms.CharField(label="Фамилия", required=False)
        firstname4 = forms.CharField(label="Имя", required=False)
        faculty4 = forms.ChoiceField(label="Факультет", choices=FACULTY, required=False)
        mail4 = forms.EmailField(label="Электронная почта", required=False)

        secondname5 = forms.CharField(label="Фамилия", required=False)
        firstname5 = forms.CharField(label="Имя", required=False)
        faculty5 = forms.ChoiceField(label="Факультет", choices=FACULTY, required=False)
        mail5 = forms.EmailField(label="Электронная почта", required=False)

        agree = forms.BooleanField(label="Согласие")
        where = forms.MultipleChoiceField(label="где узнал", choices=WHERE, widget=forms.CheckboxSelectMultiple({"id": "kek"}))

        enter = forms.ChoiceField(label="вступил в опк?", choices=ENTER)
