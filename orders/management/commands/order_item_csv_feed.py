from django.core.management.base import BaseCommand, CommandError
from orders.models import OrderItem
import csv

class Command(BaseCommand):
    help = 'Feed order_item_csv file into OrderItem table.'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The csv file of order_item data')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                try:
                    order_item = OrderItem(order_id=row['order_id'], product_name=row['product_name'], qty=row['qty'])
                    order_item.save()
                except Exception as e:
                    raise CommandError('OrderItem save fail')
        self.stdout.write(self.style.SUCCESS('%s.csv Data Feed Success!' % file_name))