import numpy as np
np.random.seed(42)

# Define city-specific KPIs under themes. We can produce a json file from this dictionary later on.
pilot_kpis = {
    "Barcelona_1": [
        {"name": "Number of participants engaged",
        "theme": "Engagement", 
        "kpi_theme_id": "1", 
        "unit": "counts", 
        "baseline_range": (20, 120), 
        "post_range": (20, 150)},
        {"name": "reported risk factors affecting perceived road safety", 
        "theme": "road safety", 
         "kpi_theme_id": "2",
         "unit": "counts", 
         "baseline_range": (20, 120), 
         "post_range": (20, 150)}
        ],
    "Barcelona_2": [
        {"name": "Engagement in co-creation",
        "theme": "Engagement", 
        "kpi_theme_id": "1", 
        "unit": "counts", 
        "baseline_range": (20, 120), 
        "post_range": (20, 150)},
        {"name": "Increase in users of special services through DRT", 
        "theme": "Accessibility", 
         "kpi_theme_id": "3",
         "unit": "counts", 
         "baseline_range": (20, 120), 
         "post_range": (20, 150)}
        ],
    "Heidelberg_1": [
        {"name": "Engagement in co-creation",
        "theme": "Engagement", 
        "kpi_theme_id": "1", 
        "unit": "counts", 
        "baseline_range": (20, 120), 
        "post_range": (20, 150)},
        {"name": "Collaboration agreement",
        "theme": "Engagement", 
         "kpi_theme_id": "1",
         "unit": "counts", 
         "baseline_range": (20, 120), 
         "post_range": (20, 150)}
        ],
    "Heidelberg_2": [
        {"name": "Pedestrian and Cyclist counts",
        "theme": "road safety", 
        "kpi_theme_id": "2", 
        "unit": "counts", 
        "baseline_range": (20, 120), 
        "post_range": (20, 150)},
        {"name": "Impact on traffic flows",
        "theme": "road safety", 
         "kpi_theme_id": "2",
         "unit": "Vehicles/24h", 
         "baseline_range": (1000, 2000), 
         "post_range": (1000, 2000)},
        {"name": "Conversion from impermeable to permeable/vegetated surface",
        "theme": "Environment", 
         "kpi_theme_id": "4",
         "unit": "%", 
         "baseline_range": (0, 100), 
         "post_range": (0, 100)}
        ],
    "Gothenburg_1": [
        {"name": "Engagement in co-creation",
        "theme": "Engagement", 
        "kpi_theme_id": "1",
        "unit": "Counts", 
        "baseline_range": (60, 120), 
        "post_range": (60, 150)},
        {"name": "Active mobility mode share",
        "theme": "Mobility", 
         "kpi_theme_id": "5",
         "unit": "%", 
         "baseline_range": (0, 100), 
         "post_range": (0, 100)}
        ],
    "Gothenburg_2": [
        {"name": "Accessibility active modes",
        "theme": "Accessibility", 
        "kpi_theme_id": "3",
        "unit": "%", 
        "baseline_range": (0, 100), 
        "post_range": (0, 100)}
        ],
    "Budapest_1": [
        {"name": "Active mobility mode share",
        "theme": "Mobility", 
        "kpi_theme_id": "5",
        "unit": "Counts", 
        "baseline_range": (100, 1000), 
        "post_range": (100, 1300)},
        {"name": "Active mobility mode share (schoolchildren)",
        "theme": "Mobility", 
         "kpi_theme_id": "5",
         "unit": "%", 
         "baseline_range": (0, 100), 
         "post_range": (0, 100)},
        {"name": "Green area expansion",
        "theme": "Environment", 
         "kpi_theme_id": "4",
         "unit": "%", 
         "baseline_range": (0, 100), 
         "post_range": (0, 100)}
        ],
    "Budapest_2": [
        {"name": "Active Mobility mode share",
        "theme": "Mobility", 
        "kpi_theme_id": "5",
        "unit": "Counts", 
        "baseline_range": (60, 120), 
        "post_range": (60, 150)},    
        ],
    "Lyon_1": [
        {"name": "Active mobility mode share",
        "theme": "Mobility", 
        "kpi_theme_id": "5",
        "unit": "Counts", 
        "baseline_range": (60, 120), 
        "post_range": (30, 80)},
        ],
    "Lyon_2": [
        {"name": "test",
        "theme": "test", 
        "kpi_theme_id": "test",
        "unit": "test", 
        "baseline_range": (60, 120), 
        "post_range": (30, 80)},    
        ],
    "Bologna": [
        {"name": "Active mobility mode share",
        "theme": "Mobility", 
        "kpi_theme_id": "5",
        "unit": "%", 
        "baseline_range": (0, 100), 
        "post_range": (0, 100)},
        {"name": "Pedestrian and Cyclist comfort rating",
        "theme": "road safety", 
         "kpi_theme_id": "2",
         "unit": "Rating", 
         "baseline_range": (1, 10), 
         "post_range": (1, 10)}
        ],
    "Tampere": [
        {"name": "Active mobility mode share/school travel mode share", 
        "theme": "Mobility", 
        "kpi_theme_id": "5",
        "unit": "Counts", 
        "baseline_range": (60, 120), 
        "post_range": (60, 150)},
        {"name": "Engagement in co-creation",
        "theme": "Engagement", 
         "kpi_theme_id": "1",
         "unit": "Counts", 
         "baseline_range": (20, 40), 
         "post_range": (20, 60)}
        ],
    "Utrecht": [
        {"name": "Active mobility mode share",
        "theme": "Mobility", 
        "kpi_theme_id": "5",
        "unit": "Counts", 
        "baseline_range": (60, 120), 
        "post_range": (60, 150)},
        {"name": "Engagement in co-creation",
        "theme": "Engagement", 
         "kpi_theme_id": "2",
         "unit": "%", 
         "baseline_range": (20, 40), 
         "post_range": (15, 30)}
        ],
    "Warsaw": [
        {"name": "Number of participants in co-creation workshops", 
        "theme": "Engagement", 
        "kpi_theme_id": "2",
        "unit": "Counts", 
        "baseline_range": (60, 120), 
        "post_range": (60, 150)},
        {"name": "Active mobility mode share",
        "theme": "Mobility", 
         "kpi_theme_id": "5",
         "unit": "%", 
         "baseline_range": (0, 100), 
         "post_range": (0, 100)},
        {"name": "Active mobility adoption",
        "theme": "Mobility", 
         "kpi_theme_id": "5",
         "unit": "%", 
         "baseline_range": (0, 100), 
         "post_range": (0, 100)}
        ],
    "Zagreb": [
        {"name": "Public space reallocation area",
        "theme": "Accessibility", 
        "kpi_theme_id": "3",
        "unit": "m²", 
        "baseline_range": (5, 50), 
        "post_range": (5, 70)},
        {"name": "Pedestrian and cyclist comfort index",
        "theme": "road safety", 
         "kpi_theme_id": "2",
         "unit": "%", 
         "baseline_range": (0, 1), 
         "post_range": (0, 1)},
        {"name": "Active mobility mode share",
        "theme": "Mobility", 
         "kpi_theme_id": "5",
         "unit": "%", 
         "baseline_range": (0, 100), 
         "post_range": (0, 100)}
        ]
    }

