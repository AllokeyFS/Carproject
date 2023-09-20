from django.db import models
from decimal import Decimal
from datetime import datetime

class CarsBrand(models.Model):
    name = models.CharField(max_length=30, verbose_name='Brand name', unique=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Car Brand'
        verbose_name_plural = 'Car Brands'


class CarsModel(models.Model):
    brand = models.ForeignKey(CarsBrand, on_delete=models.CASCADE, verbose_name='Brand name')
    model = models.CharField(max_length=30, verbose_name='Model name')


    def __str__(self) -> str:
        return f'{self.brand.name} {self.model}'
    
    class Meta:
        verbose_name = 'Car Model'
        verbose_name_plural = 'Car Models'

class CarsColor(models.Model):
    color = models.CharField(max_length=30, verbose_name='Car Color')

    def __str__(self) -> str:
        return self.color
    
    class Meta:
        verbose_name = 'Car Color'
        verbose_name_plural = 'Car Colors'

class Country(models.Model):
    name = models.CharField(max_length=40, verbose_name='Country', unique=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

class Cars(models.Model):
    KPP_CHOICES = (
        ('akpp', 'Automatic'),
        ('kpp', 'Manual'),
        ('tiptronic', 'Tiptronic'),
        ('variator', 'Variator'),
        ('robot', 'Robot'),
    )

    WD_CHOICES = (
        ('FWD', 'Front Wheel Drive'),
        ('RWD', 'Rear Wheel Drive'),
        ('4WD', '4WD'),
        ('AWD', 'All Wheel Drive'),
    )
    STEERING_WHEEL_CHOICES = (
        ('right', 'Right'),
        ('left', 'Left'),
    )
    CARCASE_CHOICES = (
        ('sedan', 'Sedan'),
        ('limousine', 'Limousine'),
        ('pickup', 'Pickup'),
        ('crossover', 'Crossover'),
        ('hatchback', 'Hatchback'),
        ('wagon', 'Wagon'),
        ('liftback', 'Liftback'),
        ('minivan', 'Minivan'),
        ('coupe', 'Coupe'),
        ('cabriolet', 'Cabroilet'),
        ('roadster', 'Roadster'),
        ('targa', 'Targa')
    )
    FUEL_CHOICES = (
        ('petrol', 'Petrol'),
        ('gas', 'Gas'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electro', 'Electrical'),
    )
    STATE_CHOICES = (
        ('used', 'Used'),
        ('new', 'New'),
        ('good', 'Good'),
        ('ideal', 'Ideal'),
        ('for_parts', 'For parts'),
        ('accident', 'Accidental'),
        ('crashed', 'Crashed'),
        ('repainted', 'Repainted'),
)
    VIN_CHOICES = [
        ('vin_code', 'Has VIN code'),
        ('no_vin_code', 'Has not VIN code'),
    ]

    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('KGS', 'KGS'),
    )

    VEHICLE_TYPE_CHOICES = (
        ('car', 'Passenger'),
        ('bus', 'Bus'),
        ('truck', 'Truck'),
        ('rental', 'Rental'),
        ('commercial', 'Commercial'),
        ('special', 'Special'),
    )


    cars = models.ForeignKey(CarsModel, on_delete=models.PROTECT,verbose_name='Car name')
    year = models.IntegerField(choices=[(year, str(year)) for year in range(1900, 2100)],default=2023 ,verbose_name='Year of issue')
    currency = models.CharField(max_length=15, choices=CURRENCY_CHOICES, verbose_name='Currency')
    price = models.BigIntegerField(default=0)
    mileage = models.IntegerField(verbose_name='Mileage', default=0)
    colors = models.ForeignKey(CarsColor, on_delete=models.PROTECT, verbose_name='Car Color')
    kpp = models.CharField(max_length=30, choices=KPP_CHOICES, verbose_name='KPP')
    wd = models.CharField(max_length=20, choices=WD_CHOICES, verbose_name='Wheel Drive')
    steering_wheel = models.CharField(max_length=15, choices=STEERING_WHEEL_CHOICES, verbose_name='Steering wheel')
    vehicle_type = models.CharField(max_length=30, choices=VEHICLE_TYPE_CHOICES, verbose_name='Vehicle type')
    carcase = models.CharField(max_length=30, choices=CARCASE_CHOICES, verbose_name='Carcase')
    fuel = models.CharField(max_length=30, choices=FUEL_CHOICES, verbose_name='Fuel')
    state = models.CharField(max_length=30, choices=STATE_CHOICES, verbose_name='State')
    vin = models.CharField(max_length=30, choices=VIN_CHOICES ,verbose_name='VIN code')
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1, choices=[(Decimal(str(v)), "{:.1f}".format(v)) for v in [i * 0.1 for i in range(5, 101)]],default=0.5, verbose_name='Engine volume')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Country')
    description = models.TextField(verbose_name='Description')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')

    def __str__(self) -> str:
        return f'{self.cars}'
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class MotorcycleBrand(models.Model):
    name = models.CharField(max_length=50, verbose_name='Motorcycle Brand')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Motorcycle brand'
        verbose_name_plural = 'Motorcycle brands'


class MotorcycleModel(models.Model):
    brand = models.ForeignKey(MotorcycleBrand, on_delete=models.CASCADE, verbose_name='Motorcycle brand')
    model = models.CharField(max_length=30, verbose_name='Motorcycle model')

    def __str__(self) -> str:
        return f'{self.brand}'
    
    class Meta:
        verbose_name = 'Motorcycle model'
        verbose_name_plural = 'Motorcycle models'


class Motorcycle(models.Model):

    TYPE_CHOICES = (
        ('moped', 'Мопед'),
        ('scooter', 'Скутер'),
        ('sport', 'Спортивный мотоцикл'),
        ('cruiser', 'Круизер'),
        ('touring', 'Туринговый мотоцикл'),
        ('dirt_bike', 'Дирт-байк'),
        ('naked_bike', 'Нейкед-байк'),
        ('adventure', 'Приключенческий мотоцикл'),
        ('cafe_racer', 'Кафе-рейсер'),
        ('chopper', 'Чоппер'),
        ('bobber', 'Боббер'),
        ('off-road', 'Внедорожный мотоцикл'),
        ('trike', 'Трайк'),
        ('atv', 'Квадроцикл'),
        ('electric', 'Электромотоцикл'),
        ('vintage', 'Винтажный мотоцикл')
    )

    FUEL_CHOICES = (
        ('petrol', 'Petrol'),
        ('gas', 'Gas'),
        ('diesel', 'Diesel'),
        ('hybrid', 'Hybrid'),
        ('electro', 'Electrical'),
    )
    STATE_CHOICES = (
        ('used', 'Used'),
        ('new', 'New'),
        ('good', 'Good'),
        ('ideal', 'Ideal'),
        ('for_parts', 'For parts'),
        ('accident', 'Accidental'),
        ('crashed', 'Crashed'),
        ('repainted', 'Repainted'),
)
    VIN_CHOICES = [
        ('vin_code', 'Has VIN code'),
        ('no_vin_code', 'Has not VIN code'),
    ]

    CURRENCY_CHOICES = (
        ('USD', 'USD'),
        ('KGS', 'KGS'),
    )
    KPP_CHOICES = (
        ('akpp', 'Automatic'),
        ('kpp', 'Manual'),
    )

    motorcycle = models.ForeignKey(MotorcycleModel, on_delete=models.PROTECT, verbose_name='Motorcycle')
    color = models.ForeignKey(CarsColor, on_delete=models.PROTECT, verbose_name='Motorcycle color  ')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Country')
    year = models.IntegerField(choices=[(year, str(year)) for year in range(1900, 2100)],null=True, blank=True, verbose_name='Year of issue')
    currency = models.CharField(max_length=15, choices=CURRENCY_CHOICES, verbose_name='Currency')
    price = models.BigIntegerField(null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True, verbose_name='Mileage')
    vehicle_type = models.CharField(max_length=30, choices=TYPE_CHOICES, verbose_name='Motorcycle type')
    kpp = models.CharField(max_length=30, choices=KPP_CHOICES, verbose_name='KPP')
    fuel = models.CharField(max_length=30, choices=FUEL_CHOICES, verbose_name='Fuel')
    state = models.CharField(max_length=30, choices=STATE_CHOICES, verbose_name='State')
    vin = models.CharField(max_length=30, choices=VIN_CHOICES, verbose_name='VIN code')
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1, choices=[(Decimal(str(v)), "{:.1f}".format(v)) for v in [i * 0.1 for i in range(5, 101)]], null=True, blank=True, verbose_name='Engine volume')
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Country')
    description = models.TextField(verbose_name='Description')
    publication_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication date')


    def __str__(self) -> str:
        return f'{self.motorcycle}'
    
    class Meta:
        verbose_name = 'Motorcycle'
        verbose_name_plural = 'Motorcycles'


class CarPart(models.Model):
    STATE_CHOICES = (
        ('used', 'Used'),
        ('new', 'New'),
        ('good', 'Good'),
        ('ideal', 'Ideal'),
        )

    name = models.CharField(max_length=50, verbose_name='Spare part name')
    car = models.ForeignKey(CarsModel, on_delete=models.PROTECT, verbose_name='Spare part for car')
    year = models.DateField(null=True, blank=True, verbose_name='Year of issue')
    price = models.IntegerField(verbose_name='Price')
    state = models.CharField(max_length=10, choices=STATE_CHOICES, verbose_name='Part state')

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

