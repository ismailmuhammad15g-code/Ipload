# 🚀 Ipload

نظام رفع الملفات وإدارة عناوين IP - File Upload and IP Management System

## 📋 الوصف | Description

Ipload هو تطبيق ويب بسيط وسهل الاستخدام لرفع الملفات وعرض عنوان IP الخاص بالمستخدم. يتميز بواجهة باللغة العربية وتصميم عصري وجذاب.

Ipload is a simple and easy-to-use web application for uploading files and displaying the user's IP address. It features an Arabic interface with a modern and attractive design.

## ✨ المميزات | Features

- 📤 رفع الملفات بحجم يصل إلى 10MB | Upload files up to 10MB
- 🌐 عرض عنوان IP الخاص بالمستخدم | Display user's IP address
- 📊 عرض قائمة الملفات المرفوعة | List uploaded files
- 🎨 واجهة مستخدم عصرية وسهلة الاستخدام | Modern and user-friendly interface
- 📱 تصميم متجاوب يعمل على جميع الأجهزة | Responsive design for all devices
- 🌍 دعم كامل للغة العربية | Full Arabic language support

## 🛠️ التثبيت | Installation

### المتطلبات | Requirements

- Node.js (الإصدار 14 أو أحدث | version 14 or higher)
- npm أو yarn

### خطوات التثبيت | Installation Steps

1. استنساخ المشروع | Clone the repository:
```bash
git clone https://github.com/ismailmuhammad15g-code/Ipload.git
cd Ipload
```

2. تثبيت المكتبات المطلوبة | Install dependencies:
```bash
npm install
```

3. تشغيل التطبيق | Start the application:
```bash
npm start
```

4. افتح المتصفح على | Open browser at:
```
http://localhost:3000
```

## 🚀 الاستخدام | Usage

### للتطوير | For Development

لتشغيل التطبيق في وضع التطوير مع إعادة التشغيل التلقائي:

```bash
npm run dev
```

### الإنتاج | Production

```bash
npm start
```

## 📁 هيكل المشروع | Project Structure

```
Ipload/
├── src/
│   └── index.js          # ملف الخادم الرئيسي | Main server file
├── public/
│   ├── index.html        # الصفحة الرئيسية | Main page
│   ├── style.css         # ملف التنسيقات | Styles
│   └── script.js         # الجافاسكريبت | JavaScript
├── uploads/              # مجلد الملفات المرفوعة | Uploaded files directory
├── package.json          # معلومات المشروع | Project info
├── .gitignore           # ملفات التجاهل | Ignored files
└── README.md            # هذا الملف | This file
```

## 🔧 التكوين | Configuration

يمكنك تغيير منفذ الخادم باستخدام متغير البيئة:

```bash
PORT=5000 npm start
```

## 📝 API Endpoints

- `GET /` - الصفحة الرئيسية | Main page
- `GET /api/ip` - الحصول على عنوان IP | Get IP address
- `POST /api/upload` - رفع ملف | Upload file
- `GET /api/files` - قائمة الملفات | List files

## 🤝 المساهمة | Contributing

المساهمات مرحب بها! يرجى فتح issue أو pull request.

Contributions are welcome! Please open an issue or pull request.

## 📄 الترخيص | License

MIT License

## 👨‍💻 المطور | Developer

تم التطوير بواسطة | Developed by: ismailmuhammad15g-code

## 📞 التواصل | Contact

إذا كان لديك أي أسئلة أو اقتراحات، يرجى فتح issue في المستودع.

If you have any questions or suggestions, please open an issue in the repository.