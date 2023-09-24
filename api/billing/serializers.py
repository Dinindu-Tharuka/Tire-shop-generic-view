from rest_framework import serializers
from billing_data.models import Bill, BillItems, BillServises, BillPayment
from billing_data.models import PaymentCash, PaymentCheque, PaymentCreditCard, PaymentCredit
from stock_data.models import StockItem, StockItemUnique

class BillItemsSerializer(serializers.ModelSerializer):
    bill = serializers.CharField(read_only=True)
    class Meta:
        model = BillItems
        fields = ['id', 'item', 'stock_item_unique', 'bill', 'qty', 'customer_discount', 'customer_price']


class BillServicesSerilizer(serializers.ModelSerializer):
    bill = serializers.CharField(read_only = True)
    class Meta:
        model = BillServises
        fields =  ['id', 'service', 'employee', 'bill']


class PaymentCashSerializer(serializers.ModelSerializer):
    bill_payment = serializers.CharField(read_only=True)
    class Meta:
        model = PaymentCash
        fields =  ['id', 'bill_payment', 'date', 'payeename', 'amount']

class PaymentChequeSerializer(serializers.ModelSerializer):
    bill_payment = serializers.CharField(read_only=True)
    class Meta:
        model = PaymentCheque
        fields = ['id', 'bill_payment', 'date', 'amount', 'cheque_no', 'payeename', 'bank', 'branch', 'cheque_date']

class PaymentCreditCardSerializer(serializers.ModelSerializer):
    bill_payment = serializers.CharField(read_only=True)
    class Meta:
        model = PaymentCreditCard
        fields = ['id', 'bill_payment', 'date', 'payeename', 'amount']

class PaymentCreditSerializer(serializers.ModelSerializer):
    bill_payment = serializers.CharField(read_only=True)
    class Meta:
        model = PaymentCredit
        fields = ['id', 'bill_payment', 'date', 'due_date', 'payeename', 'amount']

class BillPaymentSerializer(serializers.ModelSerializer):
    payments_cash = PaymentCashSerializer(many=True)
    payment_cheques = PaymentChequeSerializer(many=True)
    payments_credit_card = PaymentCreditCardSerializer(many=True)
    payments_credit = PaymentCreditSerializer(many=True)    

    
    bill_id = serializers.CharField()
    class Meta:
        model = BillPayment
        fields = ['id', 'bill_id', 'date', 'discount', 'payments_cash', 'payment_cheques', 'payments_credit_card', 'payments_credit']

    def create(self, validated_data):
        payments_cash = validated_data.pop('payments_cash')
        payment_cheques = validated_data.pop('payment_cheques')
        payments_credit_card = validated_data.pop('payments_credit_card')
        payments_credit = validated_data.pop('payments_credit')
        bill_id = str(validated_data.pop('bill_id'))

        bill_payment = BillPayment.objects.create(bill_id=bill_id, **validated_data)


        for cash in payments_cash:
            PaymentCash.objects.create(bill_payment=bill_payment, **cash)

        for cheque in payment_cheques:
            PaymentCheque.objects.create(bill_payment=bill_payment, **cheque)

        for credit_card in payments_credit_card:
            PaymentCreditCard.objects.create(bill_payment=bill_payment, **credit_card)

        for credit in payments_credit:
            PaymentCredit.objects.create(bill_payment=bill_payment, **credit)

        return bill_payment
    
    
class BillSerializer(serializers.ModelSerializer):
    bill_items = BillItemsSerializer(many=True)
    bill_services = BillServicesSerilizer(many=True)
    class Meta:
        model = Bill
        fields = ['invoice_id', 'customer', 'date', 'discount_amount', 'sub_total', 'custome_item_value', 'bill_items', 'bill_services']

    

    def create(self, validated_data):
        items = validated_data.pop('bill_items')
        services = validated_data.pop('bill_services')
        bill = Bill.objects.create(**validated_data)
        
        for item in items:
            sold_stock_item = item.get('qty', 'None')
            stock_item = item.get('stock_item_unique', 'None')
            customer_price = item['customer_price']
            qty = item['qty']
            customer_unit_price = customer_price/qty

            try:
                stock_item_unique = StockItemUnique.objects.get(item=stock_item.item.item_id, unit_price=customer_unit_price)                
                stock_item_unique.total_qty = stock_item_unique.total_qty - sold_stock_item
                stock_item_unique.save()
                stock_items = StockItem.objects.all()
                

                for stock_item in stock_items:
                    if stock_item_unique.id == stock_item.stock_item_unique.id:
                        if stock_item.qty > sold_stock_item:
                            stock_item.qty = stock_item.qty - sold_stock_item
                            stock_item.save()
                            break
                        else:
                            sold_stock_item = sold_stock_item - stock_item.qty 
                            stock_item.qty = 0
                            stock_item.save()                  
                    
            except:
                print('not ok')
                pass
            BillItems.objects.create(bill=bill, customer_unit_price=customer_unit_price, **item)

        for service in services:
            BillServises.objects.create(bill=bill, **service)        

        return bill
    
   
    