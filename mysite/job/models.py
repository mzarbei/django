from django.db import models

#list all city
class city(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')

class address(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile =models.IntegerField()
    email  = models.EmailField()

class Store(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    #article = models.ForeignKey(Article, on_delete=models.CASCADE)

    sotre_address = models.CharField(max_length=300)
    


class job(models.Model):
    job_title  = models.CharField(max_length=200)
    job_address = models.CharField(max_length=500)
    job_owner = models.ForeignKey(Person, on_delete=models.CASCADE)

#centers for providing service for different customers
class service_center(models.manager):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')

    
#selling geroceiried products
class gerovery(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')



#Corporative centers
class service_corp(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')



#doctor office
#service providing for human, dental , pet and animals
class phesetion(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')


#heath and hospital center
class heath_center(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')



#drugstore list all drugstore 
class drugstore(model.class ModelName(models.Model):

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')
#list all car and product corpation dealers 
class dealers(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')

#learning centers language , car , carpenter, swinging
class learning_center(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')


# educational center university, schools,
class educational_center(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')

#travel agency 
class travel_agency(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')

# fuel center petrol, cng, gasoline

class fuel_station(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')


# touristic sites , parks, river, 
class touristic_site(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')


# job category geroceries, gold and jewelery, sands
class category(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')


# Expertise masonery, pipeline, blackstone, mdf, cabinet
class expertise(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')


# Selling products and properties, fruit, garden, farm, bycicle, home
class sellers(models.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')



# priviledges 


    def __str__(self):
        return 

    def __unicode__(self):
        return 

    

    def __str__(self):
        return 

    def __unicode__(self):
        return 



#office for service and other refferals
class office(model.Model):
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames')

# Create your models here.
