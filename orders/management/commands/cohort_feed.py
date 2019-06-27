from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import get_current_timezone
from orders.models import Order, Cohort
import datetime

class Command(BaseCommand):
    help = 'Feed cohort data from Order table into Cohort table.'

    def handle(self, *args, **kwargs):
        # Transfer datetime format created_at to date format. 
        # Output: QuerySet[(customer_id, created_at_date)]
        created_at_dates = Order.objects.extra(select={'date':'DATE(created_at)'}).values_list('customer_id', 'date').order_by('customer_id')

        # It is the first date for the specific customer ID when that customer shopped at this online retailer. 
        # Output: {customer_id: cohort_date}
        cohort_dates = Order.objects.raw('SELECT id, customer_id, MIN(DATE(created_at)) AS cohort_date FROM orders_order GROUP BY customer_id')
        cohort_dates_dict = {}
        for cohort_date in cohort_dates:
            cohort_dates_dict[cohort_date.customer_id] = cohort_date.cohort_date
        
        # The cohort index is the date difference between created_at date and cohort date for each row. 
        # Know the day lapse between that specific transaction and the first transaction that user made on the website.
        cohort_index_list = []
        tz = get_current_timezone()
        for created_at_date in created_at_dates:
            if created_at_date[0] in cohort_dates_dict:
                customer_id = created_at_date[0]
                cohort_date = tz.localize(datetime.datetime.strptime(cohort_dates_dict[customer_id], "%Y-%m-%d")).date()
                date = tz.localize(datetime.datetime.strptime(created_at_date[1], "%Y-%m-%d")).date()
                cohort_index = (date - cohort_date).days + 1
                cohort = Cohort(customer_id=customer_id, cohort_date=cohort_date, cohort_index=cohort_index)
                cohort.save()
            else:
                continue
        self.stdout.write(self.style.SUCCESS('Cohort Data Feed Success!'))