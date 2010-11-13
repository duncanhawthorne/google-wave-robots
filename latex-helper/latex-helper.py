#!python latex-helper robot
 
import re
import os
import htmlentitydefs  

'''
this file came from
plasex file Entities.py
import into ipython
look at dictionary globals()
mild tweak into this dictionary
'''
latex_dict = {'#': u'#',
 '$': u'$',
 '%': u'%',
 ',': u'\u2009',
 '-': u'\xad',
 ':': u'\u2004',
 ';': u'\u2002',
 'AA': u'\u212b',
 'AE': u'\xc6',
 'Bumpeq': u'\u224e',
 'CYRA': u'\u0410',
 'CYRB': u'\u0411',
 'CYRC': u'\u0426',
 'CYRCH': u'\u0427',
 'CYRD': u'\u0414',
 'CYRDJE': u'\u0402',
 'CYRDZE': u'\u0405',
 'CYRDZHE': u'\u040f',
 'CYRE': u'\u0415',
 'CYREREV': u'\u042d',
 'CYRERY': u'\u042b',
 'CYRF': u'\u0424',
 'CYRG': u'\u0413',
 'CYRGUP': u'\u0403',
 'CYRH': u'\u0425',
 'CYRHRDSN': u'\u042a',
 'CYRI': u'\u0418',
 'CYRIE': u'\u0404',
 'CYRII': u'\u0406',
 'CYRISHRT': u'\u0419',
 'CYRJE': u'\u0408',
 'CYRK': u'\u041a',
 'CYRKBEAK': u'\u040c',
 'CYRL': u'\u041b',
 'CYRLJE': u'\u0409',
 'CYRM': u'\u041c',
 'CYRN': u'\u041d',
 'CYRNJE': u'\u040a',
 'CYRO': u'\u041e',
 'CYRP': u'\u041f',
 'CYRR': u'\u0420',
 'CYRS': u'\u0421',
 'CYRSFTSN': u'\u042c',
 'CYRSH': u'\u0428',
 'CYRSHCH': u'\u0429',
 'CYRT': u'\u0422',
 'CYRTSHE': u'\u040b',
 'CYRU': u'\u0423',
 'CYRUSHRT': u'\u040e',
 'CYRV': u'\u0412',
 'CYRYA': u'\u042f',
 'CYRYI': u'\u0407',
 'CYRYO': u'\u0401',
 'CYRYU': u'\u042e',
 'CYRZ': u'\u0417',
 'CYRZH': u'\u0416',
 'Cap': u'\u22d2',
 'Cdprime': u'\u042a',
 'Cprime': u'\u042c',
 'Cup': u'\u22d3',
 'DH': u'\xd0',
 'DJ': u'\u0110',
 'Delta': u'\u0394',
 'Doteq': u'\u2251',
 'Downarrow': u'\u21d3',
 'Dz': u'\u0405',
 'Dzh': u'\u040f',
 'Gamma': u'\u0393',
 'Hstrok': u'\u0126',
 'Im': u'\u2111',
 'L': u'\u0141',
 'Lambda': u'\u039b',
 'Leftarrow': u'\u21d0',
 'Leftrightarrow': u'\u21d4',
 'Lleftarrow': u'\u21da',
 'Lmidot': u'\u013f',
 'Lsh': u'\u21b0',
 'NG': u'\u014a',
 'O': u'\xd8',
 'OE': u'\u0152',
 'Omega': u'\u2126',
 'P': u'\xb6',
 'Phi': u'\u03a6',
 'Pi': u'\u03a0',
 'Psi': u'\u03a8',
 'Re': u'\u211c',
 'Rightarrow': u'\u21d2',
 'Rrightarrow': u'\u21db',
 'Rsh': u'\u21b1',
 'S': u'\xa7',
 'Sigma': u'\u03a3',
 'Subset': u'\u22d0',
 'Supset': u'\u22d1',
 'TH': u'\xde',
 'Theta': u'\u0398',
 'Thorn': u'\xde',
 'Tstrok': u'\u0166',
 'Uparrow': u'\u21d1',
 'Updownarrow': u'\u21d5',
 'Upsilon': u'\u03d2',
 'Vdash': u'\u22a9',
 'Vert': u'\u2016',
 'Vvdash': u'\u22aa',
 'Xi': u'\u039e',
# '\\\\': u'\n',
# '__builtins_': <type 'unicode'>,
 'aa': u'\xe5',
 'ae': u'\xe6',
 'aleph': u'\u2135',
 'alpha': u'\u03b1',
 'amalg': u'\u2210',
 'angle': u'\u2220',
 'approx': u'\u2248',
 'approxeq': u'\u224a',
 'ast': u'*',
 'asymp': u'\u224d',
 'backcong': u'\u224c',
 'backepsilon': u'\u220d',
 'backsim': u'\u223d',
 'backsimeq': u'\u22cd',
 'backslash': u'\\',
 'barwedge': u'\u22bc',
 'because': u'\u2235',
 'beta': u'\u03b2',
 'beth': u'\u2136',
 'between': u'\u226c',
 'bigcirc': u'\u25ef',
 'bigstar': u'\u2605',
 'bigtriangledown': u'\u25bd',
 'bigtriangleup': u'\u25b3',
 'blacklozenge': u'\ue80b',
 'blacksquare': u'\u25aa',
 'blacktriangle': u'\u25b4',
 'blacktriangledown': u'\u25be',
 'blacktriangleleft': u'\u25c2',
 'blacktriangleright': u'\u25b8',
 'block': u'\u2588',
 'bot': u'\u22a5',
 'bowtie': u'\u22c8',
 'boxDL': u'\u2557',
 'boxDR': u'\u2554',
 'boxDl': u'\u2556',
 'boxDr': u'\u2553',
 'boxH': u'\u2550',
 'boxHD': u'\u2566',
 'boxHU': u'\u2569',
 'boxHd': u'\u2564',
 'boxHu': u'\u2567',
 'boxUL': u'\u255d',
 'boxUR': u'\u255a',
 'boxUl': u'\u255c',
 'boxUr': u'\u2559',
 'boxV': u'\u2551',
 'boxVH': u'\u256c',
 'boxVL': u'\u2563',
 'boxVR': u'\u2560',
 'boxVh': u'\u256b',
 'boxVl': u'\u2562',
 'boxVr': u'\u255f',
 'boxdL': u'\u2555',
 'boxdR': u'\u2552',
 'boxdl': u'\u2510',
 'boxdot': u'\u22a1',
 'boxdr': u'\u250c',
 'boxh': u'\u2500',
 'boxhD': u'\u2565',
 'boxhU': u'\u2568',
 'boxhd': u'\u252c',
 'boxhu': u'\u2534',
 'boxminus': u'\u229f',
 'boxplus': u'\u229e',
 'boxtimes': u'\u22a0',
 'boxuL': u'\u255b',
 'boxuR': u'\u2558',
 'boxul': u'\u2518',
 'boxur': u'\u2514',
 'boxv': u'\u2502',
 'boxvH': u'\u256a',
 'boxvL': u'\u2561',
 'boxvR': u'\u255e',
 'boxvh': u'\u253c',
 'boxvl': u'\u2524',
 'boxvr': u'\u251c',
 'brokenvert': u'\xa6',
 'bullet': u'\u2022',
 'bumpeq': u'\u224f',
 'cap': u'\u2229',
 'cdot': u'\xb7',
 'cdotp': u'\xb7',
 'cdprime': u'\u044a',
 'cent': u'\xa2',
 'centerdot': u'\xb7',
 'checkmark': u'\u2713',
 'chi': u'\u03c7',
 'circ': u'\u25cb',
 'circeq': u'\u2257',
 'circlearrowleft': u'\u21ba',
 'circlearrowright': u'\u21bb',
 'circledR': u'\xae',
 'circledS': u'\u24c8',
 'circledast': u'\u229b',
 'circledcirc': u'\u229a',
 'circleddash': u'\u229d',
 'clubsuit': u'\u2663',
 'colon': u':',
 'complement': u'\u2201',
 'cong': u'\u2245',
 'coprod': u'\u2210',
 'copyright': u'\xa9',
 'cprime': u'\u044c',
 'cup': u'\u222a',
 'curlyeqprec': u'\u22de',
 'curlyeqsucc': u'\u22df',
 'curlyvee': u'\u22ce',
 'curlywedge': u'\u22cf',
 'currency': u'\xa4',
 'curvearrowleft': u'\u21b6',
 'curvearrowright': u'\u21b7',
 'cyra': u'\u0430',
 'cyrb': u'\u0431',
 'cyrc': u'\u0446',
 'cyrch': u'\u0447',
 'cyrd': u'\u0434',
 'cyrdje': u'\u0452',
 'cyrdze': u'\u0455',
 'cyrdzhe': u'\u045f',
 'cyre': u'\u0435',
 'cyrerev': u'\u044d',
 'cyrery': u'\u044b',
 'cyrf': u'\u0444',
 'cyrg': u'\u0433',
 'cyrgup': u'\u0453',
 'cyrh': u'\u0445',
 'cyrhrdsn': u'\u044a',
 'cyri': u'\u0438',
 'cyrie': u'\u0454',
 'cyrii': u'\u0456',
 'cyrishrt': u'\u0439',
 'cyrje': u'\u0458',
 'cyrk': u'\u043a',
 'cyrkbeak': u'\u045c',
 'cyrl': u'\u043b',
 'cyrlje': u'\u0459',
 'cyrm': u'\u043c',
 'cyrn': u'\u043d',
 'cyrnje': u'\u045a',
 'cyro': u'\u043e',
 'cyrp': u'\u043f',
 'cyrr': u'\u0440',
 'cyrs': u'\u0441',
 'cyrsftsn': u'\u044c',
 'cyrsh': u'\u0448',
 'cyrshch': u'\u0449',
 'cyrt': u'\u0442',
 'cyrtshe': u'\u045b',
 'cyru': u'\u0443',
 'cyrushrt': u'\u045e',
 'cyrv': u'\u0432',
 'cyrya': u'\u044f',
 'cyryi': u'\u0457',
 'cyryo': u'\u0451',
 'cyryu': u'\u044e',
 'cyrz': u'\u0437',
 'cyrzh': u'\u0436',
 'dag': u'\u2020',
 'dagger': u'\u2020',
 'daleth': u'\u2138',
 'dasharrow': u'\u21e2',
 'dashleftarrow': u'\u21e0',
 'dashrightarrow': u'\u21e2',
 'dashv': u'\u22a3',
 'ddag': u'\u2021',
 'ddagger': u'\u2021',
 'delta': u'\u03b4',
 'dh': u'\xf0',
 'diamond': u'\u22c4',
 'diamondsuit': u'\u2666',
 'digamma': u'\u03dc',
 'div': u'\xf7',
 'divideontimes': u'\u22c7',
 'dj': u'\u0111',
 'dlcrop': u'\u230d',
 'doteq': u'\u2250',
 'doteqdot': u'\u2251',
 'dotplus': u'\u2214',
 'doublebarwedge': u'\u2306',
 'doublecap': u'\u22d2',
 'doublecup': u'\u22d3',
 'downarrow': u'\u2193',
 'downdownarrows': u'\u21ca',
 'downharpoonleft': u'\u21c3',
 'downharpoonright': u'\u21c2',
 'drcrop': u'\u230c',
 'dz': u'\u0455',
 'dzh': u'\u045f',
 'eighthnote': u'\u266a',
 'ell': u'\u2113',
 'emptyset': u'\u2205',
 'epsilon': u'\u03b5',
 'eqcirc': u'\u2256',
 'eqslantgtr': u'\u22dd',
 'eqslantless': u'\u22dc',
 'equiv': u'\u2261',
 'eta': u'\u03b7',
 'eth': u'\xf0',
 'exists': u'\u2203',
 'fallingdotseq': u'\u2252',
 'female': u'\u2640',
 'flat': u'\u266d',
 'forall': u'\u2200',
 'frown': u'\u2322',
 'gamma': u'\u03b3',
 'ge': u'\u2265',
 'geq': u'\u2265',
 'geqq': u'\u2267',
 'gg': u'\u226b',
 'ggg': u'\u22d9',
 'gggtr': u'\u22d9',
 'gimel': u'\u2137',
 'gneq': u'\u2269',
 'gneqq': u'\u2269',
 'gnsim': u'\u22e7',
 'gtrdot': u'\u22d7',
 'gtreqless': u'\u22db',
 'gtreqqless': u'\u22db',
 'gtrless': u'\u2277',
 'gtrsim': u'\u2273',
 'guillemotleft': u'\xab',
 'guillemotright': u'\xbb',
 'guilsinglleft': u'\u2039',
 'guilsinglright': u'\u203a',
 'gvertneqq': u'\u2269',
 'hbar': u'\u210f',
 'heartsuit': u'\u2665',
 'hookleftarrow': u'\u21a9',
 'hookrightarrow': u'\u21aa',
 'hstrok': u'\u0127',
 'hybull': u'\u2043',
 'i': u'\u0131',
 'iff': u'\u21d4',
 'in': u'\u2208',
 'infty': u'\u221e',
 'int': u'\u222b',
 'intercal': u'\u22ba',
 'iota': u'\u03b9',
 'kappa': u'\u03ba',
 'l': u'\u0142',
 'lambda': u'\u03bb',
 'land': u'\u2227',
 'langle': u'\u3008',
 'lbrace': u'{',
 'lceil': u'\u2308',
 'ldotp': u'.',
 'ldots': u'\u2026',
 'le': u'\u2264',
 'leftarrow': u'\u2190',
 'leftarrowtail': u'\u21a2',
 'leftharpoondown': u'\u21bd',
 'leftharpoonup': u'\u21bc',
 'leftleftarrows': u'\u21c7',
 'leftrightarrow': u'\u2194',
 'leftrightarrows': u'\u21c6',
 'leftrightharpoons': u'\u21cb',
 'leftrightsquigarrow': u'\u21ad',
 'leftthreetimes': u'\u22cb',
 'leq': u'\u2264',
 'leqq': u'\u2266',
 'lessdot': u'\u22d6',
 'lesseqgtr': u'\u22da',
 'lesseqqgtr': u'\u22da',
 'lessgtr': u'\u2276',
 'lesssim': u'\u2272',
 'lfloor': u'\u230a',
 'lhblk': u'\u2584',
 'll': u'\u226a',
 'llbracket': u'\u301a',
 'llcorner': u'\u231e',
 'lll': u'\u22d8',
 'llless': u'\u22d8',
 'lmidot': u'\u0140',
 'lneq': u'\u2268',
 'lneqq': u'\u2268',
 'lnot': u'\xac',
 'lnsim': u'\u22e6',
 'looparrowleft': u'\u21ab',
 'looparrowright': u'\u21ac',
 'lor': u'\u2228',
 'lozenge': u'\u25ca',
 'lrcorner': u'\u231f',
 'ltimes': u'\u22c9',
 'lvertneqq': u'\u2268',
 'male': u'\u2642',
 'maltese': u'\u2720',
 'mapsto': u'\u21a6',
 'marker': u'\u25ae',
 'mathsterling': u'\xa3',
 'measuredangle': u'\u2221',
 'mho': u'\u2127',
 'mid': u'\u2223',
 'mldr': u'\u2026',
 'models': u'\u22a7',
 'mp': u'\u2213',
 'mu': u'\u03bc',
 'multimap': u'\u22b8',
 'nLeftarrow': u'\u21cd',
 'nLeftrightarrow': u'\u21ce',
 'nRightarrow': u'\u21cf',
 'nVDash': u'\u22af',
 'nVdash': u'\u22ae',
 'nabla': u'\u2207',
 'natural': u'\u266e',
 'ncong': u'\u2247',
 'ne': u'\u2260',
 'nearrow': u'\u2197',
 'neq': u'\u2260',
 'nexists': u'\u2204',
 'ng': u'\u014b',
 'ngeq': u'\u2271',
 'ngeqslant': u'\u2271',
 'ngtr': u'\u226f',
 'ni': u'\u220b',
 'nldr': u'\u2025',
 'nleftarrow': u'\u219a',
 'nleftrightarrow': u'\u21ae',
 'nleq': u'\u2270',
 'nleqslant': u'\u2270',
 'nless': u'\u226e',
 'nmid': u'\u2224',
 'not': u'\u226f',
 'nparallel': u'\u2226',
 'nprec': u'\u2280',
 'npreceq': u'\u22e0',
 'nrightarrow': u'\u219b',
 'nsim': u'\u2241',
 'nsubseteq': u'\u2288',
 'nsubseteqq': u'\u2288',
 'nsucc': u'\u2281',
 'nsucceq': u'\u22e1',
 'nsupseteq': u'\u2289',
 'nsupseteqq': u'\u2289',
 'ntriangleleft': u'\u22ea',
 'ntrianglelefteq': u'\u22ec',
 'ntriangleright': u'\u22eb',
 'ntrianglerighteq': u'\u22ed',
 'nu': u'\u03bd',
 'nvDash': u'\u22ad',
 'nvdash': u'\u22ac',
 'nwarrow': u'\u2196',
 'o': u'\xf8',
 'odot': u'\u2299',
 'oe': u'\u0153',
 'oint': u'\u222e',
 'omega': u'\u03c9',
 'ominus': u'\u2296',
 'oplus': u'\u2295',
 'oslash': u'\u2298',
 'otimes': u'\u2297',
 'owns': u'\u220b',
 'parallel': u'\u2225',
 'partial': u'\u2202',
 'permil': u'\u2030',
 'perp': u'\u22a5',
 'phi': u'\u03c6',
 'phone': u'\u260e',
 'pi': u'\u03c0',
 'pitchfork': u'\u22d4',
 'pm': u'\xb1',
 'pounds': u'\xa3',
 'prec': u'\u227a',
 'preccurlyeq': u'\u227c',
 'preceq': u'\u227c',
 'precnsim': u'\u22e8',
 'precsim': u'\u227e',
 'prod': u'\u220f',
 'propto': u'\u221d',
 'psi': u'\u03c8',
 'quad': u'\u2003',
 'quotedblbase': u'\u201e',
 'quotesinglbase': u'\u201a',
 'rangle': u'\u3009',
 'rbrace': u'}',
 'rceil': u'\u2309',
 'recorder': u'\u2315',
 'rfloor': u'\u230b',
 'rho': u'\u03c1',
 'rightarrow': u'\u2192',
 'rightarrowtail': u'\u21a3',
 'rightharpoondown': u'\u21c1',
 'rightharpoonup': u'\u21c0',
 'rightleftarrows': u'\u21c4',
 'rightleftharpoons': u'\u21cc',
 'rightrightarrows': u'\u21c9',
 'rightsquigarrow': u'\u21dd',
 'rightthreetimes': u'\u22cc',
 'risingdotseq': u'\u2253',
 'rrbracket': u'\u301b',
 'rtimes': u'\u22ca',
 'searrow': u'\u2198',
 'setminus': u'\u2216',
 'sharp': u'\u266f',
 'sigma': u'\u03c3',
 'sim': u'\u223c',
 'simeq': u'\u2243',
 'smallsetminus': u'\ufe68',
 'smile': u'\u2323',
 'spadesuit': u'\u2660',
 'sphericalangle': u'\u2222',
 'sqangle': u'\u221f',
 'sqcap': u'\u2293',
 'sqcup': u'\u2294',
 'sqsubset': u'\u228f',
 'sqsubseteq': u'\u2291',
 'sqsupset': u'\u2290',
 'sqsupseteq': u'\u2292',
 'square': u'\u25a1',
 'ss': u'\xdf',
 'star': u'\u22c6',
 'subset': u'\u2282',
 'subseteq': u'\u2286',
 'subseteqq': u'\u2286',
 'subsetneq': u'\u228a',
 'subsetneqq': u'\u228a',
 'succ': u'\u227b',
 'succcurlyeq': u'\u227d',
 'succeq': u'\u227d',
 'succnsim': u'\u22e9',
 'succsim': u'\u227f',
 'sum': u'\u2211',
 'supset': u'\u2283',
 'supseteq': u'\u2287',
 'supseteqq': u'\u2287',
 'supsetneq': u'\u228b',
 'supsetneqq': u'\u228b',
 'surd': u'\u221a',
 'swarrow': u'\u2199',
 'tau': u'\u03c4',
 'textacutedbl': u'\u02dd',
 'textasciiacute': u'\xb4',
 'textasciibreve': u'\u02d8',
 'textasciicaron': u'\u02c7',
 'textasciicircum': u'^',
 'textasciidieresis': u'\xa8',
 'textasciigrave': u'`',
 'textasciimacron': u'\xaf',
 'textasciitilde': u'~',
 'textbackslash': u'\\',
 'textbar': u'|',
 'textbardbl': u'\u2016',
 'textbigcircle': u'\u25ef',
 'textbraceleft': u'{',
 'textbrokenbar': u'\xa6',
 'textbullet': u'\u2022',
 'textcent': u'\xa2',
 'textcircledP': u'\u2117',
 'textcopyright': u'\xa9',
 'textcurrency': u'\xa4',
 'textdagger': u'\u2020',
 'textdaggerdbl': u'\u2021',
 'textdegree': u'\xb0',
 'textdiv': u'\xf7',
 'textdollar': u'$',
 'textdownarrow': u'\u2193',
 'textellipsis': u'\u2026',
 'textemdash': u'\u2014',
 'textendash': u'\u2013',
 'texteuro': u'\u20ac',
 'textexclamdown': u'\xa1',
 'textfractionsolidus': u'\u2044',
 'textgreater': u'>',
 'textlangle': u'\u3008',
 'textlbrackdbl': u'\u301a',
 'textleftarrow': u'\u2190',
 'textless': u'<',
 'textlnot': u'\xac',
 'textmho': u'\u2127',
 'textminus': u'\u2212',
 'textmu': u'\xb5',
 'textmusicalnote': u'\u266a',
 'textnumero': u'\u2116',
 'textohm': u'\u2126',
 'textordfeminine': u'\xaa',
 'textordmasculine': u'\xba',
 'textparagraph': u'\xb6',
 'textperiodcentered': u'\xb7',
 'textpertenthousand': u'\u2031',
 'textperthousand': u'\u2030',
 'textpilcrow': u'\xb6',
 'textpm': u'\xb1',
 'textquestiondown': u'\xbf',
 'textquotedbl': u'"',
 'textquotedblleft': u'\u201f',
 'textquotedblright': u'\u201d',
 'textquoteleft': u'\u2018',
 'textquoteright': u'\u2019',
 'textquotesingle': u"'",
 'textrangle': u'\u3009',
 'textrbrackdbl': u'\u301b',
 'textrecipe': u'\u211e',
 'textreferencemark': u'\u203b',
 'textregistered': u'\xae',
 'textrightarrow': u'\u2192',
 'textsection': u'\xa7',
 'textsterling': u'\xa3',
 'textsurd': u'\u221a',
 'texttildelow': u'~',
 'texttimes': u'\xd7',
 'texttrademark': u'\u2122',
 'textunderscore': u'_',
 'textuparrow': u'\u2191',
 'textvisiblespace': u'\u2423',
 'textyen': u'\xa5',
 'th': u'\xfe',
 'therefore': u'\u2234',
 'theta': u'\u03b8',
 'thorn': u'\xfe',
 'times': u'\xd7',
 'top': u'\u22a4',
 'triangle': u'\u25b5',
 'triangledown': u'\u25bf',
 'triangleleft': u'\u25c3',
 'trianglelefteq': u'\u22b4',
 'triangleq': u'\u225c',
 'triangleright': u'\u25b9',
 'trianglerighteq': u'\u22b5',
 'tstrok': u'\u0167',
 'twoheadleftarrow': u'\u219e',
 'twoheadrightarrow': u'\u21a0',
 'uhblk': u'\u2580',
 'ulcorner': u'\u231c',
 'ulcrop': u'\u230f',
 'uparrow': u'\u2191',
 'updownarrow': u'\u2195',
 'upharpoonleft': u'\u21bf',
 'upharpoonright': u'\u21be',
 'uplus': u'\u228e',
 'upsilon': u'\u03c5',
 'upuparrows': u'\u21c8',
 'urcorner': u'\u231d',
 'urcrop': u'\u230e',
 'vDash': u'\u22a8',
 'varepsilon': u'\u03b5',
 'varkappa': u'\u03f0',
 'varphi': u'\u03d5',
 'varpi': u'\u03d6',
 'varpropto': u'\u221d',
 'varrho': u'\u03f1',
 'varsigma': u'\u03c2',
 'vartheta': u'\u03d1',
 'vartriangle': u'\u25b5',
 'vartriangleleft': u'\u22b2',
 'vartriangleright': u'\u22b3',
 'vdash': u'\u22a2',
 'vdots': u'\u22ee',
 'vee': u'\u2228',
 'veebar': u'\u22bb',
 'vert': u'|',
 'wedge': u'\u2227',
 'wedgeq': u'\u2259',
 'wp': u'\u2118',
 'wr': u'\u2240',
 'xi': u'\u03be',
 'yen': u'\xa5',
 'zeta': u'\u03b6',
 '{': u'{',
 '|': u'\u2016',
 '}': u'}'}


