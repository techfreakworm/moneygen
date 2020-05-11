from webscraper.security_historical import HistoricalData
from webscraper.security_historical import AvailableSecurities

# avail = AvailableSecurities()

# symbols = avail.get_available_securities(columns=['SYMBOL'], series='EQ')

# Re arrange symbol list
# TODO: Handle special cases in data like 'GET&D', symbol name in CSV is inconsistent, code might break due to special char
symbols = ['GFLLIMITED', 'GHCL', 'GICHSGFIN', 'GICRE', 'GILLETTE', 'GINNIFILA', 'GIPCL', 'GISOLUTION', 'GKWLIMITED', 'GLAXO', 'GLENMARK', 'GLOBALVECT', 'GLOBOFFS', 'GLOBUSSPR', 'GMBREW', 'GMDCLTD', 'GMMPFAUDLR', 'GMRINFRA', 'GNA', 'GNFC', 'GOCLCORP', 'GODFRYPHLP', 'GODREJAGRO', 'GODREJCP', 'GODREJIND', 'GODREJPROP', 'GOKEX', 'GOKUL', 'GOKULAGRO', 'GOLDENTOBC', 'GOLDIAM', 'GOLDTECH', 'GOODLUCK', 'GPIL', 'GPPL', 'GPTINFRA', 'GRANULES', 'GRAPHITE', 'GRASIM', 'GRAVITA', 'GREAVESCOT', 'GREENLAM', 'GREENPANEL', 'GREENPLY', 'GREENPOWER', 'GRINDWELL', 'GROBTEA', 'GRPLTD', 'GRSE', 'GSCLCEMENT', 'GSFC', 'GSPL', 'GSS', 'GTNIND', 'GTPL', 'GUFICBIO', 'GUJALKALI', 'GUJAPOLLO', 'GUJGASLTD', 'GULFOILLUB', 'GULFPETRO', 'GULPOLY', 'GVKPIL', 'HAL', 'HARITASEAT', 'HARRMALAYA', 'HATHWAY', 'HATSUN', 'HAVELLS', 'HBLPOWER', 'HBSL', 'HCC', 'HCG', 'HCLTECH', 'HDFC', 'HDFCAMC', 'HDFCBANK', 'HDFCLIFE', 'HEG', 'HEIDELBERG', 'HERCULES', 'HERITGFOOD', 'HEROMOTOCO', 'HESTERBIO', 'HEXAWARE', 'HFCL', 'HGINFRA', 'HGS', 'HIKAL', 'HIL', 'HILTON', 'HIMATSEIDE', 'HINDALCO', 'HINDCOMPOS', 'HINDCOPPER', 'HINDMOTORS', 'HINDNATGLS', 'HINDOILEXP', 'HINDPETRO', 'HINDUNILVR', 'HINDZINC', 'HIRECT', 'HISARMETAL', 'HITECH', 'HITECHCORP', 'HITECHGEAR', 'HLVLTD', 'HMVL', 'HNDFDS', 'HONAUT', 'HONDAPOWER', 'HPL', 'HSCL', 'HSIL', 'HUDCO', 'IBREALEST', 'IBULHSGFIN', 'IBULISL', 'IBVENTURES', 'ICICIBANK', 'ICICIGI', 'ICICIPRULI', 'ICIL', 'ICRA', 'IDBI', 'IDEA', 'IDFC', 'IDFCFIRSTB', 'IEX', 'IFBAGRO', 'IFBIND', 'IFCI', 'IFGLEXPOR', 'IGARASHI', 'IGL', 'IGPL', 'IIFL', 'IIFLSEC', 'IIFLWAM', 'IMFA', 'IMPAL', 'INDBANK', 'INDHOTEL', 'INDIACEM', 'INDIAGLYCO', 'INDIAMART', 'INDIANB', 'INDIANCARD', 'INDIANHUME', 'INDIGO', 'INDNIPPON', 'INDOCO', 'INDORAMA', 'INDOSTAR', 'INDOTECH', 'INDOTHAI', 'INDOWIND', 'INDRAMEDCO', 'INDTERRAIN', 'INDUSINDBK', 'INEOSSTYRO', 'INFIBEAM', 'INFRATEL', 'INFY', 'INGERRAND', 'INOXLEISUR', 'INOXWIND', 'INSECTICID', 'INSPIRISYS', 'INTEGRA', 'INTELLECT', 'INTENTECH', 'IOB', 'IOC', 'IOLCP', 'IPCALAB', 'IRB', 'IRCON', 'IRCTC', 'ISEC', 'ISFT', 'ISMTLTD', 'ITC', 'ITDC', 'ITDCEM', 'ITI', 'IVC', 'J&KBANK', 'JAGRAN', 'JAGSNPHARM', 'JAICORPLTD', 'JAMNAAUTO', 'JAYBARMARU', 'JBCHEPHARM', 'JBMA', 'JCHAC', 'JHS', 'JINDALPOLY', 'JINDALSAW', 'JINDALSTEL', 'JINDRILL', 'JINDWORLD', 'JIYAECO', 'JKCEMENT', 'JKIL', 'JKLAKSHMI', 'JKPAPER', 'JKTYRE', 'JMA', 'JMCPROJECT', 'JMFINANCIL', 'JOCIL', 'JPASSOCIAT', 'JPOLYINVST', 'JSL', 'JSLHISAR', 'JSWENERGY', 'JSWHL', 'JSWSTEEL', 'JTEKTINDIA', 'JUBILANT', 'JUBLFOOD', 'JUBLINDS', 'JUMPNET', 'JUSTDIAL', 'JYOTHYLAB', 'KABRAEXTRU', 'KAJARIACER', 'KAKATCEM', 'KALPATPOWR', 'KAMATHOTEL', 'KAMDHENU', 'KANORICHEM', 'KANSAINER', 'KARDA', 'KARMAENG', 'KARURVYSYA', 'KAUSHALYA', 'KAYA', 'KCP', 'KCPSUGIND', 'KDDL', 'KEC', 'KECL', 'KEI', 'KELLTONTEC', 'KENNAMET', 'KESORAMIND', 'KHADIM', 'KHANDSE', 'KICL', 'KILITCH', 'KINGFA', 'KIOCL', 'KIRIINDUS', 'KIRLFER', 'KIRLOSBROS', 'KIRLOSENG', 'KIRLOSIND', 'KITEX', 'KKCL', 'KMSUGAR', 'KNRCON', 'KOKUYOCMLN', 'KOLTEPATIL', 'KOPRAN', 'KOTAKBANK', 'KOTARISUG', 'KOTHARIPET', 'KOTHARIPRO', 'KPITTECH', 'KPRMILL', 'KRBL', 'KREBSBIO', 'KSB', 'KSCL', 'KSK', 'KSL', 'KTKBANK', 'KUANTUM', 'L&TFH', 'LAKSHVILAS', 'LALPATHLAB', 'LAMBODHARA', 'LAOPALA', 'LAURUSLABS', 'LAXMIMACH', 'LEMONTREE', 'LFIC', 'LGBBROSLTD', 'LGBFORGE', 'LIBERTSHOE', 'LICHSGFIN', 'LINCOLN', 'LINCPEN', 'LINDEINDIA', 'LOKESHMACH', 'LOTUSEYE', 'LOVABLE', 'LSIL', 'LT', 'LTI', 'LTTS', 'LUMAXIND', 'LUMAXTECH', 'LUPIN', 'LUXIND', 'LYKALABS', 'LYPSAGEMS', 'M&M', 'M&MFIN', 'MAANALU', 'MADHAV', 'MAGADSUGAR', 'MAGMA', 'MAHABANK', 'MAHEPC', 'MAHESHWARI', 'MAHINDCIE', 'MAHLIFE', 'MAHLOG', 'MAHSCOOTER', 'MAHSEAMLES', 'MAITHANALL', 'MAJESCO', 'MALUPAPER', 'MANAKALUCO', 'MANAKCOAT', 'MANAKSTEEL', 'MANALIPETC', 'MANAPPURAM', 'MANGCHEFER', 'MANGLMCEM', 'MANGTIMBER', 'MANINDS', 'MANINFRA', 'MANUGRAPH', 'MARALOVER', 'MARATHON', 'MARICO', 'MARKSANS', 'MARUTI', 'MASFIN', 'MASTEK', 'MATRIMONY', 'MAWANASUG', 'MAXINDIA', 'MAXVIL', 'MAYURUNIQ', 'MAZDA', 'MCDOWELL-N', 'MCX', 'MEGASOFT', 'MEGH', 'MENONBE', 'METROPOLIS', 'MFSL', 'MGL', 'MHRIL', 'MIDHANI', 'MINDACORP', 'MINDAIND', 'MINDTECK', 'MINDTREE', 'MIRCELECTR', 'MIRZAINT', 'MITTAL', 'MMFL', 'MMP', 'MMTC', 'MOHITIND', 'MOHOTAIND', 'MOIL', 'MOLDTECH', 'MOLDTKPAC', 'MONTECARLO', 'MORARJEE', 'MOREPENLAB', 'MOTHERSUMI', 'MOTILALOFS', 'MOTOGENFIN', 'MPHASIS', 'MPSLTD', 'MRF', 'MRO-TEK', 'MRPL', 'MSTCLTD', 'MTEDUCARE', 'MTNL', 'MUKANDLTD', 'MUKTAARTS', 'MUNJALAU', 'MUNJALSHOW', 'MURUDCERA', 'MUTHOOTCAP', 'MUTHOOTFIN', 'NACLIND', 'NAGREEKCAP', 'NAGREEKEXP', 'NAHARCAP', 'NAHARINDUS', 'NAHARPOLY', 'NAHARSPING', 'NAM-INDIA', 'NATCOPHARM', 'NATHBIOGEN', 'NATIONALUM', 'NATNLSTEEL', 'NAUKRI', 'NAVINFLUOR', 'NAVKARCORP', 'NAVNETEDUL', 'NBCC', 'NBIFIN', 'NBVENTURES', 'NCC', 'NCLIND', 'NDGL', 'NDL', 'NDTV', 'NECCLTD', 'NECLIFE', 'NELCAST', 'NESCO', 'NESTLEIND', 'NETWORK18', 'NEULANDLAB', 'NEWGEN', 'NFL', 'NH', 'NHPC', 'NIACL', 'NIITLTD', 'NIITTECH', 'NILAINFRA', 'NILASPACES', 'NILKAMAL', 'NIPPOBATRY', 'NITCO', 'NITINSPIN', 'NKIND', 'NLCINDIA', 'NMDC', 'NOCIL', 'NOIDATOLL', 'NORBTEAEXP', 'NRAIL', 'NRBBEARING', 'NSIL', 'NTL', 'NTPC', 'NUCLEUS', 'NXTDIGITAL', 'OAL', 'OBEROIRLTY', 'OCCL', 'OFSS', 'OIL', 'OLECTRA', 'OMAXAUTO', 'OMAXE', 'OMMETALS', 'ONELIFECAP', 'ONEPOINT', 'ONGC', 'ONMOBILE', 'ONWARDTEC', 'ORBTEXP', 'ORICONENT', 'ORIENTABRA', 'ORIENTALTL', 'ORIENTBELL', 'ORIENTCEM', 'ORIENTELEC', 'ORIENTHOT', 'ORIENTLTD', 'ORIENTPPR', 'ORIENTREF', 'ORISSAMINE', 'OSWALAGRO', 'PAEL', 'PAGEIND', 'PAISALO', 'PALASHSECU', 'PALREDTEC', 'PANACEABIO', 'PANACHE', 'PANAMAPET', 'PAPERPROD', 'PARACABLES', 'PARAGMILK', 'PATELENG', 'PATINTLOG', 'PDMJEPAPER', 'PDSMFL', 'PEARLPOLY', 'PEL', 'PENIND', 'PERSISTENT', 'PETRONET', 'PFC', 'PFIZER', 'PFOCUS', 'PFS', 'PGEL', 'PGHH', 'PGHL', 'PGIL', 'PHILIPCARB', 'PHOENIXLTD', 'PIDILITIND', 'PIIND', 'PILANIINVS', 'PILITA', 'PIONEEREMB', 'PITTIENG', 'PLASTIBLEN', 'PNB', 'PNBGILTS', 'PNBHOUSING', 'PNC', 'PNCINFRA', 'PODDARHOUS', 'PODDARMENT', 'POLYCAB', 'POLYMED', 'POLYPLEX', 'PONNIERODE', 'POWERGRID', 'POWERINDIA', 'POWERMECH', 'PPAP', 'PPL', 'PRABHAT', 'PRADIP', 'PRAENG', 'PRAJIND', 'PRAKASH', 'PRAXIS', 'PRECAM', 'PRECOT', 'PRECWIRE', 'PREMIER', 'PREMIERPOL', 'PRESSMN', 'PRESTIGE', 'PRIMESECU', 'PRINCEPIPE', 'PROSEED', 'PRSMJOHNSN', 'PSB', 'PSPPROJECT', 'PTC', 'PTL', 'PUNJABCHEM', 'PURVA', 'PVR', 'QUESS', 'QUICKHEAL', 'RADAAN', 'RADICO', 'RADIOCITY', 'RAIN', 'RAJESHEXPO', 'RAJTV', 'RALLIS', 'RAMANEWS', 'RAMASTEEL', 'RAMCOCEM', 'RAMCOIND', 'RAMCOSYS', 'RAMKY', 'RANEHOLDIN', 'RATNAMANI', 'RAYMOND', 'RBL', 'RBLBANK', 'RCF', 'RECLTD', 'REDINGTON', 'REFEX', 'RELAXO', 'RELIANCE', 'RELIGARE', 'REMSONSIND', 'RENUKA', 'REPCOHOME', 'REPRO', 'RESPONIND', 'REVATHI', 'RGL', 'RICOAUTO', 'RIIL', 'RITES', 'RKDL', 'RKFORGE', 'RML', 'ROHLTD', 'ROSSELLIND', 'RPGLIFE', 'RPOWER', 'RPPINFRA', 'RSSOFTWARE', 'RSWM', 'RSYSTEMS', 'RTNPOWER', 'RUBYMILLS', 'RUCHIRA', 'RUPA', 'RUSHIL', 'RVNL', 'SADBHAV', 'SADBHIN', 'SAFARI', 'SAGCEM', 'SAIL', 'SAKAR', 'SAKSOFT', 'SAKUMA', 'SALASAR', 'SALONA', 'SALZERELEC', 'SAMBHAAV', 'SANCO', 'SANDESH', 'SANDHAR', 'SANGAMIND', 'SANGHIIND', 'SANGHVIMOV', 'SANGINITA', 'SANOFI', 'SARDAEN', 'SAREGAMA', 'SARLAPOLY', 'SASKEN', 'SATHAISPAT', 'SATIA', 'SATIN', 'SBICARD', 'SBILIFE', 'SBIN', 'SCHAEFFLER', 'SCHNEIDER', 'SCI', 'SEAMECLTD', 'SELAN', 'SEQUENT', 'SESHAPAPER', 'SETCO', 'SEYAIND', 'SFL', 'SGL', 'SHAHALLOYS', 'SHALBY', 'SHALPAINTS', 'SHANKARA', 'SHANTIGEAR', 'SHARDACROP', 'SHARDAMOTR', 'SHEMAROO', 'SHIL', 'SHILPAMED', 'SHIRPUR-G', 'SHIVAMAUTO', 'SHIVAMILLS', 'SHK', 'SHOPERSTOP', 'SHREDIGCEM', 'SHREECEM', 'SHREEPUSHK', 'SHREERAMA', 'SHRENIK', 'SHREYANIND', 'SHREYAS', 'SHRIRAMCIT', 'SHRIRAMEPC', 'SHYAMCENT', 'SHYAMTEL', 'SICAGEN', 'SIEMENS', 'SIGIND', 'SILINV', 'SIMBHALS', 'SIMPLEXINF', 'SINTEX', 'SIRCA', 'SIS', 'SIYSIL', 'SJVN', 'SKFINDIA', 'SKIPPER', 'SKMEGGPROD', 'SMARTLINK', 'SMLISUZU', 'SMSLIFE', 'SMSPHARMA', 'SNOWMAN', 'SOBHA', 'SOLARA', 'SOLARINDS', 'SOMANYCERA', 'SOMATEX', 'SOMICONVEY', 'SONATSOFTW', 'SORILINFRA', 'SOTL', 'SOUTHBANK', 'SOUTHWEST', 'SPAL', 'SPANDANA', 'SPARC', 'SPECIALITY', 'SPENCERS', 'SPIC', 'SPICEJET', 'SPLIL', 'SPMLINFRA', 'SPYL', 'SREEL', 'SREINFRA', 'SRF', 'SRHHYPOLTD', 'SRIPIPES', 'SRTRANSFIN', 'SSWL', 'STAMPEDE', 'STAR', 'STARCEMENT', 'STARPAPER', 'STEELCITY', 'STEELXIND', 'STEL', 'STERTOOLS', 'STINDIA', 'STRTECH', 'SUBEX', 'SUBROS', 'SUDARSCHEM', 'SUMEETINDS', 'SUMICHEM', 'SUMMITSEC', 'SUNCLAYLTD', 'SUNDARAM', 'SUNDARMFIN', 'SUNDARMHLD', 'SUNDRMBRAK', 'SUNDRMFAST', 'SUNFLAG', 'SUNPHARMA', 'SUNTECK', 'SUNTV', 'SUPERHOUSE', 'SUPPETRO', 'SUPRAJIT', 'SUPREMEIND', 'SURANASOL', 'SURANAT&P', 'SURYAROSNI', 'SUTLEJTEX', 'SUVEN', 'SUVENPHAR', 'SUZLON', 'SWANENERGY', 'SWARAJENG', 'SWELECTES', 'SWSOLAR', 'SYMPHONY', 'SYNGENE', 'TAINWALCHM', 'TAJGVK', 'TAKE', 'TALBROAUTO', 'TANLA', 'TARMAT', 'TASTYBITE', 'TATACHEM', 'TATACOFFEE', 'TATACOMM', 'TATACONSUM', 'TATAELXSI', 'TATAINVEST', 'TATAMETALI', 'TATAMOTORS', 'TATAMTRDVR', 'TATAPOWER', 'TATASTEEL', 'TATASTLBSL', 'TATASTLLP', 'TBZ', 'TCI', 'TCIDEVELOP', 'TCIEXP', 'TCIFINANCE', 'TCNSBRANDS', 'TCPLPACK', 'TCS', 'TDPOWERSYS', 'TEAMLEASE', 'TECHIN', 'TECHM', 'TECHNOE', 'TECHNOFAB', 'TERASOFT', 'TEXINFRA', 'TEXMOPIPES', 'TEXRAIL', 'TFCILTD', 'TFL', 'TGBHOTELS', 'THANGAMAYL', 'THEINVEST', 'THERMAX', 'THOMASCOOK', 'THYROCARE', 'TI', 'TIDEWATER', 'TIIL', 'TIINDIA', 'TIJARIA', 'TIL', 'TIMESGTY', 'TIMETECHNO', 'TIMKEN', 'TINPLATE', 'TIPSINDLTD', 'TIRUMALCHM', 'TITAN', 'TNPETRO', 'TNPL', 'TOKYOPLAST', 'TORNTPHARM', 'TORNTPOWER', 'TOUCHWOOD', 'TPLPLASTEH', 'TREEHOUSE', 'TRENT', 'TRIDENT', 'TRIGYN', 'TRIL', 'TRITURBINE', 'TRIVENI', 'TTKHLTCARE', 'TTKPRESTIG', 'TTL', 'TV18BRDCST', 'TVSELECT', 'TVSMOTOR', 'TVSSRICHAK', 'TVTODAY', 'TWL', 'UBL', 'UCALFUEL', 'UCOBANK', 'UFLEX', 'UFO', 'UGARSUGAR', 'UJAAS', 'UJJIVAN', 'UJJIVANSFB', 'ULTRACEMCO', 'UMANGDAIRY', 'UNICHEMLAB', 'UNIENTER', 'UNIONBANK', 'UNIPLY', 'UNITEDTEA', 'UNIVCABLES', 'UNIVPHOTO', 'UPL', 'USHAMART', 'UTTAMSUGAR', 'V2RETAIL', 'VADILALIND', 'VAIBHAVGBL', 'VAISHALI', 'VAKRANGEE', 'VARDHACRLC', 'VARROC', 'VASCONEQ', 'VASWANI', 'VBL', 'VEDL', 'VENKEYS', 'VESUVIUS', 'VETO', 'VGUARD', 'VHL', 'VIDHIING', 'VIJIFIN', 'VIKASECO', 'VIKASPROP', 'VIKASWSP', 'VIMTALABS', 'VINATIORGA', 'VINDHYATEL', 'VINYLINDIA', 'VIPCLOTHNG', 'VIPIND', 'VIPULLTD', 'VISAKAIND', 'VISHNU', 'VISHWARAJ', 'VIVIDHA', 'VLSFINANCE', 'VMART', 'VOLTAMP', 'VOLTAS', 'VRLLOG', 'VSSL', 'VSTIND', 'VSTTILLERS', 'VTL', 'WABAG', 'WABCOINDIA', 'WATERBASE', 'WEIZMANIND', 'WELCORP', 'WELENT', 'WELINV', 'WELSPUNIND', 'WENDT', 'WESTLIFE', 'WHEELS', 'WHIRLPOOL', 'WILLAMAGOR', 'WIPRO', 'WOCKPHARMA', 'WONDERLA', 'WSTCSTPAPR', 'XCHANGING', 'XELPMOC', 'XPROINDIA', 'YESBANK', 'ZEEL', 'ZEELEARN', 'ZENITHEXPO', 'ZENSARTECH', 'ZENTEC', 'ZICOM', 'ZODIACLOTH', 'ZODJRDMKJ', 'ZOTA', 'ZUARIGLOB', 'ZYDUSWELL']
print(len(symbols))
hist = HistoricalData()

# hist.create_table_for_securities(symbols)

for index, symbol in enumerate(symbols):
    print(f"Security #{index + 1}: {symbol}")
    df = hist.get_data_for_security(symbol)
    hist.upsert_data(df, symbol)