import csv
import os

from django.core.management.base import BaseCommand

from transport_subsidiary.models import UnitName, VehicleType


class Command(BaseCommand):
    help = "Import data from a CSV file"

    def import_data(self, file_path, model, foreign_keys=None):
        with open(file_path, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            print(
                f"Waiting for data to be imported from {os.path.basename(file_path)}..."
            )
            for row in reader:
                if foreign_keys:
                    for key, related_model in foreign_keys.items():
                        row[key] = related_model.objects.get(id=row[key])
                model.objects.create(**row)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully imported data from {os.path.basename(file_path)}"
                )
            )

    def handle(self, *args, **kwargs):

        base_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "fixtures/csv/subsidiary_table/",
        )
        self.import_data(os.path.join(base_path, "unit_name.csv"), UnitName)
        self.import_data(os.path.join(base_path, "vehicle_type.csv"), VehicleType)
