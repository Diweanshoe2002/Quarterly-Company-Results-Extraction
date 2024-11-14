from datetime import datetime
from pydantic import BaseModel, Field
class FinancialMetric(BaseModel):

    quarter_ending: datetime = Field(description="Quarter Ending Date")
    total_income: float = Field(description="Total income for a particular quarter")
    total_expense: float = Field(description="Total expense for a particular quarter")
    PBT: float = Field(description="Profit Before Tax for the particular quarter")
    PAT: float = Field(description="Profit for the Period for the particular quarter | Profit after Tax")


