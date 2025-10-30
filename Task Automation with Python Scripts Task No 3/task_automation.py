import os
import shutil
import re
import requests
import time  # Used for simulated processing delay in chatbot

# --- Task 1: File and Web Operations (lp) ---

INPUT_FILE = "emails.txt"
OUTPUT_EMAILS_FILE = "extracted_emails.txt"
OUTPUT_TITLE_FILE = "website_title.txt"
TARGET_URL = "https://example.com"  # A safe and stable website for scraping


def setup_and_cleanup_files():
    """
    Creates a dummy input file and uses shutil to copy it (demonstrating shutil).
    """
    print(f"--- 1. File Setup ---")

    # 1. Create a dummy input file (emails.txt)
    dummy_content = (
        "Contact List:\n"
        "Alice <alice@example.com>\n"
        "Bob (bob.smith@work.net) is here.\n"
        "No email here.\n"
        "marketing-123@promo.org\n"
        "Final Check: user@sub.domain.co\n"
    )
    with open("temp_input.txt", "w") as f:
        f.write(dummy_content)

    # 2. Use shutil to copy the content to the final input file (demonstrates shutil concept)
    # If the file already exists, it is overwritten.
    shutil.copy("temp_input.txt", INPUT_FILE)
    print(f"Created sample input file: '{INPUT_FILE}'")

    # Clean up temp file
    os.remove("temp_input.txt")

    # Ensure output files are clean for a fresh run (demonstrates os concept)
    for f in [OUTPUT_EMAILS_FILE, OUTPUT_TITLE_FILE]:
        if os.path.exists(f):
            os.remove(f)
            print(f"Cleaned up previous output file: '{f}'")

    print("-" * 30)


def extract_emails():
    """
    Reads the input file, extracts all valid email addresses using regex,
    and saves them to a new output file.
    """
    print(f"--- 2. Email Extraction (re and File Handling) ---")

    try:
        # File Handling: Read the content
        with open(INPUT_FILE, 'r') as f:
            content = f.read()

        # Key Concept: Regex (re) to find emails
        # This is a standard, moderately complex email regex pattern
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        extracted_list = re.findall(email_pattern, content)

        if extracted_list:
            # File Handling: Write the extracted emails
            with open(OUTPUT_EMAILS_FILE, 'w') as out_f:
                out_f.write('\n'.join(extracted_list))

            print(f"Successfully extracted {len(extracted_list)} emails.")
            print(f"Emails saved to: '{OUTPUT_EMAILS_FILE}'")
        else:
            print("No emails found in the input file.")

    except FileNotFoundError:
        print(f"Error: Input file '{INPUT_FILE}' not found. Please run setup first.")

    print("-" * 30)


def scrape_website_title():
    """
    Scrapes the title of a fixed webpage using the 'requests' library and saves it.
    """
    print(f"--- 3. Web Scraping (requests and re) ---")
    print(f"Target URL: {TARGET_URL}")

    try:
        # Key Concept: requests to fetch the page content
        response = requests.get(TARGET_URL, timeout=10)
        response.raise_for_status()  # Check for bad status codes (4xx or 5xx)

        # Key Concept: Regex (re) to find the title tag content
        # Finds content between <title> and </title>
        title_match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL)

        if title_match:
            title = title_match.group(1).strip()
            print(f"Scraped Title: '{title}'")

            # File Handling: Save the title
            with open(OUTPUT_TITLE_FILE, 'w') as f:
                f.write(f"URL: {TARGET_URL}\n")
                f.write(f"Title: {title}\n")
            print(f"Title saved to: '{OUTPUT_TITLE_FILE}'")

        else:
            print("Could not find the page title.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during web request: {e}")

    print("-" * 30)


# --- Goal: Simple Rule-Based Chatbot ---

def chatbot():
    """
    A simple rule-based chatbot that responds to predefined keywords.
    Key concepts: if-elif, functions, loops, input/output.
    """
    print("--- 4. Basic Rule-Based Chatbot ---")
    print("Chatbot activated. Type 'bye' to exit.")

    # Key Concept: Loop for continuous interaction
    while True:
        try:
            # Key Concept: Input/Output (input)
            user_input = input("You: ").strip().lower()

            # Key Concept: if-elif for rule-based logic
            if user_input == "hello" or user_input == "hi":
                response = "Hi! How can I help you today?"
            elif user_input == "how are you":
                response = "I'm fine, thanks for asking! I'm a Python script running smoothly."
            elif user_input == "bye" or user_input == "goodbye":
                response = "Goodbye! Have a wonderful day."
                print(f"Bot: {response}")
                break  # Exit the loop
            elif "email" in user_input and "extract" in user_input:
                response = "I already extracted the emails! Check the 'extracted_emails.txt' file."
            elif "title" in user_input and "scrape" in user_input:
                response = "I scraped the website title and saved it to 'website_title.txt'."
            else:
                response = "I'm a basic chatbot. I only understand 'hello', 'how are you', and 'bye'."

            # Key Concept: Input/Output (print)
            time.sleep(0.5)  # A small delay to make it feel more conversational
            print(f"Bot: {response}")

        except EOFError:
            print("\nChatbot exiting due to EOF (End of File) or user interruption.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

    print("-" * 30)
    print("Chatbot task finished.")


def main():
    """
    The main execution function to run all tasks.
    """
    print("Starting Combined Python Tasks Script...")

    # 1. Execute the file and web operations first
    setup_and_cleanup_files()
    extract_emails()
    scrape_website_title()

    # 2. Start the interactive chatbot
    chatbot()

    print("All tasks complete. Check your directory for the output files!")


if __name__ == "__main__":
    main()
