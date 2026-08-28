import subprocess
import sys


def run_script(script_name):
    print("\n" + "=" * 60)
    print(f"Running: {script_name}")
    print("=" * 60)

    result = subprocess.run(
        [sys.executable, f"src/{script_name}"]
    )

    if result.returncode != 0:
        print(f"\n❌ Error while running {script_name}")
        sys.exit(1)

    print(f"\n✅ {script_name} completed successfully!")


def main():

    print("\n" + "=" * 60)
    print("     SMART DATA MODERNIZATION PROJECT")
    print("=" * 60)

    # Step 1: Inspect Dataset
    run_script("data_inspection.py")

    # Step 2: Clean Dataset
    run_script("data_cleaning.py")

    # Step 3: Perform EDA
    run_script("eda.py")

    # Step 4: Generate Visualizations
    run_script("visualization.py")

    print("\n" + "=" * 60)
    print("        PROJECT PIPELINE COMPLETED")
    print("=" * 60)

    print("\n✅ Data Inspection completed")
    print("✅ Data Cleaning completed")
    print("✅ Exploratory Data Analysis completed")
    print("✅ Business Analysis completed")
    print("✅ Visualizations generated")

    print("\n🎉 Smart Data Modernization project completed successfully!")


if __name__ == "__main__":
    main()