import os
import pandas as pd

from django.core.management.base import BaseCommand

from transport import models as transport_models
from transport_subsidiary.models import UnitName, VehicleType


class Command(BaseCommand):
    help = "Import data from a CSV file"

    def import_data(self, file_path, model, foreign_keys=None):

        df = pd.read_csv(file_path)
        batch_size = 1000  # 調整批次大小

        objects = list()
        for _, row in df.iterrows():
            print(row)
            if foreign_keys:
                for key, related_model in foreign_keys.items():
                    if row[key]:
                        row[key] = related_model.objects.get(id=row[key])
                    else:
                        row[key] = None

        objects.append(model(**row))
        model.objects.bulk_create(objects, batch_size=batch_size)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported data from {os.path.basename(file_path)}"
            )
        )

    def handle(self, *args, **kwargs):
        base_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "fixtures/csv/main_table/"
        )
        self.import_data(
            os.path.join(base_path, "accident_records.csv"),
            transport_models.AccidentRecords,
            {"處理單位名稱警局層": UnitName},
        )
        self.import_data(
            os.path.join(base_path, "cause_analysis.csv"),
            transport_models.CauseAnalysis,
            {"accident_id": transport_models.AccidentRecords},
        )
        self.import_data(
            os.path.join(base_path, "party_info.csv"),
            transport_models.PartyInfo,
            {
                "accident_id": transport_models.AccidentRecords,
                "當事者區分_類別_大類別名稱_車種": VehicleType,
            },
        )
        self.import_data(
            os.path.join(base_path, "road_conditions.csv"),
            transport_models.RoadConditions,
            {"accident_id": transport_models.AccidentRecords},
        )
        self.import_data(
            os.path.join(base_path, "traffic_facilities.csv"),
            transport_models.TrafficFacilities,
            {"accident_id": transport_models.AccidentRecords},
        )
