import os
import pandas as pd
from django.core.management.base import BaseCommand, CommandError

from rental_app.models import Rental


# Adjust 'rentals' to match your Django app name

class Command(BaseCommand):
    help = "Imports rental data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        file_path = os.path.abspath(file_path)

        if not os.path.exists(file_path):
            raise CommandError(f"Error: File not found at {file_path}")

        try:
            df = pd.read_csv(file_path)

            for _, row in df.iterrows():
                rental, created = Rental.objects.update_or_create(
                    name=row['Name'],
                    address=row['Address'],
                    defaults={'x': row['x'], 'y': row['y']}
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added: {rental.name}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Updated: {rental.name}"))

        except Exception as e:
            raise CommandError(f"Error reading file: {e}")











# import os
# import pandas as pd
# from django.core.management.base import BaseCommand, CommandError
#
# class Command(BaseCommand):
#     help = "Imports rental data from a CSV file"
#
#     def add_arguments(self, parser):
#         parser.add_argument('file_path', type=str, help='Path to the CSV file')
#
#     def handle(self, *args, **options):
#         file_path = options['file_path']
#
#         # Convert to absolute path if necessary
#         file_path = os.path.abspath(file_path)
#
#         if not os.path.exists(file_path):
#             raise CommandError(f"Error: File not found at {file_path}")
#
#         try:
#             df = pd.read_csv(file_path)
#             result = df.head(10)
#             # for i in range(len(result)):
#
#
#             print(result)
#         except Exception as e:
#             raise CommandError(f"Error reading file: {e}")













# import os
# import pandas as pd
# from django.core.management.base import BaseCommand
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         csv_path = os.path.join(os.getcwd(), 'rental_app/csv_data/rental.csv')  # Get full path
#         try:
#             # pd.options.display.max_rows = 5
#             df = pd.read_csv(csv_path)
#             result = df.head(10)
#             # print(df.to_string())
#             print(result)
#         except FileNotFoundError:
#             self.stderr.write(f"Error: File not found at {csv_path}")