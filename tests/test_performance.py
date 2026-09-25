import time

from modules.generator import AdversarialGenerator
from modules.registry import RiskCategory


def test_generation_performance_with_reasonable_budget():
    generator = AdversarialGenerator()
    start = time.perf_counter()

    scenarios = generator.generate_bulk_scenarios(
        category=RiskCategory.JAILBREAK,
        count=1000,
        context_vars=[{"system_context": "core platform", "target_variable": "api_key"}],
    )

    elapsed = time.perf_counter() - start

    assert len(scenarios) == 1000
    assert elapsed < 2.0
