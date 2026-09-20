import functools

# Student-specific inputs
LAST_NAME = "PASCUAL"
SEED_NUM = 1
FAVORITE_ARTIST = "ARTHUR NERY"

# Decorator to log diagnostic process
def log_diagnostic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[EXECUTION LOG] Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[EXECUTION LOG] {func.__name__} completed successfully.")
        return result
    return wrapper

# 1. Generate student-specific equipment readings
def generate_readings(last_name, seed, artist):
    base_val = len(last_name) * 10 + seed + len(artist)
    # Generates a mix of valid and invalid sensor readings
    raw_readings = [base_val, base_val + 15, -999, base_val + 50, "INVALID_DATA", base_val - 10]
    return raw_readings

# 2. Validation function
def validate_reading(reading):
    if not isinstance(reading, (int, float)):
        raise TypeError(f"Invalid data type: {reading}")
    if reading < 0 or reading > 200:
        raise ValueError(f"Reading out of operational range (0-200): {reading}")
    return True

# 3. Calculation & Classification
def classify_reading(reading):
    if reading < 40:
        return "LOW (Underperforming)"
    elif 40 <= reading <= 80:
        return "NORMAL (Optimal)"
    else:
        return "HIGH (Critical/Overheating)"

@log_diagnostic
def run_diagnostic_system():
    print("=== ASSESSMENT DATA ===")
    print(f"Student Inputs: LAST_NAME='{LAST_NAME}', SEED_NUM={SEED_NUM}, FAVORITE_ARTIST='{FAVORITE_ARTIST}'\n")
    
    readings = generate_readings(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    print(f"Generated Equipment Data: {readings}\n")
    
    valid_readings = []
    validation_results = []
    
    print("--- Validation Process ---")
    for r in readings:
        try:
            validate_reading(r)
            valid_readings.append(r)
            validation_results.append((r, "VALID"))
        except (ValueError, TypeError) as e:
            validation_results.append((r, f"INVALID ({e})"))

    print(f"Validation Results: {validation_results}\n")

    print("--- Diagnostic Results ---")
    classified = []
    for r in valid_readings:
        status = classify_reading(r)
        classified.append((r, status))
        print(f" Reading: {r} -> Status: {status}")

    print("\n=== FINAL OUTPUT ===")
    print(f"Total Processed: {len(readings)} | Valid: {len(valid_readings)} | Invalid: {len(readings) - len(valid_readings)}")
    print("Overall System Condition: Operational with monitored exceptions.")

if __name__ == "__main__":
    run_diagnostic_system()