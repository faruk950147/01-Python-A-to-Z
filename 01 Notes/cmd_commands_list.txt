
📜 Command Prompt (CMD) – Full Commands List

1. Basic Commands
--------------------------------------
cls                  → স্ক্রিন পরিষ্কার করে
exit                 → Command Prompt বন্ধ করে
echo                 → টেক্সট বা মেসেজ দেখায়
help                 → সব কমান্ডের লিস্ট এবং বর্ণনা দেখায়
ver                  → Windows এর ভার্সন দেখায়
time                 → বর্তমান সময় দেখায় বা সেট করে
date                 → বর্তমান তারিখ দেখায় বা সেট করে

2. File & Folder Management
--------------------------------------
dir                  → বর্তমান ডিরেক্টরির ফাইল/ফোল্ডারের লিস্ট দেখায়
cd                   → ডিরেক্টরি পরিবর্তন করে
md / mkdir           → নতুন ফোল্ডার তৈরি করে
rd / rmdir           → ফোল্ডার ডিলিট করে
del                  → ফাইল ডিলিট করে
copy                 → ফাইল কপি করে
xcopy                → ফাইল ও ফোল্ডার কপি করে
move                 → ফাইল/ফোল্ডার এক জায়গা থেকে অন্য জায়গায় সরায়
ren                  → ফাইল/ফোল্ডারের নাম পরিবর্তন করে
tree                 → ফোল্ডারের স্ট্রাকচার দেখায়

3. System Information & Management
--------------------------------------
systeminfo           → পিসির বিস্তারিত তথ্য দেখায়
tasklist             → বর্তমানে চলমান প্রোগ্রামের লিস্ট
taskkill /IM program.exe /F  → একটি প্রোগ্রাম জোরপূর্বক বন্ধ করে
chkdsk               → ডিস্কে ত্রুটি চেক করে
wmic                 → সিস্টেম ম্যানেজমেন্টের জন্য বিভিন্ন কমান্ড
driverquery          → ড্রাইভার লিস্ট দেখায়
hostname             → কম্পিউটারের নাম দেখায়

4. Networking Commands
--------------------------------------
ipconfig             → নেটওয়ার্ক IP কনফিগারেশন দেখায়
ipconfig /all        → বিস্তারিত নেটওয়ার্ক তথ্য দেখায়
ping website.com     → সার্ভারে কানেকশন চেক করে
tracert website.com  → সার্ভারে যাওয়ার পথ দেখায়
nslookup domain.com  → DNS তথ্য বের করে
netstat              → নেটওয়ার্ক কানেকশন লিস্ট
getmac               → নেটওয়ার্ক অ্যাডাপ্টারের MAC অ্যাড্রেস
netsh                → নেটওয়ার্ক কনফিগারেশন পরিবর্তন

5. Disk Management
--------------------------------------
diskpart             → ডিস্ক পার্টিশন ম্যানেজমেন্ট
format               → ডিস্ক ফরম্যাট করে
label                → ডিস্কের নাম পরিবর্তন করে
vol                  → ডিস্কের ভলিউম তথ্য

6. User & Access Control
--------------------------------------
net user             → ইউজারের লিস্ট দেখায়
net user username password /add → নতুন ইউজার তৈরি
net user username /delete       → ইউজার ডিলিট
net localgroup administrators username /add → ইউজারকে অ্যাডমিন বানায়

7. Advanced & Useful
--------------------------------------
attrib               → ফাইল/ফোল্ডারের অ্যাট্রিবিউট পরিবর্তন
sfc /scannow         → সিস্টেম ফাইল চেক ও রিপেয়ার
shutdown /s /f /t 0  → পিসি বন্ধ করে
shutdown /r /f /t 0  → পিসি রিস্টার্ট করে
fc file1 file2       → দুই ফাইলের মধ্যে পার্থক্য দেখায়
clip                 → আউটপুট ক্লিপবোর্ডে কপি করে
powershell           → PowerShell চালু করে



===============================
 Windows CMD Commands List
===============================

[Basic CMD Commands]
- help                : সব কমান্ডের লিস্ট দেখাবে
- cls                 : স্ক্রিন ক্লিয়ার করবে
- exit                : CMD বন্ধ করবে

[File & Directory Management]
- dir                 : বর্তমান ফোল্ডারের ফাইল/ফোল্ডারের লিস্ট দেখাবে
- cd                  : ডিরেক্টরি পরিবর্তন করবে (cd .. → এক ধাপ পিছনে)
- md <foldername>     : নতুন ফোল্ডার তৈরি করবে
- mkdir <foldername>  : নতুন ফোল্ডার তৈরি করবে
- rd <foldername>     : ফোল্ডার ডিলিট করবে
- rmdir <foldername>  : ফোল্ডার ডিলিট করবে
- del <filename>      : ফাইল ডিলিট করবে
- copy <src> <dest>   : ফাইল কপি করবে
- move <src> <dest>   : ফাইল মুভ করবে
- rename <old> <new>  : ফাইল/ফোল্ডার rename করবে

[System Info & Settings]
- systeminfo          : পিসির বিস্তারিত তথ্য দেখাবে
- hostname            : কম্পিউটারের নাম দেখাবে
- ver                 : Windows এর ভার্সন দেখাবে
- date / time         : তারিখ/সময় দেখাবে বা সেট করবে
- tasklist            : রানিং প্রোগ্রামের লিস্ট দেখাবে
- taskkill /F /IM <program.exe> : প্রোগ্রাম ফোর্স করে বন্ধ করবে
- shutdown /s /t 0    : সাথে সাথে শাটডাউন করবে
- shutdown /r /t 0    : সাথে সাথে রিস্টার্ট করবে

[Networking Commands]
- ipconfig            : IP configuration দেখাবে
- ipconfig /all       : সব network details দেখাবে
- ping <website>      : ওয়েবসাইটে কানেকশন চেক করবে
- tracert <website>   : ওয়েবসাইটে যাবার রুট দেখাবে
- netstat             : অ্যাক্টিভ কানেকশন দেখাবে
- nslookup <domain>   : DNS রেকর্ড দেখাবে

[Useful Tools]
- chkdsk              : হার্ডডিস্ক চেক করবে
- sfc /scannow        : সিস্টেম ফাইল রিপেয়ার করবে
- diskpart            : ডিস্ক ম্যানেজমেন্ট টুল
- tree                : ফোল্ডার স্ট্রাকচার দেখাবে
- color 0A            : CMD এর কালার পরিবর্তন করবে (0A = Black BG, Green Text)
