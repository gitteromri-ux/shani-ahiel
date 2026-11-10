import json,os
SITE="https://gitteromri-ux.github.io/shani-ahiel/"
WA="https://wa.me/972546644489?text="
WAT={'he':'%D7%94%D7%99%D7%99%20%D7%A9%D7%A0%D7%99%2C%20%D7%94%D7%92%D7%A2%D7%AA%D7%99%20%D7%9E%D7%94%D7%90%D7%AA%D7%A8','en':'Hi%20Shani%2C%20I%20found%20you%20through%20your%20website'}
SVG=open('/tmp/wasvg').read().strip()
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@300;400;500&family=Heebo:wght@300;400;500&family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">'
def head(lang,title,desc,path,root,alt_path,typ="website"):
    url=SITE+path
    he_url=SITE+(path if lang=='he' else alt_path); en_url=SITE+(alt_path if lang=='he' else path)
    schema={"@context":"https://schema.org","@type":"ProfessionalService","name":"Shani Ahiel – Hospitality & F&B Consulting","alternateName":"שני אחיאל – ייעוץ אירוח ומסעדנות","url":SITE,"image":SITE+"assets/og.jpg","email":"Shanini.a@gmail.com","telephone":"+972546644489","areaServed":["Berlin","Germany","Israel","Europe"],"knowsLanguage":["he","en","de"],"description":"Hospitality and food & beverage consulting, openings, turnarounds and outsourced F&B management for restaurants and hotels.","founder":{"@type":"Person","name":"Shani Ahiel","alumniOf":"B.A. Communications & Business Administration"},"sameAs":["https://www.yafoberlin.com/"]}
    return f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url}"><link rel="alternate" hreflang="he" href="{he_url}"><link rel="alternate" hreflang="en" href="{en_url}"><link rel="alternate" hreflang="x-default" href="{he_url}">
