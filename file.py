class Employee:
    """
    Klasa za vraboteni.
    """
    def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None, job_Offer=None):
        """
        Inicijalizirame objekt od klasata Employee.

        :param first_name: str, ime
        :param last_name: str, prezime
        :param email: str, email
        :param position: str, pozicija vo kompanijata
        :param company: str, kompanija
        :param salary: int, plata
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary
        self.job_Offer = job_Offer

    def receive_job_Offer(self, offer):
        """
        Ja primame ponudata za rabota

        :param offer: JobOffer, ponuda 
        """
        self.job_Offer = offer

    def accept_job_Offer(self):
        """
        Ja prifakjame ponudata za rabota
        """
        if self.job_Offer:
            print(f'{self.first_name} prifakja ponuda za rabota.')
            self.position = self.job_Offer.position
            self.salary = self.job_Offer.salary
            self.company = self.job_Offer.company
            

        else:
            print('Nema ponuda')

    def reject_job_Offer(self):
        """
        Ja otfrlame ponudata za rabota.
        """
        if self.job_Offer:
            print(f'{self.first_name} ja otfrla ponudata za rabota.')
            
        else:
            print('Nema ponuda')


class JobOffer:
    """
    Klasa za ponuda na rabota
    """
    def __init__(self, position:str, company:str, salary:int):
        """
        Inicijalizirame objekt od klasata JobOffer.

        :param position: str, pozicija
        :param company: str, kompanija
        :param salary: int, plata
        """
        self.position = position
        self.company = company
        self.salary = salary


class Company:
    """
    Klasa za kompanija.
    """
    def __init__(self, name:str, company_id:int, address=None):
        """
        Inicijalizirame objekt od klasata Company.

        :param name: str, ime na kompanijata
        :param company_id: int, unikaten broj na kompanija 
        :param address: str, adresa
        """
        self.name = name
        self.company_id = company_id
        self.address = address
    
    def hire(self, employee:Employee, position:str, salary:int):
        """
        Vrabotuvanje

        :param employee: Employee, vraboten
        :param position: str, pozicija
        :param salary: int, plata
        """
        job_Offer = JobOffer(position, self.name, salary)
        employee.receive_job_Offer(job_Offer)
        print(f'{self.name} mu prati ponuda na  {employee.first_name}.')
        print(f'Pozicija: {position}, Plata: {salary}, Kompanija: {self.name}')

semos_mk = Company("Semos Makedonija", 1234)
ime1 = Employee("Ime1", "Prezime1", "ime1@ime1.com", "developer", "semos_mk")

print(ime1.position, ime1.salary)
semos_mk.hire(ime1, 'support', 10000000)


