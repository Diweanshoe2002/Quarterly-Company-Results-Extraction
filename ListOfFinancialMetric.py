from FinancialMetric import FinancialMetric
from pydantic import BaseModel
class ListOfFinancialMetric(BaseModel):

    metricList : list[FinancialMetric]
