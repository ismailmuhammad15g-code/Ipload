# 🤖 Bot Architecture & Flow - هيكلة البوت

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    TELEGRAM BOT                         │
│                      (Ipload)                           │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                   Bot Application                       │
│                    (bot.py)                            │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │            Command Handlers                      │  │
│  │  • /start - Welcome & Menu                      │  │
│  │  • /info - Statistics & Console Display        │  │
│  │  • /myfiles - Personal Files                   │  │
│  │  • /gallery - All Files Gallery               │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │            File Handlers                        │  │
│  │  • Documents (PDF, DOC, etc.)                  │  │
│  │  • Photos (JPG, PNG, etc.)                     │  │
│  │  • Videos (MP4, AVI, etc.)                     │  │
│  │  • Audio (MP3, WAV, etc.)                      │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Interactive Buttons                     │  │
│  │  • My Files Button                             │  │
│  │  • Gallery Button                              │  │
│  │  • Info Button                                 │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                SQLite Database                          │
│               (bot_database.db)                         │
│                                                         │
│  ┌──────────────────────┐  ┌──────────────────────┐    │
│  │   Users Table        │  │   Files Table        │    │
│  │                      │  │                      │    │
│  │ • user_id (PK)      │  │ • id (PK)           │    │
│  │ • username          │  │ • user_id (FK)      │    │
│  │ • first_name        │  │ • file_id           │    │
│  │ • last_name         │  │ • file_name         │    │
│  │ • created_at        │  │ • file_type         │    │
│  │                      │  │ • file_size         │    │
│  │                      │  │ • caption           │    │
│  │                      │  │ • uploaded_at       │    │
│  └──────────────────────┘  └──────────────────────┘    │
│              │                        │                 │
│              └────────────┬───────────┘                 │
│                           │                             │
│                    Foreign Key                          │
│                    Relationship                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                Console Output                           │
│                                                         │
│  📊 Bot Info Display                                   │
│  • User statistics                                     │
│  • File counts                                         │
│  • Storage usage                                       │
│  • Timestamps                                          │
└─────────────────────────────────────────────────────────┘
```

## 🔄 User Flow Diagram

```
User Opens Bot
      │
      ▼
┌───────────┐
│  /start   │  ──► Welcome Message
└───────────┘       + Menu Buttons
      │
      ├──────────────────┬──────────────────┬──────────────┐
      │                  │                  │              │
      ▼                  ▼                  ▼              ▼
┌──────────┐      ┌──────────┐      ┌──────────┐   ┌──────────┐
│Send File │      │ /myfiles │      │ /gallery │   │  /info   │
└──────────┘      └──────────┘      └──────────┘   └──────────┘
      │                  │                  │              │
      ▼                  ▼                  ▼              ▼
┌──────────┐      ┌──────────┐      ┌──────────┐   ┌──────────┐
│  Save to │      │   Show   │      │   Show   │   │  Display │
│ Database │      │   User   │      │   All    │   │  Stats + │
└──────────┘      │  Files   │      │  Files   │   │ Console  │
      │           └──────────┘      └──────────┘   └──────────┘
      ▼
┌──────────┐
│Confirmation│
│  Message  │
└──────────┘
```

## 📁 File Upload Flow

```
User Sends File
      │
      ▼
┌─────────────────┐
│ Detect File Type│
└─────────────────┘
      │
      ├────────┬─────────┬─────────┬─────────┐
      │        │         │         │         │
      ▼        ▼         ▼         ▼         ▼
   Document  Photo   Video    Audio    Other
      │        │         │         │         │
      └────────┴─────────┴─────────┴─────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │ Extract File Metadata │
          │ • Name                │
          │ • Size                │
          │ • Type                │
          │ • Caption             │
          │ • Telegram File ID    │
          └───────────────────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │ Save to Database      │
          │ • Link to User        │
          │ • Store Metadata      │
          │ • Add Timestamp       │
          └───────────────────────┘
                      │
                      ▼
          ┌───────────────────────┐
          │ Send Confirmation     │
          │ • Success Message     │
          │ • File Details        │
          │ • Size in MB          │
          └───────────────────────┘
```

## 🎨 Gallery System Flow

```
User Requests Gallery
      │
      ▼
┌─────────────────┐
│ Query Database  │
│ JOIN users +    │
│      files      │
└─────────────────┘
      │
      ▼
