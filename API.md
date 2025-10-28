# API Documentation

## نظرة عامة | Overview

توثيق شامل لجميع نقاط النهاية (API Endpoints) المتاحة في Ipload.

Comprehensive documentation for all available API endpoints in Ipload.

## Base URL

```
http://localhost:3000
```

---

## Endpoints

### 1. الصفحة الرئيسية | Home Page

**GET** `/`

عرض واجهة المستخدم الرئيسية.

Display the main user interface.

**Response:**
- HTML page

---

### 2. الحصول على عنوان IP | Get IP Address

**GET** `/api/ip`

الحصول على عنوان IP الخاص بالمستخدم.

Get the user's IP address.

**Response:**
```json
{
  "ip": "192.168.1.1",
  "timestamp": "2025-10-28T17:47:25.243Z"
}
```

**Response Fields:**
- `ip` (string): عنوان IP الخاص بالمستخدم | User's IP address
- `timestamp` (string): وقت الطلب بتنسيق ISO 8601 | Request time in ISO 8601 format

**Example:**
```bash
curl http://localhost:3000/api/ip
```

---

### 3. رفع ملف | Upload File

**POST** `/api/upload`

رفع ملف إلى الخادم.

Upload a file to the server.

**Request:**
- Content-Type: `multipart/form-data`
- Body:
  - `file` (file): الملف المراد رفعه | File to upload

**Constraints:**
- الحد الأقصى لحجم الملف: 10MB | Maximum file size: 10MB

**Success Response (200):**
```json
{
  "message": "File uploaded successfully",
  "file": {
    "filename": "file-1635432123456-123456789.pdf",
    "originalname": "document.pdf",
    "size": 1024000,
    "mimetype": "application/pdf"
  },
  "uploadedBy": "192.168.1.1",
  "timestamp": "2025-10-28T17:47:25.243Z"
}
```

**Error Response (400):**
```json
{
  "error": "No file uploaded"
}
```

**Response Fields:**
- `message` (string): رسالة النجاح | Success message
- `file` (object): معلومات الملف | File information
  - `filename` (string): اسم الملف المحفوظ | Saved filename
  - `originalname` (string): الاسم الأصلي للملف | Original filename
  - `size` (number): حجم الملف بالبايتات | File size in bytes
  - `mimetype` (string): نوع الملف | File MIME type
- `uploadedBy` (string): عنوان IP للرافع | Uploader's IP address
- `timestamp` (string): وقت الرفع | Upload timestamp

**Example:**
```bash
curl -X POST -F "file=@document.pdf" http://localhost:3000/api/upload
```

**JavaScript Example:**
```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('http://localhost:3000/api/upload', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

---

### 4. قائمة الملفات | List Files

**GET** `/api/files`

الحصول على قائمة بجميع الملفات المرفوعة.

Get a list of all uploaded files.

**Response:**
```json
{
  "files": [
    {
      "filename": "file-1635432123456-123456789.pdf",
      "size": 1024000,
      "created": "2025-10-28T17:47:25.243Z"
    },
    {
      "filename": "file-1635432567890-987654321.jpg",
      "size": 2048000,
      "created": "2025-10-28T18:30:15.123Z"
    }
  ]
}
```

**Response Fields:**
- `files` (array): قائمة الملفات | List of files
  - `filename` (string): اسم الملف | Filename
  - `size` (number): حجم الملف بالبايتات | File size in bytes
  - `created` (string): تاريخ الإنشاء | Creation date

**Example:**
```bash
curl http://localhost:3000/api/files
```

---

## أكواد الحالة | Status Codes

| Code | المعنى | Meaning |
|------|--------|---------|
| 200  | نجاح | Success |
| 400  | طلب خاطئ | Bad Request |
| 500  | خطأ في الخادم | Server Error |

---

## معالجة الأخطاء | Error Handling

جميع الأخطاء يتم إرجاعها بتنسيق JSON:

All errors are returned in JSON format:

```json
{
  "error": "Error message here"
}
```

---

## أمثلة الاستخدام | Usage Examples

### مثال كامل بـ JavaScript | Complete JavaScript Example

```javascript
// الحصول على عنوان IP | Get IP Address
async function getIP() {
  const response = await fetch('/api/ip');
  const data = await response.json();
  console.log('Your IP:', data.ip);
}

// رفع ملف | Upload File
async function uploadFile(file) {
  const formData = new FormData();
  formData.append('file', file);
  
  const response = await fetch('/api/upload', {
    method: 'POST',
    body: formData
  });
  
  const data = await response.json();
  console.log('Upload result:', data);
}

// قائمة الملفات | List Files
async function listFiles() {
  const response = await fetch('/api/files');
  const data = await response.json();
  console.log('Files:', data.files);
}
```

### مثال بـ Python | Python Example

```python
import requests

# الحصول على عنوان IP | Get IP Address
response = requests.get('http://localhost:3000/api/ip')
print(response.json())

# رفع ملف | Upload File
files = {'file': open('document.pdf', 'rb')}
response = requests.post('http://localhost:3000/api/upload', files=files)
print(response.json())

# قائمة الملفات | List Files
response = requests.get('http://localhost:3000/api/files')
print(response.json())
```

---

## الأمان | Security

- الحد الأقصى لحجم الملف محدود بـ 10MB لمنع استهلاك الموارد
- أسماء الملفات يتم توليدها تلقائياً لمنع الكتابة فوق الملفات الموجودة
- يتم تتبع عنوان IP لكل عملية رفع

- Maximum file size limited to 10MB to prevent resource exhaustion
- Filenames are auto-generated to prevent overwriting existing files
- IP address tracking for each upload operation

---

## ملاحظات | Notes

1. جميع التواريخ بتنسيق ISO 8601 | All timestamps in ISO 8601 format
2. الملفات المرفوعة تُحفظ في مجلد `uploads/` | Uploaded files saved in `uploads/` directory
3. أسماء الملفات تتضمن طابع زمني فريد | Filenames include unique timestamp
