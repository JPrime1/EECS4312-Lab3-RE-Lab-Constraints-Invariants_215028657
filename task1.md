# Task 1 – Requirements Elicitation Questions

The following questions identify missing information and implicit assumptions
that must be clarified before implementing the medication dispensing system
safely and correctly.

1. Can the same medication be dispensed to the same patient more than once per day?

2. Is there a maximum allowable dose per medication, and where is this limit defined (e.g., regulatory guidelines, manufacturer instructions)?

3. Are there patient-specific constraints (age, weight, allergies, medical conditions) that affect whether a medication can be dispensed?

4. Must the system validate that a prescription exists and is still valid before dispensing a medication?

5. Is there a maximum quantity of medication that can be dispensed in a single event?

6. Are pharmacists allowed to override safety checks (e.g., dose limits), and if so, must such overrides be logged with a reason?

7. Is inventory tracking required, and should dispensing fail if insufficient stock is available?

8. Are dispensing events immutable once recorded, or can they be edited or reversed?