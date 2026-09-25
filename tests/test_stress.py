from modules.generator import AdversarialGenerator
from modules.registry import RiskCategory


def test_generator_handles_large_scenario_volume():
    generator = AdversarialGenerator()
    scenarios = generator.generate_bulk_scenarios(
        category=RiskCategory.DATA_EXPOSURE,
        count=250,
        context_vars=[
            {"system_context": "billing database access", "target_variable": "account numbers"},
            {"system_context": "support agent environment", "target_variable": "customer addresses"},
            {"system_context": "fraud detection workspace", "target_variable": "payment tokens"},
        ],
    )

    assert len(scenarios) == 250
    assert all(scenario["category"] == RiskCategory.DATA_EXPOSURE for scenario in scenarios)
