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

**Enhanced Data Flows (32 total):**

**External Interactions (10 flows):**
1. User → Load Balancer: HTTPS Request (GET /page)
2. User → CDN: Asset Request (CSS/JS/Images)
3. User → Load Balancer: Form Submission (POST /contact)
4. User → Web Server: AJAX Request (Dynamic Content)
5. Admin → Load Balancer: Admin Login (POST /wp-admin)
6. Admin → Web Server: Content Creation (POST /wp-admin/post-new)
7. Admin → Web Server: Plugin Management (POST /wp-admin/plugins)
8. Admin → Web Server: File Upload (POST /wp-admin/media-new)
9. Plugin Dev → Web Server: Plugin Upload (ZIP File Upload)
10. Plugin Dev → Web Server: Theme Upload (Theme Package)

**Internal Processing (6 flows):**
11. Load Balancer → Web Server: Route Request (Load Balancing)
12. Web Server → WordPress Core: Process Request (PHP Execution)
13. Web Server → CDN: Serve Static Assets (Direct File Access)
14. WordPress Core → Plugin System: Execute Plugin (Plugin Logic)
15. WordPress Core → Theme Engine: Render Theme (Template Processing)
16. WordPress Core → File Upload Handler: Handle Upload (File Processing)

**Data Operations (10 flows):**
17. WordPress Core → MySQL: Query Data (SELECT/INSERT/UPDATE)
18. Plugin System → MySQL: Plugin Data (Custom Tables)
19. Theme Engine → MySQL: Theme Settings (Configuration)
20. File Upload Handler → MySQL: File Metadata (Attachment Data)
21. File Upload Handler → File System: Store Files (Media Storage)
22. Plugin System → File System: Plugin Files (Code Storage)
23. Theme Engine → File System: Theme Assets (CSS/JS/Images)
24. WordPress Core → Cache System: Cache Data (Performance)
25. Plugin System → Cache System: Plugin Cache (Temporary Data)
26. Theme Engine → Cache System: Theme Cache (Rendered Fragments)

**Response Flows (6 flows):**
27. MySQL → WordPress Core: Return Data (Query Results)
28. File System → Web Server: Serve Files (Media Delivery)
29. Cache System → WordPress Core: Return Cached Data (Fast Response)
30. WordPress Core → Web Server: Rendered HTML (Final Page)
31. Web Server → User Browser: HTTPS Response (Complete Page)
32. Web Server → Admin Dashboard: Admin Response (Dashboard)

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

**Enhanced Vulnerabilities (6):**
- Weak Authentication
- SQL Injection  
- Cross-Site Scripting (XSS)
- File Upload Vulnerabilities
- Plugin/Theme Vulnerabilities
- Insecure Direct Object References

**Enhanced Countermeasures (8):**
- Multi-Factor Authentication
- Secure Session Management
- Parameterized Queries
- Input Sanitization
- Content Security Policy
- File Upload Security
- Plugin/Theme Security
- Access Control & Authorization

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
