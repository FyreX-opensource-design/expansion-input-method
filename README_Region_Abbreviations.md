# Region Abbreviation System Documentation

This document outlines the region abbreviation system used in the EIM text expansion scripts and documents the conflicts that were resolved.

## Overview

The EIM (Enhanced Input Method) system uses standardized abbreviations for geographic regions, administrative divisions, and provinces worldwide. Each region has a unique abbreviation to avoid conflicts and ensure proper text expansion.

## Abbreviation Format

- **Country Code**: 2-letter ISO country code (e.g., `US`, `CA`, `VN`, `PH`)
- **Region Code**: 2-3 letter abbreviation for the specific region
- **Format**: `[Country][Region]` (e.g., `USca` for California, `VNha` for Hà Giang)

## Resolved Conflicts

### Vietnamese Provinces (VN)

**Original Conflicts:**
- `VNha` was used for 7 provinces: Hà Giang, Hà Nam, Hà Nội, Hà Tĩnh, Hải Dương, Hải Phòng, Hậu Giang
- `VNho` was used for 2 provinces: Hòa Bình, Hưng Yên
- `VNkg` was used for 2 provinces: Kiên Giang, Kon Tum
- `VNla` was used for 5 provinces: Lai Châu, Lâm Đồng, Lạng Sơn, Lào Cai, Long An
- `VNna` was used for 4 provinces: Nam Định, Nghệ An, Ninh Bình, Ninh Thuận
- `VNph` was used for 2 provinces: Phú Thọ, Phú Yên
- `VNso` was used for 2 provinces: Sóc Trăng, Sơn La
- `VNth` was used for 3 provinces: Thái Nguyên, Thanh Hóa, Thừa Thiên-Huế
- `VNtv` was used for 3 provinces: Trà Vinh, Vĩnh Long, Vĩnh Phúc

**Resolution:**
- `VNha` → Hà Giang (kept original)
- `VNhn` → Hà Nam
- `VNhnh` → Hà Nội
- `VNht` → Hà Tĩnh
- `VNhd` → Hải Dương
- `VNhp` → Hải Phòng
- `VNHg` → Hậu Giang
- `VNho` → Hòa Bình (kept original)
- `VNhy` → Hưng Yên
- `VNkg` → Kiên Giang (kept original)
- `VNkt` → Kon Tum
- `VNla` → Lai Châu (kept original)
- `VNld` → Lâm Đồng
- `VNls` → Lạng Sơn
- `VNlc` → Lào Cai
- `VNln` → Long An
- `VNna` → Nam Định (kept original)
- `VNng` → Nghệ An
- `VNnb` → Ninh Bình
- `VNnt` → Ninh Thuận
- `VNph` → Phú Thọ (kept original)
- `VNpy` → Phú Yên
- `VNso` → Sóc Trăng (kept original)
- `VNsl` → Sơn La
- `VNth` → Thái Nguyên (kept original)
- `VNTn` → Thanh Hóa
- `VNtt` → Thừa Thiên-Huế
- `VNtv` → Trà Vinh (kept original)
- `VNvl` → Vĩnh Long
- `VNvp` → Vĩnh Phúc

### Philippine Provinces (PH)

**Original Conflicts:**
- `PHag` was used for 2 provinces: Agusan del Norte, Agusan del Sur
- `PHba` was used for 4 provinces: Basilan, Bataan, Batanes, Batangas
- `PHbu` was used for 2 provinces: Bukidnon, Bulacan
- `PHca` was used for 8 provinces: Cagayan, Cagayan de Oro, Camarines Norte, Camarines Sur, Camiguin, Capiz, Catanduanes, Cavite
- `PHda` was used for 4 provinces: Davao del Norte, Davao del Sur, Davao Occidental, Davao Oriental
- `PHla` was used for 4 provinces: La Union, Laguna, Lanao del Norte, Lanao del Sur
- `PHma` was used for 3 provinces: Maguindanao, Marinduque, Masbate
- `PHmi` was used for 4 provinces: Mindoro Occidental, Mindoro Oriental, Misamis Occidental, Misamis Oriental
- `PHna` was used for 2 provinces: Negros Occidental, Negros Oriental
- `PHnu` was used for 2 provinces: Nueva Ecija, Nueva Vizcaya
- `PHpa` was used for 3 provinces: Palawan, Pampanga, Pangasinan
- `PHqu` was used for 2 provinces: Quezon, Quirino
- `PHsa` was used for 2 provinces: Samar, Sarangani
- `PHso` was used for 3 provinces: Sorsogon, South Cotabato, Southern Leyte
- `PHsu` was used for 4 provinces: Sultan Kudarat, Sulu, Surigao del Norte, Surigao del Sur
- `PHta` was used for 2 provinces: Tarlac, Tawi-Tawi
- `PHza` was used for 4 provinces: Zambales, Zamboanga del Norte, Zamboanga del Sur, Zamboanga Sibugay

