import json
BASE="https://gitteromri-ux.github.io/shani-ahiel/v3/"
WAN="972546644489"
SVG='<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C9 3 3.3 8.6 3.3 15.6c0 2.5.7 4.8 1.9 6.8L3 29l6.8-2.1c1.9 1 4 1.6 6.2 1.6 7 0 12.7-5.6 12.7-12.6S23 3 16 3zm0 23.1c-2 0-3.9-.6-5.5-1.6l-.4-.2-4 1.2 1.3-3.9-.3-.4c-1.1-1.7-1.7-3.6-1.7-5.6C5.4 9.8 10.2 5.1 16 5.1s10.6 4.7 10.6 10.5S21.8 26.1 16 26.1zm5.8-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-.3-.2-1.3-.5-2.6-1.6-1-.9-1.6-1.9-1.8-2.2-.2-.3 0-.5.1-.7l.5-.6c.2-.2.2-.4.3-.6.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.5c.2.2 2.4 3.6 5.7 5 .8.3 1.4.5 1.9.7.8.3 1.5.2 2.1.1.6-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg>'
PRESS=[("The Infatuation","https://www.theinfatuation.com/berlin/reviews/yafo"),("The Berliner","https://www.the-berliner.com/food/berlins-hot-new-israeli-restaurants/"),("femtastics","https://femtastics.com/business/shani-ahiel"),("Mit Vergnügen","https://mitvergnuegen.com/tipps/yafo-2/"),("Creme Guides","https://www.cremeguides.com/berlin/yafo/"),("urbanite","https://www.urbanite.net/berlin/artikel/yafo-crossover-mit-herz/"),("nomyblog","https://www.nomyblog.de/nomyblog/gastronomie/shani-ahiel/"),("Expats in Wonderland","https://www.expatsinwonderland.com/post/locally-sourced-israeli-food-shishi-kreuzberg")]
ARTS=['hotel-lobby-restaurant','fnb-outsourcing-hotels','restaurant-turnaround']
IMG={'hotel-lobby-restaurant':'bar','fnb-outsourcing-hotels':'table','restaurant-turnaround':'dining'}
T={'he':dict(dir='rtl',title='שני אחיאל · ייעוץ, הקמה וניהול מזון ומשקאות למסעדות ולמלונות',desc='שני אחיאל מלווה מסעדות ומלונות בהקמה, בהבראה ובניהול שוטף של מערכי מזון ומשקאות, מתוך ניסיון של הקמה וניהול מסעדות בברלין.',
 brand='שני אחיאל',nav=[('about','אודות'),('services','שירותים'),('record','ניסיון'),('journal','מגזין'),('contact','יצירת קשר')],lang=('English','en/'),
 h1='שני אחיאל',lead='ייעוץ, הקמה וניהול של מערכי מזון ומשקאות <em>למסעדות ולמלונות</em>.',cta='לתיאום שיחת היכרות',
 press='כתבו על המסעדות שלי',
 ab_l='אודות',ab_h='<em>מתל אביב</em> לברלין.',
 ab=['התחלתי את דרכי בשירות ובבר בתל אביב, ומשם עברתי לניהול אירועים. בברלין הקמתי את Yafo, מסעדה ובר עם אירועים שבועיים, ואחריה את Shishi, מסעדת שף שעבדה ישירות מול חקלאים.',
     'בהמשך עבדתי עם מלונות: במלון Amano הפכנו את הלובי למסעדה של ממש, וב־Selina ברלין הובלתי את כל מערך המזון והמשקאות, לפי יעדים מדידים ובמודל שותפות.',
     'כל מה שאני מציעה ללקוחות עשיתי קודם בעצמי, כבעלים וכמנהלת. היום אני מלווה בעלי מסעדות, יזמים ומלונות שרוצים עסק שעובד, וגם מרוויח.'],
 facts='תואר ראשון בתקשורת ובמנהל עסקים · אזרחות ישראלית וגרמנית · עברית, אנגלית וגרמנית',
 sv_l='שירותים',sv_h='ארבע דרכים <em>לעבוד יחד</em>.',sv_p='אפשר לבחור מסלול אחד או לשלב כמה, לפי השלב שבו העסק נמצא.',
 svc=[('הקמת עסק חדש','מהרעיון ועד יום הפתיחה.',['תוכנית עסקית ותכנון','קונספט ומיתוג','סטנדרטים תפעוליים']),
      ('הבראת עסק','כשהמספרים לא מסתדרים, אני עוזרת להחזיר את השליטה.',['בקרת רווח והפסד','שליטה בעלות העבודה','שליטה בעלות המזון']),
      ('ליווי שוטף','למסעדה או למלון שרוצים לצמוח.',['לוגיסטיקה ותפעול שוטף','אסטרטגיה, פיתוח ורשתות חברתיות','חוויית אירוח','סדנאות לצוות והקמת מחלקות חדשות']),
      ('אירועים','הפקה והובלה של אירועים פרטיים ועסקיים.',['הפקה ותפעול','הקמת מחלקת אירועים והכשרת צוות'])],
 rc_l='ניסיון',rc_h='איפה <em>עבדתי</em>.',rc_p='מסעדות שהקמתי וניהלתי, ומלונות שאיתם עבדתי על מערך המזון והמשקאות.',
 rows=[('Yafo','מסעדה ובר · ברלין','הקמתי וניהלתי מסעדה ובר עם אירועים שבועיים, שנעשתה לכתובת מוכרת של אירוח ישראלי בעיר.'),
       ('Selina Berlin','מלון · ברלין','הובלתי את כל מערך המזון והמשקאות במלון, לפי יעדים מדידים ובמודל שותפות.'),
       ('Amano','מלון · ברלין','הפכנו את לובי המלון למסעדה של ממש, ופיתחנו בתוכו את המותג.'),
       ('Shishi','מסעדת שף · ברלין','ברוח ״מהחווה לשולחן״, עם חומרי גלם ישירות מחקלאים בברנדנבורג.')],
 md_l='תהליך העבודה',md_h='איך <em>זה עובד</em>.',
 steps=[('שיחת היכרות','אני לומדת איפה העסק נמצא ומה היעד.'),('אבחון','אני בוחנת את התפעול, המספרים, הצוות והמותג.'),('תוכנית','אני בונה סדרי עדיפויות ברורים, עם יעדים ולוחות זמנים.'),('ליווי ביישום','אני עובדת לצדכם בשטח, עד שהשינוי מחזיק.')],
 jr_l='מגזין',jr_h='מה <em>למדתי בדרך</em>.',jr_p='מחשבות על מסעדות ומלונות, מתוך העבודה בברלין.',
 arts={'hotel-lobby-restaurant':('מלונות','איך הופכים לובי של מלון למסעדה של ממש','מה למדתי במלון Amano, ומה כל מלון יכול ליישם.'),
       'fnb-outsourcing-hotels':('מיקור חוץ','מזון ומשקאות במיקור חוץ: מתי זה נכון למלון','מודל שותפות, יעדים מדידים, ומי אחראי בפועל להצלחה.'),
       'restaurant-turnaround':('הבראה','מסעדה מלאה, קופה ריקה','שלושה מספרים שמחזירים את השליטה בעסק.')},
 ct_l='יצירת קשר',ct_h='בואו נדבר על <em>העסק שלכם</em>.',ct_p='ספרו לי בכמה משפטים איפה העסק נמצא ומה אתם צריכים, ואחזור אליכם תוך 24 שעות.',
 fl=['שם מלא','שם העסק או המלון','טלפון','אימייל','במה אוכל לעזור?','כמה מילים על העסק','שליחה','תודה, קיבלתי. אחזור אליכם תוך 24 שעות.'],
 chips=['הקמת עסק חדש','הבראת עסק','ליווי שוטף','אירועים'],sending='שולחת…',subj='פנייה חדשה מהאתר',
 foot='© 2026 שני אחיאל · ייעוץ אירוח ומסעדנות · ברלין',wa='שליחת הודעה בוואטסאפ',wat='היי שני, הגעתי דרך האתר',
 by='שני אחיאל הקימה וניהלה את Yafo ו־Shishi בברלין, והובילה את מערך המזון והמשקאות של Selina ברלין.',read='לקריאה',more='עוד מהמגזין',back='לעמוד הבית',mins='דקות קריאה'),
'en':dict(dir='ltr',title='Shani Ahiel · Hospitality and F&amp;B consulting for restaurants and hotels',desc='Shani Ahiel advises restaurants and hotels on openings, turnarounds and ongoing food &amp; beverage operations, drawing on years of building and running restaurants in Berlin.',
 brand='Shani Ahiel',nav=[('about','About'),('services','Services'),('record','Experience'),('journal','Journal'),('contact','Contact')],lang=('עברית','../'),
 h1='Shani Ahiel',lead='Advisory, openings and food &amp; beverage management <em>for restaurants and hotels</em>.',cta='Book an introductory call',
 press='My restaurants have been featured in',
 ab_l='About',ab_h='From <em>Tel Aviv</em> to Berlin.',
 ab=['I started out on the floor and behind the bar in Tel Aviv, then moved into event management. In Berlin I founded Yafo, a restaurant and bar with weekly events, followed by Shishi, a chef-led restaurant that worked directly with farmers.',
     'I went on to work with hotels: at Amano we turned the lobby into a true restaurant, and at Selina Berlin I led the entire food &amp; beverage operation against measurable targets, in a partnership model.',
     'Everything I offer clients, I have done myself first, as an owner and operator. Today I work with restaurant owners, founders and hotels who want a business that works, and makes money.'],
 facts='B.A. in Communications and Business Administration · Israeli and German citizen · Hebrew, English and German',
 sv_l='Services',sv_h='Four ways <em>to work together</em>.',sv_p='Choose one engagement or combine several, depending on where the business is today.',
 svc=[('New openings','From first idea to opening day.',['Business plan and planning','Concept and branding','Operating standards']),
      ('Turnarounds','When the numbers don’t add up, I help you take back control.',['Profit and loss control','Labour cost control','Food cost control']),
      ('Ongoing support','For restaurants and hotels ready to grow.',['Logistics and day-to-day operations','Strategy, development and social media','Guest experience','Team workshops and new departments']),
      ('Events','Producing and leading private and corporate events.',['Production and operations','Building an events department and training the team'])],
 rc_l='Experience',rc_h='Where <em>I have worked</em>.',rc_p='Restaurants I founded and ran, and hotels I worked with on food &amp; beverage.',
 rows=[('Yafo','Restaurant &amp; bar · Berlin','Founded and ran a restaurant and bar with weekly events that became a well-known address for Israeli hospitality in the city.'),
       ('Selina Berlin','Hotel · Berlin','Led the hotel’s entire food &amp; beverage operation against measurable targets, in a partnership model.'),
       ('Amano','Hotel · Berlin','Turned the hotel lobby into a true restaurant and developed the brand within it.'),
       ('Shishi','Chef’s restaurant · Berlin','Farm to table, with produce sourced directly from Brandenburg farmers.')],
 md_l='Process',md_h='How <em>it works</em>.',
 steps=[('Introductory call','I learn where the business stands and where it needs to go.'),('Diagnosis','I review operations, numbers, team and brand.'),('Plan','I set clear priorities, with targets and timelines.'),('Implementation','I work alongside you on site until the change holds.')],
 jr_l='Journal',jr_h='What <em>I have learned</em>.',jr_p='Notes on restaurants and hotels, from my work in Berlin.',
 arts={'hotel-lobby-restaurant':('Hotels','How to turn a hotel lobby into a real restaurant','What I learned at Amano, and what any hotel can apply.'),
       'fnb-outsourcing-hotels':('Outsourcing','Outsourced food &amp; beverage: when it is right for a hotel','Partnership models, measurable targets, and who really owns the outcome.'),
       'restaurant-turnaround':('Turnarounds','Full room, empty till','Three numbers that put you back in control.')},
 ct_l='Contact',ct_h='Let’s talk about <em>your business</em>.',ct_p='Tell me in a few sentences where the business is today and what you need, and I will get back to you within 24 hours.',
 fl=['Full name','Business or hotel','Phone','Email','How can I help?','A few words about the business','Send','Thank you. I will be in touch within 24 hours.'],
 chips=['New opening','Turnaround','Ongoing support','Events'],sending='Sending…',subj='New website enquiry',
 foot='© 2026 Shani Ahiel · Hospitality consulting · Berlin',wa='Message on WhatsApp',wat='Hi Shani, I found you through your website',
 by='Shani Ahiel founded and ran Yafo and Shishi in Berlin, and led the food &amp; beverage operation at Selina Berlin.',read='Read',more='More from the journal',back='Back to home',mins='min read')}
