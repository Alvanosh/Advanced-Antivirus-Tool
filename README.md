
# 🎊 **👾 Advanced Antivirus Tool** - Your Shield Against Malware 👾 🎊

## 🌟 **Introduction**
Welcome to the **Advanced Antivirus Tool**! Designed to help you **detect** and **manage malware threats** efficiently, this tool features user-friendly capabilities and robust functionalities to provide you with an **enhanced security experience**. The tool is currently **under construction**, and we are continually working to improve its capabilities.

## 🚀 **Key Features**
1. **Manual File Scan** 🕵️‍♂️
   - **Scan** any file on your system for malware using **MD5 hash checking** and **YARA rules**.
   - Provides immediate feedback on whether the file is **clean** ✅ or **flagged as malicious** ❌.

2. **Real-Time Monitoring** 🔍
   - **Monitor** specified directories for file changes.
   - Automatically **scan** modified files for immediate threat detection.

3. **Add Malware Signature to Database** 📝
   - **Add** custom signatures for known malware by entering the file's name and its **MD5 hash**.
   - Keep the detection capabilities updated by enhancing the signature database.

4. **List Malware Signatures** 📜
   - **View** all malware signatures stored in the database.
   - Manage and review known threats efficiently.

5. **Delete Malware Signature from Database** ❌
   - **Remove** outdated or unnecessary signatures.
   - Maintain a clean and relevant signature database.

## ⚙️ **Installation Instructions**
### How to Run the Tool
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd antivirus_tool
   ```

2. **Set Up a Virtual Environment (Optional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```
   Make sure to install packages such as `yara-python`, `watchdog`, and `sqlite3`.

4. **Run the Tool:**
   ```bash
   python main.py
   ```
   Follow the on-screen prompts for navigation.

## 🛠️ **Usage Guide**
- **Option 1:** **Manual File Scan** - Enter the file path for scanning. 📂
- **Option 2:** **Start Real-Time Monitoring** - Specify the directory to monitor for changes. 🔔
- **Option 3:** **Add Malware Signature** - Enter the name and MD5 hash of the malware to add. ➕
- **Option 4:** **List Malware Signatures** - View all current signatures in the database. 📊
- **Option 5:** **Delete Malware Signature** - Remove a selected signature from the database. 🗑️
- **Option 6:** **Exit** - Close the application. ❌

## 🧑‍💻 **About the Author**
**Alvanosh Jojo** is a passionate cybersecurity expert and ethical hacker dedicated to creating innovative security solutions. He is focused on building a robust antivirus tool that adapts to the ever-evolving threat landscape, empowering users with the knowledge to protect against malware and cyber threats. 🌐

### **Connect with Alvanosh Jojo:**
- **Website:** [alvanosh.info](https://alvanosh.info) 🌟
- **GitHub:** [Alvanosh](https://github.com/Alvanosh) 🛠️

## 💡 **Conclusion**
The **Advanced Antivirus Tool** represents a significant step towards enhanced protection against malware threats. Your feedback and contributions are invaluable as we strive to improve and expand the tool’s features. Stay tuned for exciting updates and enhancements! 🚀
