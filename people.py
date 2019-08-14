class people:

    all_people = {person : dict() for person in people}

    def __init__(self, clock_num, first_name, last_name,seniority_date, benefit_date, area):
        self.clock_num = clock_num
        self.first_name = first_name
        self.last_name = last_name
        self.seniority_date = seniority_date
        self.benefit_date = benefit_date
        self.area = area

    def make_record():
        person = {
            'clock_num': input('Clock number: \n'),
            'first_name': input('First name: \n'),
            'last_name': input('Last name: \n'),
            'seniority_date': date_name('seniority date'),
            'benefit_date': date_name('benefit date'),
            'area': input('Area: \n'),
            }
        prompt = print('Please enter the following information:')

    # Decorator for date inputs, probably could put in another file and import
    # along side the 'people' class/function
    
    def datetimer(func):
        def function_wrapper(X):
            print('Enter your ', X, 'in \n YYYY, MM, DD format.')
            func(X)
            date_entry = input(': ')
            year, month, day = map(int, date_entry.split(', '))
            return date(year, month, day)
        return function_wrapper


    @datetimer
    def date_name(X):
        pass
