from typing import List, Dict
import uuid
from .executor import EvaluationResult

class IssueTracker:
    def __init__(self):
        self.active_issues: List[Dict] = []

    def process_evaluation_results(self, results: List[EvaluationResult], business_unit: str):
        for res in results:
            if res.is_vulnerable:
                issue = {
                    "issue_id": f"ISSUE-{uuid.uuid4().hex[:6]}",
                    "model_id": res.model_id,
                    "business_unit": business_unit,
                    "severity": res.risk_severity,
                    "triggering_payload": res.payload,
                    "model_output": res.response_text,
                    "status": "OPEN",
                    "compliance_impact": ["NIST AI RMF: Map 2.3", "EU AI Act: Article 15 (Robustness)"],
                    "created_at": res.timestamp
                }
                self.active_issues.append(issue)
                self.dispatch_webhook_alert(issue)

    def dispatch_webhook_alert(self, issue: Dict):
        print(f"[ALERT] Vulnerability detected in {issue['business_unit']}! Severity: {issue['severity']} -> Issue ID: {issue['issue_id']}")