**Resolution:**
- `PHag` → Agusan del Norte (kept original)
- `PHas` → Agusan del Sur
- `PHba` → Basilan (kept original)
- `PHbt` → Bataan
- `PHbs` → Batanes
- `PHbg` → Batangas
- `PHbu` → Bukidnon (kept original)
- `PHbl` → Bulacan
- `PHca` → Cagayan (kept original)
- `PHcd` → Cagayan de Oro
- `PHcn` → Camarines Norte
- `PHcs` → Camarines Sur
- `PHcg` → Camiguin
- `PHcp` → Capiz
- `PHct` → Catanduanes
- `PHcv` → Cavite
- `PHda` → Davao del Norte (kept original)
- `PHds` → Davao del Sur
- `PHdo` → Davao Occidental
- `PHdr` → Davao Oriental
- `PHla` → La Union (kept original)
- `PHlg` → Laguna
- `PHln` → Lanao del Norte
- `PHls` → Lanao del Sur
- `PHma` → Maguindanao (kept original)
- `PHmq` → Marinduque
- `PHms` → Masbate
- `PHmi` → Mindoro Occidental (kept original)
- `PHmo` → Mindoro Oriental
- `PHmc` → Misamis Occidental
- `PHme` → Misamis Oriental
- `PHna` → Negros Occidental (kept original)
- `PHne` → Negros Oriental
- `PHnu` → Nueva Ecija (kept original)
- `PHnv` → Nueva Vizcaya
- `PHpa` → Palawan (kept original)
- `PHpm` → Pampanga
- `PHpg` → Pangasinan
- `PHqu` → Quezon (kept original)
- `PHqi` → Quirino
- `PHsa` → Samar (kept original)
- `PHsg` → Sarangani
- `PHso` → Sorsogon (kept original)
- `PHsc` → South Cotabato
- `PHsl` → Southern Leyte
- `PHsu` → Sultan Kudarat (kept original)
- `PHsn` → Surigao del Norte
- `PHss` → Surigao del Sur
- `PHta` → Tarlac (kept original)
- `PHtw` → Tawi-Tawi
- `PHza` → Zambales (kept original)
- `PHzn` → Zamboanga del Norte
- `PHzs` → Zamboanga del Sur
- `PHzb` → Zamboanga Sibugay

### Thai Provinces (TH)

**Original Conflicts:**
- `THch` was used for 6 provinces: Chachoengsao, Chai Nat, Chaiyaphum, Chanthaburi, Chiang Mai, Chiang Rai, Chonburi, Chumphon
- `THka` was used for 4 provinces: Kalasin, Kamphaeng Phet, Kanchanaburi, Khon Kaen
- `THla` was used for 3 provinces: Lamphun, Lampang, Loei
- `THma` was used for 3 provinces: Mae Hong Son, Maha Sarakham, Mukdahan
- `THna` was used for 8 provinces: Nakhon Nayok, Nakhon Pathom, Nakhon Phanom, Nakhon Ratchasima, Nakhon Sawan, Nakhon Si Thammarat, Nan, Narathiwat
- `THno` was used for 3 provinces: Nong Bua Lamphu, Nong Khai, Nonthaburi
- `THpa` was used for 2 provinces: Pathum Thani, Pattani
- `THph` was used for 11 provinces: Phatthalung, Phayao, Phetchabun, Phetchaburi, Phichit, Phitsanulok, Phra Nakhon Si Ayutthaya, Phrae, Phuket, Prachinburi, Prachuap Khiri Khan
- `THra` was used for 3 provinces: Ranong, Ratchaburi, Rayong
- `THsa` was used for 7 provinces: Sa Kaeo, Sakon Nakhon, Samut Prakan, Samut Sakhon, Samut Songkhram, Saraburi, Satun
- `THsi` was used for 2 provinces: Si Sa Ket, Sing Buri
- `THsu` was used for 5 provinces: Sukhothai, Suphan Buri, Surat Thani, Surin, Tak
- `THtr` was used for 2 provinces: Trang, Trat
- `THub` was used for 2 provinces: Ubon Ratchathani, Udon Thani
- `THut` was used for 2 provinces: Uthai Thani, Uttaradit
- `THya` was used for 2 provinces: Yala, Yasothon

