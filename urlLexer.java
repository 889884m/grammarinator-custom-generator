// Generated from url.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class urlLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		TEXT=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"TEXT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'.'", "'.com'", "'.org'", "'.net'", "'.gov'", "'/'", "'https://'", 
			"'http://'", "'www.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "TEXT"
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


	public urlLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "url.g4"; }

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
		"\u0004\u0000\nJ\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tI\b\t\u0000\u0000\n\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0001\u0000\u0003\u0002\u000009az\u0001\u0000"+
		"az\u0001\u000009K\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001"+
		"\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001"+
		"\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000"+
		"\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000"+
		"\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000"+
		"\u0000\u0001\u0015\u0001\u0000\u0000\u0000\u0003\u0017\u0001\u0000\u0000"+
		"\u0000\u0005\u001c\u0001\u0000\u0000\u0000\u0007!\u0001\u0000\u0000\u0000"+
		"\t&\u0001\u0000\u0000\u0000\u000b+\u0001\u0000\u0000\u0000\r-\u0001\u0000"+
		"\u0000\u0000\u000f6\u0001\u0000\u0000\u0000\u0011>\u0001\u0000\u0000\u0000"+
		"\u0013H\u0001\u0000\u0000\u0000\u0015\u0016\u0005.\u0000\u0000\u0016\u0002"+
		"\u0001\u0000\u0000\u0000\u0017\u0018\u0005.\u0000\u0000\u0018\u0019\u0005"+
		"c\u0000\u0000\u0019\u001a\u0005o\u0000\u0000\u001a\u001b\u0005m\u0000"+
		"\u0000\u001b\u0004\u0001\u0000\u0000\u0000\u001c\u001d\u0005.\u0000\u0000"+
		"\u001d\u001e\u0005o\u0000\u0000\u001e\u001f\u0005r\u0000\u0000\u001f "+
		"\u0005g\u0000\u0000 \u0006\u0001\u0000\u0000\u0000!\"\u0005.\u0000\u0000"+
		"\"#\u0005n\u0000\u0000#$\u0005e\u0000\u0000$%\u0005t\u0000\u0000%\b\u0001"+
		"\u0000\u0000\u0000&\'\u0005.\u0000\u0000\'(\u0005g\u0000\u0000()\u0005"+
		"o\u0000\u0000)*\u0005v\u0000\u0000*\n\u0001\u0000\u0000\u0000+,\u0005"+
		"/\u0000\u0000,\f\u0001\u0000\u0000\u0000-.\u0005h\u0000\u0000./\u0005"+
		"t\u0000\u0000/0\u0005t\u0000\u000001\u0005p\u0000\u000012\u0005s\u0000"+
		"\u000023\u0005:\u0000\u000034\u0005/\u0000\u000045\u0005/\u0000\u0000"+
		"5\u000e\u0001\u0000\u0000\u000067\u0005h\u0000\u000078\u0005t\u0000\u0000"+
		"89\u0005t\u0000\u00009:\u0005p\u0000\u0000:;\u0005:\u0000\u0000;<\u0005"+
		"/\u0000\u0000<=\u0005/\u0000\u0000=\u0010\u0001\u0000\u0000\u0000>?\u0005"+
		"w\u0000\u0000?@\u0005w\u0000\u0000@A\u0005w\u0000\u0000AB\u0005.\u0000"+
		"\u0000B\u0012\u0001\u0000\u0000\u0000CI\u0007\u0000\u0000\u0000DE\u0007"+
		"\u0001\u0000\u0000EI\u0003\u0013\t\u0000FG\u0007\u0002\u0000\u0000GI\u0003"+
		"\u0013\t\u0000HC\u0001\u0000\u0000\u0000HD\u0001\u0000\u0000\u0000HF\u0001"+
		"\u0000\u0000\u0000I\u0014\u0001\u0000\u0000\u0000\u0002\u0000H\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}