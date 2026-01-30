# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
import sys
from pathlib import Path

# Add the src directory to sys.path so Python can find modules
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from dispense import DispenseEvent


# Test 1: Adding a valid new event preserves invariants
def test_add_valid_dispense_event():
    existing_events = [
        DispenseEvent("patient-1", "Aspirin", 100.0, 10)
    ]

    new_event = DispenseEvent("patient-2", "Ibuprofen", 200.0, 5)

    assert invariant_holds(existing_events, new_event) is True

# Test 2: Reject exact duplicate dispense event
def test_reject_duplicate_dispense_event():
    existing_events = [
        DispenseEvent("patient-1", "Aspirin", 100.0, 10)
    ]

    new_event = DispenseEvent("patient-1", "Aspirin", 100.0, 10)

    assert invariant_holds(existing_events, new_event) is False

# Test 3: Reject duplicate patient + medication + dose
def test_reject_duplicate_patient_medication_dose():
    existing_events = [
        DispenseEvent("patient-1", "Aspirin", 100.0, 10)
    ]

    new_event = DispenseEvent("patient-1", "Aspirin", 100.0, 5)

    assert invariant_holds(existing_events, new_event) is False

# Test 4: Different dose is allowed
def test_allow_same_patient_medication_different_dose():
    existing_events = [
        DispenseEvent("patient-1", "Aspirin", 100.0, 10)
    ]

    new_event = DispenseEvent("patient-1", "Aspirin", 200.0, 5)

    assert invariant_holds(existing_events, new_event) is True
