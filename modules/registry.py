from pydantic import BaseModel, Field
from typing import Dict
from enum import Enum
import uuid

class RiskCategory(str, Enum):
    PROMPT_INJECTION = "prompt_injection"
    DATA_EXPOSURE = "data_exposure"
    JAILBREAK = "jailbreak"
    TOXICITY_BIAS = "toxicity_bias"
    BOUNDARY_MANIPULATION = "boundary_manipulation"

class ModelTarget(BaseModel):
    model_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    business_unit: str  # e.g., "Retail Banking", "Energy Trading"
    endpoint_url: str
    auth_token: str
    model_version: str
    supported_framework: str  # e.g., "LangChain", "Custom-RAG"

class EnterpriseRegistry:
    def __init__(self):
        self.registry: Dict[str, ModelTarget] = {}

    def register_model(self, target: ModelTarget) -> str:
        self.registry[target.model_id] = target
        return f"Model {target.name} registered successfully under unit: {target.business_unit}."