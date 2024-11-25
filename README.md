
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
   python3 scan.py
   ```

   (Make sure to replace `scan.py` with the actual name of the script.)

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

### **Contributing**

Feel free to fork this repository, open issues, or submit pull requests to improve this tool.

---

# **Support Me on Saweria**

Hi there! 👋 If you enjoy the tools, scripts, or content I provide, you can support me via **Saweria**. Your support helps me continue developing and maintaining projects like this!

### **How to Support**

You can donate to me through the following link:

<a href="https://saweria.co/Sansekai" target="_blank"><img src="https://user-images.githubusercontent.com/26188697/180601310-e82c63e4-412b-4c36-b7b5-7ba713c80380.png" alt="Donate For Yusril" height="41" width="174"></a>

---

### **Why Support?**

Your support helps me:
- Maintain and improve the tools I develop.
- Create more resources and tutorials.
- Keep the project open-source and free for everyone.

---

### **How to Donate**

1. Click the button or the link to visit my Saweria page:  
   [Support Me on Saweria](https://saweria.co/AsmaraHancur)

2. Choose an amount you’d like to contribute and follow the donation process.

---

### **Thank You! 🙏**

Every contribution is deeply appreciated. Even if you're unable to donate, simply sharing my tools with others or providing feedback is also incredibly helpful!

---

### **Contact**

Feel free to reach out if you have any questions or would like to contribute in other ways. I’m always open to feedback!

---

### **Follow Me**

You can also follow me on other platforms:

- [GitHub](https://github.com/AsmaraHancur)
- [Telegram](https://t.me/AsmaraHancur)
- [Twitter](https://twitter.com/AsmaraHancur)

---

### **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
