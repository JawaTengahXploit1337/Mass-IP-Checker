
---

# **Fast Scan Mass IP & Same IP Checker Tool**

This tool allows you to perform fast IP scanning and check which websites share the same IP address. It's designed to process a list of websites and return their corresponding IP addresses, with the option to gather all websites that share the same IP.

---

### **Features**

- Fast scan of mass websites for their IP addresses.
- Checks which websites share the same IP address.
- Displays colorful outputs in the terminal for a better user experience.
- Simple and efficient way to process a list of URLs from a file.

---

### **Requirements**

Before running the tool, you need to have the following Python packages installed:

- **colorama**: Used for coloring the terminal output.

You can install it using pip:

```bash
pip install colorama
```

---

### **How to Use**

1. **Prepare Your Website List File**:
   Create a text file (e.g., `list.txt`) with each website URL on a new line. Example:

   ```
   example.com
   google.com
   github.com
   ```

2. **Run the Tool**:
   Clone or download the repository containing this script, then run the tool using Python.

   ```bash
   python your_script_name.py
   ```

   (Make sure to replace `your_script_name.py` with the actual name of the script.)

3. **Enter the File Path**:
   When prompted, input the path of your `list.txt` file containing the website URLs. Example:

   ```
   Enter Your List.txt File: list.txt
   ```

4. **View Results**:
   The tool will print out each website and its corresponding IP address. Websites with the same IP will be grouped together.

   Example output:

   ```
   Websites With IP 192.168.1.1:
   example.com
   google.com
   ```

5. **Optional: Gather Websites With The Same IP**:
   If you want to check which websites share the same IP, type `yes` when prompted:

   ```
   Would You Like To Gather Websites With The Same IP? (yes/no): yes
   Enter The IP Address You Want To Check: 192.168.1.1
   ```

   The tool will then display all websites that share the given IP address.

6. **Finish**:
   After the scan and optional IP check, the tool will display a thank you message:

   ```
   Terima kasih!
   ```

---

### **Example Usage**

1. Run the script:

   ```bash
   python scan_ip.py
   ```

2. Provide the file path:

   ```
   Enter Your List.txt File: websites.txt
   ```

3. Output will display the website and its corresponding IP:

   ```
   example.com: 192.168.1.1
   google.com: 192.168.1.2
   ```

4. Optionally, gather websites with the same IP:

   ```
   Would You Like To Gather Websites With The Same IP? (yes/no): yes
   Enter The IP Address You Want To Check: 192.168.1.1
   ```

   Result:

   ```
   Websites With IP 192.168.1.1:
   example.com
   ```

---

### **Contributing**

Feel free to fork this repository, open issues, or submit pull requests to improve this tool.

---

### **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
