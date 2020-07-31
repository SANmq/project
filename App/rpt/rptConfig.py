"""
@date:2020-07-27
@time：15:51
@author:smq
@description:描述
"""

FOW_GOOD_ID = {"605635862044": "Pro眼霜",
               "608307748293": "A醇",
               "35399645973": "冰川套装",
               "526250011782": "30g美白防晒",
               "593810916668": "薇娅安瓶",
               "521952626778": "紧致礼盒",
               "535575862926": "雪润气垫",
               "544864793945": "人鱼膜法-21片",
               "591792639412": "水光白修护礼盒",
               "16541174270": "冰川美容液",
               "21176872955": "冰川补水霜",
               "520987824839": "海泉精华水",
               "544842582800": "修颜隔离乳",
               "36442399390": "冰川洁面乳",
               "37874885829": "海泉套装",
               "41681863329": "补水面膜"
               }

GOOD_DICT = {
    "35399645973": "冰川套装",
    "37874885829": "海泉套装",
    "526250011782": "30g美白防晒",
    "539161789130": "小蓝盒",
    "41681863329": "补水面膜",
    "593810916668": "薇娅安瓶",
    "544842582800": "修颜隔离乳",
    "535575862926": "雪润气垫",
    "36442399390": "冰川洁面乳",
    "21176872955": "冰川补水霜",
    "16541174270": "冰川美容液",
    "544864793945": "人鱼膜法-21片",
    "521952626778": "紧致礼盒",
    "537322993074": "海泉去角质",
    "548383141347": "海洋修护套装",
    "532992590037": "卸妆水",
    "16722770075": "冰川洁面泡泡",
    "18002979744": "60gBB",
    "19587239290": "冰川精华乳",
    "21456192773": "冰川睡眠面膜",
    "21456512549": "冰川眼部精华",
    "27082252283": "雪颜萃护肤礼盒",
    "520985013382": "海泉精华乳",
    "520987824839": "海泉精华水",
    "520987964067": "海泉深洁面乳",
    "521515760655": "海泉精华霜",
    "522992929706": "海泉肌源精华液",
    "525166676360": "海泉精华原液",
    "533342384055": "舒缓喷雾",
    "537211579955": "玫瑰精油",
    "538332227810": "海泉素颜霜",
    "538774066371": "补水面膜10片-美白",
    "549438013916": "卸妆膏",
    "553694604410": "遮瑕液",
    "558640518253": "海洋精华油",
    "559005882880": "幻彩修颜液",
    "561504870112": "护手霜",
    "564106965755": "手工皂礼盒",
    "569402067619": "唇釉（软萌珊瑚色333）",
    "569492923444": "唇膏（初恋樱花粉521）",
    "570464992377": "海洋啫喱",
    "570691494404": "海洋细肤水",
    "570782975898": "海洋乳",
    "573803689227": "海洋霜",
    "576112411178": "雪颜萃洗颜乳",
    "576768666754": "手霜（小仙女）",
    "576978819773": "眉笔（咖色）",
    "577554516697": "唇膏（倾心斩男色520）",
    "577724001494": "15g隔离乳",
    "579305661790": "水水兔小魔盒",
    "581397404360": "5g蜜粉",
    "582030628228": "唇膏（幸运西柚色666）",
    "582173762231": "补水面膜10片-保湿",
    "588798152107": "30g睡眠面膜",
    "590386672591": "水密码粉底液",
    "590941627629": "40g水感防晒",
    "591792639412": "水光白修护礼盒",
    "558833730254": "口红套装",
    "540014841873": "眼霜套装",
    "576385153585": "补水面膜-18年",
    "554676071044": "人鱼膜法-黑包装",
    "549336188357": "芦荟胶",
    "558089377977": "去黑头套装",
    "540662661594": "定制礼盒",
    "529114983965": "手工皂套装",
    "578369804032": "精华礼盒",
    "564843243408": "海泉套装-18年",
    "586147152260": "初恋防晒",
    "590767182825": "美白防晒",
    "520987786632": "海泉眼部精华",
    "523218657223": "护手霜-18年",
    "527380692554": "海泉睡眠面膜",
    "540103983861": "补水护眼贴",
    "540462740999": "睡眠护眼罩",
    "543548275968": "润唇膏",
    "564577572250": "爽肤水",
    "558456296895": "人鱼膜法",
    "565191801603": "防晒喷雾",
    "522171872651": "美白套装",
    "565191709581": "人鱼膜法会员",
    "539206144147": "眼霜套装-旧",
    "559372345626": "海泉精华面膜",
    "570465608888": "海洋源萃修护面霜",
    "545085414101": "人鱼膜法黑珍珠",
    "570100092757": "补水面膜+海泉水",
    "576561183177": "水兔兔气垫CC",
    "576611251472": "精华套装",
    "577566735373": "补水面膜-旧",
    "578675111834": "人鱼膜法黑面膜24片",
    "522854334411": "雪颜萃护肤礼盒-旧",
    "541179002996": "冰川套装-旧",
    "560760005805": "海泉套装-旧",
    "579602805204": "海泉精华水-旧",
    "549407138891": "海洋套装",
    "577954351159": "护手霜-赠品1",
    "579603777196": "护手霜-赠品2",
    "581094205551": "眉笔",
    "583653420966": "气垫隔离霜",
    "593184901401": "安瓶-预售",
    "591760896442": "海泉套装-预售",
    "591835368039": "紧致套装-预售",
    "591837020238": "海洋套装-预售",
    "593272406062": "水光白套装-预售",
    "593654078048": "粉底液礼盒装-预售",
    "592770687720": "小蓝盒-预售",
    "558707516225": "口红礼盒-预售",
    "592393151137": "人鱼膜法-预售",
    "522855761030": "冰川套装-预售",
    "593259944322": "安瓶-现货",
    "567655218013": "气垫CC霜",
    "561125811760": "黑珍珠面膜",
    "593855902799": "安瓶预售298",
    "595588644137": "补水面膜预售",
    "594755942226": "安瓶预售买一送一",
    "594083639461": "水光白套装预售",
    "593703864309": "粉底液礼盒装",
    "540468755472": "冰川套装-洁水霜",
    "594760374168": "安瓶+瘦脸仪",
    "593470944138": "冰川洁面",
    "593655178095": "人鱼面膜",
    "594758250904": "水感防晒",
    "35467290492": "冰川爽肤水",
    "595997774692": "隔离乳",
    "595644032700": "雪润气垫CC",
    "594117895940": "水光白套装洁水乳",
    "594763714506": "安瓶+CC",
    "540468221635": "素颜霜",
    "593736329890": "粉底液礼盒",
    "594364908601": "安瓶+细肤水",
    "558708991696": "紧致套装",
    "595592188514": "蜜粉",
    "594930371088": "安瓶+细肤水预售",
    "596178847946": "小蓝盒+隔离乳",
    "16721946840": "补水霜+芦荟胶",
    "594357220581": "安瓶+小蓝盒气垫",
    "594759858085": "素颜霜+补水霜",
    "593960035725": "水光白套装",
    "542987467416": "眼部精华套装",
    "599328766226": "彩妆3件套",
    "599789281792": "粉漾初色美唇膏口红",
    "600044464814": "身体乳",
    "600596281269": "美容护肤/美体/精油",
    "600887528241": "去角质",
    "600886100909": "洁面泡泡",
    "601892951038": "安瓶",
    "602881996966": "补水面膜1",
    "604155359746": "唇釉",
    "604007706553": "身体乳1",
    "604219479534": "海洋水",
    "604111313178": "Pro眼霜",
    "604537691910": "Pro眼霜1",
    "604600747122": "唇釉1",
    "603967080883": "身体乳2",
    "605635862044": "Pro眼霜2",
    "605634966742": "安瓶熬夜",
    "605278453711": "Pro眼霜3",
    "608762763292": "水光白洁面乳",
    "607930224948": "水光白眼霜",
    "608372490646": "水光白面霜",
    "608590971854": "水光白精华乳",
    "608582051608": "水光白精华水",
    "608104281310": "水光白精华液",
    "607392396447": "新品口红",
    "608097559100": "九色眼影",
    "608307748293": "A醇",
    "608909954916": "海泉魔道套装",
    "610771668482": "A醇",
    "611039917781": "自组套装",
    "611952953361": "自组套装",
    "612025977239": "消毒液",
    "612031909880": "洗手液",
    "612691207945": "九色眼影",
    "612206481130": "口红",
    "612293497174": "去角质慕斯",
    "613189495583": "人鱼面膜3",
    "614043689262": "Pro眼霜",
    "613770708691": "海泉套装",
    "616094115434": "Pro眼霜",
    "615846154514": "防晒霜",
    "616095579437": "补水面膜",
    "616298930706": "A醇",
    "615917092535": "去角质慕斯",
    "616460002187": "冰川套装",
    "616133888136": "眼霜",
    "616960258868": "眼影",
    "617215291590": "新品口红",
    "616725125197": "去角质慕斯",
    "616727321155": "身体乳",
    "617239099749": "A醇",
    "617111158192": "蜜粉",
    "617119894443": "遮瑕液",
    "16726077266": "去角质啫喱",
    "617543101299": "睡眠面膜",
    "617545465564": "气垫CC霜",
    "617803806820": "BB霜",
    "617930442487": "防晒",
    "617952262575": "自组套装",
    "617455976336": "素颜霜",
    "617455956896": "隔离乳",
    "617527892410": "补水面膜",
    "617968873863": "安瓶",
    "617925660154": "自组套装",
    "617931668714": "自组套装",
    "618243689500": "海泉面霜",
    "618245265128": "隔离乳",
    "618505222861": "洁肤晶露",
    "618766015905": "水盈清透三件套",
    "618507770019": "消毒液",
    "618249869192": "面膜",
    "618772631048": "自组套装",
    "618644430422": "气垫CC霜",
    "618337100000": "Pro眼霜",
    "618835458904": "Pro眼霜",
    "619119667814": "青春套盒",
    "618367356310": "安瓶",
    "619189303253": "面膜",
    "618692308747": "眼霜+A醇",
    "620007423495": "乳糖酸原液",
    "619964626097": "轻奢礼盒",
    "620268771934": "烟酰胺面膜",
    "619439216712": "金盏花面膜",
    "620292658225": "清平乐礼盒",
    "620292894603": "宝可梦面膜",
    "619952040874": "福袋",
    "621015186993": "安瓶",
    "621016882971": "紧致眼霜",
    "620841433469": "胶囊面膜",
    "620858865627": "A醇",
    "620859949041": "Pro眼霜",
    "620560080487": "冰川套装",
    "620560440973": "胶囊面膜",
    "621402351600": "防晒喷雾",
    "621136118314": "粉底液",
    "620862717673": "洁面泡泡",
    "621136586901": "紧致套装",
    "620563524477": "海泉精华霜",
    "620864085078": "安瓶",
    "621405335104": "清平乐礼盒",
    "621405275114": "海泉套装",
    "620564044642": "口红",
    "621137778523": "美白套装",
    "621405059724": "眼影",
    "620864701107": "新款身体乳",
    "621405351400": "防晒喷雾",
    "620564300572": "清平乐面膜",
    "621405775101": "散粉",
    "620564612673": "水光瓶",
    "621901539676": "宝可梦眼霜",
    "621734493943": "樱花洁面",
    "621511432069": "洁肤晶露",
    "622461347757": "乳糖酸原液",
    "622249630070": "酒精喷雾",
    "622364890241": "樱花洁面",
    "622383817545": "遮瑕液",
    "622974003192": "海泉套装",
    "622988399671": "幻彩隔离",
    "622988543865": "防晒",
    "622132424766": "胶囊面膜",
    "622990211173": "冰川套装",
    "623152623646": "粉漾雪肌礼盒",
    "622599929779": "紧致眼霜",
    "622601317241": "乳糖酸原液",
    "622878298707": "樱花洁面",
    "622296332971": "烟酰胺面膜",
    "623338519535": "紧致安瓶",
    "623062362068": "金盏花面膜",
    "622485312345": "去角质慕斯",
    "622790221759": "洁面",
    "622486216869": "睡眠面膜",
    "623070442559": "洁肤晶露",
    "622798269587": "水盈清透三件套",
    "622494716207": "人鱼面膜",
    "622802149253": "美白面膜",
    "623080418896": "宝可梦面膜",
    "623397263318": "幻彩隔离",
    "622535696898": "素颜霜",
    "623119790209": "隔离乳",
    "623119774734": "BB霜",
    "622537188859": "气垫CC霜·",
    "622843585103": "遮瑕液",
}

