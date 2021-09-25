from datetime import datetime
from typing import Any
from django.http.request import HttpRequest
from coupons.models import Coupon
from django.contrib import admin


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    model = Coupon
    list_display = [
        "order_date",
        "customer_cpf",
        "order_id",
        "code",
        "valid_until",
        "used_in",
        "show_coupon_status",
    ]
    list_display_links = ["order_date", "customer_cpf", "order_id", "code", "valid_until", "used_in"]
    readonly_fields = ["code", "valid_until", "used_in"]
    search_fields = ["code", "customer_cpf", "order_id"]
    list_filter = ["order_date", "valid_until", "used_in"]

    def has_delete_permission(self, request: HttpRequest, obj: Any = None) -> bool:
        return False

    def show_coupon_status(self, obj):
        if obj.valid_until < datetime.today().date():
            return "EXPIRADO"
        elif obj.used_in is not None:
            return "JÁ UTILIZADO"
        else:
            return "DISPONÍVEL"

    show_coupon_status.short_description = "Status"
