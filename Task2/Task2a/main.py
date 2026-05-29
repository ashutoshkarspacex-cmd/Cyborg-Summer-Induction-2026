import os
from script2a import localize_bot

# ==========================================
# MAIN DRIVER FILE FOR TASK 2A
# ==========================================

def main():
    print("Running Task 2A Localization Pipeline...\n")
    
    # Run student solution
    try:
        result = localize_bot()
    except Exception as e:
        print(f"Error executing script: {e}")
        return

    # Print formatted output
    print("========== DETECTED OUTPUT ==========\n")

    if not result:
        print("No output returned.")
    else:
        for key, value in result.items():
            if key == "markers":
                print("markers:")
                for marker_id, data in value.items():
                    print(f"  {marker_id} : {data}")
            else:
                print(f"{key} : {value}")

    print("\n=====================================\n")

if __name__ == "__main__":
    main()