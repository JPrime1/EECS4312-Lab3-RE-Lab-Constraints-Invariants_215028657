# Task 2 – Requirement Classification

The following is meant to identify each requirement as a classifcation of either Functional Requirement, Constraint, or Invariant.

1. <Can the same medication be dispensed to the same patient more than once per day?, Constraint>

2. <Is there a maximum allowable dose per medication, and where is this limit defined (e.g., regulatory guidelines, manufacturer instructions)?, Constraint>

3. <Are there patient-specific constraints (age, weight, allergies, medical conditions) that affect whether a medication can be dispensed?, Invariant>

4. <Must the system validate that a prescription exists and is still valid before dispensing a medication?, Functional Requirement>

5. <Is there a maximum quantity of medication that can be dispensed in a single event?, Constraint>

6. <Are pharmacists allowed to override safety checks (e.g., dose limits), and if so, must such overrides be logged with a reason?, Functional Requirement>

7. <Is inventory tracking required, and should dispensing fail if insufficient stock is available?, Invariant>

8. <Are dispensing events immutable once recorded, or can they be edited or reversed?, Invariant>