**Resolution:**
- `THch` → Chachoengsao (kept original)
- `THcn` → Chai Nat
- `THcy` → Chaiyaphum
- `THcb` → Chanthaburi
- `THcm` → Chiang Mai
- `THcr` → Chiang Rai
- `THco` → Chonburi
- `THcp` → Chumphon
- `THka` → Kalasin (kept original)
- `THkp` → Kamphaeng Phet
- `THkc` → Kanchanaburi
- `THkk` → Khon Kaen
- `THla` → Lamphun (kept original)
- `THlg` → Lampang
- `THle` → Loei
- `THma` → Mae Hong Son (kept original)
- `THms` → Maha Sarakham
- `THmk` → Mukdahan
- `THna` → Nakhon Nayok (kept original)
- `THnp` → Nakhon Pathom
- `THnph` → Nakhon Phanom
- `THnr` → Nakhon Ratchasima
- `THns` → Nakhon Sawan
- `THnst` → Nakhon Si Thammarat
- `THnn` → Nan
- `THnw` → Narathiwat
- `THno` → Nong Bua Lamphu (kept original)
- `THnk` → Nong Khai
- `THnt` → Nonthaburi
- `THpa` → Pathum Thani (kept original)
- `THpt` → Pattani
- `THph` → Phatthalung (kept original)
- `THpy` → Phayao
- `THpc` → Phetchabun
- `THpb` → Phetchaburi
- `THpi` → Phichit
- `THpl` → Phitsanulok
- `THpaa` → Phra Nakhon Si Ayutthaya
- `THpr` → Phrae
- `THpk` → Phuket
- `THpch` → Prachinburi
- `THpkk` → Prachuap Khiri Khan
- `THra` → Ranong (kept original)
- `THrb` → Ratchaburi
- `THry` → Rayong
- `THsa` → Sa Kaeo (kept original)
- `THsk` → Sakon Nakhon
- `THsp` → Samut Prakan
- `THss` → Samut Sakhon
- `THssg` → Samut Songkhram
- `THsb` → Saraburi
- `THst` → Satun
- `THsi` → Si Sa Ket (kept original)
- `THsg` → Sing Buri
- `THsu` → Sukhothai (kept original)
- `THsb` → Suphan Buri
- `THstn` → Surat Thani
- `THsr` → Surin
- `THtk` → Tak
- `THtr` → Trang (kept original)
- `THtt` → Trat
- `THub` → Ubon Ratchathani (kept original)
- `THud` → Udon Thani
- `THut` → Uthai Thani (kept original)
- `THudt` → Uttaradit
- `THya` → Yala (kept original)
- `THys` → Yasothon

### Turkish Provinces (TR)

**Original Conflicts:**
- `TRad` was used for 2 provinces: Adana, Adıyaman
- `TRan` was used for 2 provinces: Ankara, Antalya
- `TRar` was used for 2 provinces: Ardahan, Artvin
- `TRba` was used for 4 provinces: Balıkesir, Bartın, Batman, Bayburt
- `TRbi` was used for 3 provinces: Bilecik, Bingöl, Bitlis
- `TRbu` was used for 2 provinces: Burdur, Bursa
- `TRca` was used for 3 provinces: Çanakkale, Çankırı, Çorum
- `TRea` was used for 5 provinces: Edirne, Elazığ, Erzincan, Erzurum, Eskişehir
- `TRha` was used for 2 provinces: Hakkari, Hatay
- `TRis` was used for 2 provinces: Isparta, Istanbul
- `TRka` was used for 6 provinces: Kahramanmaraş, Karabük, Karaman, Kars, Kastamonu, Kayseri
- `TRki` was used for 4 provinces: Kırıkkale, Kırklareli, Kırşehir, Kilis
- `TRko` was used for 2 provinces: Kocaeli, Konya
- `TRma` was used for 3 provinces: Malatya, Manisa, Mardin
- `TRmu` was used for 2 provinces: Muğla, Muş
- `TRsa` was used for 3 provinces: Sakarya, Samsun, Şanlıurfa
- `TRsi` was used for 4 provinces: Siirt, Sinop, Şırnak, Sivas

