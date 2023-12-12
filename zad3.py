# domasna zadaca 1

# domasna zadaca 2

# domasna zadaca 2+ : Da se isprintaat site atributi za zadaden objekt od employee_list.


# zadaca 1
#Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.
# class Employee:
#     """
#     Klasa za vraboteni.
#     """
#     def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None, job_Offer=None):
#         """
#         Inicijalizirame objekt od klasata Employee.

#         :param first_name: str, ime
#         :param last_name: str, prezime
#         :param email: str, email
#         :param position: str, pozicija vo kompanijata
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.position = position
#         self.company = company
#         self.salary = salary
#         self.job_Offer = job_Offer

#     def receive_job_Offer(self, offer):
#         """
#         Ja primame ponudata za rabota

#         :param offer: JobOffer, ponuda 
#         """
#         self.job_Offer = offer

#     def accept_job_Offer(self):
#         """
#         Ja prifakjame ponudata za rabota
#         """
#         if self.job_Offer:
#             print(f'{self.first_name} prifakja ponuda za rabota.')
#             self.position = self.job_Offer.position
#             self.salary = self.job_Offer.salary
#             self.company = self.job_Offer.company
#         else:
#             print('Nema ponuda')

#     def reject_job_Offer(self):
#         """
#         Ja otfrlame ponudata za rabota.
#         """
#         if self.job_Offer:
#             print(f'{self.first_name} ja otfrla ponudata za rabota.')
#         else:
#             print('Nema ponuda')


# class JobOffer:
#     """
#     Klasa za ponuda na rabota
#     """
#     def __init__(self, position:str, company:str, salary:int):
#         """
#         Inicijalizirame objekt od klasata JobOffer.

#         :param position: str, pozicija
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.position = position
#         self.company = company
#         self.salary = salary


# class Company:
#     """
#     Klasa za kompanija.
#     """
#     def __init__(self, name:str, company_id:int, address=None):
#         """
#         Inicijalizirame objekt od klasata Company.

#         :param name: str, ime na kompanijata
#         :param company_id: int, unikaten broj na kompanija 
#         :param address: str, adresa
#         """
#         self.name = name
#         self.company_id = company_id
#         self.address = address
    
#     def hire(self, employee:Employee, position:str, salary:int):
#         """
#         Vrabotuvanje

#         :param employee: Employee, vraboten
#         :param position: str, pozicija
#         :param salary: int, plata
#         """
#         job_Offer = JobOffer(position, self.name, salary)
#         employee.receive_job_Offer(job_Offer)
#         print(f'{self.name} mu prati ponuda na  {employee.first_name}.')
#         print(f'Pozicija: {position}, Plata: {salary}, Kompanija: {self.name}')

# # Create instances of the Company class
# company1 = Company("Semos Makedonija", 123, "Address1" )
# company2 = Company("Company2", 567, "Address2")

# # Create instances of the Employee class
# employee1 = Employee("FirstName1", "LastName1", "user1@example.com", "developer", "Semos Makedonija")
# employee2 = Employee("FirstName2", "LastName2", "user2@example.com", "manager", "Company2")

# print(f"Employee 1: {employee1.first_name}, Position: {employee1.position}, Salary: {employee1.salary}")
# print(f"Employee 2: {employee2.first_name}, Position: {employee2.position}, Salary: {employee2.salary}")


# print(f"Company 1: {company1.name}, Id: {company1.company_id}, Address: {company1.address}")
# print(f"Company 1: {company2.name}, Id: {company2.company_id}, Address: {company2.address}")


# zadaca 2
# Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.



# zadaca 3
# Da se napise metod days_off so koj employee ke ima pravo da bara denovi odmor.
# Pritoa imame annual leave, special circumstances leave, maternity leave, sick days leave.

# class Employee:
#     """
#     Klasa za vraboteni.
#     """
#     def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None, job_Offer=None):
#         """
#         Inicijalizirame objekt od klasata Employee.

#         :param first_name: str, ime
#         :param last_name: str, prezime
#         :param email: str, email
#         :param position: str, pozicija vo kompanijata
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.position = position
#         self.company = company
#         self.salary = salary
#         self.job_Offer = job_Offer

#     def days_off(self, leave_type, requested_days):
#         """
#         Metod za baranje denovi odmor