BODY={'he':{
'hotel-lobby-restaurant':(6,"""<p class="dek">הלובי הוא המקום הראשון שאורח רואה, ולעיתים קרובות המקום האחרון שהמלון חושב עליו כעסק. במלון Amano ראיתי שהוא יכול להיות הרבה יותר: מסעדה עם שם, עם קהל משלה, ועם סיבה להגיע גם למי שלא ישן במלון.</p>
<p>רוב הלובים מתוכננים סביב הצ'ק־אין: כורסאות, קפה, ואולי בר קטן שנפתח בערב. הם משרתים את מי שכבר נמצא במלון, אבל לא מביאים אף אחד מהרחוב. ב־Amano המטרה הייתה הפוכה: מסעדה של ממש, ולא פינת אוכל בתוך מלון.</p>
<h2>הקונספט קודם לכול</h2><p>מסעדה בלובי מצליחה רק כשיש לה זהות משלה: תפריט, מוזיקה, תאורה ושירות שאנשים מספרים עליהם לחברים. לא התאמנו את Yafo למלון. הבאנו את הרוח שלה, את האוכל הישראלי, את האנרגיה ואת האירוח החם, והמלון נהנה מהם.</p>
<blockquote>אורחים לא באים ללובי. הם באים למקום.</blockquote>
<h2>לתכנן את התנועה, לא רק את הריהוט</h2><ul><li>הפרדה ברורה בין הקבלה לאזור הישיבה, כדי שסועדים לא ירגישו שהם יושבים במסדרון.</li><li>בר שנראה כבר מהכניסה, כי הוא ההזמנה להיכנס.</li><li>תאורה שמשתנה בין הבוקר לערב, כי אותו חלל צריך לעבוד גם כבית קפה וגם כמסעדה.</li></ul>
<h2>צוות של מסעדה, לא של מלון</h2><p>קבלה ושירות במסעדה הם שני מקצועות שונים, וההבדל מורגש מהשנייה הראשונה: האם מקבלים אותך כאורח או כמספר חדר. חלק גדול מהעבודה הוא בניית צוות שמבין אירוח, וחלוקת אחריות ברורה מול הנהלת המלון: מי אחראי על מה, איך מתנהלות הזמנות לאירועים, ומה קורה בשעות העומס.</p>
<h2>למדוד כמו מסעדה</h2><p>אם הלובי הוא עסק, צריך למדוד אותו כעסק: הכנסות, עלות מזון, עלות עבודה, וכמה מהסועדים מגיעים מחוץ למלון. כשהמספרים האלה מונחים על השולחן בכל שבוע, קל יותר להחליט על התפריט, על המשמרות ועל האירועים.</p>
<p>לובי שהופך למסעדה מביא למלון הכנסה נוספת ותדמית של מקום חי. זה לא תמיד דורש שיפוץ גדול. זה דורש קונספט, צוות ושיטה.</p>"""),
'fnb-outsourcing-hotels':(5,"""<p class="dek">מלון יודע למכור חדרים. מסעדה, בר ואירועים הם עסק אחר לגמרי, עם קצב, צוות וסיכונים משלהם. לשם כך קיים מיקור חוץ של מערך המזון והמשקאות.</p>
<p>ב־Selina ברלין הובלתי את כל מערך המזון והמשקאות של המלון, לפי יעדים מדידים ובמודל שותפות. זה המודל שאני ממליצה עליו ללא מעט מלונות: מי שמנהל את המסעדה הוא שותף אמיתי לתוצאה, ולא עוד ספק.</p>
<h2>הסימנים שהגיע הזמן</h2><ul><li>המסעדה פתוחה, אבל קהל מקומי כמעט לא מגיע אליה.</li><li>מנהלי המלון מבלים יותר זמן בבעיות של המטבח מאשר עם האורחים.</li><li>אין לכם תמונה שבועית ברורה של עלות המזון ועלות העבודה.</li><li>פניות לאירועים מגיעות, אבל אין מי שיודע למכור, לתמחר ולהפיק אותם.</li></ul>
<h2>למה מודל שותפות</h2><p>כשהתגמול קשור ליעדים מוסכמים, כולם מסתכלים על אותם מספרים. המלון מקבל מסעדה שמנוהלת כמו עסק עצמאי, והמפעיל מקבל סיבה אמיתית להצליח. החשוב ביותר הוא להגדיר מראש את המדדים: מה נמדד, באיזו תדירות, ומה עושים כשמספר זז.</p>
<blockquote>מיקור חוץ טוב לא מוריד מהמלון את האחריות. הוא מעביר אותה למי שיודע לשאת אותה.</blockquote>
<h2>מה צריך להיות בהסכם</h2><ul><li>יעדים ברורים: הכנסות, עלויות ושביעות רצון של אורחים.</li><li>חלוקת אחריות על הצוות, הרכש, התחזוקה והאירועים.</li><li>שקיפות מלאה: דוחות קבועים ופגישות עבודה שבועיות.</li><li>קונספט שמתאים למותג של המלון ומושך גם קהל מבחוץ.</li></ul>
<p>אם המסעדה במלון היא חובה ולא נכס, ייתכן שהיא מחכה למודל אחר. שיחת היכרות קצרה מספיקה כדי לבדוק אם מיקור חוץ מתאים לכם.</p>"""),
'restaurant-turnaround':(6,"""<p class="dek">אחד המצבים המתסכלים ביותר בענף: המקום מלא, האורחים מרוצים, ובסוף החודש אין כסף. כמעט תמיד התשובה מסתתרת בשלושה מספרים.</p>
<p>הקמתי וניהלתי את Yafo, מסעדה ובר עם אירועים שבועיים. בעסק כזה, הבדל קטן בעלויות הופך מהר מאוד להבדל גדול בשורה התחתונה. אלה המספרים שאני בודקת ראשונים כשאני נכנסת לעסק שצריך הבראה.</p>
<h2>עלות המזון</h2><p>לא רק כמה עולה הסחורה, אלא כמה ממנה הולך לפח, לנדיבות שלא תומחרה ולמנות שלא מצדיקות את מקומן בתפריט. תמחור מתכונים, ספירות מלאי קבועות ורכש מסודר הם הבסיס.</p>
<p>ב־Shishi עבדנו ישירות מול חקלאים. כשלאחד הספקים חסר חומר גלם, המנה פשוט ירדה מהתפריט באותו שבוע. הגמישות הזאת עולה כסף כשלא מתכננים אותה, וחוסכת כסף כשמתכננים.</p>
<h2>עלות העבודה</h2><p>ברוב המסעדות זה הסעיף הגדול ביותר, והראשון שיוצא משליטה. אני משווה את סידור המשמרות לעומס האמיתי לפי שעות וימים, ובודקת את חלוקת התפקידים ואת מה שהצוות עושה בשעות השקטות. המטרה איננה לקצץ באנשים, אלא להציב את האנשים הנכונים בשעות הנכונות.</p>
<blockquote>צוות טוב הוא לא הוצאה. צוות שלא תוכנן, כן.</blockquote>
<h2>דוח רווח והפסד שבועי</h2><p>דוח שמגיע פעם ברבעון מספר לכם מה קרה. דוח שבועי מאפשר לשנות את מה שיקרה. מבנה פשוט וקבוע (הכנסות, עלות מזון, עלות עבודה והוצאות קבועות) שנבדק בכל שבוע עם ההנהלה הוא הדרך המהירה ביותר להחזיר את השליטה.</p>
<h2>מה עושים מחר בבוקר</h2><ul><li>מתמחרים מחדש את חמש המנות הנמכרות ביותר.</li><li>משווים את סידור המשמרות של השבוע שעבר למכירות לפי שעה.</li><li>קובעים פגישת מספרים שבועית, באותו יום ובאותה שעה.</li></ul>
<p>ואם המספרים עדיין לא מסתדרים, זו בדיוק נקודת ההתחלה של אבחון.</p>""")},
'en':{
'hotel-lobby-restaurant':(6,"""<p class="dek">The lobby is the first thing a guest sees, and often the last thing a hotel thinks of as a business. At Amano I saw it could be far more: a restaurant with a name, an audience of its own, and a reason to come even if you are not staying upstairs.</p>
<p>Most lobbies are planned around check-in: armchairs, coffee, perhaps a small bar that opens in the evening. They serve people already in the building, but bring no one in from the street. At Amano the goal was the opposite: a real restaurant, not a dining corner inside a hotel.</p>
<h2>Concept comes first</h2><p>A lobby restaurant only works when it has an identity of its own: a menu, music, lighting and service people tell their friends about. We did not adapt Yafo to the hotel. We brought its spirit, the Israeli food, the energy and the warm hospitality, and the hotel benefited.</p>
<blockquote>Guests don’t come to a lobby. They come to a place.</blockquote>
<h2>Design the flow, not just the furniture</h2><ul><li>A clear separation between reception and seating, so diners never feel they are eating in a corridor.</li><li>A bar you can see from the entrance, because it is the invitation to come in.</li><li>Lighting that shifts from morning to evening, because the same room must work as a café and as a restaurant.</li></ul>
<h2>A restaurant team, not a hotel team</h2><p>Reception and restaurant service are two different professions, and the difference is felt in the first second: are you welcomed as a guest or as a room number? Much of the work is building a team that understands hospitality, and agreeing clear responsibilities with hotel management: who owns what, how event bookings work, what happens at peak times.</p>
<h2>Measure it like a restaurant</h2><p>If the lobby is a business, measure it as one: revenue, food cost, labour cost, and how many diners come from outside the hotel. When those numbers are on the table every week, decisions about the menu, the rota and events become much easier.</p>
<p>A lobby that becomes a restaurant brings the hotel additional revenue and the reputation of a living place. It does not always require a major renovation. It requires a concept, a team and a method.</p>"""),
'fnb-outsourcing-hotels':(5,"""<p class="dek">Hotels know how to sell rooms. Restaurants, bars and events are a different business, with their own rhythm, people and risks. That is what outsourced food &amp; beverage is for.</p>
<p>At Selina Berlin I led the hotel’s entire food &amp; beverage operation against measurable targets, in a partnership model. It is the model I recommend to many hotels: whoever runs the restaurant is a true partner in the outcome, not just another supplier.</p>
<h2>Signs it is time</h2><ul><li>The restaurant is open, but local guests rarely come.</li><li>Hotel managers spend more time on kitchen problems than with guests.</li><li>You have no clear weekly view of food cost and labour cost.</li><li>Event enquiries arrive, but no one knows how to sell, price and produce them.</li></ul>
<h2>Why a partnership model</h2><p>When compensation is tied to agreed targets, everyone looks at the same numbers. The hotel gets a restaurant run like an independent business; the operator gets a real reason to succeed. What matters most is defining the measures up front: what is measured, how often, and what happens when a number moves.</p>
<blockquote>Good outsourcing does not take responsibility away from the hotel. It gives it to someone who knows how to carry it.</blockquote>
<h2>What the agreement should cover</h2><ul><li>Clear targets: revenue, costs and guest satisfaction.</li><li>Ownership of team, purchasing, maintenance and events.</li><li>Full transparency: regular reporting and weekly working sessions.</li><li>A concept that fits the hotel’s brand and draws an outside crowd.</li></ul>
<p>If the restaurant in your hotel is an obligation rather than an asset, it may be waiting for a different model. A short introductory call is enough to see whether outsourcing is right for you.</p>"""),
'restaurant-turnaround':(6,"""<p class="dek">One of the most frustrating situations in this industry: the room is full, guests are happy, and at the end of the month there is no money. The answer is almost always hiding in three numbers.</p>
<p>I founded and ran Yafo, a restaurant and bar with weekly events. In a business like that, a small difference in costs quickly becomes a large difference at the bottom line. These are the numbers I look at first when I step into a business that needs a turnaround.</p>
<h2>Food cost</h2><p>Not just what the produce costs, but how much ends up in the bin, in generosity that was never priced, and in dishes that do not earn their place on the menu. Costed recipes, regular stock counts and disciplined purchasing are the foundation.</p>
<p>At Shishi we worked directly with farmers. When a supplier was short of an ingredient, the dish simply came off the menu that week. That flexibility costs money if you do not plan for it, and saves money when you do.</p>
<h2>Labour cost</h2><p>In most restaurants this is the largest line, and the first to slip. I compare the rota against real demand by hour and day, and look at how roles are split and what the team does in quiet hours. The goal is not to cut people, but to put the right people in the right hours.</p>
<blockquote>A great team is not a cost. An unplanned one is.</blockquote>
<h2>A weekly profit and loss</h2><p>A report that arrives once a quarter tells you what happened. A weekly one lets you change what will happen. A simple, consistent structure (revenue, food cost, labour and fixed costs) reviewed every week with management, is the fastest way to regain control.</p>
<h2>What to do tomorrow morning</h2><ul><li>Re-cost your five best-selling dishes.</li><li>Compare last week’s rota with sales by hour.</li><li>Set a weekly numbers meeting, same day, same time.</li></ul>
<p>And if the numbers still do not add up, that is exactly where a diagnosis begins.</p>""")}}
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@400;500&family=Heebo:wght@400;500&display=swap" rel="stylesheet">'
def head(L,lang,title,desc,path,alt,root):
    sch={"@context":"https://schema.org","@type":"ProfessionalService","name":"Shani Ahiel","url":BASE,"image":BASE+"img/og.jpg","email":"Shanini.a@gmail.com","telephone":"+"+WAN,"areaServed":["Berlin","Germany","Israel"],"knowsLanguage":["he","en","de"],"founder":{"@type":"Person","name":"Shani Ahiel"}}
    he,en=(path,alt) if lang=='he' else (alt,path)
    return f'''<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>{title}</title><meta name="description" content="{desc}">
<link rel="alternate" hreflang="he" href="{BASE}{he}"><link rel="alternate" hreflang="en" href="{BASE}{en}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}img/og.jpg"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}../favicon.svg" type="image/svg+xml">{FONTS}<script type="application/ld+json">{json.dumps(sch)}</script><link rel="stylesheet" href="{root}v3.css">'''
def nav(L,home,langhref):
    return f'<nav class="nav"><div class="w"><a class="brand" href="{home}">{L["brand"]}</a><ul>'+''.join(f'<li><a href="{home}#{i}">{n}</a></li>' for i,n in L['nav'])+f'</ul><div class="r"><a class="lang" href="{langhref}">{L["lang"][0]}</a></div></div></nav>'
