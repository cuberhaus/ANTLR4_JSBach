// Generated from jsbach.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class jsbachLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, ID=13, NUM=14, WS=15, DIV=16, MOD=17, MES=18, 
		MINUS=19, MULT=20, POT=21, COMMENT=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "ID", "NUM", "WS", "DIV", "MOD", "MES", "MINUS", 
			"MULT", "POT", "COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'|:'", "':|'", "'if'", "'else'", "'while'", "'='", "'/='", "'<'", 
			"'>'", "'<='", "'>='", "'<-'", null, null, null, "'/'", "'%'", "'+'", 
			"'-'", "'*'", "'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, "ID", "NUM", "WS", "DIV", "MOD", "MES", "MINUS", "MULT", "POT", 
			"COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public jsbachLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "jsbach.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0016\u0080\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0004\fU\b\f\u000b\f\f\fV\u0001\r\u0004\rZ\b\r\u000b"+
		"\r\f\r[\u0001\u000e\u0004\u000e_\b\u000e\u000b\u000e\f\u000e`\u0001\u000e"+
		"\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015"+
		"\u0005\u0015v\b\u0015\n\u0015\f\u0015y\t\u0015\u0001\u0015\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001w\u0000\u0016\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016\u0001\u0000"+
		"\u0003\u0002\u0000AZaz\u0001\u000009\u0002\u0000\t\n  \u0083\u0000\u0001"+
		"\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005"+
		"\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001"+
		"\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000"+
		"\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000"+
		"\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000"+
		"\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000"+
		"\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000"+
		"\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000"+
		"\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000"+
		"\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001"+
		"\u0000\u0000\u0000\u0001-\u0001\u0000\u0000\u0000\u00030\u0001\u0000\u0000"+
		"\u0000\u00053\u0001\u0000\u0000\u0000\u00076\u0001\u0000\u0000\u0000\t"+
		";\u0001\u0000\u0000\u0000\u000bA\u0001\u0000\u0000\u0000\rC\u0001\u0000"+
		"\u0000\u0000\u000fF\u0001\u0000\u0000\u0000\u0011H\u0001\u0000\u0000\u0000"+
		"\u0013J\u0001\u0000\u0000\u0000\u0015M\u0001\u0000\u0000\u0000\u0017P"+
		"\u0001\u0000\u0000\u0000\u0019T\u0001\u0000\u0000\u0000\u001bY\u0001\u0000"+
		"\u0000\u0000\u001d^\u0001\u0000\u0000\u0000\u001fd\u0001\u0000\u0000\u0000"+
		"!f\u0001\u0000\u0000\u0000#h\u0001\u0000\u0000\u0000%j\u0001\u0000\u0000"+
		"\u0000\'l\u0001\u0000\u0000\u0000)n\u0001\u0000\u0000\u0000+p\u0001\u0000"+
		"\u0000\u0000-.\u0005|\u0000\u0000./\u0005:\u0000\u0000/\u0002\u0001\u0000"+
		"\u0000\u000001\u0005:\u0000\u000012\u0005|\u0000\u00002\u0004\u0001\u0000"+
		"\u0000\u000034\u0005i\u0000\u000045\u0005f\u0000\u00005\u0006\u0001\u0000"+
		"\u0000\u000067\u0005e\u0000\u000078\u0005l\u0000\u000089\u0005s\u0000"+
		"\u00009:\u0005e\u0000\u0000:\b\u0001\u0000\u0000\u0000;<\u0005w\u0000"+
		"\u0000<=\u0005h\u0000\u0000=>\u0005i\u0000\u0000>?\u0005l\u0000\u0000"+
		"?@\u0005e\u0000\u0000@\n\u0001\u0000\u0000\u0000AB\u0005=\u0000\u0000"+
		"B\f\u0001\u0000\u0000\u0000CD\u0005/\u0000\u0000DE\u0005=\u0000\u0000"+
		"E\u000e\u0001\u0000\u0000\u0000FG\u0005<\u0000\u0000G\u0010\u0001\u0000"+
		"\u0000\u0000HI\u0005>\u0000\u0000I\u0012\u0001\u0000\u0000\u0000JK\u0005"+
		"<\u0000\u0000KL\u0005=\u0000\u0000L\u0014\u0001\u0000\u0000\u0000MN\u0005"+
		">\u0000\u0000NO\u0005=\u0000\u0000O\u0016\u0001\u0000\u0000\u0000PQ\u0005"+
		"<\u0000\u0000QR\u0005-\u0000\u0000R\u0018\u0001\u0000\u0000\u0000SU\u0007"+
		"\u0000\u0000\u0000TS\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000"+
		"VT\u0001\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000W\u001a\u0001\u0000"+
		"\u0000\u0000XZ\u0007\u0001\u0000\u0000YX\u0001\u0000\u0000\u0000Z[\u0001"+
		"\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000\u0000\u0000"+
		"\\\u001c\u0001\u0000\u0000\u0000]_\u0007\u0002\u0000\u0000^]\u0001\u0000"+
		"\u0000\u0000_`\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000ab\u0001\u0000\u0000\u0000bc\u0006\u000e\u0000\u0000"+
		"c\u001e\u0001\u0000\u0000\u0000de\u0005/\u0000\u0000e \u0001\u0000\u0000"+
		"\u0000fg\u0005%\u0000\u0000g\"\u0001\u0000\u0000\u0000hi\u0005+\u0000"+
		"\u0000i$\u0001\u0000\u0000\u0000jk\u0005-\u0000\u0000k&\u0001\u0000\u0000"+
		"\u0000lm\u0005*\u0000\u0000m(\u0001\u0000\u0000\u0000no\u0005^\u0000\u0000"+
		"o*\u0001\u0000\u0000\u0000pq\u0005~\u0000\u0000qr\u0005~\u0000\u0000r"+
		"s\u0005~\u0000\u0000sw\u0001\u0000\u0000\u0000tv\t\u0000\u0000\u0000u"+
		"t\u0001\u0000\u0000\u0000vy\u0001\u0000\u0000\u0000wx\u0001\u0000\u0000"+
		"\u0000wu\u0001\u0000\u0000\u0000xz\u0001\u0000\u0000\u0000yw\u0001\u0000"+
		"\u0000\u0000z{\u0005~\u0000\u0000{|\u0005~\u0000\u0000|}\u0005~\u0000"+
		"\u0000}~\u0001\u0000\u0000\u0000~\u007f\u0006\u0015\u0000\u0000\u007f"+
		",\u0001\u0000\u0000\u0000\u0005\u0000V[`w\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}