#         :param leave_type: str, tip na odmor
#         :param requested_days: int, broj na barani denovi
#         """
#         if leave_type == 'annual':
#             print(f'{self.first_name} bara {requested_days} denovi godisen odmor.')
            
#         elif leave_type == 'special':
#             print(f'{self.first_name} bara {requested_days} denovi odmor za specificni okolnosti.')
           
#         elif leave_type == 'maternity':
#             print(f'{self.first_name} bara {requested_days} denovi odmor za porodilno.')
         
#         elif leave_type == 'sick':
#             print(f'{self.first_name} bara {requested_days} denovi odmor bidejki e bolen.')
            
#         else:
#             print('Nevalidno')

# employee1 = Employee("FirstName", "LastName", "user@example.com", "developer", "Semos Makedonija", 80000)
# employee1.days_off('annual', 20)
# employee1.days_off('special', 5)
# employee1.days_off('maternity', 20)
# employee1.days_off('sick', 3)
# employee1.days_off('invalid_type', 1)

# zadaca 4
# Da se napise metod promotion so koj employee ke moze da bide unapreden.

# class Employee:
#     """
#     Klasa za vraboteni.
#     """
#     def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None, job_Offer=None):
#         """
#         Inicijalizirame objekt od klasata Employee.

#         :param first_name: str, ime
#         :param last_name: str, prezime
#         :param email: str, email
#         :param position: str, pozicija vo kompanijata
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.position = position
#         self.company = company
#         self.salary = salary
#         self.job_Offer = job_Offer

#     def promotion(self, new_position):
#        """
#         Metod za unapreduvanje

#         :param new_position: str, nova pozicija
#         """
#        print(f"{self.first_name} bara unapreduvanje na pozicija {new_position}")
#        self.position=new_position

# employee1 = Employee("FirstName", "LastName", "user@example.com", "manager", "Semos Makedonija")
# employee1.promotion("senior developer")

# zadaca 5
# Da se napravi klasa Produkt.
# Da se dodadat zadolzitelni atriibuti pri kreiranje na instanca od Produkt: naziv, seriski_broj, cena, tip
# i opcionalen atribut kolicina.

# class Product:
#     def __init__(self, naziv:str, seriski_broj:str, cena:float, tip:str, kolicina=None):
#         """
#         Inicijalizacija na objekt od klasata Product.

#         :param naziv: str, naziv na produktot
#         :param seriski_broj: str, seriski broj na produktot
#         :param cena: float, cena na produktot
#         :param tip: str, tip na produktot
#         :param kolicina:opcionalno
        
#         """
#         self.naziv=naziv
#         self.seriski_broj=seriski_broj
#         self.cena=cena
#         self.tip=tip
#         self.kolicina=kolicina

# product1=Product("Amazfit watch", "MM1230", "4.499","Elektronika", kolicina=2)
# print(f"Product1: {product1.naziv}, Seriski broj: {product1.seriski_broj}, Cena: {product1.cena}, Tip: {product1.tip}, Kolicina:{product1.kolicina}")



# zadaca 6
# Da se napravi klasa Prodavnica.
# Instancata od prodavnicata, mora da ima: ime, seriski_broj.
# Da se kreira metod dodaj_produkt, koj kje dodava produkti vo prodavnicata,
# so toa sto mora da se proveri dali e od tip Produkt.
# class Product:
#     def __init__(self, naziv:str, seriski_broj:str, cena:float, tip:str, kolicina=None):
#         """
#         Inicijalizacija na objekt od klasata Product.

#         :param naziv: str, naziv na produktot
#         :param seriski_broj: str, seriski broj na produktot
#         :param cena: float, cena na produktot
#         :param tip: str, tip na produktot
#         :param kolicina:opcionalno
        
#         """
#         self.naziv=naziv
#         self.seriski_broj=seriski_broj
#         self.cena=cena
#         self.tip=tip
#         self.kolicina=kolicina

# class Store:
#     def __init__(self, ime: str, seriski_broj: str):
#         """
#         Inicijalizacija na objekt od klasata Store.

#         :param ime: str, ime na prodavnicata
#         :param seriski_broj: str, seriski broj na prodavnicata
#         """
#         self.ime = ime
#         self.seriski_broj= seriski_broj
#         self.product=[]

#     def dodaj_produkt(self, product):
#         """
#         Dodavanje na produkt vo prodavnicata.

