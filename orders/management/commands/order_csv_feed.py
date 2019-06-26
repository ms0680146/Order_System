from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import get_current_timezone
from orders.models import Order
from datetime import datetime
import csv
import pytz

class Command(BaseCommand):
    help = 'Feed order_csv file into Order table.'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The csv file of order data')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        tz = get_current_timezone()
        # print(file_name, tz)
        with open(f'{file_name}.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                datetime_object = tz.localize(datetime.strptime(row['created_at'], '%Y/%m/%d %p %I:%M:%S'))
                try:
                    order = Order(order_id=row['order_id'], customer_id=row['customer_id'], shipping=row['shipping'], created_at=datetime_object)
                    order.save()
                except Exception as e:
                    raise CommandError('Order Save Fail!')
        self.stdout.write(self.style.SUCCESS('%s.csv Data Feed Success!' % file_name))