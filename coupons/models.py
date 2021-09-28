import uuid
import datetime
from datetime import date
from django.db import models


class Coupon(models.Model):

    code = models.CharField("Código", max_length=25, blank=True, null=True, unique=True)
    order_date = models.DateField("Data to pedido")
    order_id = models.CharField("Id do pedido", max_length=50)
    customer_cpf = models.CharField("CPF do cliente", max_length=11, help_text="Somente números")
    valid_until = models.DateField("Data de Validade", null=True, blank=True)
    used_in = models.DateField("Utilizado em", null=True, blank=True)

    class Meta:
        verbose_name = "Cupom"
        verbose_name_plural = "Cupons"
        ordering = ["-order_date"]

    def __str__(self) -> str:
        return f"[{self.customer_cpf}] - {self.code}"

    def save(self, *args, **kwargs):
        code = self.code
        if not self.pk:
            self.valid_until = self.add_years(self.order_date, 1)
            code = uuid.uuid4().hex[:10].upper()
            while Coupon.objects.filter(code=code).exists():
                code = uuid.uuid4().hex[:10].upper()
        self.code = code
        super(Coupon, self).save(*args, **kwargs)

    def add_years(self, base_date, years):
        try:
            return base_date.replace(year=base_date.year + years)
        except ValueError:
            return base_date + (date(base_date.year + years, 1, 1) - date(base_date.year, 1, 1))

    def is_expired(self):
        return self.valid_until < datetime.datetime.today().date()
