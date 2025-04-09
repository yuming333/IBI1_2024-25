def calculate_paracetamol_dose(weight_kg, strength):
    """
    Calculate the volume of paracetamol required for a child based on weight and strength.
    
    Args:
        weight_kg(float): Child's weight in kilograms (10-100 kg)
        strength(str): Paracetamol strength ('120mg/5ml' or '250mg/5ml')
        
    Returns:
        Volume in ml required, or error message if inputs(weight and strength) are invalid
    """
    # Check if weight is within range
    if weight_kg < 10 or weight_kg > 100:
        return "Error: Weight must be between 10 and 100 kg"
    
    # Check if strength is valid and calculate dose under three conditions.
    if strength == "120mg/5ml":
        dose_mg = 15 * weight_kg  # recommeded dose is 15 mg/kg
        volume_ml = (dose_mg / 120) * 5
        return round(volume_ml, 2)
    elif strength == "250mg/5ml":
        dose_mg = 15 * weight_kg  # recommeded dose is 15 mg/kg
        volume_ml = (dose_mg / 250) * 5
        return round(volume_ml, 2)
    else:
        return "Error: Invalid strength. Must be '120mg/5ml' or '250mg/5ml'"
weight_kg = float(input('Please enter your weight: '))
strength = str(input('Please enter strength (120mg/5ml or 250mg/5ml): '))
result = calculate_paracetamol_dose(weight_kg, strength)
print(f'drug dosage is {result}')


# Example
print(calculate_paracetamol_dose(30.1, "120mg/5ml"))  # Should  have a normal return of 18.81
