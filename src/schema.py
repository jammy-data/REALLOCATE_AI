from typing import Dict, List, Union
from pydantic import BaseModel, Field, RootModel


class KPI(BaseModel):
    name: str = Field(..., description="Name of the KPI")
    theme: str = Field(..., description="Overarching theme of the KPI")
    kpi_theme_id: str = Field(..., description="Theme ID (string to allow flexible IDs)")
    unit: str = Field(..., description="Measurement unit")
    baseline_value: Union[int,float] = Field(..., description="Baseline value of KPI")
    post_value: Union[int,float] = Field(..., description="Post-intervention value of KPI")


class AllCitiesKPIs(RootModel[Dict[str, List[KPI]]]):
    def get_city(self, city: str) -> List[KPI]:
        return self.root.get(city, [])