# Function to replace ranges with actual values
def generate_values(pilot_dict):
    output = {}
    for pilot, kpis in pilot_dict.items():
        pilot_data = []
        for kpi in kpis:
            baseline_val = round(np.random.uniform(*kpi["baseline_range"]), 2)
            post_val = round(np.random.uniform(*kpi["post_range"]), 2)
            
            pilot_data.append({
                "name": kpi["name"],
                "theme": kpi["theme"],
                "kpi_theme_id": kpi["kpi_theme_id"],
                "unit": kpi["unit"],
                "baseline_value": baseline_val,
                "post_value": post_val
            })
        output[pilot] = pilot_data
    return output

import json
import os

# Generate values
pilot_kpis_with_values = generate_values(pilot_kpis)

# === Ensure data folder exists at project root ===
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # goes up from src/
data_dir = os.path.join(root_dir, "data/Dummy")
os.makedirs(data_dir, exist_ok=True)

# === Save JSON into data/ ===
with open(os.path.join(data_dir, "pilot_kpis.json"), "w") as f:
    json.dump(pilot_kpis_with_values, f, indent=4)

# === OPTION 2: Separate JSONs for each pilot ===
#os.makedirs("pilot_jsons", exist_ok=True)
#for pilot, data in pilot_kpis_with_values.items():
#    with open(f"pilot_jsons/{pilot}.json", "w") as f:
#        json.dump(data, f, indent=4)