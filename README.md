# Hurricane Study Project Setup Guide

This guide will walk you through the steps to set up and get started with the `Hurricane_Study` project by cloning its repository from GitHub.

## 🚀 Getting Started

Follow these simple steps to get a local copy of the project up and running on your machine.

### 🛠️ Step 0: Install Prerequisites (if not already installed)

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

### 🔑 Step 0.5: Generate a GitHub Personal Access Token (PAT)

**IMPORTANT:** GitHub no longer accepts account passwords for Git operations over HTTPS. You must use a Personal Access Token (PAT) instead, especially for private repositories or if you have 2-Factor Authentication (2FA) enabled.

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
4.  **Copy the Token:** **Crucially, copy the generated token immediately!** This is the **ONLY TIME** you will see the token. Store it securely (e.g., in a password manager).

---

### 📁 Step 1: Create a New Folder

First, you need to create a new, empty folder on your system where you want to store the project. This can be anywhere convenient for you (e.g., your Desktop, Documents, or a dedicated development directory).

**Choose your operating system and follow the instructions:**

#### 💻 Windows

1.  **Right-click** on your Desktop or in any desired location within File Explorer.
2.  Select **New** from the context menu.
3.  Click on **Folder**.
4.  Type a name for your new folder (e.g., `MyHurricaneProjects`) and press `Enter`.

#### 🐧 macOS / 🖥️ Linux

1.  Open your **Terminal** application.
2.  Navigate to your desired location using the `cd` command (e.g., `cd Desktop/` or `cd Documents/`).
3.  Run the following command to create the folder:
    ```bash
    mkdir MyHurricaneProjects
    ```
    (You can replace `MyHurricaneProjects` with your preferred folder name).

### ⬇️ Step 2: Navigate to the New Folder and Clone the Repository using PAT in URL

Now that you have your empty folder, you will open your terminal or command prompt, navigate into this new folder, and then use `git clone` to download the project files. This time, you will embed your Personal Access Token directly in the URL.

#### 💻 Windows / 🐧 macOS / 🖥️ Linux

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

### 🐍 Step 3: Create and Activate Python Virtual Environment

After cloning the repository, navigate into the newly created `Hurricane_Study` project directory. It's highly recommended to set up a dedicated Python virtual environment for this project to manage its dependencies in isolation.

1.  **Navigate into the cloned repository:**
    ```bash
    cd Hurricane_Study
    ```

2.  **Create the virtual environment:**
    ```bash
    python3 -m venv hurricane-env
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

**What Happens Next?**

Now that you have cloned the project and activated its dedicated virtual environment, you are ready to install any project-specific Python dependencies. Look for a `requirements.txt` file within the `Hurricane_Study` directory. If it exists, you'll typically run:

```bash
pip install -r requirements.txt
