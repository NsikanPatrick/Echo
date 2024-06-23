Echo - An AI Chatbot for Ecommerce
-------------------------------

Echo is an AI Chatbot built to improve the customer service in Ecommerce platforms.
It interacts from a custom knowledge base stored in PDF OR DOCX Formats.


**Features:**

-   Processes text from PDF or DOCX files.
-   Uses Natural Language Processing (NLP) techniques for basic text cleaning and understanding.
-   Responds to user queries by retrieving relevant information from the knowledge base.
-   Provides a simple user interface for interactive chat.

**Requirements:**

-   Python 3.x
-   PyTorch (CPU-only version)
-   nltk library
-   PyPDF2 library (for PDF knowledge base) and python-docx library (for DOCX knowledge base)

**Getting Started:**

1.  **Clone the repository:**

    Bash

    ```
    git clone https://your_github_repo_url.git

    ```

2.  **Create a virtual environment (recommended):**

    Bash

    ```
    python -m venv echo_env
    source echo_env/bin/activate  # For macOS/Linux
    echo_env\Scripts\activate.bat  # For Windows

    ```

3.  **Install required libraries:**

    Bash

    ```
    pip install nltk PyPDF2 (or python-docx) 
    pip install torch torchvision

    ```

4.  **Download nltk resources (first time only):**

    Python

    ```
    import nltk
    nltk.download('punkt')  # Download sentence tokenizer
    # Download other resources as needed (e.g., stop words, stemming/lemmatization models)

    ```

5.  **Run the chatbot:**

    Bash

    ```
    python chatbot.py

    ```

    This will start the Echo chatbot, allowing you to interact with it by providing text input.

**Project Structure:**

-   `chatbot.py`: Main script containing chatbot logic.
-   `knowledge_base.py`: Functions for processing and storing knowledge base information.
-   `interface.py`: Code for creating a user interface.

**Further Development:**

-   Implement a rule-based or topic modeling approach for knowledge base retrieval.
-   Enhance the chatbot's response generation capabilities.
-   Design a more user-friendly interface.
-   Explore integrating with external APIs or services.

**Contributing:**

We welcome contributions to improve this project. Please refer to the CONTRIBUTING.md file for guidelines.

**License:**

This project is licensed under the MIT License (see LICENSE file).