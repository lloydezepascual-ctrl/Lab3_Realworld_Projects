# Student-specific inputs
LAST_NAME = "PASCUAL"
SEED_NUM = 1
FAVORITE_ARTIST = "ARTHUR NERY"

def parse_telemetry_stream():
    # Dynamic list construction based on student details
    raw_data = [len(LAST_NAME) * 10, SEED_NUM * 15, len(FAVORITE_ARTIST) * 5, 120, 85, 42]
    print(f"Initial Telemetry Buffer: {raw_data}")
    
    # Process buffer using list methods
    raw_data.append(99)
    raw_data.sort()
    print(f"Sorted Telemetry Stream: {raw_data}")
    
    return raw_data

def analyze_metrics(data_stream):
    metrics_summary = {
        "min_val": min(data_stream),
        "max_val": max(data_stream),
        "avg_val": sum(data_stream) / len(data_stream),
        "status_code": "OPTIMAL" if max(data_stream) < 200 else "CRITICAL"
    }
    return metrics_summary

def main():
    print("=== ASSESSMENT DATA ===")
    print(f"Student: {LAST_NAME} | Seed: {SEED_NUM} | Favorite Artist: {FAVORITE_ARTIST}\n")
    
    print("--- Processing Telemetry Data ---")
    processed_stream = parse_telemetry_stream()
    
    print("\n--- Diagnostic Results ---")
    results = analyze_metrics(processed_stream)
    for key, value in results.items():
        print(f"  {key.upper()}: {value}")
        
    print("\n=== FINAL OUTPUT ===")
    print(f"Telemetry Analysis Complete | Status: {results['status_code']} | Peak: {results['max_val']}")

if __name__ == "__main__":
    main()