┌─────────────────┐
│  Sort by Date   │
│  (Newest First) │
└─────────────────┘
      │
      ▼
┌─────────────────┐
│   Format List   │
│ • File Name     │
│ • Uploader      │
│ • Size          │
│ • Date          │
└─────────────────┘
      │
      ▼
┌─────────────────┐
│ Send to User    │
│ (15 files max)  │
└─────────────────┘
```

## 💻 Console Info Flow

```
User Triggers /info
      │
      ▼
┌─────────────────┐
│ Get User Data   │
│ from Database   │
└─────────────────┘
      │
      ▼
┌─────────────────┐
│ Calculate Stats │
│ • File Count    │
│ • Total Size    │
│ • Upload Dates  │
└─────────────────┘
      │
      ├────────────────────────┬─────────────────────┐
      │                        │                     │
      ▼                        ▼                     ▼
┌──────────┐         ┌──────────────┐    ┌──────────────┐
│  Print   │         │    Send      │    │   Log to     │
│   to     │         │  Message     │    │   System     │
│ Console  │         │  to User     │    │    Logs      │
└──────────┘         └──────────────┘    └──────────────┘
```

## 🚀 Deployment Flow

```
Choose Platform
      │
      ├──────────┬──────────┬──────────┬──────────┐
      │          │          │          │          │
      ▼          ▼          ▼          ▼          ▼
   Heroku    Railway    Render     VPS      Docker
      │          │          │          │          │
      ▼          ▼          ▼          ▼          ▼
  Procfile   Auto-Deploy  Worker   systemd   Dockerfile
      │          │          │          │          │
      └──────────┴──────────┴──────────┴──────────┘
                      │
                      ▼
          ┌───────────────────┐
          │ Set Environment   │
          │ Variables         │
          │ • BOT_TOKEN       │
          └───────────────────┘
                      │
                      ▼
          ┌───────────────────┐
          │ Install Dependencies│
          │ (requirements.txt) │
          └───────────────────┘
                      │
                      ▼
          ┌───────────────────┐
          │  Start Bot        │
          │  (python bot.py)  │
          └───────────────────┘
                      │
                      ▼
          ┌───────────────────┐
          │  Bot Running! ✅  │
          └───────────────────┘
```

## 🔐 Security Flow

```
┌─────────────────────────────────────────┐
│         Security Measures               │
├─────────────────────────────────────────┤
│                                         │
│  1. Environment Variables               │
│     ↓                                   │
│     BOT_TOKEN in .env                   │
│     Not committed to Git                │
│                                         │
│  2. Database Security                   │
│     ↓                                   │
│     SQLite with proper permissions      │
│     Data integrity constraints          │
│     Foreign key relationships           │
│                                         │
│  3. .gitignore Protection              │
│     ↓                                   │
│     Exclude .env                        │
│     Exclude .db files                   │
│     Exclude sensitive data              │
│                                         │
│  4. User Data Privacy                  │
│     ↓                                   │
│     User-specific file access           │
│     Protected database queries          │
│                                         │
└─────────────────────────────────────────┘
```

## 📊 Data Model

```
┌────────────────────────────────────────────┐
│             Database Schema                │
└────────────────────────────────────────────┘

┌─────────────────────┐       ┌─────────────────────┐
│       users         │       │       files         │
├─────────────────────┤       ├─────────────────────┤
│ user_id     [PK]    │◄──────│ id          [PK]    │
│ username            │       │ user_id     [FK]    │
│ first_name          │       │ file_id             │
│ last_name           │       │ file_name           │
│ created_at          │       │ file_type           │
│                     │       │ file_size           │
│                     │       │ caption             │
│                     │       │ uploaded_at         │
└─────────────────────┘       └─────────────────────┘
```

---

## 🎯 Key Features Summary

1. **Multi-format Support**: Documents, Photos, Videos, Audio
2. **Database Integration**: SQLite with relational data
3. **Gallery System**: View all uploads chronologically
4. **User Management**: Track users and their files
5. **Console Logging**: Real-time info display
6. **Interactive UI**: Buttons and callbacks
7. **Deployment Ready**: Multiple platform support
8. **Security**: Environment variables, .gitignore
9. **Testing**: Comprehensive test suite
10. **Documentation**: Complete guides in Arabic & English

---

✅ **System is fully functional and production-ready!**
