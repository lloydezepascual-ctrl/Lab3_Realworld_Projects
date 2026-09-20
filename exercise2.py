# Student-specific inputs
LAST_NAME = "PASCUAL"
SEED_NUM = 1
FAVORITE_ARTIST = "ARTHUR NERY"

def generate_fault_code(last_name, seed, artist):
    return (len(last_name) * seed) + len(artist) + 10

def trace_fault(fault_code, step=1, call_count=0):
    call_count += 1
    print(f"[RECURSION STEP {step}] Current Fault Code: {fault_code}")
    
    if fault_code <= 0:
        print(" -> Base condition reached! Fault fully isolated.")
        return call_count, [f"Resolved at Step {step} (Value: {fault_code})"]
    
    reduction = (SEED_NUM % 5) + 3
    next_code = fault_code - reduction
    
    total_calls, trace_log = trace_fault(next_code, step + 1, call_count)
    trace_log.insert(0, f"Step {step}: Code {fault_code} reduced to {next_code}")
    
    return total_calls, trace_log

def main():
    print("=== ASSESSMENT DATA ===")
    fault_code = generate_fault_code(LAST_NAME, SEED_NUM, FAVORITE_ARTIST)
    print(f"Generated Fault Data (Initial Code): {fault_code}\n")
    
    print("--- Recursive Trace Execution ---")
    total_calls, trace_history = trace_fault(fault_code)
    
    print("\n--- Diagnostic Results ---")
    print(f"Number of Recursive Calls: {total_calls}")
    print("\nExecution Log / Recursive Trace:")
    for entry in trace_history:
        print(f"  {entry}")
        
    print("\n=== FINAL OUTPUT ===")
    print(f"Fault Trace Complete. System safely recovered in {total_calls} recursive passes.")

if __name__ == "__main_s_":
    main()