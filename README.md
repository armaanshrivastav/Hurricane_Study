# Hurricane Study Project Setup Guide

This guide will walk you through the steps to set up and get started with the `Hurricane_Study` project by cloning its repository from GitHub.

## 🚀 Getting Started

Follow these simple steps to get a local copy of the project up and running on your machine.

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

### ⬇️ Step 2: Navigate to the New Folder and Clone the Repository

Now that you have your empty folder, you will open your terminal or command prompt, navigate into this new folder, and then use `git clone` to download the project files.

#### 💻 Windows

1.  Open **Command Prompt** or **PowerShell**.
2.  Use the `cd` command to navigate into the folder you just created.
    * **Example (if on Desktop):**
        ```cmd
        cd C:\Users\YourUsername\Desktop\MyHurricaneProjects
        ```
        (Remember to replace `YourUsername` with your actual Windows username).
3.  Once inside your new folder, execute the following command to clone the repository:
    ```bash
    git clone [https://github.com/armaanshrivastav/Hurricane_Study.git](https://github.com/armaanshrivastav/Hurricane_Study.git)
    ```

#### 🐧 macOS / 🖥️ Linux

1.  Open your **Terminal** application.
2.  Use the `cd` command to navigate into the folder you created in Step 1.
    * **Example (if on Desktop):**
        ```bash
        cd ~/Desktop/MyHurricaneProjects
        ```
3.  Once inside your new folder, execute the following command to clone the repository:
    ```bash
    git clone [https://github.com/armaanshrivastav/Hurricane_Study.git](https://github.com/armaanshrivastav/Hurricane_Study.git)
    ```

---

**What Happens Next?**

After successfully running the `git clone` command, a new subfolder named `Hurricane_Study` will be created *inside* your `MyHurricaneProjects` folder. This `Hurricane_Study` folder will contain all the files and history from the GitHub repository.

You can now navigate into this `Hurricane_Study` folder (`cd Hurricane_Study`) to explore the project's contents and follow any further instructions provided within that repository (e.g., for installing dependencies or running the project).
