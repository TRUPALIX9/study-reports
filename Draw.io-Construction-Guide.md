# Draw.io Construction Guide for L04 Threat Modeling Diagrams

## Overview
This guide provides step-by-step instructions for recreating the three required diagrams in draw.io using the Threat Modeling template. Each diagram is designed to meet the exact grading criteria for a 10/10 submission.

---

## Diagram 1: Data Flow Diagram (DFD)

### Step-by-Step Construction

#### 1. Open draw.io and Select Template
- Go to https://app.diagrams.net/
- Click "Create New Diagram"
- Search for "Threat Modeling" template
- Select "Threat Modeling" from the results

#### 2. Add External Entities
**Symbols to Use:** Rectangle with rounded corners (External Entity)
- **User Browser** (top-left)
- **Admin Dashboard** (top-right)

#### 3. Add Processes
**Symbols to Use:** Rectangle (Process)
- **Web Server** (center-left)
- **WordPress Core Application** (center-right)

#### 4. Add Data Store
**Symbols to Use:** Cylinder (Data Store)
- **MySQL Database** (far right)

#### 5. Add Trust Boundaries
**Symbols to Use:** Dashed rectangle (Trust Boundary)
- **Environment Boundary** (around Web Server)
- **Data Boundary** (around WordPress App and MySQL)

#### 6. Add Data Flows
**Symbols to Use:** Arrows with labels
- User Browser → Web Server: "HTTPS Request (GET/POST)"
- Admin Dashboard → Web Server: "HTTPS Request (Admin Access)"
- Web Server → WordPress App: "Internal HTTP/PHP (Processing)"
- WordPress App → MySQL: "SQL Query (SELECT/INSERT)"
- MySQL → WordPress App: "SQL Response (Data)"
- WordPress App → Web Server: "Internal Response (Rendered Content)"
- Web Server → User Browser: "HTTPS Response (Final Page)"
- Web Server → Admin Dashboard: "HTTPS Response (Dashboard)"

#### 7. Label Trust Boundaries
- Environment Boundary: "Environment Boundary: Internet to Web Server"
- Data Boundary: "Data Boundary: Application to Database"

#### 8. Apply Styling
- External Entities: Light blue background
- Processes: Light purple background
- Data Store: Light green background
- Trust Boundaries: Orange dashed border

---

## Diagram 2: Threat Tree Diagram (TTD)

### Step-by-Step Construction

#### 1. Start with Root Node
**Symbols to Use:** Rectangle (Root Threat)
- **Root:** "Compromise of WordPress Website Integrity and User Data"

#### 2. Add Level 1 - Vulnerabilities
**Symbols to Use:** Rectangle (Vulnerability)
- **Weak Authentication** (left branch)
- **SQL Injection** (center branch)
- **Cross-Site Scripting (XSS)** (right branch)

#### 3. Add Level 2 - Attack Methods
**Symbols to Use:** Rectangle (Attack Method)
- **Brute Force Attacks** (under Weak Authentication)
- **Plugin SQL Injection** (under SQL Injection)
- **Comment XSS Injection** (under XSS)

#### 4. Add Countermeasures
**Symbols to Use:** Rectangle (Countermeasure)
- **Multi-Factor Authentication** (connected to Weak Authentication)
- **Parameterized Queries** (connected to SQL Injection)
- **Input Sanitization** (connected to XSS)
- **Content Security Policy** (connected to XSS)

#### 5. Add Connections
- Root → Vulnerabilities (solid arrows)
- Vulnerabilities → Attack Methods (solid arrows)
- Countermeasures → Vulnerabilities (dashed arrows with "Mitigates" label)

#### 6. Apply Styling
- Root: Red background
- Vulnerabilities: Orange background
- Attack Methods: Purple background
- Countermeasures: Green background

---

## Diagram 3: Use & Misuse Diagram (UMD)

### Step-by-Step Construction

#### 1. Add Actors
**Symbols to Use:** Stick figure (Actor)
- **User** (left)
- **Admin** (center-left)
- **Malicious Attacker** (right)

#### 2. Add Use Cases
**Symbols to Use:** Oval (Use Case)
- **User Logs Into Account** (top-left)
- **Admin Publishes a Post** (top-center)
- **User Comments on a Post** (top-right)

#### 3. Add Misuse Cases
**Symbols to Use:** Oval (Misuse Case)
- **Credential Stuffing Attack** (bottom-left)
- **Malicious File Upload** (bottom-center)
- **Comment XSS Injection** (bottom-right)

#### 4. Add Mitigations
**Symbols to Use:** Rectangle (Mitigation)
- **Rate Limiting & MFA** (left)
- **File Type Validation** (center)
- **Input Sanitization** (right)

#### 5. Add Connections
- Actors → Use Cases (solid blue arrows)
- Attacker → Misuse Cases (solid red arrows)
- Misuse Cases → Use Cases (dashed red arrows with "THREATENS" label)
- Mitigations → Misuse Cases (solid green arrows with "MITIGATES" label)

#### 6. Add Legend Box
Create a legend with:
- Dashed Red Line → THREATENS
- Green Solid Line → MITIGATES
- Blue Solid Line → NORMAL FLOW

#### 7. Apply Styling
- Actors: Light blue background
- Use Cases: Light green background
- Misuse Cases: Light red background
- Mitigations: Light orange background

---

## Symbol Reference Guide

### Threat Modeling Symbols in draw.io
1. **External Entity:** Rectangle with rounded corners
2. **Process:** Rectangle
3. **Data Store:** Cylinder
4. **Trust Boundary:** Dashed rectangle
5. **Data Flow:** Arrow with label
6. **Actor:** Stick figure
7. **Use Case:** Oval
8. **Misuse Case:** Oval (different color)
9. **Mitigation:** Rectangle

### Color Coding Standards
- **External Entities:** Light blue (#e1f5fe)
- **Processes:** Light purple (#f3e5f5)
- **Data Stores:** Light green (#e8f5e8)
- **Trust Boundaries:** Orange dashed (#fff3e0)
- **Actors:** Light blue (#e3f2fd)
- **Use Cases:** Light green (#e8f5e8)
- **Misuse Cases:** Light red (#ffebee)
- **Mitigations:** Light orange (#fff3e0)

---

## Grading Criteria Checklist

### DFD Requirements ✅
- [x] At least 2 data flows (8 total)
- [x] At least 2 trust boundaries (Environment + Data)
- [x] Correct threat modeling symbols
- [x] All components labeled
- [x] OWASP-based analysis

### TTD Requirements ✅
- [x] At least 3 vulnerabilities
- [x] At least 3 countermeasures
- [x] Root threat clearly defined
- [x] Logical threat progression
- [x] OWASP Top 10 alignment

### UMD Requirements ✅
- [x] At least 3 use cases
- [x] At least 3 misuse cases
- [x] Explicit "threaten" connections
- [x] Explicit "mitigate" connections
- [x] Clear actor relationships

---

## Final Tips

1. **Use the Threat Modeling template** - This ensures you have the correct symbols
2. **Label everything clearly** - Each component needs a descriptive label
3. **Follow the color scheme** - Consistency helps with readability
4. **Add legends where needed** - Especially for UMD connections
5. **Export as PNG/SVG** - For best quality in submissions
6. **Save your work** - Draw.io auto-saves, but export copies

This guide ensures your diagrams will meet all grading criteria and look professional for your L04 submission.
