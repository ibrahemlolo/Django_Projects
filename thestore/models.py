from django.db import models

# Create your models here.
# Many_To_Many


class promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'proudact', on_delete=models.SET_NULL, null=True, related_name='+')


class proudact(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField(promotion)


class customer(models.Model):
    Membership_B = "B"
    Membership_S = "S"
    Membership_G = "G"

    Membership_statu = [
        (Membership_B, "Bronze"),
        (Membership_S, "Silver"),
        (Membership_G, "Gold"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=Membership_statu,default=Membership_B)

    class Meta:
        db_table = 'store_customer'
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]


class order(models.Model):
    payment_status_P = "P"
    payment_status_C = "C"
    payment_status_F = "F"

    payment_status_choise = [
        (payment_status_P, "Panding"),
        (payment_status_C, "Complete"),
        (payment_status_F, "Falid"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=payment_status_choise, default=payment_status_P)
    customer = models.ForeignKey(customer, on_delete=models.PROTECT)


class order_items(models.Model):
    order = models.ForeignKey(order, on_delete=models.PROTECT)
    proudact = models.ForeignKey(proudact, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)


class cart(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)


class cart_item(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    proudact = models.ForeignKey(proudact, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
