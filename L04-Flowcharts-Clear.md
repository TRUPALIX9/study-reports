# L04 Flowcharts - Clear Text Version

## Diagram 1: Data Flow Diagram (DFD)

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ 🌐 User Browser │    │ 👑 Admin Panel  │    │                 │
│ (Chrome/Firefox)│    │ (WP Admin Panel)│    │                 │
│ External Entity │    │ External Entity │    │                 │
└─────────┬───────┘    └─────────┬───────┘    │                 │
          │                      │              │                 │
          │ HTTPS Request        │ HTTPS Request │                 │
          │ (GET/POST)           │ (Admin Access)│                 │
          │                      │              │                 │
          ▼                      ▼              │                 │
┌─────────────────────────────────────────────────┐              │
│           🌐 ENVIRONMENT BOUNDARY              │              │
│                                                 │              │
│  ┌─────────────────────────────────────────┐   │              │
│  │            Web Server                   │   │              │
│  │              (Process)                  │   │              │
│  └─────────────────┬───────────────────────┘   │              │
│                    │                            │              │
│                    │ Internal HTTP/PHP          │              │
│                    │ (Processing)               │              │
│                    ▼                            │              │
│  ┌─────────────────────────────────────────┐   │              │
│  │      WordPress Core Application        │   │              │
│  │              (Process)                  │   │              │
│  └─────────────────┬───────────────────────┘   │              │
└────────────────────┼───────────────────────────┘              │
                      │                                          │
                      │ SQL Query (SELECT/INSERT)               │
                      ▼                                          │
┌─────────────────────────────────────────────────────────────┐ │
│                🗄️ DATA BOUNDARY                            │ │
│                                                             │ │
│  ┌─────────────────────────────────────────────────────┐   │ │
│  │              MySQL Database                         │   │ │
│  │              (Data Store)                          │   │ │
│  └─────────────────────────────────────────────────────┘   │ │
└─────────────────────────────────────────────────────────────┘ │
                      │                                          │
                      │ SQL Response (Data)                      │
                      │                                          │
                      │ Internal Response (Rendered Content)     │
                      │                                          │
                      │ HTTPS Response (Final Page)              │
                      │ HTTPS Response (Dashboard)              │
                      │                                          │
                      ▼                                          ▼
┌─────────────────┐    ┌─────────────────┐
│ 🌐 User Browser │    │ 👑 Admin Panel  │
│ (Chrome/Firefox)│    │ (WP Admin Panel)│
│ External Entity │    │ External Entity │
└─────────────────┘    └─────────────────┘
```

**Core Data Flows (2 Required):**

**Data Flow 1: User Request Processing (6 steps):**
1. User Browser → Web Server: HTTPS Request (GET/POST with SSL/TLS)
2. Web Server → WordPress Core: Process Request (PHP Execution)
3. WordPress Core → MySQL Database: Query Database (SELECT/INSERT/UPDATE)
4. MySQL Database → WordPress Core: Return Data (Query Results)
5. WordPress Core → Web Server: Render HTML (Final Page)
6. Web Server → User Browser: HTTPS Response (Complete Page)

**Data Flow 2: Admin Operations (6 steps):**
7. Admin Dashboard → Web Server: Admin Login (POST /wp-admin)
8. Web Server → WordPress Core: Authenticate User (Session Management)
9. WordPress Core → MySQL Database: Admin Database Query (User Permissions)
10. MySQL Database → WordPress Core: Admin Data Response (Dashboard Data)
11. WordPress Core → Web Server: Admin Interface (Dashboard Rendering)
12. Web Server → Admin Dashboard: Admin Dashboard (Secure Response)

---

## Diagram 2: Threat Tree Diagram (TTD)

```
                    🔥 ROOT THREAT
            Compromise of WordPress Website Integrity and User Data
                              │
                    ┌─────────┼─────────┐
                    │         │         │
                    ▼         ▼         ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │ Weak Authentication│ │ SQL Injection  │ │ Cross-Site      │
        │   (Vulnerability) │ │ (Vulnerability) │ │ Scripting (XSS) │
        │                   │ │                 │ │ (Vulnerability) │
        └─────────┬─────────┘ └─────────┬─────┘ └─────────┬───────┘
                  │                     │                 │
                  ▼                     ▼                 ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │ Brute Force     │ │ Plugin SQL      │ │ Comment XSS     │
        │ Attacks         │ │ Injection        │ │ Injection       │
        │ (Attack Method) │ │ (Attack Method) │ │ (Attack Method) │
        └─────────────────┘ └─────────────────┘ └─────────────────┘
                  │                     │                 │
                  │                     │                 │
                  ▼                     ▼                 ▼
        ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
        │ Multi-Factor    │ │ Parameterized   │ │ Input           │
        │ Authentication  │ │ Queries         │ │ Sanitization    │
        │ (Countermeasure) │ │ (Countermeasure) │ │ (Countermeasure)│
        └─────────────────┘ └─────────────────┘ └─────────────────┘
                                                           │
                                                           ▼
                                                 ┌─────────────────┐
                                                 │ Content Security│
                                                 │ Policy          │
                                                 │ (Countermeasure) │
                                                 └─────────────────┘
