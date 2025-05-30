# 🔐 PassHub

Welcome to **PassHub** - Your ultimate password security companion! This Streamlit-powered web application helps you generate strong passwords, analyze password strength, and check against common password databases.

## ✨ Features

### 🔍 Password Security Checker
- **Common Password Detection**: Checks your password against a database of common passwords
- **Strength Analysis**: Evaluates password strength based on multiple criteria
- **Real-time Feedback**: Provides instant suggestions for password improvement
- **Security Scoring**: Rates passwords as Strong, Medium, or Weak

### ⚙️ Password Generator
- **Customizable Length**: Generate passwords from 8 to 24 characters
- **Character Set Control**: Customize uppercase, lowercase, numbers, and special characters
- **Secure Generation**: Uses `random.SystemRandom()` for cryptographically secure randomness
- **Instant Analysis**: Built-in security check for generated passwords

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/melodies08/passhub.git
   cd passhub
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit
   ```

3. **Create the common passwords database**
   
   Create a file named `common_passwords.txt` in the project directory and populate it with common passwords (one per line). You can download popular password lists from sources like:
   - [SecLists](https://github.com/danielmiessler/SecLists)
   - [OWASP](https://owasp.org/www-community/password-special-characters)

4. **Run the application**
   ```bash
   streamlit run PassHub.py
   ```

5. **Access the app**
   
   Open your browser and navigate to `https://passhub.onrender.com/`


## 🛡️ Security Features

### Password Strength Criteria
PassHub evaluates passwords based on these security standards:

- ✅ **Length**: Minimum 8 characters (12-14 recommended)
- ✅ **Mixed Case**: Both uppercase and lowercase letters
- ✅ **Numbers**: At least one numeric digit
- ✅ **Special Characters**: Includes symbols like `{!?:;@#$%^&*<>.})`

### Common Password Protection
- Checks against a comprehensive database of commonly used passwords
- Provides ranking information (e.g., "#1 most common password")
- Helps users avoid easily guessable passwords

## 🎯 Usage Examples

### Checking Password Strength
1. Navigate to the "🔍 Check Password" tab
2. Enter your password in the secure input field
3. Review the instant feedback and suggestions
4. Implement recommended improvements

### Generating Secure Passwords
1. Go to the "⚙️ Generate Password" tab
2. Adjust the password length slider (8-24 characters)
3. Customize character sets if needed
4. Click "🔁 Regenerate Password" for new options
5. Use "🔍 Check This Generated Password" to verify strength

## 🔧 Customization

### Modifying Character Sets
You can customize the default character sets in the password generator:

- **Uppercase**: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- **Lowercase**: `abcdefghijklmnopqrstuvwxyz`
- **Numbers**: `0123456789`
- **Special**: `{!?:;@#$%^&*<>.})`

### Updating Common Passwords Database
Replace or update `common_passwords.txt` with your preferred password list. Ensure one password per line for proper functionality.

### Ideas for Contributions
- Add password history tracking
- Implement password strength meter visualization
- Add more character set options
- Create password export functionality
- Add dark/light theme toggle

