
class DispenseEvent:
    """
    Represents a single medication dispensing event for a patient.

    """

    # TODO Task 3: Encode and enforce input constraints (e.g., valid dose, quantity, identifiers)
    def __init__(self, patient_id, medication, dose_mg, quantity):
        """
        Initialize a new DispenseEvent.

        Args:
            patient_id: Unique identifier for the patient receiving medication.
            medication: Name or identifier of the medication being dispensed.
            dose_mg: Dose per unit in milligrams. Must be a positive number.
            quantity: Number of units dispensed. Must be a positive integer.

        """
        # --- Type checks ---
        if not isinstance(patient_id, str) or not patient_id.strip():
            raise ValueError("patient_id must be a non-empty string")
        
        if not isinstance(medication, str) or not patient_id.strip():
            raise ValueError("medication must be a non-empty string")

        if not isinstance(dose_mg, int, float) or not patient_id.strip():
            raise ValueError("dose_mg must be a number")

        if not isinstance(quantity, int) or not patient_id.strip():
            raise ValueError("quantity must be an integer")

        # --- Value checks ---
        if dose_mg <= 0:
            raise ValueError("dose_mg must be a positive number")

        if quantity <= 0:
            raise ValueError("quantity must be a positive integer")

        # --- Max dosage value ---
        MAX_DOSE = 1000
        MAX_QUANT = 1000

        if dose_mg >= MAX_DOSE: 
            raise ValueError("dosage too high!")
        if quantity >= MAX_QUANT: 
            raise ValueError("quantity too high!")

        # --- Assignment (only after validation passes) ---
        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = float(dose_mg)
        self.quantity = quantity

    # TODO Task 4: Define and check system invariants 
    def invariant_holds(existing_events, new_event):
        """
        Check whether adding a new dispense event preserves all system invariants.

        Args:
            existing_events: Iterable of previously recorded DispenseEvent objects.
            new_event: The proposed DispenseEvent to validate.

        Returns:
            bool: True if all invariants hold after adding new_event; False otherwise.
            
        """
        pass