```

**Vulnerabilities (3 Required):**
- Weak Authentication
- SQL Injection  
- Cross-Site Scripting (XSS)

**Countermeasures (3 Required):**
- Multi-Factor Authentication
- Parameterized Queries
- Input Sanitization

---

## Diagram 3: Use & Misuse Diagram (UMD)

```
    👤 User          👑 Admin          ⚠️ Malicious Attacker
       │                │                      │
       │                │                      │
       ▼                ▼                      ▼
┌─────────────┐ ┌─────────────┐      ┌─────────────┐
│ User Logs   │ │ Admin       │      │ Credential  │
│ Into Account│ │ Publishes   │      │ Stuffing    │
│ (Use Case)  │ │ a Post      │      │ Attack      │
└──────┬──────┘ │ (Use Case)  │      │ (Misuse Case)│
       │        └──────┬──────┘      └──────┬──────┘
       │               │                    │
       │               │                    │ 🚫 THREATENS
       │               │                    │ (Red Dashed)
       │               │                    ▼
       │               │            ┌─────────────┐
       │               │            │ User Logs   │
       │               │            │ Into Account│
       │               │            │ (Use Case)  │
       │               │            └─────────────┘
       │               │                    ▲
       │               │                    │ ✅ MITIGATES
       │               │                    │ (Green Solid)
       │               │                    │
       │               │            ┌─────────────┐
       │               │            │ Rate        │
       │               │            │ Limiting &  │
       │               │            │ MFA         │
       │               │            │ (Mitigation)│
       │               │            └─────────────┘
       │               │
       │               │ 🚫 THREATENS
       │               │ (Red Dashed)
       │               ▼
       │        ┌─────────────┐
       │        │ Admin       │
       │        │ Publishes   │
       │        │ a Post      │
       │        │ (Use Case)  │
       │        └──────┬──────┘
       │               │ ✅ MITIGATES
       │               │ (Green Solid)
       │               ▼
       │        ┌─────────────┐
       │        │ File Type   │
       │        │ Validation  │
       │        │ (Mitigation)│
       │        └─────────────┘
       │
       │ 🚫 THREATENS
       │ (Red Dashed)
       ▼
┌─────────────┐
│ User        │
│ Comments on │
│ a Post      │
│ (Use Case)  │
└──────┬──────┘
       │ ✅ MITIGATES
       │ (Green Solid)
       ▼
┌─────────────┐
│ Input       │
│ Sanitization│
│ (Mitigation)│
└─────────────┘
```

**Actors (3):**
- User
- Admin  
- Malicious Attacker

**Use Cases (3):**
- User Logs Into Account
- Admin Publishes a Post
- User Comments on a Post

**Misuse Cases (3):**
- Credential Stuffing Attack
- Malicious File Upload
- Comment XSS Injection

**Mitigations (3):**
- Rate Limiting & MFA
- File Type Validation
- Input Sanitization

---

## Legend
- 🚫 THREATENS (Red Dashed Line)
- ✅ MITIGATES (Green Solid Line)  
- ➡️ NORMAL FLOW (Blue Solid Line)
