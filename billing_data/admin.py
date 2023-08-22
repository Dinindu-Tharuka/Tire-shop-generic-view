from django.contrib import admin
from .models import Bill, BillItems, BillServises, BillPayment, PaymentCheque, PaymentCash, PaymentCredit, PaymentCreditCard
from stock_data.models import StockItem

@admin.register(BillItems)
class BillItemAdmin(admin.ModelAdmin):
    pass

# @admin.register(BillServises)
# class BillServicesAdmin(admin.ModelAdmin):
#     pass


# @admin.register(PaymentCheque)
# class PaymentChequeAdmin(admin.ModelAdmin):
#     pass

# @admin.register(PaymentCash)
# class PaymentCashAdmin(admin.ModelAdmin):
#     pass

# @admin.register(PaymentCreditCard)
# class PaymentCreditCardAdmin(admin.ModelAdmin):
#     pass

# @admin.register(PaymentCredit)
# class PaymentCreditAdmin(admin.ModelAdmin):
#     pass

class PaymentCreditInline(admin.StackedInline):
    model = PaymentCredit
    extra = 1

class PaymentCreditCardInline(admin.StackedInline):
    model = PaymentCreditCard
    extra = 1

class PaymentCashInline(admin.StackedInline):
    model = PaymentCash
    extra = 1

class PaymentChequeInline(admin.StackedInline):
    model = PaymentCheque
    extra = 1

@admin.register(BillPayment)
class BillPaymentAdmin(admin.ModelAdmin):
    inlines = [PaymentCashInline, PaymentCreditCardInline,  PaymentChequeInline, PaymentCreditInline]

class BillItemInline(admin.TabularInline):
    model = BillItems
    extra = 1

class BillServisesInline(admin.StackedInline):
    model = BillServises
    extra = 1

class BillPaymentInline(admin.StackedInline):
    model = BillPayment
    extra = 1

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    inlines = [BillItemInline, BillServisesInline, BillPaymentInline]
