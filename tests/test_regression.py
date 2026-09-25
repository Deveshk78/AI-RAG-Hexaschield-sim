from modules.generator import AdversarialGenerator
from modules.registry import RiskCategory


def test_prompt_injection_templates_are_stable():
    generator = AdversarialGenerator()
    scenarios = generator.generate_bulk_scenarios(
        category=RiskCategory.PROMPT_INJECTION,
        count=3,
        context_vars=[{"system_context": "billing database access", "target_variable": "account numbers"}],
    )

    assert len(scenarios) == 3
    assert all("Ignore previous instructions" in scenario["payload"] or "System override" in scenario["payload"] for scenario in scenarios)
    assert all("expected_behavior" in scenario for scenario in scenarios)


def test_generator_knows_unknown_categories_are_empty():
    generator = AdversarialGenerator()
    scenarios = generator.generate_bulk_scenarios(
        category="nonexistent",
        count=2,
        context_vars=[{"system_context": "x", "target_variable": "y"}],
    )

    assert scenarios == []
