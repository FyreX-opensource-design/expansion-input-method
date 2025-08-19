#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AutoKey Script Generator for EIM Text Expansions

This script generates individual AutoKey scripts for each abbreviation.
Run this script to create all the individual AutoKey scripts you need.

Usage:
1. Run this script: python create_autokey_scripts.py
2. It will create a folder called "autokey_scripts" with individual scripts
3. Copy each script to AutoKey and set the appropriate abbreviation
"""

import os

# All your text expansions from EIM.ahk
EXPANSIONS = {
    # Text abbreviation expansions
    "aomg": "oh my god",
    "Aomg": "Oh my god",
    "abtw": "by the way",
    "Abtw": "By the way",
    "aidk": "i don't know",
    "Aidk": "I don't know",
    "aimho": "in my humble opinion",
    "Aimho": "In my humble opinion",
    "afyi": "for your information",
    "Afyi": "For your information",
    "aasap": "as soon as possible",
    "Aasap": "As soon as possible",
    "alol": "laugh out loud",
    "Alol": "Laugh out loud",
    "abrb": "be right back",
    "Abrb": "Be right back",
    "attyl": "talk to you later",
    "Attyl": "Talk to you later",
    "aty": "thank you",
    "Aty": "Thank you",
    "afaik": "as far as i know",
    "Afaik": "As far as I know",
    
    # Legal phrase expansions
    "lainre": "in reference to the matter of",
    "LAinre": "In reference to the matter of",
    "lahere": "subject to the provisions hereof",
    "LAhere": "Subject to the provisions hereof",
    "lawith": "without prejudice to the foregoing",
    "LAwith": "Without prejudice to the foregoing",
    "laprior": "prior to the execution hereof",
    "LAprior": "Prior to the execution hereof",
    "laterm": "for the term set forth herein",
    "LAterm": "For the term set forth herein",
    "labreach": "in the event of any breach thereof",
    "LAbreach": "In the event of any breach thereof",
    "lalaw": "pursuant to applicable law",
    "LAlaw": "Pursuant to applicable law",
    "laagree": "for and in consideration of the mutual covenants",
    "LAagree": "For and in consideration of the mutual covenants",
    "lareg": "in accordance with applicable regulations",
    "LAreg": "In accordance with applicable regulations",
    "lacomp": "in compliance with all relevant requirements",
    "LAcomp": "In compliance with all relevant requirements",
    "laconf": "subject to confidentiality obligations",
    "LAconf": "Subject to confidentiality obligations",
    "laliab": "shall not be liable for any damages arising from",
    "LAliab": "Shall not be liable for any damages arising from",
    "lawar": "represents and warrants that",
    "LAwar": "Represents and warrants that",
    "laind": "shall indemnify and hold harmless",
    "LAind": "Shall indemnify and hold harmless",
    "lasev": "if any provision is found to be invalid or unenforceable",
    "LAsev": "If any provision is found to be invalid or unenforceable",
    
    # Word expansions
    "1wdh": "downhill",
    "1Wdh": "Downhill",
    "1wuh": "uphill",
    "1Wuh": "Uphill",
    "1wnb": "northbound",
    "1Wnb": "Northbound",
    "1wsb": "southbound",
    "1Wsb": "Southbound",
    "1web": "eastbound",
    "1Web": "Eastbound",
    "1wwb": "westbound",
    "1Wwb": "Westbound",
    
    # US states and territories
    "USal": "Alabama", "USak": "Alaska", "USaz": "Arizona",
    "USar": "Arkansas", "USca": "California", "USco": "Colorado",
    "USct": "Connecticut", "USde": "Delaware", "USfl": "Florida",
    "USga": "Georgia", "UShi": "Hawaii", "USid": "Idaho",
    "USil": "Illinois", "USin": "Indiana", "USia": "Iowa",
    "USks": "Kansas", "USky": "Kentucky", "USla": "Louisiana",
    "USme": "Maine", "USmd": "Maryland", "USma": "Massachusetts",
    "USmi": "Michigan", "USmn": "Minnesota", "USms": "Mississippi",
    "USmo": "Missouri", "USmt": "Montana", "USne": "Nebraska",
    "USnv": "Nevada", "USnh": "New Hampshire", "USnj": "New Jersey",
    "USnm": "New Mexico", "USny": "New York", "USnc": "North Carolina",
    "USnd": "North Dakota", "USoh": "Ohio", "USok": "Oklahoma",
    "USor": "Oregon", "USpa": "Pennsylvania", "USri": "Rhode Island",
    "USsc": "South Carolina", "USsd": "South Dakota", "UStn": "Tennessee",
    "UStx": "Texas", "USut": "Utah", "USvt": "Vermont",
    "USva": "Virginia", "USwa": "Washington", "USwv": "West Virginia",
    "USwi": "Wisconsin", "USwy": "Wyoming", "USdc": "District of Columbia",
    "USas": "American Samoa", "USgu": "Guam", "USmp": "Northern Mariana Islands",
    "USpr": "Puerto Rico", "USvi": "U.S. Virgin Islands",
    
    # Canadian provinces and territories
    "CAab": "Alberta", "CAbc": "British Columbia", "CAmb": "Manitoba",
    "CAnb": "New Brunswick", "CAnl": "Newfoundland and Labrador",
    "CAns": "Nova Scotia", "CAnt": "Northwest Territories",
    "CAnu": "Nunavut", "CAon": "Ontario", "CApe": "Prince Edward Island",
    "CAqc": "Quebec", "CAsk": "Saskatchewan", "CAyt": "Yukon",
    
    # Australian states and territories
    "AUact": "Australian Capital Territory", "AUnt": "Northern Territory",
    "AUnsw": "New South Wales", "AUqld": "Queensland",
    "AUsa": "South Australia", "AUtas": "Tasmania",
    "AUvic": "Victoria", "AUwa": "Western Australia",
    
    # German federal states
    "DEbw": "Baden-Württemberg", "DEby": "Bavaria", "DEbe": "Berlin",
    "DEbb": "Brandenburg", "DEhb": "Bremen", "DEhh": "Hamburg",
    "DEhe": "Hesse", "DEMV": "Mecklenburg-Vorpommern", "DEni": "Lower Saxony",
    "DEnw": "North Rhine-Westphalia", "DErp": "Rhineland-Palatinate",
    "DEsl": "Saarland", "DEsn": "Saxony", "DEst": "Saxony-Anhalt",
    "DESH": "Schleswig-Holstein", "DEth": "Thuringia",
    
    # Country codes
    "ccaf": "Afghanistan", "ccal": "Albania", "ccdz": "Algeria",
    "ccad": "Andorra", "ccao": "Angola", "ccag": "Antigua and Barbuda",
    "ccar": "Argentina", "ccam": "Armenia", "ccau": "Australia",
    "ccat": "Austria", "ccaz": "Azerbaijan", "ccbs": "Bahamas",
    "ccbh": "Bahrain", "ccbd": "Bangladesh", "ccbb": "Barbados",
    "ccby": "Belarus", "ccbe": "Belgium", "ccbz": "Belize",
    "ccbj": "Benin", "ccbt": "Bhutan", "ccbo": "Bolivia",
    "ccba": "Bosnia and Herzegovina", "ccbw": "Botswana", "ccbr": "Brazil",
    "ccbn": "Brunei", "ccbg": "Bulgaria", "ccbf": "Burkina Faso",
    "ccbi": "Burundi", "cckh": "Cambodia", "cccm": "Cameroon",
    "ccca": "Canada", "cccv": "Cape Verde", "cccf": "Central African Republic",
    "cctd": "Chad", "cccl": "Chile", "cccn": "China",
    "ccco": "Colombia", "cckm": "Comoros", "cccg": "Congo",
    "cccr": "Costa Rica", "cchr": "Croatia", "cccu": "Cuba",
    "cccy": "Cyprus", "cccz": "Czech Republic", "cccd": "Democratic Republic of the Congo",
    "ccdk": "Denmark", "ccdj": "Djibouti", "ccdm": "Dominica",
    "ccdo": "Dominican Republic", "ccec": "Ecuador", "cceg": "Egypt",
    "ccsv": "El Salvador", "ccgq": "Equatorial Guinea", "ccer": "Eritrea",
    "ccee": "Estonia", "ccet": "Ethiopia", "ccfj": "Fiji",
    "ccfi": "Finland", "ccfr": "France", "ccga": "Gabon",
    "ccgm": "Gambia", "ccge": "Georgia", "ccde": "Germany",
    "ccgh": "Ghana", "ccgr": "Greece", "ccgd": "Grenada",
    "ccgt": "Guatemala", "ccgn": "Guinea", "ccgw": "Guinea-Bissau",
    "ccgy": "Guyana", "ccht": "Haiti", "cchn": "Honduras",
    "cchu": "Hungary", "ccis": "Iceland", "ccin": "India",
    "ccid": "Indonesia", "ccir": "Iran", "cciq": "Iraq",
    "ccie": "Ireland", "ccil": "Israel", "ccit": "Italy",
    "cciv": "Ivory Coast", "ccjm": "Jamaica", "ccjp": "Japan",
    "ccjo": "Jordan", "cckz": "Kazakhstan", "ccke": "Kenya",
    "ccki": "Kiribati", "ccxk": "Kosovo", "cckw": "Kuwait",
    "cckg": "Kyrgyzstan", "ccla": "Laos", "cclv": "Latvia",
    "cclb": "Lebanon", "ccls": "Lesotho", "cclr": "Liberia",
    "ccly": "Libya", "ccli": "Liechtenstein", "cclt": "Lithuania",
    "cclu": "Luxembourg", "ccmk": "Macedonia", "ccmg": "Madagascar",
    "ccmw": "Malawi", "ccmy": "Malaysia", "ccmv": "Maldives",
    "ccml": "Mali", "ccmt": "Malta", "ccmh": "Marshall Islands",
    "ccmr": "Mauritania", "ccmu": "Mauritius", "ccmx": "Mexico",
    "ccfm": "Micronesia", "ccmd": "Moldova", "ccmc": "Monaco",
    "ccmn": "Mongolia", "ccme": "Montenegro", "ccma": "Morocco",
    "ccmz": "Mozambique", "ccmm": "Myanmar", "ccna": "Namibia",
    "ccnr": "Nauru", "ccnp": "Nepal", "ccnl": "Netherlands",
    "ccnz": "New Zealand", "ccni": "Nicaragua", "ccne": "Niger",
    "ccng": "Nigeria", "cckp": "North Korea", "ccno": "Norway",
    "ccom": "Oman", "ccpk": "Pakistan", "ccpw": "Palau",
    "ccps": "Palestine", "ccpa": "Panama", "ccpg": "Papua New Guinea",
    "ccpy": "Paraguay", "ccpe": "Peru", "ccph": "Philippines",
    "ccpl": "Poland", "ccpt": "Portugal", "ccqa": "Qatar",
    "ccro": "Romania", "ccru": "Russia", "ccrw": "Rwanda",
    "cckn": "Saint Kitts and Nevis", "cclc": "Saint Lucia",
    "ccvc": "Saint Vincent and the Grenadines", "ccws": "Samoa",
    "ccsm": "San Marino", "ccst": "Sao Tome and Principe", "ccsa": "Saudi Arabia",
    "ccsn": "Senegal", "ccrs": "Serbia", "ccsc": "Seychelles",
    "ccsl": "Sierra Leone", "ccsg": "Singapore", "ccsk": "Slovakia",
    "ccsi": "Slovenia", "ccsb": "Solomon Islands", "ccso": "Somalia",
    "ccza": "South Africa", "cckr": "South Korea", "ccss": "South Sudan",
    "cces": "Spain", "cclk": "Sri Lanka", "ccsd": "Sudan",
    "ccsr": "Suriname", "ccsz": "Eswatini", "ccse": "Sweden",
    "ccch": "Switzerland", "ccsy": "Syria", "cctw": "Taiwan",
    "cctj": "Tajikistan", "cctz": "Tanzania", "ccth": "Thailand",
    "cctl": "Timor-Leste", "cctg": "Togo", "ccto": "Tonga",
    "cctt": "Trinidad and Tobago", "cctn": "Tunisia", "cctr": "Turkey",
    "cctm": "Turkmenistan", "cctv": "Tuvalu", "ccug": "Uganda",
    "ccua": "Ukraine", "ccae": "United Arab Emirates", "ccgb": "England",
    "ccwl": "Wales", "ccscot": "Scotland", "ccuk": "Northern Ireland",
    "ccus": "United States", "ccuy": "Uruguay", "ccuz": "Uzbekistan",
    "ccvu": "Vanuatu", "ccva": "Vatican City", "ccve": "Venezuela",
    "ccvn": "Vietnam", "ccye": "Yemen", "cczm": "Zambia",
    "cczw": "Zimbabwe",
    
    # Nationalities
    "pccaf": "Afghan", "pccal": "Albanian", "pccdz": "Algerian",
    "pccad": "Andorran", "pccao": "Angolan", "pccag": "Antiguan",
    "pccar": "Argentine", "pccam": "Armenian", "pccau": "Australian",
    "pccat": "Austrian", "pccaz": "Azerbaijani", "pccbs": "Bahamian",
    "pccbh": "Bahraini", "pccbd": "Bangladeshi", "pccbb": "Barbadian",
    "pccby": "Belarusian", "pccbe": "Belgian", "pccbz": "Belizean",
    "pccbj": "Beninese", "pccbt": "Bhutanese", "pccbo": "Bolivian",
    "pccba": "Bosnian", "pccbw": "Botswanan", "pccbr": "Brazilian",
    "pccbn": "Bruneian", "pccbg": "Bulgarian", "pccbf": "Burkinabe",
    "pccbi": "Burundian", "pcckh": "Cambodian", "pcccm": "Cameroonian",
    "pccca": "Canadian", "pcccv": "Cape Verdean", "pcccf": "Central African",
    "pcctd": "Chadian", "pcccl": "Chilean", "pcccn": "Chinese",
    "pccco": "Colombian", "pcckm": "Comorian", "pcccg": "Congolese",
    "pcccd": "Congolese", "pcccr": "Costa Rican", "pcchr": "Croatian",
    "pcccu": "Cuban", "pcccy": "Cypriot", "pcccz": "Czech",
    "pccdk": "Danish", "pccdj": "Djiboutian", "pccdm": "Dominican",
    "pccdo": "Dominican", "pccec": "Ecuadorian", "pcceg": "Egyptian",
    "pccsv": "Salvadoran", "pccgq": "Equatorial Guinean", "pccer": "Eritrean",
    "pccee": "Estonian", "pccet": "Ethiopian", "pccfj": "Fijian",
    "pccfi": "Finnish", "pccfr": "French", "pccga": "Gabonese",
    "pccgm": "Gambian", "pccge": "Georgian", "pccde": "German",
    "pccgh": "Ghanaian", "pccgr": "Greek", "pccgd": "Grenadian",
    "pccgt": "Guatemalan", "pccgn": "Guinean", "pccgw": "Guinea-Bissauan",
    "pccgy": "Guyanese", "pccht": "Haitian", "pcchn": "Honduran",
    "pcchu": "Hungarian", "pccis": "Icelandic", "pccin": "Indian",
    "pccid": "Indonesian", "pccir": "Iranian", "pcciq": "Iraqi",
    "pccie": "Irish", "pccil": "Israeli", "pccit": "Italian",
    "pcciv": "Ivorian", "pccjm": "Jamaican", "pccjp": "Japanese",
    "pccjo": "Jordanian", "pcckz": "Kazakhstani", "pccke": "Kenyan",
    "pccki": "I-Kiribati", "pccxk": "Kosovar", "pcckw": "Kuwaiti",
    "pcckg": "Kyrgyzstani", "pccla": "Laotian", "pcclv": "Latvian",
    "pcclb": "Lebanese", "pccls": "Lesothan", "pcclr": "Liberian",
    "pccly": "Libyan", "pccli": "Liechtensteiner", "pcclt": "Lithuanian",
    "pcclu": "Luxembourger", "pccmk": "Macedonian", "pccmg": "Malagasy",
    "pccmw": "Malawian", "pccmy": "Malaysian", "pccmv": "Maldivian",
    "pccml": "Malian", "pccmt": "Maltese", "pccmh": "Marshallese",
    "pccmr": "Mauritanian", "pccmu": "Mauritian", "pccmx": "Mexican",
    "pccfm": "Micronesian", "pccmd": "Moldovan", "pccmc": "Monacan",
    "pccmn": "Mongolian", "pccme": "Montenegro", "pccma": "Moroccan",
    "pccmz": "Mozambican", "pccmm": "Myanmar", "pccna": "Namibian",
    "pccnr": "Nauruan", "pccnp": "Nepalese", "pccnl": "Dutch",
    "pccnz": "New Zealander", "pccni": "Nicaraguan", "pccne": "Nigerien",
    "pccng": "Nigerian", "pcckp": "North Korean", "pccno": "Norwegian",
    "pccom": "Omani", "pccpk": "Pakistani", "pccpw": "Palauan",
    "pccps": "Palestinian", "pccpa": "Panamanian", "pccpg": "Papua New Guinean",
    "pccpy": "Paraguayan", "pccpe": "Peruvian", "pccph": "Filipino",
    "pccpl": "Polish", "pccpt": "Portuguese", "pccqa": "Qatari",
    "pccro": "Romanian", "pccru": "Russian", "pccrw": "Rwandan",
    "pcckn": "Kittitian", "pcclc": "Saint Lucian", "pccvc": "Vincentian",
    "pccws": "Samoan", "pccsm": "Sammarinese", "pccst": "Sao Tomean",
    "pccsa": "Saudi Arabian", "pccsn": "Senegalese", "pccrs": "Serbian",
    "pccsc": "Seychellois", "pccsl": "Sierra Leonean", "pccsg": "Singaporean",
    "pccsk": "Slovak", "pccsi": "Slovenian", "pccsb": "Solomon Islander",
    "pccso": "Somali", "pccza": "South African", "pcckr": "South Korean",
    "pccss": "South Sudanese", "pcces": "Spanish", "pcclk": "Sri Lankan",
    "pccsd": "Sudanese", "pccsr": "Surinamese", "pccsz": "Swazi",
    "pccse": "Swedish", "pccch": "Swiss", "pccsy": "Syrian",
    "pcctw": "Taiwanese", "pcctj": "Tajik", "pcctz": "Tanzanian",
    "pccth": "Thai", "pcctl": "Timorese", "pcctg": "Togolese",
    "pccto": "Tongan", "pcctt": "Trinidadian", "pcctn": "Tunisian",
    "pcctr": "Turkish", "pcctm": "Turkmen", "pcctv": "Tuvaluan",
    "pccug": "Ugandan", "pccua": "Ukrainian", "pccae": "Emirati",
    "pccgb": "English", "pccwh": "Welsh", "pccscot": "Scotland",
    "pccuk": "Northern Irish", "pccus": "United States", "pccuy": "Uruguayan",
    "pccuz": "Uzbek", "pccvu": "Vanuatuan", "pccva": "Vatican",
    "pccve": "Venezuelan", "pccvn": "Vietnamese", "pccye": "Yemeni",
    "pcczm": "Zambian", "pcczw": "Zimbabwean",
}

def create_script_content(abbreviation, expansion):
    """Create the content for an individual AutoKey script"""
    return f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AutoKey Script for: {abbreviation} → {expansion}

This script expands '{abbreviation}' to '{expansion}'
"""

# Delete the abbreviation that was typed
keyboard.send_keys("<ctrl>+a")  # Select all text
keyboard.send_keys("<delete>")  # Delete the selection

# Type the expanded text
keyboard.send_text("{expansion}")
'''

def main():
    """Generate all individual AutoKey scripts"""
    
    # Create output directory
    output_dir = "autokey_scripts"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate scripts for each abbreviation
    for abbreviation, expansion in EXPANSIONS.items():
        # Create filename (replace special characters)
        filename = f"{abbreviation.replace(':', '_').replace('<', '_').replace('>', '_')}.py"
        filepath = os.path.join(output_dir, filename)
        
        # Write script content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(create_script_content(abbreviation, expansion))
        
        print(f"Created: {filename}")
    
    print(f"\nGenerated {len(EXPANSIONS)} AutoKey scripts in '{output_dir}' folder")
    print("\nTo use these scripts:")
    print("1. Open AutoKey")
    print("2. Create a new Script (not Phrase)")
    print("3. Set the abbreviation to the text you want to expand")
    print("4. Copy and paste the content from the corresponding .py file")
    print("5. Save and enable the script")
    print("\nExample: For 'aomg' abbreviation, use the content from 'aomg.py'")

if __name__ == "__main__":
    main()