#For each string in the array:
 #   Find the first '{'. If there is none, leave that string alone.
#    Init a counter to 0. 
#    For each character in the string:  
#        If you see a '{', increment the counter.
#        If you see a '}', decrement the counter.
#        If the counter reaches 0, break.
#    Here, if your counter is not 0, you have invalid input (unbalanced brackets)
#    If it is, then take the string from the first '{' up to the '}' that put the
#     counter at 0, and that is a new element in your array.

def match_bracket(text, i):
    start = text.find('{',i)
    assert start != -1
    count = 1
    pos = start+1
    for char in text[1+start:]:
        if char == '{':
            count += 1
        if char == '}':
            count -= 1
        if count == 0:
            break
        pos += 1
    
    assert count == 0
    return pos
 
from waveapi import events
from waveapi import robot
from waveapi import appengine_robot_runner

import logging

#from lat_dict import latex_dict
latex_dict['dots'] = latex_dict['ldots']
latex_dict['sqrt'] = u'\u221a'
latex_dict['notin'] = u'\u2209'

def ucn_to_python(ucn):
    """
    Convert a Unicode Universal Character Number (e.g. "U+4E00" or "4E00")
    to Python unicode (u'\\u4e00')
    """
    ucn = ucn.strip("U+")
    if len(ucn) > 4:
        return eval("u'\U%08x'" % int(ucn, 16)) #this would be a security hole if we didn't use `int` to make the input safe
    else:
        return eval("u'\u%s'" % ucn) #4 characters isn't enough room to do damage with the eval
        #TODO: this dies on decimal input (e.g. ucn_to_python("100")

