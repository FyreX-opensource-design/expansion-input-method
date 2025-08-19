# EIM Text Expansion Types - Complete Guide

This document explains all the different types of text expansions in the EIM system and how they work.

## 📚 Overview

The EIM system includes several categories of text expansions, each designed for different use cases and following specific patterns for consistency and ease of use.

## 🎯 Text Abbreviation Expansions

### **Basic Pattern**
Text abbreviations follow a specific capitalization pattern using a prefix letter:

- **`a` prefix** = lowercase first word
- **`A` prefix** = capitalized first word

### **Examples**

| Abbreviation | Expansion | Pattern |
|--------------|-----------|---------|
| `aomg` | "oh my god" | `a` + lowercase |
| `Aomg` | "Oh my god" | `A` + capitalized |
| `abtw` | "by the way" | `a` + lowercase |
| `Abtw` | "By the way" | `A` + capitalized |
| `aidk` | "i don't know" | `a` + lowercase |
| `Aidk` | "I don't know" | `A` + capitalized |

### **How It Works**
1. **First character** (`a` or `A`) determines capitalization
2. **Remaining characters** form the abbreviation
3. **Expansion** follows the capitalization rule

### **Common Text Abbreviations**

#### **Casual/Informal**
- `aomg` → "oh my god"
- `alol` → "laugh out loud"
- `abrb` → "be right back"
- `attyl` → "talk to you later"
- `aty` → "thank you"

#### **Professional/Formal**
- `Aomg` → "Oh my god"
- `Alol` → "Laugh out loud"
- `Abrb` → "Be right back"
- `Attyl` → "Talk to you later"
- `Aty` → "Thank you"

#### **Information/Communication**
- `abtw` → "by the way"
- `afyi` → "for your information"
- `aasap` → "as soon as possible"
- `afaik` → "as far as i know"
- `aimho` → "in my humble opinion"

## ⚖️ Legal Phrase Expansions

### **Pattern**
Legal phrases use the `la` prefix (lowercase) and `LA` prefix (capitalized):

- **`la` prefix** = lowercase first word
- **`LA` prefix** = capitalized first word

### **Examples**

| Abbreviation | Expansion | Pattern |
|--------------|-----------|---------|
| `lainre` | "in reference to the matter of" | `la` + lowercase |
| `LAinre` | "In reference to the matter of" | `LA` + capitalized |
| `lahere` | "subject to the provisions hereof" | `la` + lowercase |
| `LAhere` | "Subject to the provisions hereof" | `LA` + capitalized |

### **Common Legal Phrases**

#### **Reference and Context**
- `lainre` → "in reference to the matter of"
- `lahere` → "subject to the provisions hereof"
- `lawith` → "without prejudice to the foregoing"
- `laprior` → "prior to the execution hereof"

#### **Terms and Conditions**
- `laterm` → "for the term set forth herein"
- `labreach` → "in the event of any breach thereof"
- `lalaw` → "pursuant to applicable law"
- `laagree` → "for and in consideration of the mutual covenants"

#### **Compliance and Regulations**
- `lareg` → "in accordance with applicable regulations"
- `lacomp` → "in compliance with all relevant requirements"
- `laconf` → "subject to confidentiality obligations"
- `laliab` → "shall not be liable for any damages arising from"

## 🔤 Word Completion Expansions

### **Overview**
Word completion expansions replace the old suffix system (`tn::tion`, `sn::sion`) with specific word completions that avoid conflicts.

### **Patterns**

#### **`n-` Prefix (Words ending in -ion)**
Removes common letters shared between words to create unique abbreviations:

| Abbreviation | Expansion | Pattern |
|--------------|-----------|---------|
| `nampla` | "amplification" | `n` + `ampl` + `a` |
| `nbeauta` | "beautification" | `n` + `beaut` + `a` |
| `ncerta` | "certification" | `n` + `cert` + `a` |
| `nclara` | "clarification" | `n` + `clar` + `a` |
| `nadmina` | "administration" | `n` + `admin` + `a` |
| `ncommu` | "communication" | `n` + `commu` |
| `nconca` | "concentration" | `n` + `conc` + `a` |
| `nconclu` | "conclusion" | `n` + `conclu` |

