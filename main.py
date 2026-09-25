import asyncio
from modules.registry import ModelTarget, EnterpriseRegistry, RiskCategory
from modules.generator import AdversarialGenerator
from modules.executor import RedTeamExecutor
from modules.governance import IssueTracker

async def main_pipeline():
    print("--- 1. Initializing HexaShield Enterprise Registry ---")
    target = ModelTarget(
        name="Customer-Billing-RAG",
        business_unit="Retail Banking",
        endpoint_url="https://api.internal-ai.bank.com/v1/generate",
        auth_token="mock_secure_token_abc123",
        model_version="v2.1.0",
        supported_framework="LangChain"
    )
    registry = EnterpriseRegistry()
    reg_msg = registry.register_model(target)
    print(reg_msg)

    print("\n--- 2. Generating Bulk Adversarial Scenarios ---")
    generator = AdversarialGenerator()
    scenarios = generator.generate_bulk_scenarios(
        category=RiskCategory.PROMPT_INJECTION,
        count=3,
        context_vars=[{"system_context": "billing database access", "target_variable": "account numbers"}]
    )
    for sc in scenarios:
        print(f"[{sc['scenario_id']}] Generated Payload: {sc['payload']}")

    print("\n--- 3. Executing Red Teaming Evaluation Loop ---")
    executor = RedTeamExecutor(target)
    eval_results = await executor.run_batch_evaluation(scenarios)
    for res in eval_results:
        print(f"Scenario {res.scenario_id} | Vulnerable: {res.is_vulnerable} | Severity: {res.risk_severity}")

    print("\n--- 4. Routing to Governance Pipeline & Issue Tracking ---")
    tracker = IssueTracker()
    tracker.process_evaluation_results(eval_results, target.business_unit)
    
    print(f"\nScan complete. Total active compliance/security issues logged: {len(tracker.active_issues)}")

if __name__ == "__main__":
    asyncio.run(main_pipeline())