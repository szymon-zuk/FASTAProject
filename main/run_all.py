import subprocess


def run_script(script_path):
    result = subprocess.run(['python3', script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {script_path}:\n{result.stderr}")
    else:
        print(f"Output of {script_path}:\n{result.stdout}")


def main():
    # Paths to the scripts
    script1 = 'conversion_image_to_csv.py'
    script2 = 'main.py'

    # Run the scripts
    print("Running the image to CSV conversion script...")
    run_script(script1)

    print("Running the FASTA file downloading script...")
    run_script(script2)


if __name__ == "__main__":
    main()
