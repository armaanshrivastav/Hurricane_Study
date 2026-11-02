# Hurricane Study Project Setup Guide

This guide will walk you through the steps to set up and get started with the `Hurricane_Study` project by cloning its repository from GitHub.

## Overview

The Hurricane Visualization Tool is an interactive 3D visualization interface for exploring NOAA dropwindsonde measurements from multiple hurricanes. It allows users to examine six atmospheric measurements simultaneously through synchronized 3D plots, making it easier to compare conditions within hurricanes.

The interface includes navigation between hurricane datasets, synchronized plot interactions, and PDF export.

## Getting Started

Follow these simple steps to get a local copy of the project up and running on your machine.

### Step 0: Install Prerequisites (if not already installed)

Before you begin, ensure you have **Git** and **Python 3+** installed on your system.

#### Git Installation 

Git is essential for cloning the project repository.

* **Check if Git is installed:** Open your terminal/command prompt and run:
    ```bash
    git --version
    ```
    If you see a version number (e.g., `git version 2.30.0`), Git is installed. Otherwise, proceed with the installation below.

* **Install Git:**
    * **Windows:** Download the installer from the official Git website: [Git for Windows](https://git-scm.com/download/win)
        Follow the setup wizard. The default options are usually fine.
    * **macOS:**
        * **Recommended (Homebrew):** If you have Homebrew installed, open your terminal and run:
            ```bash
            brew install git
            ```
        * **Alternative (Xcode Command Line Tools):** Git is often included with Xcode Command Line Tools. Try running `git --version` in your terminal; if it prompts you to install command line tools, agree to it.
    * **Linux (Debian/Ubuntu):** Open your terminal and run:
        ```bash
        sudo apt update
        sudo apt install git
        ```
    * **Linux (Fedora):**
        ```bash
        sudo dnf install git
        ```

#### Python 3+ Installation

This project likely requires Python to run. Ensure you have Python version 3.x installed.

* **Check if Python 3+ is installed:** Open your terminal/command prompt and run:
    ```bash
    python3 --version
    ```
    or simply
    ```bash
    python --version
    ```
    If you see a version number like `Python 3.9.7`, you're good to go. If you see `Python 2.x.x` or an error, you need to install Python 3.

* **Install Python 3+:**
    * **Windows/macOS:** Download the appropriate installer from the official Python website:
        [Python Downloads](https://www.python.org/downloads/)
        * **Important for Windows:** During installation, make sure to check the box that says "**Add Python X.Y to PATH**" (where X.Y is the version number). This makes it easier to run Python from the command line.
    * **Linux (most distributions):** Python 3 is often pre-installed or easily available via your package manager:
        ```bash
        sudo apt update          # Debian/Ubuntu
        sudo apt install python3 # Debian/Ubuntu
        # Or for Fedora:
        sudo dnf install python3
        ```

### Step 0.5: Generate a GitHub Personal Access Token (PAT)

**IMPORTANT:** You must use a Personal Access Token (PAT) instead, especially for private repositories or if you have 2-Factor Authentication (2FA) enabled.

**SECURITY WARNING:** Embedding your PAT directly in the clone URL (as shown in Step 2) is generally **NOT RECOMMENDED** for long-term or shared use. It exposes your token in your shell history and potentially other logs, which is a security risk. For better security, consider using a Git credential helper (refer to Git documentation). This method is provided for specific scenarios where direct URL embedding is preferred despite the risks.

1.  **Log in to GitHub:** Go to [github.com](https://github.com/) and log in to your account in your web browser.
2.  **Navigate to Developer Settings:**
    * Click your **profile picture** in the top-right corner.
    * Select **Settings**.
    * In the left sidebar, scroll down and click **Developer settings**.
    * Click **Personal access tokens** and then select **Tokens (classic)**.
3.  **Generate a New Token:**
    * Click the **"Generate new token"** button.
    * **Note:** Give your token a descriptive name (e.g., `Hurricane Study Project Access`).
    * **Expiration:** Choose an expiration date. For security, it's recommended to set an expiration (e.g., 90 days, 1 year) rather than "No expiration".
    * **Scopes:** Select the necessary permissions (scopes). For cloning public and private repositories, select at least `repo` (which grants full control of private repositories). You might only need `public_repo` if you are sure you will *only* interact with public repositories.
    * Click **"Generate token"** at the bottom of the page.
4.  **Copy the Token:** **Copy the generated token immediately!** This is the **ONLY TIME** you will see the token. Store it securely (e.g., in a password manager).

---

### Step 1: Create a New Folder

First, you need to create a new, empty folder on your system where you want to store the project. This can be anywhere convenient for you (e.g., your Desktop, Documents, or a dedicated development directory).

**Choose your operating system and follow the instructions:**

#### Windows

1.  **Right-click** on your Desktop or in any desired location within File Explorer.
2.  Select **New** from the context menu.
3.  Click on **Folder**.
4.  Type a name for your new folder (e.g., `MyHurricaneProjects`) and press `Enter`.

#### macOS / Linux

1.  Open your **Terminal** application.
2.  Navigate to your desired location using the `cd` command (e.g., `cd Desktop/` or `cd Documents/`).
3.  Run the following command to create the folder:
    ```bash
    mkdir MyHurricaneProjects
    ```
    (You can replace `MyHurricaneProjects` with your preferred folder name).

### Step 2: Navigate to the New Folder and Clone the Repository using PAT in URL

Now that you have your empty folder, you will open your terminal or command prompt, navigate into this new folder, and then use `git clone` to download the project files. This time, you will embed your Personal Access Token directly in the URL.

#### Windows / macOS / Linux

1.  Open your **Terminal** or **Command Prompt** / **PowerShell**.
2.  Use the `cd` command to navigate into the folder you created in Step 1.
    * **Example (if on Desktop, Linux/macOS):**
        ```bash
        cd ~/Desktop/MyHurricaneProjects
        ```
    * **Example (if on Desktop, Windows):**
        ```cmd
        cd C:\Users\YourUsername\Desktop\MyHurricaneProjects
        ```
        (Remember to replace `YourUsername` with your actual Windows username).
3.  Once inside your new folder, execute the following command to clone the repository. **Replace `<YOUR_PERSONAL_ACCESS_TOKEN>` with the actual token you generated in Step 0.5.**
    ```bash
    git clone https://<YOUR_PERSONAL_ACCESS_TOKEN>@github.com/armaanshrivastav/Hurricane_Study.git
    ```
    *Note: You will not be prompted for a username or password when using this method, as the token is directly provided in the URL.*

---

### Step 3: Create and Activate Python Virtual Environment

After cloning the repository, navigate into the newly created `Hurricane_Study` project directory. It's highly recommended to set up a dedicated Python virtual environment for this project to manage its dependencies in isolation.

1.  **Navigate into the cloned repository:**
    ```bash
    cd Hurricane_Study
    ```

2.  **Create the virtual environment:**
    ```bash
    python -m venv hurricane-env
    ```
    This command creates a new folder named `hurricane-env` inside your `Hurricane_Study` directory, containing a private copy of the Python interpreter and associated files.

3.  **Activate the virtual environment:**
    * **On Linux/macOS:**
        ```bash
        source hurricane-env/bin/activate
        ```
    * **On Windows (Command Prompt):**
        ```cmd
        hurricane-env\Scripts\activate.bat
        ```
    * **On Windows (PowerShell):**
        ```powershell
        .\hurricane-env\Scripts\Activate.ps1
        ```
    Once activated, your terminal prompt will usually show `(hurricane-env)` at the beginning, indicating that you are now working within this isolated environment.

---

### Step 4: Install Python Dependencies

Now that you have cloned the project and activated its dedicated virtual environment, you are ready to install any project-specific Python dependencies. Look for a `requirements.txt` file within the `Hurricane_Study` directory. If it exists, you'll typically run:

```bash
pip install -r requirements.txt
```


### Step 5: Download and Prepare Project Data

This project requires external data from Google Drive. Follow these steps to download it and place it correctly for processing.

1.  **Download the Data from Google Drive:**
    * Access the Google Drive link: https://drive.google.com/drive/folders/1-0gmto35N7WkK2AC-FP9s8Qhs_o4Aigc?usp=sharing
    * Download the entire dataset. It will likely be a zipped file (e.g., `HurricaneData.zip`).
    * Save this downloaded file to a temporary location on your computer (e.g., your Downloads folder).

2.  **Create the Data Folder:**
    * Navigate back to your `Hurricane_Study` project directory in your terminal (if you're not already there):
        ```bash
        cd /path/to/MyHurricaneProjects/Hurricane_Study
        ```
        (Replace `/path/to/MyHurricaneProjects` with the actual path to your top-level folder).
    * Create a new folder specifically for the raw data:
        ```bash
        mkdir HurricaneCompleteData
        ```
        This creates `Hurricane_Study/HurricaneCompleteData/`.

3.  **Extract Data into the Folder:**
    * **Unzip** the downloaded data file (`HurricaneData.zip` or similar). This will typically create a folder containing the actual data files.
    * **Move** the *contents* of the unzipped folder into the `HurricaneCompleteData` folder you just created.
        * **Example (Conceptual):** If unzipping `HurricaneData.zip` creates a folder `unzipped_data_contents`, you would move everything from `unzipped_data_contents/*` to `Hurricane_Study/HurricaneCompleteData/`.
        * **Verify:** After moving, the `HurricaneCompleteData` folder should directly contain the raw data files or subfolders, not another single folder with the same name.

4.  **Run the Data Transformation Script:**
    * **Ensure your `hurricane-env` virtual environment is still active.**
    * Execute the `transformData.py` script, which will process the raw data.
        ```bash
        python transformData.py
        ```
        Verify whether the Processed Data folder was made under the MyHurricaneProject folder.
    * Monitor the terminal for any output or errors from the script.
    * If you experience any issues, please contact Armaan Shrivastav for assistance.

---

### Step 6: Run the Common Utilities Script (`common.py`)

After the data has been transformed, the `common.py` script needs to be executed to set up common utilities or perform further essential processing for the project.

1.  **Ensure your `hurricane-env` virtual environment is still active.**
2.  **Ensure you are in the `Hurricane_Study` directory.**
3.  **Run the `common.py` script:**
    ```bash
    python common.py
    ```
    * Pay attention to any output or prompts in the terminal during its execution.
    * If you experience any issues, please contact Armaan Shrivastav for assistance.

---

### Step 7: View the Generated Graphs (Local Server)

The `common.py` script directly generates a `graphs` folder containing the visualization files. To view these (likely HTML files or similar), you'll need to serve them using a simple Python web server.

1.  **Locate the `graphs` Folder:**
    * After `common.py` runs, you should find a new folder named `graphs` within your `Hurricane_Study` directory.
    * **Remember the exact path** to this `graphs` folder.

2.  **Navigate to the `graphs` Folder in Command Prompt:**
    * Open a **new** terminal or command prompt window.
    * Use the `cd` command to go into the *`graphs` folder*.
        * **Example:** If your `Hurricane_Study` project is at `C:\Users\YourUsername\MyHurricaneProjects\Hurricane_Study`, then the `graphs` folder would likely be at `C:\Users\YourUsername\MyHurricaneProjects\Hurricane_Study\graphs`.
            ```cmd
            cd C:\Users\YourUsername\MyHurricaneProjects\Hurricane_Study\graphs
            ```
        * **Example (Linux/macOS):** If your `Hurricane_Study` project is at `~/Desktop/MyHurricaneProjects/Hurricane_Study`, then the `graphs` folder would likely be at `~/Desktop/MyHurricaneProjects/Hurricane_Study/graphs`.
            ```bash
            cd ~/Desktop/MyHurricaneProjects/Hurricane_Study/graphs
            ```
    * **It is crucial that you are *inside* this `graphs` folder** when you run the next command.

3.  **Run the Python HTTP Server:**
    * With your terminal/command prompt inside the `graphs` folder, run the following command to start a simple local web server:
        ```bash
        python -m http.server
        ```
        * You should see output like `Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...` This means the server is running.
        * **Keep this terminal window open** as long as you want the server to run.

4.  **Open the Graphs in Your Browser:**
    * Open your web browser (Chrome, Firefox, Edge, Safari, etc.).
    * In the address bar, type the following URL and press Enter:
        ```
        http://localhost:8000/root.html
        ```
        
    * This should open the main page of your generated graphs.

---

**Final Notes:**

* Ensure all Python scripts (`transformData.py`, `common.py`) complete successfully without errors before proceeding to the next steps.
* The `python -m http.server` command serves files from the directory where it's executed. Make sure you are in the *unzipped `graphs` folder* for it to work correctly.
* To stop the local web server, go back to the terminal window where it's running and press `Ctrl + C` (Command + C on macOS).