#def OnRobotAdded(event, wavelet):
#    """Invoked when the robot has been added."""
#    wavelet.reply("Try typing \\alpha_1\\beta^{10}\\gamma. See http://code.google.com/p/wave-latex-helper/")
 
def OnBlipSubmitted(event, wavelet):
    #return
    logging.debug('OnBlipSubmitted: '+event.blip.text)
    
    blip = event.blip
    if blip == None: return 
#    logging.debug(blip.child_blips)
#    if len(blip.child_blips) > 0: #overcome bug in waveapi
#        logging.debug('child blips so quitting')
#        return
#    else:
#        logging.debug('no child blips, phew')

    for tester,key_values in [
#    ['\\mathbf', ['style/fontWeight', 'bold']]
#    ,['\\mathbb', ['style/fontWeight', 'bold']]
#    ,['\\section*', ['style/fontWeight', 'bold']]
#    ,['\\section', ['style/fontWeight', 'bold']]#FIXME change to heading
#    ,['\\subsection*', ['style/fontWeight', 'bold']]
#    ,['\\subsection', ['style/fontWeight', 'bold']]
#    ,['\\mathit', ['style/fontStyle', 'italic']]
#    ,['\\underline', ['style/textDecoration', 'underline']]
#    ,['\\mathcal', [None, None]]
#    ,['\\text',[None,None]]
##    ,['\\subsection',[]]
    ['_',[["style/verticalAlign",'sub'],["style/fontSize", '0.6666666666666666em']]]#should do a relative font size (ie smaller) rather than set to smallest availble FIXME
    ,['^',[["style/verticalAlign", 'super'],["style/fontSize", '0.6666666666666666em']]]
    ,['--',[["style/verticalAlign", 'normal'],["style/fontSize", '1em']]]#should delete this annotation
    ]:#FIXME applying bold by api to text that is subscripted losed the subscripts
    
        blip = event.blip
        text = blip.text

        if '$$' in text:#to avoid conflicts with latex wave gadgets
            return
    
        matches = []
    
        current_pos = 0
        while text.find(tester,current_pos) != -1:
            real_pos = text.find(tester,current_pos)

            #FIXME dont want to set something as sub/sup if next character is a \\
            if text[real_pos+len(tester)] != '{':
                annot_start = real_pos+len(tester)
                annot_end = real_pos+len(tester)+1
                final_end = annot_end+0
                current_pos = annot_end+0
            else:
                annot_start = real_pos+len(tester)+1
                annot_end = match_bracket(text,real_pos+len(tester))
                final_end = annot_end + 1
                current_pos = annot_end+1
            matches.append([real_pos,annot_start,annot_end,final_end])
    
        matches.sort(None, lambda x: x[0], True)
    
        for m in matches:
            logging.debug('on match: '+str(m)+' '+blip.text[m[0]:m[3]])
            good_to_go = True
            for key,value in key_values:
                #for annot_range in blipDoc.RangesForAnnotation(key):#such as style/verticalalign
                for annot in blip.annotations:#such as style/verticalalign
                    #logging.debug('found annotation '+annot.name)
                    if annot.name == key or annot.name == 'link/auto':
                        
                        if annot.start <= real_pos and annot.end >= final_end:
                            if not key == '--':#so -- overrides
                                good_to_go = False
            logging.debug('good_to_go = '+str(good_to_go))
            if good_to_go:
                blip.range(m[0], m[3]).replace(text[m[1]:m[2]])
                #blipDoc.SetTextInRange(document.Range(m[0], m[3]), text[m[1]:m[2]])#old
                for key,value in key_values:
                    if len(blip.text) == m[0]+(m[2]-m[1]) and key != '--':
                        blip.append(' ')
                    elif blip.text[m[0]+(m[2]-m[1])] == '\n' and key != '--':
                        blip.at(m[0]+(m[2]-m[1])).insert(' ')
                    blip.range(m[0],m[0]+(m[2]-m[1])).annotate(key, value)
                    #blipDoc.SetAnnotation(document.Range(m[0],m[0]+(m[2]-m[1])), key, value)#old
    
    #CLEANUP
    for annot in blip.annotations:
        if annot.name == "style/verticalAlign" and annot.value == 'normal':
            blip.range(annot.start, annot.end).clear_annotation('style/verticalAlign')
        if annot.name == "style/fontSize" and annot.value == '1em':
            blip.range(annot.start, annot.end).clear_annotation('style/fontSize')

    OnDocumentChanged(event, wavelet, True)            
    
