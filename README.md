# Tkinter Password Manager
A secure and user-friendly password management application built with Python using Tkinter, offering robust password generation and storage capabilities.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![Security](https://img.shields.io/badge/Security-Password-red)
![Storage](https://img.shields.io/badge/Local-Storage-green)

## 🎯 Overview
This project creates a comprehensive password management system where users can:
1. Generate secure, randomized passwords
2. Store website credentials safely
3. Manage multiple platform logins
4. Auto-populate common fields
5. Save credentials locally

## 🔐 Application Features
### Interactive Elements
- Clean, intuitive user interface
- Automated password generation
- Credential storage system
- Input validation checks
- Auto-populated email field

### Data Management
- Secure password generation
- Local credential storage
- Data validation system
- Organized data formatting
- User confirmation dialogs

## 🔧 Technical Components
### Password Generation System
```python
def generate_password(self):
    password_letters = [random.choice(letters) for _ in range(self.nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(self.nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(self.nr_symbols)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
```

### Key Features
1. **Password Generation**
   - Mixed character types
   - Randomized selection
   - Customizable length
   - Character shuffling

2. **Data Validation**
   - Empty field checking
   - User confirmations
   - Input verification
   - Safe storage format

3. **Interface Management**
   - Responsive controls
   - Clear field labeling
   - Visual feedback
   - Intuitive layout

## 💻 Implementation Details
### Class Structure
- `Interface`: Main application window and UI components
- `PasswordGenerator`: Password creation and complexity management
- Data handling with file I/O operations

### Data Management
- Local file-based storage
- Organized credential format
- Secure data handling
- User data validation

## 🚀 Usage
1. Install required packages:
```bash
pip install tkinter
```

2. Launch the application:
```bash
python main.py
```

3. Input credentials:
   - Enter website name
   - Provide email/username
   - Generate or input password
   - Save your credentials

## 🎯 Application Rules
1. Fill in all required fields
2. Generate secure passwords when needed
3. Confirm credential storage
4. Access saved passwords in data.txt
5. Keep credentials file secure

## 🛠️ Project Structure
```
password-manager/
├── main.py              # Application initialization and UI
├── password_generator.py # Password generation logic
├── data.txt             # Credential storage
└── logo.png             # Application logo
```

## 📊 Features
### Input Processing
- Field validation
- Email auto-population
- Password generation
- Data formatting

### Storage Management
- Local file storage
- Organized data format
- Secure handling
- Easy access system

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Author
Burak TÜZEL
