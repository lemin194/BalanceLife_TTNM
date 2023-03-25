from django.db import models

# Create your models here.



class Food(models.Model):
    food_name = models.CharField(max_length=30)
    fat = models.DecimalField(max_digits=15, decimal_places=2, default=100)
    calories = models.DecimalField(max_digits=15, decimal_places=2, default=100)
    proteins = models.DecimalField(max_digits=15, decimal_places=2, default=100)
    carbohydrates = models.DecimalField(max_digits=15, decimal_places=2, default=100)
    serving = models.IntegerField(default=100)
    def __str__(self):
        return self.food_name

        

class Meal(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    def __str__(self):
        return self.title + ' ' + self.time.strftime('%Y-%m-%d %H:%M')

class NutrientCategory(models.Model):
    category_name = models.CharField(max_length = 200)
    class Meta:
        verbose_name = 'Nutrient Category'
        verbose_name_plural = 'Nutrient Categories'
    
    def __str__(self):
        return f'{self.category_name}'
    
    @property
    def count_nutrient_by_category(self):
        return Nutrient.objects.filter(category=self).count()
class Nutrient(models.Model) :
    name = models.CharField(max_length=200)
    rda = models.DecimalField(max_digits=15, decimal_places=2, default=100)
    wiki = models.TextField()
    required = models.BooleanField(default=True)
    _category = models.ForeignKey(NutrientCategory, default=None, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name}'

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category_name):
        try:
            if (category_name=='' or category_name==None) :
                self._category = None
            else:
                self._category = NutrientCategory.objects.all().get(category_name=category_name)
        except NutrientCategory.DoesNotExist:
            print("Category %s doesn't exist." % category_name)


class NutrientInstance(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=100)
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nutrient.name}'


class FoodInstance(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    amount = models.IntegerField(default=100)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    def __str__(self):
        return self.food.food_name
