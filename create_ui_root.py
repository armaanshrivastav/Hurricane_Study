import os
import re

def create_root_html_with_larger_subcategory_buttons(base_directory, output_file, project_title, placeholder_name):
    # Group subdirectories by the prefix (e.g., 'beryl')
    grouped_folders = {}
    for folder in os.listdir(base_directory):
        if os.path.isdir(os.path.join(base_directory, folder)):
            match = re.match(r'([a-zA-Z]+)\d+_', folder)
            if match:
                prefix = match.group(1)
                if prefix not in grouped_folders:
                    grouped_folders[prefix] = []
                grouped_folders[prefix].append(folder)

    # Sort the prefixes alphabetically
    sorted_prefixes = sorted(grouped_folders.keys())

    # Print the grouped subdirectories
    print("Grouped subdirectories:")
    for prefix, folders in grouped_folders.items():
        print(f"{prefix}: {sorted(folders)}")

    # Start creating the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{project_title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            header {{
                text-align: center;
                margin-bottom: 20px;
            }}
            .category-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
                gap: 10px;
                width: 80%;
                margin: auto;
                margin-bottom: 20px;
            }}
            .category-item {{
                background-color: #007BFF;
                color: white;
                cursor: pointer;
                padding: 10px;
                border-radius: 5px;
                text-align: center;
                font-size: 14px;
                transition: background-color 0.3s;
            }}
            .category-item:hover {{
                background-color: #0056b3;
            }}
            .subcategory-grid {{
                display: grid;
                grid-template-columns: repeat(2, minmax(150px, 1fr)); /* Force two columns */
                gap: 15px; /* Adjust gap as needed */
                width: 80%;
                margin: 10px auto;
                padding: 15px;
                background-color: #f9f9f9;
                border: 1px solid #ccc;
                border-radius: 5px;
                display: none;
            }}
            .subcategory-item {{
                background-color: #00A087;
                color: white;
                text-align: center;
                padding: 12px; /* Adjust padding as needed */
                border-radius: 3px;
                text-decoration: none;
                font-size: 14px;
                transition: background-color 0.3s;
            }}
            .subcategory-item:hover {{
                background-color: #00705a;
            }}
            footer {{
                text-align: center;
                margin-top: 20px;
                font-size: 14px;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>{project_title}</h1>
        </header>
        <div class="category-grid">
    """

    # Add category items for each prefix
    for prefix in sorted_prefixes:
        html_content += f"""
            <div class="category-item" onclick="toggleSubcategories('{prefix}')">
                {prefix}
            </div>
        """

    html_content += f"""
        </div>
    """

    # Add subcategory grids for each prefix
    for prefix in sorted_prefixes:
        html_content += f"""
        <div id="{prefix}-subgrid" class="subcategory-grid">
        """
        # Add sub-links for each folder under the prefix
        for folder in sorted(grouped_folders[prefix]):
            folder_path = os.path.basename(folder)
            html_content += f'<a href="{folder}/main.html" class="subcategory-item">{folder_path}</a>\n'
        html_content += f"""
        </div>
        """

    # Add footer with placeholder
    html_content += f"""
        <footer>
            <p>Created by: {placeholder_name}</p>
        </footer>
        <script>
            function toggleSubcategories(prefix) {{
                var subgrid = document.getElementById(prefix + '-subgrid');
                if (subgrid.style.display === 'grid') {{
                    subgrid.style.display = 'none';
                }} else {{
                    subgrid.style.display = 'grid';
                }}
                var allSubgrids = document.querySelectorAll('.subcategory-grid');
                for (var i = 0; i < allSubgrids.length; i++) {{
                    if (allSubgrids[i].id !== prefix + '-subgrid') {{
                        allSubgrids[i].style.display = 'none';
                    }}
                }}
            }}
        </script>
    </body>
    </html>
    """

    # Write the content to the root.html file
    with open(output_file, "w") as file:
        file.write(html_content)

    print(f"root.html created successfully at {output_file}")

if __name__ == '__main__':
    base_dir = '.'  # Replace with your actual base directory
    output_file = 'root.html'
    project_name = 'Data Overview'
    user_name = 'Your Name'

    # Create some dummy directories for testing
    os.makedirs(os.path.join(base_dir, 'beryl01_20240701_005016'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'beryl02_20240703_015520'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'beryl03_20240704_025520'), exist_ok=True) # Added a third beryl folder
    os.makedirs(os.path.join(base_dir, 'alpha01_20240705_100000'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'alpha02_20240706_120000'), exist_ok=True)
    os.makedirs(os.path.join(base_dir, 'gamma_other'), exist_ok=True) # This one won't be grouped

    create_root_html_with_two_subcategories_per_row(base_dir, output_file, project_name, user_name)

    # Clean up dummy directories (optional)
    import shutil
    shutil.rmtree(os.path.join(base_dir, 'beryl01_20240701_005016'), ignore_errors=True)
    shutil.rmtree(os.path.join(base_dir, 'beryl02_20240703_015520'), ignore_errors=True)
    shutil.rmtree(os.path.join(base_dir, 'beryl03_20240704_025520'), ignore_errors=True)
    shutil.rmtree(os.path.join(base_dir, 'alpha01_20240705_100000'), ignore_errors=True)
    shutil.rmtree(os.path.join(base_dir, 'alpha02_20240706_120000'), ignore_errors=True)
    shutil.rmtree(os.path.join(base_dir, 'gamma_other'), ignore_errors=True)
    os.remove(output_file)