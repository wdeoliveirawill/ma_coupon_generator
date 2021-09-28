from datetime import datetime
from typing import Any
from django.contrib import admin
from django.contrib.admin.utils import model_ngettext
from django.db import models
from django.db.models import query
from django.http.request import HttpRequest
from django.template.response import TemplateResponse
from django.utils.html import format_html

from coupons.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    model = Coupon
    list_display = [
        "formatted_order_date",
        "customer_cpf",
        "order_id",
        "code",
        "valid_until",
        "used_in",
        "show_coupon_status",
    ]
    list_display_links = [
        "formatted_order_date",
        "customer_cpf",
        "order_id",
        "code",
        "valid_until",
        "used_in",
    ]
    actions = ["mark_as_used"]
    readonly_fields = ["code", "valid_until", "used_in"]
    search_fields = ["code", "customer_cpf", "order_id"]
    list_filter = ["order_date", "valid_until", "used_in"]

    def has_delete_permission(self, request: HttpRequest, obj: Any = None) -> bool:
        return False

    def show_coupon_status(self, obj):
        html = '<h4><span class="badge bg-{}">{}</span></h4>'
        if obj.is_expired():
            return format_html(html, "danger", "EXPIRADO")
        elif obj.used_in:
            return format_html(html, "danger", "JÁ UTILIZADO")
        else:
            return format_html(html, "success", "DISPONÍVEL")

    show_coupon_status.short_description = "Status"
    show_coupon_status.allow_tags = True

    def formatted_order_date(self, obj):
        return obj.order_date.strftime("%d/%m/%Y")

    formatted_order_date.short_description = "Data Pedido"
    formatted_order_date.admin_order_field = "order_date"

    def require_confirmation(func):
        def get_available_and_unavailable(queryset):
            available = []
            unavailable = []
            if isinstance(queryset, models.query.QuerySet):
                for item in queryset.all():
                    if item.used_in:
                        unavailable.append({"reason": " Cupom já utilizado", "item": item})
                    elif item.is_expired():
                        unavailable.append({"reason": " Cupom expirado", "item": item})
                    else:
                        available.append(item)

            return available, unavailable

        def wrapper(modeladmin, request, queryset):
            if request.POST.get("confirmation") is None:
                request.current_app = modeladmin.admin_site.name
                opts = modeladmin.model._meta
                objects_name = model_ngettext(queryset)
                available, unavailable = get_available_and_unavailable(queryset)
                context = {
                    **modeladmin.admin_site.each_context(request),
                    "title": "Você tem certeza?",
                    "objects_name": str(objects_name),
                    "queryset": queryset,
                    "opts": opts,
                    "action_checkbox_name": "Marcar selecionados como utilizados",
                    "media": modeladmin.media,
                    "available": available,
                    "unavailable": unavailable,
                    "action": request.POST["action"],
                }
                return TemplateResponse(request, "admin/action_confirmation.html", context)

            return func(modeladmin, request, queryset)

        wrapper.__name__ = func.__name__
        return wrapper

    @require_confirmation
    def mark_as_used(self, request, queryset):
        queryset.update(used_in=datetime.now())

    mark_as_used.short_description = "Marcar selecionados como utilizados"