# 常用的单品销售ID的商品配置
PRO_SALE_ID = {
    "16541174270": "冰川美容液",
    "16722770075": "冰川洁面泡泡",
    "21176872955": "冰川补水霜",
    "21456192773": "冰川睡眠面膜",
    "35399645973": "冰川套装",
    "36442399390": "冰川洁面乳",
    "37874885829": "海泉套装",
    "41681863329": "补水面膜",
    "520987824839": "海泉精华水",
    "521952626778": "紧致礼盒",
    "522855761030": "冰川套装-预售",
    "525166676360": "海泉精华原液",
    "526250011782": "30g美白防晒",
    "532992590037": "卸妆水",
    "535575862926": "雪润气垫",
    "537322993074": "海泉去角质",
    "538774066371": "补水面膜10片-美白",
    "544842582800": "修颜隔离乳",
    "544864793945": "人鱼膜法-21片",
    "548383141347": "海洋修护套装",
    "591760896442": "海泉套装-预售",
    "591792639412": "水光白修护礼盒",
    "592393151137": "人鱼膜法-预售",
    "593810916668": "薇娅安瓶",
    "595588644137": "补水面膜预售",
    "596178847946": "小蓝盒+隔离乳",
    "600044464814": "身体乳",
    "604537691910": "Pro眼霜1",
    "605635862044": "Pro眼霜2",
    "613770708691": "海泉套装",
    "616095579437": "补水面膜",
    "617527892410": "补水面膜",
    "618337100000": "Pro眼霜",
    "620007423495": "乳糖酸原液"
}