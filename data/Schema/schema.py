import pandera as pa
from pandera import Column, DataFrameSchema, Check

# ---------------------------
# Intervention-level schema
# ---------------------------
intervention_schema = DataFrameSchema(
    {
        "intervention_id": Column(str, nullable=False),
        "city": Column(str, nullable=False),
        "modal_shift": Column(
            float,
            checks=[
                Check.ge(0),   # >= 0
                Check.le(100)  # <= 100
            ],
            nullable=False,
        ),
        "safety_score": Column(
            int,
            checks=[
                Check.ge(0),
                Check.le(10)
            ],
            nullable=False,
        ),
        "inclusiveness": Column(
            float,
            checks=[
                Check.ge(0),
                Check.le(100)
            ],
            nullable=True,  # allow missing values
        ),
        "population": Column(
            int,
            checks=Check.ge(0),
            nullable=False,
        ),
        "year": Column(
            int,
            checks=Check.in_range(2000, 2100),
            nullable=False,
        ),
    },
    strict=True,  # no extra columns allowed
    coerce=True,  # auto-convert types
)