<meta property="og:type" content="{typ}"><meta property="og:site_name" content="Shani Ahiel"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}assets/og.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:locale" content="{'he_IL' if lang=='he' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{SITE}assets/og.jpg">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{root}apple-touch-icon.png"><meta name="theme-color" content="#120F0D">
{FONTS}<link rel="preload" as="image" href="{root}assets/feast.webp">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
<link rel="stylesheet" href="{root}style.css">'''

T={
'he':dict(dir='rtl',title='שני אחיאל | ייעוץ, הקמה וניהול F&amp;B למסעדות ולמלונות',desc='שני אחיאל – מייסדת Yafo ו-Shishi בברלין, הובילה את מערך ה-F&amp;B של Selina ברלין. הקמה, הבראה וניהול מזון ומשקאות במיקור חוץ למסעדות ולמלונות.',
 brand='שני אחיאל',nav=['אודות','שירותים','שיטת העבודה','ניסיון','עיתונות','מגזין'],cta='לתיאום שיחה',toggle=('EN','en/'),
 eyebrow='מיפו לברלין · מסעדות · מלונות · אירועים',h1a='מסעדה שעובדת.',h1b='וגם מרוויחה.',
 lead='ייעוץ, הקמה וניהול מערכי מזון ומשקאות למסעדות ולמלונות – מהקונספט ועד השורה התחתונה. למעלה מעשור של הובלת מותגי אירוח בברלין, כבעלים וכמנהלת.',
 b1='בואו נדבר על העסק שלכם',b2='הניסיון שלי',
 heroband=[('Yafo','מסעדה ובר · 200 מקומות'),('Selina Berlin','F&amp;B מלא במלון'),('Amano','לובי שהפך למסעדה'),('Shishi','מסעדת שף · Farm to Table')],
 ab_e='אודות',ab_h='כל מה שאני מציעה – בניתי בעצמי, בשטח.',
 ab_p1='התחלתי מאחורי הבר ובשירות בתל אביב, התקדמתי לניהול אירועים, ובברלין הקמתי מאפס את <b>Yafo</b> – מסעדה ובר בני 200 מקומות ישיבה שהפכו לאחד ממוקדי האירוח הישראלי המוכרים בעיר. אחריה הגיעה <b>Shishi</b>, מסעדת שף על עקרונות Farm to Table, ושיתופי פעולה עם מלונות: הפיכת הלובי של <b>Amano</b> למסעדה של ממש, והובלת כל מערך המזון והמשקאות של <b>Selina ברלין</b>.',
 ab_p2='היום אני מביאה את הניסיון הזה לבעלי מסעדות, יזמים ומלונות: מבנה תפעולי, שליטה בעלויות, צוות שיודע לארח, וחוויה שאורחים חוזרים אליה. בלי תיאוריה – רק מה שהוכח מול קהל אמיתי, כל ערב.',
 ab_p3='תואר ראשון בתקשורת ומנהל עסקים · אזרחות ישראלית וגרמנית · עברית, אנגלית וגרמנית.',
 stats=[('10','+','שנות הובלה של עסקי אירוח בברלין',''),('200','','מקומות ישיבה במסעדת הדגל Yafo',''),('50','~','עובדים בשתי המסעדות','femtastics, 2020'),('4','','מותגי אירוח – שתי מסעדות ושני מלונות','')],
 sv_e='שירותים',sv_h='ארבעה מסלולים.<br>שותפה אחת לכל השלבים.',sv_p='למסעדות, לבתי מלון ולמתחמי אירוח. אפשר לבחור מסלול אחד או לשלב – ואפשר גם להעביר אליי את ניהול ה-F&amp;B כולו, במודל מיקור חוץ.',
 svc=[('הקמת עסק חדש','מסעדות · מלונות · קונספטים חדשים','מהרעיון ועד ערב הפתיחה – עם תוכנית שמחזיקה מים כבר מהיום הראשון.',['תוכנית עסקית, תקציב ותכנון פיננסי','קונספט, מיתוג וחוויית אורח','תכנון תפעולי, ספקים וסטנדרטים','גיוס והכשרת צוות פתיחה'],'אני רוצה להקים'),
  ('הבראת עסק','כשהמספרים לא מסתדרים','אבחון מהיר, החלטות ברורות והחזרת השליטה לידיים שלכם.',['בקרת P&amp;L ודוחות שבועיים','שליטה בעלות עבודה ובסידורי משמרות','שליטה בעלות מזון, הנדסת תפריט ורכש','תוכנית פעולה ל-90 הימים הראשונים'],'העסק שלי צריך סדר'),
  ('ליווי וניהול שוטף','מסעדות פעילות · F&amp;B במלונות','לעסק שעובד ורוצה לצמוח – או למלון שרוצה מערך F&amp;B מקצועי בלי לבנות אותו לבד.',['לוגיסטיקה ותפעול שוטף','אסטרטגיה, פיתוח עסקי ונוכחות ברשתות','Hosting וחוויית אירוח','סדנאות צוות והקמת מחלקות חדשות'],'לליווי שוטף'),
  ('אירועים','פרטיים · עסקיים · מחלקות אירועים','הפקה והובלה של אירועים, ובניית מחלקת אירועים רווחית בתוך עסק קיים.',['הפקה ותפעול מקצה לקצה','בניית מחלקת אירועים ותמחור','הכשרת צוות לאירועים גדולים'],'לתכנון אירוע')],
 bd_e='F&amp;B במיקור חוץ',bd_h='המלון שלכם. המסעדה – עליי.',
 bd_p='בתי מלון רבים יודעים לארח לילה, אבל לא תמיד לנהל מטבח, בר ולובי כעסק רווחי. ב-Selina ברלין הובלתי את כל מערך המזון והמשקאות לפי יעדי KPI ובמודל שותפות; ב-Amano הפכנו לובי מלון למסעדה של ממש. את אותו מודל אני מביאה למלונות בוטיק, מתחמי אירוח ומסעדות שרוצים תוצאה – לא עוד יועץ.',
 pts=[('מודל שותפות','תגמול שמחובר ליעדים'),('KPI ברורים','עלות מזון, עבודה והכנסה לאורח'),('צוות ותרבות','אירוח שמרגישים מהדלת'),('קונספט שמושך קהל','גם מבחוץ, לא רק אורחי המלון')],
 md_e='שיטת העבודה',md_h='תהליך ברור. בלי הפתעות.',steps=[('שיחת היכרות','מבינים איפה העסק נמצא, מה היעד ומה מפריע להגיע אליו.'),('אבחון','בחינה של התפעול, המספרים, הצוות והמותג – בשטח, לא רק בגיליון.'),('תוכנית','סדרי עדיפויות ברורים, יעדים מדידים ולוחות זמנים.'),('ליווי ביישום','עבודה צמודה בשטח, עד שהשינוי מחזיק גם בלעדיי.')],
 tl_e='ניסיון',tl_h='ארבעה מותגים.<br>עיר אחת שלא מוותרת לאף אחד.',
 tl=[('2015 – היום','Yafo','מסעדה ובר · ברלין','הקמה וניהול של מסעדה בת 200 מקומות ישיבה, עם אירועים שבועיים – מוסד ישראלי בברלין, תחילה במיטה (Mitte) והיום בקרויצברג.','logo-yafo.png'),
  ('2022 – 2023','Selina Berlin','מלון · F&amp;B מלא','הובלת כל מערך המזון והמשקאות במלון, לפי יעדי KPI ובמודל שותפות.','logo-selina.png'),
  ('2019 – 2021','Amano','מלון · קונספט לובי','הפיכת לובי מלון למסעדה של ממש ופיתוח המותג בתוכו.',''),
  ('2018 – 2022','Shishi','מסעדת שף · Farm to Table','מסעדת שף בעבודה ישירה מול חקלאים, עם חומרי גלם מספקים נבחרים בברנדנבורג.','logo-shishi.png')],
 pr_e='עיתונות',pr_h='מה כותבים עלינו בברלין.',
 q=['״Yafo היא אחת מארוחות הערב הכי כיפיות שאפשר לאכול בעיר.״','״…הביאה בלגן מבורך לפינה מכופתרת של העיר.״','על Shishi: ״…רמת שירות גבוהה שכל כך נדיר למצוא בברלין.״'],read='לכתבה',
 jr_e='המגזין',jr_h='מהמטבח ומהלובי.<br>תובנות מהשטח.',jr_p='מה שלמדתי בעשור של מסעדות ומלונות בברלין – כתוב לבעלי עסקים, למנהלי מלונות וליזמים.',
 ct_e='צרו קשר',ct_h='ספרו לי על הפרויקט שלכם.',ct_p='כמה פרטים על העסק ועל מה שאתם צריכים – ואחזור אליכם תוך 24 שעות לתיאום שיחת היכרות.',
 f=['שם מלא','שם העסק / המלון','טלפון / WhatsApp','אימייל','במה אפשר לעזור?','ספרו בכמה משפטים איפה העסק נמצא ומה היעד','שליחה','חוזרים אליכם תוך 24 שעות','תודה! קיבלתי את הפרטים ואחזור אליכם תוך 24 שעות.'],
 chips=['הקמת עסק חדש','הבראת עסק','ליווי שוטף','F&amp;B למלון','אירועים'],
 foot='© 2026 שני אחיאל · Hospitality &amp; F&amp;B Consulting · Berlin',foot2='ברלין · תל אביב',wa='דברו איתי בוואטסאפ',
 more='עוד מהמגזין',endE='רוצים לדבר על העסק שלכם?',endH='שיחת היכרות. בלי התחייבות.',back='חזרה לאתר',by='שני אחיאל',sending='שולח…',subj='פנייה חדשה מהאתר'),
'en':dict(dir='ltr',title='Shani Ahiel | Hospitality &amp; F&amp;B Consulting for Restaurants and Hotels',desc='Shani Ahiel founded Yafo and Shishi in Berlin and led the full F&amp;B operation at Selina Berlin. Openings, turnarounds and outsourced food &amp; beverage management for restaurants and hotels.',
 brand='Shani Ahiel',nav=['About','Services','Method','Track record','Press','Journal'],cta='Book a call',toggle=('עב','../'),
 eyebrow='From Jaffa to Berlin · Restaurants · Hotels · Events',h1a='Restaurants that work.',h1b='And make money.',
 lead='Advisory, openings and food &amp; beverage management for restaurants and hotels, from concept to bottom line. More than a decade building and running hospitality brands in Berlin, as owner and operator.',
 b1='Talk to us about your business',b2='Track record',
 heroband=[('Yafo','Restaurant &amp; bar · 200 seats'),('Selina Berlin','Full hotel F&amp;B'),('Amano','Hotel lobby turned restaurant'),('Shishi','Chef-led · farm to table')],
 ab_e='About',ab_h='Everything I advise on, I have built myself.',
 ab_p1='I started behind the bar and on the floor in Tel Aviv, moved into event management, and in Berlin built <b>Yafo</b> from the ground up: a 200-seat restaurant and bar that became one of the city’s best-known addresses for Israeli hospitality. Then came <b>Shishi</b>, a chef-led farm-to-table restaurant, and partnerships with hotels: turning the lobby at <b>Amano</b> into a true restaurant, and leading the entire food &amp; beverage operation at <b>Selina Berlin</b>.',
 ab_p2='Today I bring that experience to restaurant owners, founders and hotels: operating structure, cost control, teams that know how to host, and guest experiences people come back for. No theory – only what has been proven in front of real guests, every night.',
 ab_p3='B.A. in Communications &amp; Business Administration · Israeli and German citizen · Hebrew, English and German.',
 stats=[('10','+','years leading hospitality businesses in Berlin',''),('200','','seats at the Yafo flagship',''),('50','~','team members across two restaurants','femtastics, 2020'),('4','','hospitality brands – two restaurants, two hotels','')],
 sv_e='Services',sv_h='Four engagements.<br>One partner at every stage.',sv_p='For restaurants, hotels and hospitality venues. Choose a single engagement or combine them – or hand over your entire F&amp;B operation on an outsourced basis.',
 svc=[('New openings','Restaurants · hotels · new concepts','From first idea to opening night, with a plan that holds from day one.',['Business plan, budget and financial model','Concept, brand and guest experience','Operations design, suppliers and standards','Hiring and training the opening team'],'Plan an opening'),
  ('Turnarounds','When the numbers don’t add up','Rapid diagnosis, clear decisions, and control back in your hands.',['P&amp;L control and weekly reporting','Labour cost and rota discipline','Food cost, menu engineering and purchasing','A 90-day action plan'],'Fix my business'),
  ('Ongoing partnership','Operating restaurants · hotel F&amp;B','For businesses ready to grow – and hotels that want professional F&amp;B without building it alone.',['Logistics and day-to-day operations','Strategy, business development and social','Hosting and guest experience','Team workshops and new departments'],'Start a partnership'),
  ('Events','Private · corporate · events departments','Producing and leading events, and building a profitable events department inside an existing business.',['End-to-end production and operations','Events department set-up and pricing','Team training for large-scale events'],'Plan an event')],
 bd_e='Outsourced F&amp;B',bd_h='Your hotel. Your restaurant – run by us.',
 bd_p='Many hotels know how to sell a night’s stay, but not how to run a kitchen, bar and lobby as a profitable business. At Selina Berlin I led the entire food &amp; beverage operation against KPI targets in a partnership model; at Amano we turned a hotel lobby into a true restaurant. I bring the same model to boutique hotels, hospitality venues and restaurants that want results – not another consultant.',
 pts=[('Partnership model','Compensation tied to targets'),('Clear KPIs','Food cost, labour and spend per guest'),('Team &amp; culture','Hospitality you feel at the door'),('A concept that draws a crowd','Locals too, not just hotel guests')],
 md_e='Method',md_h='A clear process. No surprises.',steps=[('Introductory call','Where the business stands, where it needs to go, and what’s in the way.'),('Diagnosis','Operations, numbers, team and brand – on the floor, not just on a spreadsheet.'),('Plan','Clear priorities, measurable targets and timelines.'),('Implementation','Hands-on support on site, until the change holds without me.')],
 tl_e='Track record',tl_h='Four brands.<br>One city that forgives no one.',
 tl=[('2015 – today','Yafo','Restaurant &amp; bar · Berlin','Founded and runs a 200-seat restaurant with weekly events – an Israeli institution in Berlin, first in Mitte and now in Kreuzberg.','logo-yafo.png'),
  ('2022 – 2023','Selina Berlin','Hotel · full F&amp;B','Led the hotel’s entire food &amp; beverage operation against KPI targets, in a partnership model.','logo-selina.png'),
  ('2019 – 2021','Amano','Hotel · lobby concept','Turned a hotel lobby into a true restaurant and developed the brand within it.',''),
  ('2018 – 2022','Shishi','Chef-led · farm to table','A chef’s restaurant sourcing directly from farmers, with produce from selected Brandenburg suppliers.','logo-shishi.png')],
 pr_e='Press',pr_h='What Berlin says.',q=['','',''],read='Read',
 jr_e='Journal',jr_h='From the kitchen and the lobby.<br>Notes from the floor.',jr_p='What a decade of restaurants and hotels in Berlin has taught me – written for owners, hotel managers and founders.',
 ct_e='Contact',ct_h='Tell us about your project.',ct_p='Share a few details about your business and what you need – we’ll get back to you within 24 hours to arrange an introductory call.',
 f=['Full name','Business / hotel','Phone / WhatsApp','Email','How can we help?','In a few sentences: where is the business today, and where should it be?','Send','We reply within 24 hours','Thank you. We have your details and will be in touch within 24 hours.'],
 chips=['New opening','Turnaround','Ongoing partnership','Hotel F&amp;B','Events'],
 foot='© 2026 Shani Ahiel · Hospitality &amp; F&amp;B Consulting · Berlin',foot2='Berlin · Tel Aviv',wa='Chat on WhatsApp',
 more='More from the journal',endE='Want to talk about your business?',endH='An introductory call. No obligation.',back='Back to site',by='Shani Ahiel',sending='Sending…',subj='New website enquiry'),
}
QUOTES=[('“Yafo is one of the most fun dinners you can have in the city.”','The Infatuation','https://www.theinfatuation.com/berlin/reviews/yafo'),('“…brought a welcome spot of balagan to a buttoned-up corner of the city.”','The Berliner, 2023','https://www.the-berliner.com/food/berlins-hot-new-israeli-restaurants/'),('“…that high standard of service so rare to find in Berlin.”','Expats in Wonderland · on Shishi','https://www.expatsinwonderland.com/post/locally-sourced-israeli-food-shishi-kreuzberg')]
OUTLETS=[('femtastics','https://femtastics.com/business/shani-ahiel'),('Mit Vergnügen','https://mitvergnuegen.com/tipps/yafo-2/'),('Creme Guides','https://www.cremeguides.com/berlin/yafo/'),('urbanite','https://www.urbanite.net/berlin/artikel/yafo-crossover-mit-herz/'),('nomyblog / fizzz','https://www.nomyblog.de/nomyblog/gastronomie/shani-ahiel/'),('Mux Mäuschen Wild','https://www.muxmaeuschenwild.de/magazin/kreuzberg-mit-shishi/'),('visitBerlin','https://www.visitberlin.de/de/yafo')]
EN_BODIES={
'hotel-lobby-restaurant':"""<p class="dek">The lobby is the first thing a guest sees and the last thing a hotel thinks of as a business. At Amano we saw it could be far more: a restaurant with a name, an audience of its own, and a reason to come even if you’re not staying upstairs.</p>
<p>Most lobbies are designed around check-in: armchairs, acceptable coffee, perhaps a small bar that opens in the evening. They serve guests who are already in the building, but they don’t bring anyone in from the street. When we came to Amano in Berlin, the brief was the opposite: build a real restaurant, not a dining corner inside a hotel.</p>
<h2>1. Concept comes first</h2><p>A lobby restaurant only works when it has an identity that stands on its own – a menu, music, lighting and service people talk about to their friends. We didn’t “adapt” Yafo to the hotel. We brought its spirit – Israeli food, energy and warm hospitality – and let the hotel benefit from it.</p>
<blockquote>Guests don’t come to a lobby. They come to a place. The lobby just has to stop getting in the way.</blockquote>
<h2>2. Design the flow, not just the furniture</h2><ul><li>A clear separation between reception and seating, so diners never feel they’re eating in a corridor.</li><li>A bar visible from the entrance – it is the invitation to come in.</li><li>Lighting that shifts from morning to night, because the same room has to work as a café and as a restaurant.</li></ul>
<h2>3. A restaurant team, not a hotel team</h2><p>Front desk and restaurant service are two different professions, and the difference is felt in the first second: are you welcomed as a guest, or as a room number? Much of the work is building a team that understands hospitality, and agreeing clear lines with hotel management – who owns what, how event bookings flow, what happens at peak times.</p>
<h2>4. Measure it like a restaurant</h2><p>If the lobby is a business, measure it as one: revenue, food cost, labour cost, and how many diners come from outside the hotel. When those numbers are on the table every week, decisions about the menu, the rota and events become much easier.</p>
<h2>The bottom line</h2><p>A lobby that becomes a restaurant delivers two things: additional revenue for the hotel, and the reputation of a living place people want to be in. It doesn’t necessarily require a major renovation. It requires a concept, a team and a method.</p>""",
'fnb-outsourcing-hotels':"""<p class="dek">Hotels know how to sell rooms. Restaurants, bars and events are a different business entirely, with their own rhythm, people and risks. That is what outsourced food &amp; beverage is for.</p>
<p>At Selina Berlin I led the hotel’s entire F&amp;B operation against KPI targets, in a partnership model. It is the model I recommend to many boutique hotels: whoever runs the restaurant is a true partner in the outcome, not just another supplier.</p>
<h2>Signs it’s time</h2><ul><li>The restaurant is open, but rarely full of local guests.</li><li>Hotel managers spend more time on kitchen problems than on guests.</li><li>You have no clear weekly view of food cost and labour cost.</li><li>Event enquiries arrive, but there is no team that knows how to sell, price and produce them.</li></ul>
<h2>Why a partnership model</h2><p>When compensation is tied to agreed targets, everyone looks at the same numbers. The hotel gets a restaurant run like an independent business; the operator gets a real reason to succeed. What matters is defining the KPIs up front: what is measured, how often, and what happens when a number moves.</p>
<blockquote>Good outsourcing doesn’t take responsibility away from the hotel. It places it with someone who knows how to carry it.</blockquote>
<h2>What the agreement should cover</h2><ul><li>Clear targets: revenue, costs and guest satisfaction.</li><li>Ownership of team, purchasing, maintenance and events.</li><li>Full transparency: regular reporting and weekly working sessions.</li><li>A concept that serves the hotel’s brand and draws an outside crowd.</li></ul>
<h2>The bottom line</h2><p>If the restaurant in your hotel is an obligation rather than an asset, it is probably waiting for a different model. A short introductory call is enough to see whether outsourcing is right for you.</p>""",
'restaurant-turnaround':"""<p class="dek">One of the most frustrating situations in this industry: the room is full, guests are happy, and at the end of the month there is no money. The answer is almost always hiding in three numbers.</p>
<p>I built Yafo from scratch, and today it is a 200-seat restaurant and bar with weekly events. At that scale, a small difference in costs very quickly becomes a large difference at the bottom line. These are the numbers I look at first when I step into a business that needs a turnaround.</p>
<h2>1. Food cost</h2><p>Not just what the produce costs, but how much of it ends up in the bin, in generosity that was never priced, and in dishes that don’t earn their place on the menu. Menu engineering, costed recipes, weekly stock counts and disciplined purchasing are the foundation.</p>
<p>At Shishi we worked directly with farmers. When one of our regular suppliers was short of an ingredient, the dish simply came off the menu that week. That flexibility costs money if you don’t plan for it – and saves money when you do.</p>
<h2>2. Labour cost</h2><p>The largest line in most restaurants, and the first to slip out of control. I compare the rota against real demand by hour and day, look at how roles are split, and what the team does in quiet hours. The goal is not to cut people – it is to put the right people in the right hours.</p>
<blockquote>A great team is not a cost. An unplanned one is.</blockquote>
<h2>3. A weekly P&amp;L</h2><p>A P&amp;L that arrives once a quarter tells you what happened. A weekly one lets you change what will happen. A simple, consistent structure – revenue, food cost, labour, fixed costs – reviewed every week with management is the fastest way to regain control.</p>
<h2>What to do tomorrow morning</h2><ul><li>Re-cost your five best-selling dishes.</li><li>Compare last week’s rota against sales by hour.</li><li>Set a weekly numbers meeting – same day, same time.</li></ul><p>And if the numbers still don’t add up, that is exactly where a diagnosis begins.</p>"""}
HE_BODIES=json.load(open('/tmp/he_bodies.json'))
ARTS=[('hotel-lobby-restaurant','lobby',('מלונות','Hotels'),('איך הופכים לובי של מלון למסעדה של ממש','How to turn a hotel lobby into a real restaurant'),('לובי הוא הנכס הכי פחות מנוצל במלון. מה עשינו ב-Amano, ומה כל מלון יכול ליישם.','The lobby is a hotel’s most under-used asset. What we did at Amano – and what any hotel can apply.'),7),
 ('fnb-outsourcing-hotels','dining',('מיקור חוץ','Outsourcing'),('F&amp;B במיקור חוץ: מתי זה נכון למלון שלכם','Outsourced F&amp;B: when it’s right for your hotel'),('מודל שותפות, KPI ומי באמת אחראי על הצלחת המסעדה. לקחים מ-Selina ברלין.','Partnership models, KPIs, and who really owns the restaurant’s success. Lessons from Selina Berlin.'),6),
 ('restaurant-turnaround','cheers',('הבראה','Turnarounds'),('מסעדה מלאה, קופה ריקה: שלושת המספרים שמחזירים שליטה','Full room, empty till: the three numbers that restore control'),('עלות מזון, עלות עבודה ו-P&amp;L שבועי – למה מסעדות מצליחות מפסידות כסף, ואיך עוצרים את זה.','Food cost, labour cost and a weekly P&amp;L – why busy restaurants lose money, and how to stop it.'),8)]
def li(lang): return 0 if lang=='he' else 1
def nav(L,root,home,toggle_href):
    ids=['about','services','method','work','press','journal']
    items=''.join(f'<li><a href="{home}#{i}">{n}</a></li>' for i,n in zip(ids,L['nav']))
    return f'''<div class="progress"></div><nav class="nav"><div class="wrap"><a href="{home}" class="brand">{L['brand']}<small>Hospitality · F&amp;B · Berlin</small></a><ul>{items}</ul><div class="nav-r"><a class="lang" href="{toggle_href}" hreflang="{'en' if L['dir']=='rtl' else 'he'}">{L['toggle'][0]}</a><a href="{home}#contact" class="btn cta">{L['cta']}</a><button class="burger" aria-label="Menu">☰</button></div></div></nav>'''
def wa(L,lang): return f'<a class="wa" href="{WA+WAT[lang]}" target="_blank" rel="noopener" aria-label="WhatsApp">{SVG}<span class="t">{L["wa"]}</span></a>'
def foot(L,extra=''): return f'<footer><div class="wrap"><span>{L["foot"]}</span><span>{extra or L["foot2"]}</span></div></footer>'
def index(lang):
    L=T[lang]; root='' if lang=='he' else '../'; A=root+'assets/'; i=li(lang)
    path='' if lang=='he' else 'en/'; alt='en/' if lang=='he' else ''
    toggle='en/' if lang=='he' else '../'
    mq=''.join(f'<span>{x}</span><i>✦</i>' for x in ['Yafo','Selina Berlin','Amano','Shishi','Restaurants','Hotels','Events']*2)
    stats=''.join(f'<div class="stat r d{k}"><b data-count="{n}" data-pre="{s if s=="~" else ""}" data-suf="{s if s=="+" else ""}">{(s if s=="~" else "")+n+(s if s=="+" else "")}</b><span>{t}</span>'+(f'<small>{src}</small>' if src else '')+'</div>' for k,(n,s,t,src) in enumerate(L['stats']))
    svc=''.join(f'<article class="r d{k%2}"><span class="num">0{k+1}</span><h3>{h}</h3><div class="for">{f}</div><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+f'</ul><a href="#contact" class="more">{m}</a></article>' for k,(h,f,p,ul,m) in enumerate(L['svc']))
    pts=''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in L['pts'])
    steps=''.join(f'<div class="step"><b>0{k+1}</b><h3>{a}</h3><p>{b}</p></div>' for k,(a,b) in enumerate(L['steps']))
    tl=''.join(f'<div class="tl-row r"><div class="tl-n">0{k+1}</div><div class="yr">{y}</div><h3>{n}<small>{s}</small></h3><p>{d}</p>'+(f'<img class="logo" src="{A}{lg}" alt="{n}" loading="lazy">' if lg else f'<span class="logo-t">{n}</span>')+'</div>' for k,(y,n,s,d,lg) in enumerate(L['tl']))
    hb=''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in L['heroband'])
    quotes=''.join(f'<div class="q r d{k}"><blockquote>{qq}</blockquote>'+(f'<p class="he">{L["q"][k]}</p>' if L['q'][k] else '')+f'<cite>{src} <a href="{u}" target="_blank" rel="noopener">{L["read"]}</a></cite></div>' for k,(qq,src,u) in enumerate(QUOTES))
    outlets=''.join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n,u in OUTLETS)
    posts=''.join(f'<a class="post r d{k}" href="blog/{s}.html"><div class="ph"><img src="{A}{im}.webp" alt="" loading="lazy"><span class="tag">{tg[i]}</span></div><h3>{tt[i]}</h3><p>{ex[i]}</p><div class="meta">{mn} {"דק׳ קריאה" if lang=="he" else "min read"}</div></a>' for k,(s,im,tg,tt,ex,mn) in enumerate(ARTS))
    gal=''.join(f'<img src="{A}{g}.webp" alt="" loading="lazy">' for g in ['chandelier','courtyard-night','crowd','guests','moment','candle']*2)
    F=L['f']; chips=''.join(f'<label><input type="checkbox" name="service" value="{c}"><span>{c}</span></label>' for c in L['chips'])
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,L['title'],L['desc'],path,root,alt)}</head><body>
{nav(L,root,'./' if lang=='he' else './',toggle)}
<header class="hero"><div class="bg"></div><div class="hero-frame"></div><div class="wrap hero-in">
<span class="eyebrow r in">{L['eyebrow']}</span>
<h1><span class="line-reveal"><span>{L['h1a']}</span></span><span class="line-reveal"><span style="animation-delay:.15s"><em>{L['h1b']}</em></span></span></h1>
<p class="lead r in d2">{L['lead']}</p>
<div class="actions r in d3"><a href="#contact" class="btn solid">{L['b1']}</a><a href="#work" class="btn">{L['b2']}</a></div></div>
<div class="hero-band"><div class="wrap">{hb}</div></div></header>
<div class="marquee" aria-hidden="true"><div>{mq}</div></div>
<section id="about"><div class="wrap intro"><div class="img r"><img data-par src="{A}bar.webp" alt="Yafo Berlin" loading="lazy"></div><div>
<span class="eyebrow r">{L['ab_e']}</span><h2 class="r d1">{L['ab_h']}</h2><p class="r d1">{L['ab_p1']}</p><p class="r d2">{L['ab_p2']}</p><p class="r d2 creds">{L['ab_p3']}</p><div class="sig r d3">{L['by']}</div></div></div></section>
<div class="stats"><div class="wrap">{stats}</div></div>
<section id="services"><div class="wrap"><div class="svc-head"><div><span class="eyebrow r">{L['sv_e']}</span><h2 class="r d1">{L['sv_h']}</h2></div><p class="r d2">{L['sv_p']}</p></div><div class="svc">{svc}</div></div></section>
<section class="band"><div class="wrap"><div class="img r"><img src="{A}table.webp" alt="" loading="lazy"></div><div><span class="eyebrow r">{L['bd_e']}</span><h2 class="r d1">{L['bd_h']}</h2><p class="r d2">{L['bd_p']}</p><div class="pts r d3">{pts}</div></div></div></section>
<section id="method" class="method"><div class="wrap"><span class="eyebrow r">{L['md_e']}</span><h2 class="r d1">{L['md_h']}</h2><div class="steps">{steps}</div></div></section>
<section id="work" class="work"><div class="wrap"><span class="eyebrow r">{L['tl_e']}</span><h2 class="r d1">{L['tl_h']}</h2><div class="tl">{tl}</div></div></section>
<div class="gallery" aria-hidden="true"><div class="track">{gal}</div></div>
<section id="press" class="press"><div class="wrap"><span class="eyebrow r">{L['pr_e']}</span><h2 class="r d1">{L['pr_h']}</h2><div class="quotes">{quotes}</div><div class="outlets r">{outlets}</div></div></section>
<section id="journal"><div class="wrap"><div class="svc-head"><div><span class="eyebrow r">{L['jr_e']}</span><h2 class="r d1">{L['jr_h']}</h2></div><p class="r d2">{L['jr_p']}</p></div><div class="posts">{posts}</div></div></section>
<section id="contact" class="contact"><div class="wrap"><div class="side"><span class="eyebrow r">{L['ct_e']}</span><h2 class="r d1">{L['ct_h']}</h2><p class="r d2">{L['ct_p']}</p>
<div class="direct r d3"><a href="{WA+WAT[lang]}" target="_blank" rel="noopener"><span>WhatsApp</span><span class="arr">→</span></a><a href="mailto:Shanini.a@gmail.com"><span>Shanini.a@gmail.com</span><span class="arr">→</span></a><a href="tel:+972546644489"><span dir="ltr">054-6644489</span><span class="arr">→</span></a></div></div>
<form id="lead" class="r d2" data-sending="{L['sending']}" data-subj="{L['subj']}">
<div class="f"><input name="name" id="n" placeholder=" " required><label for="n">{F[0]}</label></div><div class="f"><input name="business" id="b" placeholder=" "><label for="b">{F[1]}</label></div>
<div class="f"><input name="phone" id="p" type="tel" placeholder=" " required><label for="p">{F[2]}</label></div><div class="f"><input name="email" id="e" type="email" placeholder=" " required><label for="e">{F[3]}</label></div>
<div class="chips"><p>{F[4]}</p>{chips}</div><div class="f full"><textarea name="message" id="m" placeholder=" "></textarea><label for="m">{F[5]}</label></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn solid" type="submit">{F[6]}</button><p class="promise">{F[7]}</p><p class="ok">{F[8]}</p></form></div></section>
{foot(L)}{wa(L,lang)}<script src="{root}main.js"></script></body></html>'''
def article(lang,k):
    L=T[lang]; i=li(lang); s,im,tg,tt,ex,mn=ARTS[k]
    root='../' if lang=='he' else '../../'; A=root+'assets/'
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html'; alt=('en/' if lang=='he' else '')+f'blog/{s}.html'
    body=(HE_BODIES if lang=='he' else EN_BODIES)[s]
    body=body.replace('<p>','<p class="r">').replace('<h2>','<h2 class="r">').replace('<blockquote>','<blockquote class="r">').replace('<ul>','<ul class="r">')
    others=''.join(f'<a href="{a[0]}.html">{a[3][i]} <span class="arr">→</span></a>' for a in ARTS if a[0]!=s)
    home='../' if lang=='he' else '../'
    toggle=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(lang,tt[i]+(' | שני אחיאל' if lang=='he' else ' | Shani Ahiel'),ex[i],path,root,alt,'article')}</head><body>
{nav(L,root,home,toggle)}
<header class="art-hero"><div class="bg" style="background-image:url({A}{im}.webp)"></div><div class="wrap"><span class="eyebrow">{tg[i]} · {L['jr_e']}</span><h1><span class="line-reveal"><span>{tt[i]}</span></span></h1><div class="meta">{L['by']} · {mn} {"דק׳ קריאה" if lang=="he" else "min read"}</div></div></header>
<article class="article">{body}<div class="src r"><span class="eyebrow">{L['more']}</span>{others}</div></article>
<div class="endcta"><span class="eyebrow">{L['endE']}</span><h2>{L['endH']}</h2><a class="btn solid" href="{home}#contact">{L['cta']}</a></div>
{foot(L,f'<a href="{home}">{L["back"]}</a>')}{wa(L,lang)}<script src="{root}main.js"></script></body></html>'''
os.makedirs('en/blog',exist_ok=True)
open('index.html','w').write(index('he')); open('en/index.html','w').write(index('en'))
for k,a in enumerate(ARTS):
    open(f'blog/{a[0]}.html','w').write(article('he',k)); open(f'en/blog/{a[0]}.html','w').write(article('en',k))
urls=['','en/']+[f'blog/{a[0]}.html' for a in ARTS]+[f'en/blog/{a[0]}.html' for a in ARTS]
open('sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE}{u}</loc></url>' for u in urls)+'</urlset>')
open('robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n')
print('built')