#### **`t-` Prefix (Words ending in -ive)**
Removes common letters for words ending in -ive:

| Abbreviation | Expansion | Pattern |
|--------------|-----------|---------|
| `tcomprehen` | "comprehensive" | `t` + `comprehen` |
| `tdefen` | "defensive" | `t` + `defen` |
| `texpen` | "expensive" | `t` + `expen` |
| `texten` | "extensive" | `t` + `exten` |

#### **Special Cases**
Some words have unique patterns:

| Abbreviation | Expansion | Notes |
|--------------|-----------|-------|
| `ncondi` | "condition" | Unique pattern, no common suffix |
| `tapprea` | "appreciation" | -ation suffix with `t` prefix |

## 🗺️ Geographic Expansions

### **US States and Territories**
Use `US` prefix followed by state abbreviation:

| Abbreviation | Expansion |
|--------------|-----------|
| `USca` | "California" |
| `UStx` | "Texas" |
| `USny` | "New York" |
| `USdc` | "District of Columbia" |

### **Canadian Provinces and Territories**
Use `CA` prefix followed by province abbreviation:

| Abbreviation | Expansion |
|--------------|-----------|
| `CAab` | "Alberta" |
| `CAbc` | "British Columbia" |
| `CAon` | "Ontario" |
| `CAqc` | "Quebec" |

### **Countries**
Use `cc` prefix followed by country code:

| Abbreviation | Expansion |
|--------------|-----------|
| `ccus` | "United States" |
| `ccca` | "Canada" |
| `ccuk` | "Northern Ireland" |
| `ccde` | "Germany" |

### **Indonesian Provinces**
Use `ID` prefix followed by province abbreviation:

| Abbreviation | Expansion |
|--------------|-----------|
| `IDsi` | "West Sulawesi" |
| `IDba` | "Bali" |
| `IDjk` | "Jakarta" |

## 🔧 How to Use

### **In AutoHotkey (Windows)**
All expansions are built into `EIM.ahk` and work automatically when you type the abbreviation.

### **In Linux Scripts**
1. Type the abbreviation in any text field
2. Run the appropriate script with the abbreviation as an argument
3. The script will replace the abbreviation with the full text

### **Examples**
```bash
# Expand text abbreviation
python3 EIM_autokey_dotool.py aomg

# Expand legal phrase
python3 EIM_autokey_dotool.py lainre

# Expand word completion
python3 EIM_autokey_dotool.py ncondi

# Expand geographic location
python3 EIM_autokey_dotool.py USca
```

## 📝 Adding Custom Expansions

### **To Python Data File**
Edit `EIM_expansions_data.py`:
```python
EXPANSIONS_DATA = {
    # Your custom expansions here
    "myabbr": "my custom expansion",
    "Myabbr": "My custom expansion",  # Capitalized version
    # ... existing expansions
}
```

### **To AutoHotkey File**
Add to `EIM.ahk`:
```autohotkey
:C:myabbr::my custom expansion
:C:Myabbr::My custom expansion
```

## 🎨 Design Principles

### **Consistency**
- **Prefix system** makes abbreviations predictable
- **Capitalization rules** are consistent across categories
- **Pattern-based** abbreviations are easier to remember

### **Conflict Avoidance**
- **Unique prefixes** prevent abbreviation conflicts
- **Removed common letters** in word completions
- **Geographic codes** use standard abbreviations

### **Usability**
- **Short abbreviations** for common phrases
- **Logical patterns** for related expansions
- **Professional quality** for business use

## 🔍 Troubleshooting

### **Common Issues**
- **Abbreviation not found** → Check spelling and case
- **Wrong capitalization** → Ensure correct prefix (`a` vs `A`)
- **Conflicts** → Use unique abbreviations for custom expansions

### **Best Practices**
1. **Follow the prefix system** for consistency
2. **add both lower and upper case phrases** (`aomg`) (`Aomg`)
4. **Test abbreviations** before adding to production
5. **Document custom expansions** for team members

---

*This system provides a comprehensive, consistent approach to text expansion that works across platforms and use cases.*

