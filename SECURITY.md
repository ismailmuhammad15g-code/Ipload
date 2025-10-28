# سياسة الأمان | Security Policy

## الإصدارات المدعومة | Supported Versions

نحن نوفر تحديثات الأمان للإصدارات التالية:

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## الإبلاغ عن ثغرة أمنية | Reporting a Vulnerability

إذا اكتشفت ثغرة أمنية، يرجى اتباع الخطوات التالية:

If you discover a security vulnerability, please follow these steps:

### 1. لا تقم بنشرها علناً | Do Not Disclose Publicly

يرجى عدم الإبلاغ عن الثغرات الأمنية عبر GitHub Issues العامة.

Please do not report security vulnerabilities through public GitHub issues.

### 2. أبلغ بشكل خاص | Report Privately

قم بإرسال تقرير مفصل يتضمن:

Send a detailed report including:

- وصف الثغرة | Vulnerability description
- خطوات إعادة الإنتاج | Steps to reproduce
- الإصدار المتأثر | Affected version
- التأثير المحتمل | Potential impact
- اقتراحات للحل (إن وجدت) | Suggestions for fixing (if any)

### 3. التواصل | Contact

يمكنك التواصل عبر:

You can contact via:
- فتح Security Advisory خاص في GitHub | Open a private Security Advisory on GitHub
- مراسلة صاحب المستودع مباشرة | Message the repository owner directly

### 4. ماذا تتوقع | What to Expect

- **24 ساعة:** تأكيد استلام التقرير | Acknowledgment of report
- **7 أيام:** تقييم أولي للثغرة | Initial assessment
- **30 يوماً:** تطوير ونشر الحل | Development and deployment of fix

## إرشادات الأمان | Security Guidelines

### للمستخدمين | For Users

1. **حافظ على التحديثات:**
   - قم بتحديث Ipload إلى أحدث إصدار بانتظام
   - Keep Ipload updated to the latest version

2. **استخدم HTTPS:**
   - استخدم دائماً اتصال HTTPS في الإنتاج
   - Always use HTTPS connection in production

3. **إدارة الملفات:**
   - راقب حجم مجلد uploads
   - قم بحذف الملفات غير المستخدمة بانتظام
   - Monitor uploads folder size
   - Delete unused files regularly

4. **متغيرات البيئة:**
   - لا تشارك ملف .env أبداً
   - احتفظ بالمعلومات الحساسة آمنة
   - Never share .env file
   - Keep sensitive information secure

### للمطورين | For Developers

1. **مراجعة الكود:**
   - راجع جميع التغييرات قبل الدمج
   - استخدم أدوات تحليل الكود الثابت
   - Review all changes before merging
   - Use static code analysis tools

2. **التبعيات:**
   - قم بتحديث المكتبات بانتظام
   - استخدم `npm audit` للتحقق من الثغرات
   - Update dependencies regularly
   - Use `npm audit` to check vulnerabilities

3. **اختبار الأمان:**
   - اختبر الحماية من حقن الكود
   - تحقق من صحة المدخلات
   - اختبر حدود حجم الملفات
   - Test for code injection protection
   - Validate input properly
   - Test file size limits

## الثغرات المعروفة | Known Vulnerabilities

حالياً لا توجد ثغرات معروفة.

Currently, there are no known vulnerabilities.

## سجل الأمان | Security Changelog

### [1.0.0] - 2025-10-28

#### الإضافات الأمنية | Security Additions
- حد أقصى لحجم الملف (10MB) | Maximum file size limit (10MB)
- تسمية ملفات آمنة | Safe file naming
- تتبع عنوان IP للرافعين | IP address tracking for uploaders
- التحقق من نوع الملفات | File type validation

## أفضل الممارسات | Best Practices

### تكوين الأمان | Security Configuration

```javascript
// مثال على تحسينات الأمان | Example security improvements

// 1. إضافة helmet للحماية
const helmet = require('helmet');
app.use(helmet());

// 2. إضافة rate limiting
const rateLimit = require('express-rate-limit');
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100 // limit each IP to 100 requests per windowMs
});
app.use('/api/', limiter);

// 3. التحقق من نوع الملف
const fileFilter = (req, file, cb) => {
  const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
  if (allowedTypes.includes(file.mimetype)) {
    cb(null, true);
  } else {
    cb(new Error('Invalid file type'), false);
  }
};
```

### فحص الأمان | Security Scanning

```bash
# فحص الثغرات في المكتبات | Check for vulnerabilities
npm audit

# إصلاح الثغرات تلقائياً | Auto-fix vulnerabilities
npm audit fix

# فحص شامل | Comprehensive scan
npm audit fix --force
```

## الالتزام | Commitment

نحن ملتزمون بـ:

We are committed to:

- الاستجابة السريعة لتقارير الأمان | Quick response to security reports
- الشفافية في التعامل مع الثغرات | Transparency in handling vulnerabilities
- توفير تحديثات منتظمة | Providing regular updates
- حماية خصوصية المستخدمين | Protecting user privacy

## شكراً | Thank You

نشكر جميع الباحثين الأمنيين الذين يساعدون في جعل Ipload أكثر أماناً!

Thank you to all security researchers who help make Ipload more secure!