#         :param product: Product, objekt od klasata Product
#         """
#         if isinstance(product, Product):
#             self.product.append(product)
#             print(f'{product.naziv} e dodaden/a vo prodavnicata {self.ime}.')
#         else:
#             print('Nevaliden produkt')


# store1 = Store("Store1", "AA234")
# store2 = Store("Store2", "BB234")

# product1 = Product("Laptop", "AB353", 27000, "Elektronika", kolicina=4)
# product2 = Product("Smartphone", "XYZ789", 50000, "Elektronika",kolicina=2)


# store1.dodaj_produkt(product1)
# store2.dodaj_produkt(product2)




# zadaca 7
# Da se kreira klasa Kupuvac.
# Sekoj Kupuvac mora da ima: ime, prezime, dostapni_paricni_sredstva.
# class Buyer:
#     def __init__(self, ime: str, prezime: str, dostapni_paricni_sredstva: float):
#         """
#         Inicijalizacija na objekt od klasata Buyer.

#         :param ime: str, ime na kupuvacot
#         :param prezime: str, prezime na kupuvacot
#         :param dostapni_paricni_sredstva: float, dostapni paricni sredstva na kupuvacot
#         """
#         self.ime=ime
#         self.prezime=prezime
#         self.dostapni_paricni_sredstva=dostapni_paricni_sredstva



# zadaca 8
# Da se kreiraat __str__ metodi za klasite.
# Da se kreira metod pecati_produkti na klasata Prodavnica koj sto kje gi printa site dostapni produkti.

# zadaca 9
#  Da se kreiraat 5 produkti.
# Da se kreiraat 2 prodavnici.
# Da se dodadat produkti vo prodavnicite.
# Da se kreiraat kupuvaci.
# Da se napravi scenario, kupuvacot da kupi produkt od prodavnica. Vo slucaj ako go nema produktot,
# da proba da go kupi produktot od drugata prodavnica.
# Pri kupuvanje na produkt od prodavnica, treba da se izbrise istoit od listata na produkti. Za ova da se koristi
# privaten metod __brisi_produkt.
# Da se vnimava na dostapnite sredstva na kupuvacot.
# domasna zadaca 1

# domasna zadaca 2

# domasna zadaca 2+ : Da se isprintaat site atributi za zadaden objekt od employee_list.


# zadaca 1
#Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.
# class Employee:
#     """
#     Klasa za vraboteni.
#     """
#     def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None, job_Offer=None):
#         """
#         Inicijalizirame objekt od klasata Employee.

#         :param first_name: str, ime
#         :param last_name: str, prezime
#         :param email: str, email
#         :param position: str, pozicija vo kompanijata
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.position = position
#         self.company = company
#         self.salary = salary
#         self.job_Offer = job_Offer

#     def receive_job_Offer(self, offer):
#         """
#         Ja primame ponudata za rabota

#         :param offer: JobOffer, ponuda 
#         """
#         self.job_Offer = offer

#     def accept_job_Offer(self):
#         """
#         Ja prifakjame ponudata za rabota
#         """
#         if self.job_Offer:
#             print(f'{self.first_name} prifakja ponuda za rabota.')
#             self.position = self.job_Offer.position
#             self.salary = self.job_Offer.salary
#             self.company = self.job_Offer.company
#         else:
#             print('Nema ponuda')

#     def reject_job_Offer(self):
#         """
#         Ja otfrlame ponudata za rabota.
#         """
#         if self.job_Offer:
#             print(f'{self.first_name} ja otfrla ponudata za rabota.')
#         else:
#             print('Nema ponuda')


# class JobOffer:
#     """
#     Klasa za ponuda na rabota
#     """
#     def __init__(self, position:str, company:str, salary:int):
#         """
#         Inicijalizirame objekt od klasata JobOffer.

#         :param position: str, pozicija
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.position = position
#         self.company = company
#         self.salary = salary


# class Company:
#     """
#     Klasa za kompanija.
#     """
#     def __init__(self, name:str, company_id:int, address=None):
#         """
#         Inicijalizirame objekt od klasata Company.

#         :param name: str, ime na kompanijata
#         :param company_id: int, unikaten broj na kompanija 
#         :param address: str, adresa
#         """
#         self.name = name
#         self.company_id = company_id
#         self.address = address
    
#     def hire(self, employee:Employee, position:str, salary:int):
#         """
#         Vrabotuvanje

