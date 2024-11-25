
---

# **Pindai Cepat IP Massal &amp; Alat Pemeriksa IP yang Sama**

Alat ini memungkinkan Anda melakukan pemindaian IP dengan cepat dan memeriksa situs web mana yang berbagi alamat IP yang sama. Ini dirancang untuk memproses daftar situs web dan mengembalikan alamat IP yang sesuai, dengan opsi untuk mengumpulkan semua situs web yang berbagi IP yang sama.

---

### **Fitur**

- Pemindaian cepat situs web massal untuk mengetahui alamat IP-nya.
- Memeriksa situs web mana yang berbagi alamat IP yang sama.
- Menampilkan keluaran berwarna-warni di terminal untuk pengalaman pengguna yang lebih baik.
- Cara sederhana dan efisien untuk memproses daftar URL dari suatu file.

---

### **Urutannya**

Sebelum menjalankan alat ini, Anda perlu menginstal paket Python berikut:

- **colorama**: Digunakan untuk mewarnai keluaran terminal.

You can install it using pip:

```bash
pip install colorama
```

---

### **Cara Menggunakan**

1. **Siapkan File Daftar Website Anda**:
   Create a text file (e.g., `list.txt`) with each website URL on a new line. Example:

   ```
   example.com
   google.com
   github.com
   ```

2. **Jalankan Alat**:
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

### **Example Usage**

1. Run the script:

   ```bash
   python3 scan.py
   ```

2. Berikan jalur file:

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

# **Support Me on Saweria**

Hi there! 👋 If you enjoy the tools, scripts, or content I provide, you can support me via **Saweria**. Your support helps me continue developing and maintaining projects like this!

### **How to Support**

You can donate to me through the following link:

<a href="https://saweria.co/AsmaraHancur" target="_blank"><img src="https://user-images.githubusercontent.com/26188697/180601310-e82c63e4-412b-4c36-b7b5-7ba713c80380.png" alt="Donate For AsmaraHancur" height="41" width="174"></a>

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
- 
---

### **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
