def makename(name):
    def wrapped(self):
        names = self.split(' ')
        names_list = list()
        i = 0
        for name in names:

            name = name.lower().replace('ц', 'ts').replace('ч', 'ch').replace('ю',
                                                                              'yu').replace(
                'а', 'a').replace('б', 'b').replace('қ', 'q').replace('қ', "o'").replace('ғ', "g'").replace('ҳ',
                                                                                                            "h'").replace(
                'в', 'v').replace('г', 'g').replace('д', 'd').replace('е',
                                                                      'e').replace(
                'ё', 'yo').replace('ж', 'j').replace('з', 'z').replace('и', 'i').replace('й', 'y').replace('к',
                                                                                                           'k').replace(
                'л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р',
                                                                                                          'r').replace(
                'с', 's').replace('т', 't').replace('у', 'u').replace('ш', 'sh').replace('щ', 'sh').replace('ф',
                                                                                                            'f').replace(
                'э', 'e').replace('ы', 'i').replace('я', 'ya').replace('ў',"o'").replace('ь', "'").replace('ъ', "'").replace('*',
                                                                                                           '').replace(
                '!', '').replace('~', '').replace('@', '').replace('#', '').replace('№', '').replace('$', '').replace(
                '%', '').replace('^', '').replace(':', '').replace('&', '').replace('?', '').replace('(', '').replace(
                ')', '').replace('-', '').replace('+', '').replace('=', '').replace('/', '').replace('<', '').replace(
                '>', '').replace('|', '').replace('€', '').replace('`',"'").replace(';',"'").replace('"',"'")

            i += 1
            if i != 4:
                name = name.capitalize()
            names_list.append(name)
        final_name = ' '.join(names_list)

        return final_name

    return wrapped


def makepassport(passport):
    def wrapped(self):
        passport = str(self)
        passport = passport.replace('А', 'A').replace('В', 'B').replace('С', 'C').replace('Т', 'T').replace('О',
                                                                                                          'O').replace(
            'М', 'M').replace('Р', 'P').replace('Ф', 'F').replace('Й', 'Y').replace('У', 'U').replace('К', 'K').replace('Е', 'E').replace('Ц', 'TS').replace('Н', 'N').replace('Г', 'G').replace('Ш', 'SH').replace('З', 'Z').replace('Х', 'X').replace('П', 'P').replace('Л', 'L').replace('Ж', 'J').replace('Э', 'Е').replace('Я', 'YA').replace('Ч', 'CH').replace('И', 'I').replace('Б', 'B').replace('Ю', 'YU').replace(' ','').replace('*','').replace('!', '').replace('~', '').replace('@', '').replace('#', '').replace('№', '').replace('$', '').replace(
                '%', '').replace('^', '').replace(':', '').replace('&', '').replace('?', '').replace('(', '').replace(
                ')', '').replace('-', '').replace('+', '').replace('=', '').replace('/', '').replace('<', '').replace(
                '>', '').replace('|', '').replace('€', '').replace('`',"'").replace(';',"'").replace('"',"'").replace('   ','')

        return passport
    return wrapped



def makeaddress(address):
    def wrapped(self):
        address = str(self)
        address = address.lower().replace('ц', 'ts').replace('ч', 'ch').replace('ю',
                                                                              'yu').replace(
                'а', 'a').replace('б', 'b').replace('қ', 'q').replace('қ', "o'").replace('ғ', "g'").replace('ҳ',
                                                                                                            "h'").replace(
                'в', 'v').replace('г', 'g').replace('д', 'd').replace('е',
                                                                      'e').replace(
                'ё', 'yo').replace('ж', 'j').replace('з', 'z').replace('и', 'i').replace('й', 'y').replace('к',
                                                                                                           'k').replace(
                'л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р',
                                                                                                          'r').replace(
                'с', 's').replace('т', 't').replace('у', 'u').replace('ш', 'sh').replace('щ', 'sh').replace('ф',
                                                                                                            'f').replace(
                'э', 'e').replace('ы', 'i').replace('я', 'ya').replace('ў',"o'").replace('ь', "'").replace('ъ', "'").replace('*',
                                                                                                           '').replace(
                '!', '').replace('~', '').replace('@', '').replace('#', '').replace('№', '').replace('$', '').replace(
                '%', '').replace('^', '').replace(':', '').replace('&', '').replace('?', '').replace('(', '').replace(
                ')', '').replace('+', '').replace('=', '').replace('/', '').replace('<', '').replace(
                '>', '').replace('|', '').replace('€', '').replace('`',"'").replace(';',"'").replace('"',"'")

        return address.capitalize()

    return wrapped

@makename
def get_name(name):
    return name


@makepassport
def get_passport(passport):
    return passport


@makeaddress
def get_address(address):
    return address