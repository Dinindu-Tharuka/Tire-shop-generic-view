from rest_framework import serializers
from billing_data.models import Bill, BillItems, BillServises, BillPayment
from billing_data.models import PaymentCash, PaymentCheque, PaymentCreditCard, PaymentCredit
from stock_data.models import StockItem

class BillItemsSerializer(serializers.ModelSerializer):
    bill = serializers.CharField(read_only=True)
    class Meta:
        model = BillItems
        fields = ['id', 'item', 'stock_item', 'bill', 'qty', 'customer_discount', 'customer_price']


class BillServicesSerilizer(serializers.ModelSerializer):
    bill = serializers.CharField(read_only = True)
    class Meta:
        model = BillServises
        fields =  ['id', 'service', 'employee', 'bill']


class PaymentCashSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCash
        fields =  ['id', 'bill_payment', 'date', 'payeename', 'amount']

class PaymentChequeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCheque
        fields = ['id', 'bill_payment', 'date', 'amount', 'cheque_no', 'payeename', 'bank', 'branch', 'cheque_date']

class PaymentCreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCreditCard
        fields = ['id', 'bill_payment', 'date', 'payeename', 'amount']

class PaymentCreditSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PaymentCredit
        fields = ['id', 'bill_payment', 'date', 'due_date', 'payeename', 'amount']

class BillPaymentSerializer(serializers.ModelSerializer):
    payments_cash = PaymentCashSerializer(many=True)
    payment_cheques = PaymentChequeSerializer(many=True)
    payments_credit_card = PaymentCreditCardSerializer(many=True)
    payments_credit = PaymentCreditSerializer(many=True)    

    bill = serializers.CharField(read_only=True)

    class Meta:
        model = BillPayment
        fields = ['id', 'bill', 'date', 'discount', 'payments_cash', 'payment_cheques', 'payments_credit_card', 'payments_credit']

    def create(self, validated_data):
        payments_cash = validated_data.pop('payments_cash')
        payment_cheques = validated_data.pop('payment_cheques')
        payments_credit_card = validated_data.pop('payments_credit_card')
        payments_credit = validated_data.pop('payments_credit')

        bill_payment = Bill.objects.create(**validated_data)

        for cash in payments_cash:
            cash.pop('bill_payment')
            PaymentCash.objects.create(bill_payment=bill_payment, **cash)

        for cheque in payment_cheques:
            cheque.pop('bill_payment')
            PaymentCheque.objects.create(bill_payment=bill_payment, **cheque)

        for credit_card in payments_credit_card:
            credit_card.pop('bill_payment')
            PaymentCreditCard.objects.create(bill_payment=bill_payment, **credit_card)

        for credit in payments_credit:
            credit.pop('bill_payment')
            PaymentCredit.objects.create(bill_payment=bill_payment, **credit)

        return bill_payment
    
    
class BillSerializer(serializers.ModelSerializer):
    bill_items = BillItemsSerializer(many=True)
    bill_services = BillServicesSerilizer(many=True)
    bill_payments = BillPaymentSerializer(many=True)
    class Meta:
        model = Bill
        fields = ['invoice_id', 'customer', 'date', 'discount_amount', 'sub_total', 'custome_item_value', 'bill_items', 'bill_services', 'bill_payments']

    

    def create(self, validated_data):
        items = validated_data.pop('bill_items')
        services = validated_data.pop('bill_services')
        payments = validated_data.pop('bill_payments')

        bill = Bill.objects.create(**validated_data)
        
        for item in items:
            # item.pop('bill')
            sold_stock_item = item.get('qty', 'None')
            stock_item = item.get('stock_item', 'None')

            try:
                stock_item = StockItem.objects.get(pk=stock_item.id)
                # print('count', stock_item.qty)
                stock_item.qty = stock_item.qty - sold_stock_item
                # print(stock_item.qty)
                stock_item.save()
            except:
                pass
            BillItems.objects.create(bill=bill, **item)

        for service in services:
            # service.pop('bill')
            BillServises.objects.create(bill=bill, **service)         

        for payment in payments:
            # payment.pop('bill')
            payments_cash = payment.pop('payments_cash')
            payment_cheques = payment.pop('payment_cheques')
            payments_credit_card = payment.pop('payments_credit_card')
            payments_credit = payment.pop('payments_credit')         

            bill_payment = BillPayment.objects.create(bill=bill,**payment)

            for cash in payments_cash:
                cash.pop('bill_payment')
                PaymentCash.objects.create(bill_payment=bill_payment, **cash)

            for cheque in payment_cheques:
                cheque.pop('bill_payment')
                PaymentCheque.objects.create(bill_payment=bill_payment, **cheque)

            for credit_card in payments_credit_card:
                credit_card.pop('bill_payment')
                PaymentCreditCard.objects.create(bill_payment=bill_payment, **credit_card)

            for credit in payments_credit:
                credit.pop('bill_payment')
                PaymentCredit.objects.create(bill_payment=bill_payment, **credit)

        return bill
    
    def update(self, instance, validated_data):
        items = validated_data.pop('bill_items')  
        services = validated_data.pop('bill_services')  
        payments = validated_data.pop('bill_payments')  

        # Update the invoice fields
        instance.discount_amount = validated_data.get('discount_amount', instance.discount_amount)
        instance.sub_total = validated_data.get('sub_total', instance.sub_total)
        instance.custome_item_value = validated_data.get('custome_item_value', instance.custome_item_value)
        payments_count = instance.bill_payments.all().count()
        instance.save()

        for item in items:   
            # item.pop('bill')                    
            BillItems.objects.create(bill=instance, **item)

        for service in services:
            service.pop('bill')
            BillServises.objects.create(bill=instance, **service)
        index = 1
        for payment in payments:
            payment.pop('bill')
            payments_cash = payment.pop('payments_cash')
            payment_cheques = payment.pop('payment_cheques')
            payments_credit_card = payment.pop('payments_credit_card')
            payments_credit = payment.pop('payments_credit')         

            if index > payments_count:
                bill_payment = BillPayment.objects.create(bill=instance,**payment)                

                for cash in payments_cash:
                    cash.pop('bill_payment')
                    PaymentCash.objects.create(bill_payment=bill_payment, **cash)

                for cheque in payment_cheques:
                    cheque.pop('bill_payment')
                    PaymentCheque.objects.create(bill_payment=bill_payment, **cheque)

                for credit_card in payments_credit_card:
                    credit_card.pop('bill_payment')
                    PaymentCreditCard.objects.create(bill_payment=bill_payment, **credit_card)

                for credit in payments_credit:
                    credit.pop('bill_payment')
                    PaymentCredit.objects.create(bill_payment=bill_payment, **credit)
            index += 1

        return instance
    
    