def wa(L): 
    import urllib.parse
    return f'<a class="wa" href="https://wa.me/{WAN}?text={urllib.parse.quote(L["wat"])}" target="_blank" rel="noopener" aria-label="{L["wa"]}" title="{L["wa"]}">{SVG}</a>'
def card(L,s,root,href):
    t,h,p=L['arts'][s]
    return f'<a class="card fu" href="{href}"><div class="ph"><img src="{root}img/{IMG[s]}.webp" alt="" loading="lazy"></div><span class="t">{t}</span><h3>{h}</h3><p>{p}</p></a>'
def index(lang):
    L=T[lang]; root='' if lang=='he' else '../'; path='' if lang=='he' else 'en/'; alt='en/' if lang=='he' else ''
    svc=''.join(f'<article class="fu"><span class="n">0{k+1}</span><h3>{h}</h3><p>{p}</p><ul>'+''.join(f'<li>{x}</li>' for x in ul)+'</ul></article>' for k,(h,p,ul) in enumerate(L['svc']))
    rows=''.join(f'<div class="row fu"><h3>{n}</h3><span class="t">{t}</span><p>{d}</p></div>' for n,t,d in L['rows'])
    steps=''.join(f'<div class="fu"><span class="n">0{k+1}</span><h3>{a}</h3><p>{b}</p></div>' for k,(a,b) in enumerate(L['steps']))
    cards=''.join(card(L,s,root,f'blog/{s}.html') for s in ARTS)
    press=''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{n}</a></li>' for n,u in PRESS)
    F=L['fl']; chips=''.join(f'<label><input type="checkbox" name="service" value="{c}"><span>{c}</span></label>' for c in L['chips'])
    import urllib.parse
    waurl=f'https://wa.me/{WAN}?text={urllib.parse.quote(L["wat"])}'
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(L,lang,L['title'],L['desc'],path,alt,root)}</head><body>
{nav(L,'./',L['lang'][1])}
<header class="hero"><div class="w"><div><h1>{L['h1']}</h1><p>{L['lead']}</p><a class="btn" href="#contact">{L['cta']}</a></div><div class="ph"><img src="{root}img/portrait.webp" alt="{L['brand']}" fetchpriority="high" width="800" height="1000"></div></div></header>
<section class="press"><div class="w"><span class="label">{L['press']}</span><ul>{press}</ul></div></section>
<section id="about" class="about"><div class="w"><div class="fu"><span class="label">{L['ab_l']}</span><h2>{L['ab_h']}</h2><div class="ph"><img src="{root}img/kitchen.webp" alt="" loading="lazy"></div></div><div class="fu">{''.join(f'<p>{x}</p>' for x in L['ab'])}<p class="facts">{L['facts']}</p></div></div></section>
<section id="services"><div class="w"><div class="head fu"><span class="label">{L['sv_l']}</span><h2>{L['sv_h']}</h2><p>{L['sv_p']}</p></div><div class="svc">{svc}</div></div></section>
<section id="record" class="record"><div class="w"><div class="head fu"><span class="label">{L['rc_l']}</span><h2>{L['rc_h']}</h2><p>{L['rc_p']}</p></div><div class="ph fu"><img src="{root}img/feast.webp" alt="" loading="lazy"></div><div class="rows">{rows}</div></div></section>
<section id="method"><div class="w"><div class="head fu"><span class="label">{L['md_l']}</span><h2>{L['md_h']}</h2></div><div class="steps">{steps}</div></div></section>
<section id="journal"><div class="w"><div class="head fu"><span class="label">{L['jr_l']}</span><h2>{L['jr_h']}</h2><p>{L['jr_p']}</p></div><div class="cards">{cards}</div></div></section>
<section id="contact" class="contact"><div class="w"><div><span class="label">{L['ct_l']}</span><h2>{L['ct_h']}</h2><p>{L['ct_p']}</p><div class="direct"><a href="{waurl}" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:Shanini.a@gmail.com">Shanini.a@gmail.com</a><a href="tel:+{WAN}" dir="ltr" style="text-align:{'right' if lang=='he' else 'left'}">054-664-4489</a></div></div>
<form id="lead" data-sending="{L['sending']}" data-subj="{L['subj']}"><div class="f"><label for="n">{F[0]}</label><input id="n" name="name" required autocomplete="name"></div><div class="f"><label for="b">{F[1]}</label><input id="b" name="business" autocomplete="organization"></div>
<div class="f"><label for="p">{F[2]}</label><input id="p" name="phone" type="tel" required autocomplete="tel"></div><div class="f"><label for="e">{F[3]}</label><input id="e" name="email" type="email" required autocomplete="email"></div>
<fieldset class="chips"><legend>{F[4]}</legend>{chips}</fieldset><div class="f full"><label for="m">{F[5]}</label><textarea id="m" name="message"></textarea></div>
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off"><button class="btn" type="submit">{F[6]}</button><p class="ok">{F[7]}</p></form></div></section>
<footer><div class="w"><span>{L['foot']}</span><a href="mailto:Shanini.a@gmail.com">Shanini.a@gmail.com</a></div></footer>
{wa(L)}<script src="{root}v3.js"></script></body></html>'''
def article(lang,s):
    L=T[lang]; root='../' if lang=='he' else '../../'; t,h,p=L['arts'][s]; mins,body=BODY[lang][s]
    path=('' if lang=='he' else 'en/')+f'blog/{s}.html'; alt=('en/' if lang=='he' else '')+f'blog/{s}.html'
    langhref=('../en/blog/' if lang=='he' else '../../blog/')+f'{s}.html'
    others=''.join(card(L,o,root,f'{o}.html') for o in ARTS if o!=s)
    return f'''<!doctype html><html lang="{lang}" dir="{L['dir']}"><head>{head(L,lang,h+' · '+L['brand'],p,path,alt,root)}</head><body>
{nav(L,'../',langhref)}
<header class="ahead"><div class="w"><span class="label">{t}</span><h1>{h}</h1><p class="meta">{L['brand']} · {mins} {L['mins']}</p></div></header>
<div class="aph"><img src="{root}img/{IMG[s]}.webp" alt="" fetchpriority="high"></div>
<article class="prose">{body}<div class="byline"><img src="{root}img/portrait.webp" alt="" loading="lazy"><p>{L['by']}</p></div></article>
<section class="more"><div class="w"><div class="head"><span class="label">{L['more']}</span></div><div class="cards">{others}</div><p style="text-align:center;margin-top:3rem"><a class="link" href="../">{L['back']}</a></p></div></section>
<footer><div class="w"><span>{L['foot']}</span><a href="mailto:Shanini.a@gmail.com">Shanini.a@gmail.com</a></div></footer>
{wa(L)}<script src="{root}v3.js"></script></body></html>'''
open('index.html','w').write(index('he')); open('en/index.html','w').write(index('en'))
for s in ARTS:
    open(f'blog/{s}.html','w').write(article('he',s)); open(f'en/blog/{s}.html','w').write(article('en',s))
print('ok')
