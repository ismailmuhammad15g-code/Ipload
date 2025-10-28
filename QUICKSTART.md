# دليل الاستخدام السريع | Quick Start Guide

## البدء السريع | Quick Start

### 1. التثبيت | Installation

```bash
# استنساخ المشروع | Clone repository
git clone https://github.com/ismailmuhammad15g-code/Ipload.git

# الدخول إلى المجلد | Navigate to directory
cd Ipload

# تثبيت المكتبات | Install dependencies
npm install
```

### 2. التشغيل | Running

```bash
# التشغيل العادي | Normal start
npm start

# التطوير مع إعادة التشغيل التلقائي | Development with auto-reload
npm run dev
```

### 3. الاستخدام | Usage

1. افتح المتصفح على `http://localhost:3000`
2. سيظهر عنوان IP الخاص بك تلقائياً
3. اضغط "اختر ملفاً" لتحديد ملف للرفع
4. اضغط "رفع الملف" لإتمام العملية
5. شاهد قائمة الملفات المرفوعة في الأسفل

---

1. Open browser at `http://localhost:3000`
2. Your IP address will be displayed automatically
3. Click "Choose File" to select a file
4. Click "Upload File" to complete the process
5. View uploaded files list at the bottom

## الميزات الإضافية | Additional Features

### تغيير المنفذ | Change Port

```bash
PORT=5000 npm start
```

### متغيرات البيئة | Environment Variables

انسخ ملف `.env.example` إلى `.env` وعدل الإعدادات:

Copy `.env.example` to `.env` and modify settings:

```bash
cp .env.example .env
```

## استكشاف الأخطاء | Troubleshooting

### المشكلة: لا يعمل الخادم | Issue: Server not starting

**الحل | Solution:**
- تأكد من تثبيت Node.js | Ensure Node.js is installed
- تأكد من تثبيت المكتبات | Ensure dependencies are installed
- تحقق من توفر المنفذ 3000 | Check if port 3000 is available

### المشكلة: فشل رفع الملف | Issue: File upload fails

**الحل | Solution:**
- تأكد من حجم الملف أقل من 10MB | Ensure file is less than 10MB
- تحقق من صلاحيات مجلد uploads | Check uploads folder permissions
- تحقق من الاتصال بالخادم | Verify server connection

## للمزيد من المساعدة | For More Help

راجع الملف README.md أو افتح issue على GitHub

See README.md or open an issue on GitHub