#         :param employee: Employee, vraboten
#         :param position: str, pozicija
#         :param salary: int, plata
#         """
#         job_Offer = JobOffer(position, self.name, salary)
#         employee.receive_job_Offer(job_Offer)
#         print(f'{self.name} mu prati ponuda na  {employee.first_name}.')
#         print(f'Pozicija: {position}, Plata: {salary}, Kompanija: {self.name}')

# # Create instances of the Company class
# company1 = Company("Semos Makedonija", 123, "Address1" )
# company2 = Company("Company2", 567, "Address2")

# # Create instances of the Employee class
# employee1 = Employee("FirstName1", "LastName1", "user1@example.com", "developer", "Semos Makedonija")
# employee2 = Employee("FirstName2", "LastName2", "user2@example.com", "manager", "Company2")

# print(f"Employee 1: {employee1.first_name}, Position: {employee1.position}, Salary: {employee1.salary}")
# print(f"Employee 2: {employee2.first_name}, Position: {employee2.position}, Salary: {employee2.salary}")


# print(f"Company 1: {company1.name}, Id: {company1.company_id}, Address: {company1.address}")
# print(f"Company 1: {company2.name}, Id: {company2.company_id}, Address: {company2.address}")


# zadaca 2
# Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.



# zadaca 3
# Da se napise metod days_off so koj employee ke ima pravo da bara denovi odmor.
# Pritoa imame annual leave, special circumstances leave, maternity leave, sick days leave.

# class Employee:
#     """
#     Klasa za vraboteni.
#     """
#     def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None, job_Offer=None):
#         """
#         Inicijalizirame objekt od klasata Employee.

#         :param first_name: str, ime
#         :param last_name: str, prezime
#         :param email: str, email
#         :param position: str, pozicija vo kompanijata
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.position = position
#         self.company = company
#         self.salary = salary
#         self.job_Offer = job_Offer

#     def days_off(self, leave_type, requested_days):
#         """
#         Metod za baranje denovi odmor

#         :param leave_type: str, tip na odmor
#         :param requested_days: int, broj na barani denovi
#         """
#         if leave_type == 'annual':
#             print(f'{self.first_name} bara {requested_days} denovi godisen odmor.')
            
#         elif leave_type == 'special':
#             print(f'{self.first_name} bara {requested_days} denovi odmor za specificni okolnosti.')
           
#         elif leave_type == 'maternity':
#             print(f'{self.first_name} bara {requested_days} denovi odmor za porodilno.')
         
#         elif leave_type == 'sick':
#             print(f'{self.first_name} bara {requested_days} denovi odmor bidejki e bolen.')
            
#         else:
#             print('Nevalidno')

# employee1 = Employee("FirstName", "LastName", "user@example.com", "developer", "Semos Makedonija", 80000)
# employee1.days_off('annual', 20)
# employee1.days_off('special', 5)
# employee1.days_off('maternity', 20)
# employee1.days_off('sick', 3)
# employee1.days_off('invalid_type', 1)

# zadaca 4
# Da se napise metod promotion so koj employee ke moze da bide unapreden.

# class Employee:
#     """
#     Klasa za vraboteni.
#     """
#     def __init__(self, first_name:str, last_name:str, email:str, position:str, company:str, salary=None, job_Offer=None):
#         """
#         Inicijalizirame objekt od klasata Employee.

#         :param first_name: str, ime
#         :param last_name: str, prezime
#         :param email: str, email
#         :param position: str, pozicija vo kompanijata
#         :param company: str, kompanija
#         :param salary: int, plata
#         """
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.position = position
#         self.company = company
#         self.salary = salary
#         self.job_Offer = job_Offer

#     def promotion(self, new_position):
#        """
#         Metod za unapreduvanje

#         :param new_position: str, nova pozicija
#         """
#        print(f"{self.first_name} bara unapreduvanje na pozicija {new_position}")
#        self.position=new_position

# employee1 = Employee("FirstName", "LastName", "user@example.com", "manager", "Semos Makedonija")
# employee1.promotion("senior developer")

# zadaca 5
# Da se napravi klasa Produkt.
# Da se dodadat zadolzitelni atriibuti pri kreiranje na instanca od Produkt: naziv, seriski_broj, cena, tip
# i opcionalen atribut kolicina.