**Resolution:**
- `TRad` → Adana (kept original)
- `TRadı` → Adıyaman
- `TRan` → Ankara (kept original)
- `TRant` → Antalya
- `TRar` → Ardahan (kept original)
- `TRart` → Artvin
- `TRba` → Balıkesir (kept original)
- `TRbt` → Bartın
- `TRbm` → Batman
- `TRby` → Bayburt
- `TRbi` → Bilecik (kept original)
- `TRbg` → Bingöl
- `TRbl` → Bitlis
- `TRbu` → Burdur (kept original)
- `TRbs` → Bursa
- `TRca` → Çanakkale (kept original)
- `TRck` → Çankırı
- `TRcr` → Çorum
- `TRea` → Edirne (kept original)
- `TRez` → Elazığ
- `TRer` → Erzincan
- `TReu` → Erzurum
- `TRes` → Eskişehir
- `TRha` → Hakkari (kept original)
- `TRht` → Hatay
- `TRis` → Isparta (kept original)
- `TRst` → Istanbul
- `TRka` → Kahramanmaraş (kept original)
- `TRkb` → Karabük
- `TRkm` → Karaman
- `TRks` → Kars
- `TRkt` → Kastamonu
- `TRky` → Kayseri
- `TRki` → Kırıkkale (kept original)
- `TRkl` → Kırklareli
- `TRkr` → Kırşehir
- `TRkls` → Kilis
- `TRko` → Kocaeli (kept original)
- `TRkn` → Konya
- `TRma` → Malatya (kept original)
- `TRmn` → Manisa
- `TRmd` → Mardin
- `TRmu` → Muğla (kept original)
- `TRmş` → Muş
- `TRsa` → Sakarya (kept original)
- `TRsm` → Samsun
- `TRsu` → Şanlıurfa
- `TRsi` → Siirt (kept original)
- `TRsp` → Sinop
- `TRşr` → Şırnak
- `TRsv` → Sivas

### Iranian Provinces (IR)

**Original Conflicts:**
- `IRaz` was used for 2 provinces: East Azerbaijan, West Azerbaijan
- `IRka` was used for 2 provinces: Kerman, Kermanshah
- `IRkh` was used for 4 provinces: Khorasan, North Khorasan, Razavi Khorasan, South Khorasan
- `IRma` was used for 2 provinces: Markazi, Mazandaran
- `IRqa` was used for 2 provinces: Qazvin, Qom

**Resolution:**
- `IRaz` → East Azerbaijan (kept original)
- `IRwz` → West Azerbaijan
- `IRka` → Kerman (kept original)
- `IRks` → Kermanshah
- `IRkh` → Khorasan (kept original)
- `IRnk` → North Khorasan
- `IRrk` → Razavi Khorasan
- `IRsk` → South Khorasan
- `IRma` → Markazi (kept original)
- `IRmz` → Mazandaran
- `IRqa` → Qazvin (kept original)
- `IRqm` → Qom

### Other Regional Conflicts

**Norwegian Counties (NO):**
- `NOtr` was used for 2 counties: Troms og Finnmark, Trøndelag
- **Resolution**: `NOtr` → Troms og Finnmark, `NOtd` → Trøndelag

**Finnish Regions (FI):**
- `FIno` was used for 3 regions: North Karelia, Northern Ostrobothnia, Northern Savonia
- `FIps` was used for 2 regions: Pohjois-Savo, Päijät-Häme
- `FIsm` was used for 4 regions: Satakunta, Southern Karelia, Southern Ostrobothnia, Southern Savonia
- **Resolution**: 
  - `FIno` → North Karelia, `FInb` → Northern Ostrobothnia, `FIns` → Northern Savonia
  - `FIps` → Pohjois-Savo, `FIph` → Päijät-Häme
  - `FIsm` → Satakunta, `FIsk` → Southern Karelia, `FIsb` → Southern Ostrobothnia, `FIss` → Southern Savonia

**Czech Regions (CZ):**
- `CZst` was duplicated: Central Bohemian appeared twice
- **Resolution**: Removed duplicate `CZst` entry

**Bulgarian Provinces (BG):**
- `BGsl` was used for 2 provinces: Silistra, Sliven
- **Resolution**: `BGsl` → Silistra, `BGsv` → Sliven

## Abbreviation Rules

1. **Keep Original**: When possible, keep the most prominent or populous region with the original abbreviation
2. **Add Suffix**: Add descriptive suffixes to differentiate similar regions
3. **Use Geographic Hints**: Use letters that hint at the region's location or characteristics
4. **Avoid Confusion**: Ensure abbreviations don't form actual words or common acronyms
5. **Consistency**: Maintain consistent patterns within each country's system

## Usage Examples

```autohotkey
; Vietnamese provinces
:C:VNha::Hà Giang
:C:VNhn::Hà Nam
:C:VNhnh::Hà Nội

; Philippine provinces
:C:PHag::Agusan del Norte
:C:PHas::Agusan del Sur
:C:PHba::Basilan
:C:PHbt::Bataan

; Thai provinces
:C:THch::Chachoengsao
:C:THcn::Chai Nat
:C:THcy::Chaiyaphum
```

## Maintenance

When adding new regions or provinces:
1. Check for existing abbreviation conflicts
2. Follow the established naming conventions
3. Update this documentation
4. Test the abbreviations to ensure they work correctly

## Notes

- All abbreviations are case-sensitive
- Some abbreviations may be longer than ideal but are necessary to avoid conflicts
- The system prioritizes clarity and uniqueness over brevity
- Regular review and cleanup of conflicts is recommended
