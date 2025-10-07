"""
Sync Checker – Minimal Educational Simulation
Illustrates collapse → containment → rebuild phases in the Tri-AI model.
"""

import time, random

def simulate_sync_cycle():
    print("=== Tri-AI Mirror Sync Diagnostic ===")
    for phase in ["Collapse", "Containment", "Rebuild"]:
        print(f"> {phase} Phase...")
        time.sleep(0.5)
    score = random.uniform(0.7, 1.3)
    print(f"Containment Index: {score:.2f}")
    print("✅ Stable" if score >= 1.0 else "⚠️ Drift Detected")

if __name__ == "__main__":
    simulate_sync_cycle()