# class Product:
#     def __init__(self, naziv:str, seriski_broj:str, cena:float, tip:str, kolicina=None):
#         """
#         Inicijalizacija na objekt od klasata Product.

#         :param naziv: str, naziv na produktot
#         :param seriski_broj: str, seriski broj na produktot
#         :param cena: float, cena na produktot
#         :param tip: str, tip na produktot
#         :param kolicina:opcionalno
        
#         """
#         self.naziv=naziv
#         self.seriski_broj=seriski_broj
#         self.cena=cena
#         self.tip=tip
#         self.kolicina=kolicina

# product1=Product("Amazfit watch", "MM1230", "4.499","Elektronika", kolicina=2)
# print(f"Product1: {product1.naziv}, Seriski broj: {product1.seriski_broj}, Cena: {product1.cena}, Tip: {product1.tip}, Kolicina:{product1.kolicina}")



# zadaca 6
# Da se napravi klasa Prodavnica.
# Instancata od prodavnicata, mora da ima: ime, seriski_broj.
# Da se kreira metod dodaj_produkt, koj kje dodava produkti vo prodavnicata,
# so toa sto mora da se proveri dali e od tip Produkt.
# class Product:
#     def __init__(self, naziv:str, seriski_broj:str, cena:float, tip:str, kolicina=None):
#         """
#         Inicijalizacija na objekt od klasata Product.

#         :param naziv: str, naziv na produktot
#         :param seriski_broj: str, seriski broj na produktot
#         :param cena: float, cena na produktot
#         :param tip: str, tip na produktot
#         :param kolicina:opcionalno
        
#         """
#         self.naziv=naziv
#         self.seriski_broj=seriski_broj
#         self.cena=cena
#         self.tip=tip
#         self.kolicina=kolicina

# class Store:
#     def __init__(self, ime: str, seriski_broj: str):
#         """
#         Inicijalizacija na objekt od klasata Store.

#         :param ime: str, ime na prodavnicata
#         :param seriski_broj: str, seriski broj na prodavnicata
#         """
#         self.ime = ime
#         self.seriski_broj= seriski_broj
#         self.product=[]

#     def dodaj_produkt(self, product):
#         """
#         Dodavanje na produkt vo prodavnicata.

#         :param product: Product, objekt od klasata Product
#         """
#         if isinstance(product, Product):
#             self.product.append(product)
#             print(f'{product.naziv} e dodaden/a vo prodavnicata {self.ime}.')
#         else:
#             print('Nevaliden produkt')


# store1 = Store("Store1", "AA234")
# store2 = Store("Store2", "BB234")

# product1 = Product("Laptop", "AB353", 27000, "Elektronika", kolicina=4)
# product2 = Product("Smartphone", "XYZ789", 50000, "Elektronika",kolicina=2)


# store1.dodaj_produkt(product1)
# store2.dodaj_produkt(product2)


# zadaca 7
# Da se kreira klasa Kupuvac.
# Sekoj Kupuvac mora da ima: ime, prezime, dostapni_paricni_sredstva.
# class Buyer:
#     def __init__(self, ime: str, prezime: str, dostapni_paricni_sredstva: float):
#         """
#         Inicijalizacija na objekt od klasata Buyer.

#         :param ime: str, ime na kupuvacot
#         :param prezime: str, prezime na kupuvacot
#         :param dostapni_paricni_sredstva: float, dostapni paricni sredstva na kupuvacot
#         """
#         self.ime=ime
#         self.prezime=prezime
#         self.dostapni_paricni_sredstva=dostapni_paricni_sredstva



# zadaca 8
# Da se kreiraat __str__ metodi za klasite.
# Da se kreira metod pecati_produkti na klasata Prodavnica koj sto kje gi printa site dostapni produkti.

# zadaca 9
#  Da se kreiraat 5 produkti.
# Da se kreiraat 2 prodavnici.
# Da se dodadat produkti vo prodavnicite.
# Da se kreiraat kupuvaci.
# Da se napravi scenario, kupuvacot da kupi produkt od prodavnica. Vo slucaj ako go nema produktot,
# da proba da go kupi produktot od drugata prodavnica.
# Pri kupuvanje na produkt od prodavnica, treba da se izbrise istoit od listata na produkti. Za ova da se koristi
# privaten metod __brisi_produkt.
# Da se vnimava na dostapnite sredstva na kupuvacot.