def OnDocumentChanged(event, wavelet, blip_sub = False):
    #return
    """Scan the wave to look for any special characters we should convert."""
    logging.debug('OnDocumentChanged: '+event.blip.text)

    blip = event.blip
    if blip == None: return 
#    logging.debug(blip.child_blips)
#    if len(blip.child_blips) > 0: #overcome bug in waveapi
#        logging.debug('child blips so quitting')
#        return
#    else:
#        logging.debug('no child blips, phew')

    blip = event.blip
    text = blip.text

    if '$$' in text:#to avoid conflicts with latex wave gadgets
        return

    if not '\\' in text:
        return

    matches = []
  
    if blip_sub == True:
  
        latex_regex = re.compile('\\\\(.+?)'+'[^a-z]')
        matches += [m for m in latex_regex.finditer(text)]
    else:
        latex_regex = re.compile('\\\\(.+?)'+'[^a-z\n]') #don't do conversion of last letter of a line in real-time as latex code is not a prefix-free code so could be in the middle of typing a larger code-word
        matches += [m for m in latex_regex.finditer(text)]    
  
    if blip_sub == True: #don't do conversion of last letter in real-time as latex code is not a prefix-free code so could be in the middle of typing a larger code-word
        latex_regex = re.compile('\\\\(.+?)'+'$')
        matches += [m for m in latex_regex.finditer(text)]
            
    matches.sort(None, lambda x: x.start(1), True)    
 
    for m in matches:
        bit = m.group(1)
    
        good_to_go = False

        if bit in latex_dict:
            proc_bit = str(latex_dict[bit].encode('utf-8'))  
            good_to_go = True
      
        if good_to_go:  

            start = m.start(1)
            end = m.end(1)
            blip.range(start-1,end).replace(proc_bit)
            if blip.text[start-1+1] == ';':
                blip.range(start-1+1, start-1+1+1).replace('')


if __name__ == '__main__':
    myRobot = robot.Robot('latex-helper', 
        image_url='http://thesaurus.maths.org/mmkb/media/png/Alpha.png',
        profile_url='http://code.google.com/p/wave-latex-helper/')  
    #myRobot.register_handler(events.WaveletSelfAdded, OnRobotAdded)
    myRobot.register_handler(events.BlipSubmitted, OnBlipSubmitted)
    myRobot.register_handler(events.DocumentChanged, OnDocumentChanged, filter='\\\\', context = events.Context.SELF)
    appengine_robot_runner.run(myRobot) 
