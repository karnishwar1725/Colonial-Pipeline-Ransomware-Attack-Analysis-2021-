"""
Data Breach Impact Analyzer - Colonial Pipeline
"""

import random
from datetime import datetime
from collections import defaultdict


class DataBreachAnalyzer:

    def __init__(self, target_breach_size_gb=100):

        self.target_breach_size = target_breach_size_gb
        self.breach_records = []

        self.data_types = [
            'Customer',
            'Financial',
            'Operational',
            'Employee',
            'IT Systems'
        ]

        self.breach_date = datetime(2021, 5, 7)
        self.threat_actor = "DarkSide"
        self.ransom_paid_btc = 75
        self.ransom_recovered_btc = 64

        self.risk_levels = {
            'CRITICAL': 0,
            'HIGH': 0,
            'MEDIUM': 0,
            'LOW': 0
        }

    def generate_breach_data(self):

        total_breach_size = 0
        record_id = 1

        while total_breach_size < self.target_breach_size:

            data_type = random.choice(self.data_types)
            sensitivity = random.randint(1, 4)
            size = round(random.uniform(0.2, 4.0), 2)

            if data_type == 'Customer':
                impact = random.randint(2000, 15000)
            elif data_type == 'Financial':
                impact = random.randint(1000, 8000)
            elif data_type == 'Employee':
                impact = random.randint(200, 2000)
            else:
                impact = random.randint(0, 800)

            record = {
                "id": record_id,
                "type": data_type,
                "sensitivity": sensitivity,
                "size_gb": size,
                "affected_people": impact,
                "risk": None,
                "detection_hours": random.randint(1, 72)
            }

            self.breach_records.append(record)

            total_breach_size += size
            record_id += 1

        print(f"\nGenerated {len(self.breach_records)} records")
        print(f"Total breach size: {total_breach_size:.2f} GB")

    def classify_risk(self):

        for r in self.breach_records:

            if r["sensitivity"] == 4 or r["affected_people"] > 8000:
                risk = "CRITICAL"
            elif r["sensitivity"] == 3:
                risk = "HIGH"
            elif r["sensitivity"] == 2:
                risk = "MEDIUM"
            else:
                risk = "LOW"

            r["risk"] = risk
            self.risk_levels[risk] += 1

    def analyze_impact(self):

        total_people = sum(r["affected_people"] for r in self.breach_records)

        print("\n====== IMPACT SUMMARY ======")
        print(f"Total people/systems affected: {total_people:,}")
        print(f"Total records: {len(self.breach_records)}")

        type_count = defaultdict(int)
        for r in self.breach_records:
            type_count[r["type"]] += 1

        print("\nData Type Distribution:")
        for t, c in type_count.items():
            print(f"{t}: {c} records")

        print("\nRisk Distribution:")
        for level, count in self.risk_levels.items():
            print(f"{level}: {count} records")

    def prioritize_response(self):

        for r in self.breach_records:
            score = r["sensitivity"] * r["affected_people"] * r["size_gb"]
            r["priority"] = score

        sorted_records = sorted(self.breach_records, key=lambda x: x["priority"], reverse=True)

        print("\nTop 5 priority records:")
        for r in sorted_records[:5]:
            print(f"ID {r['id']} | {r['type']} | Risk: {r['risk']}")

    def run(self):

        print("=" * 50)
        print("COLONIAL PIPELINE RANSOMWARE BREACH SIMULATION")
        print("=" * 50)

        print(f"Attack Date: {self.breach_date.strftime('%B %d, %Y')}")
        print(f"Threat Actor: {self.threat_actor}")
        print("Data Exfiltrated: ~100 GB")
        print(f"Ransom Paid: {self.ransom_paid_btc} BTC (~$4.4M)")
        print(f"Recovered by authorities: {self.ransom_recovered_btc} BTC (~$2.3M)")
        print("Operations Shutdown: ~5 days")

        self.generate_breach_data()
        self.classify_risk()
        self.analyze_impact()
        self.prioritize_response()


if __name__ == "__main__":
    random.seed(42)
    analyzer = DataBreachAnalyzer()
    analyzer.run()