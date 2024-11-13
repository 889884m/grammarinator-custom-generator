// Generated from url.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link urlParser}.
 */
public interface urlListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link urlParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(urlParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(urlParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link urlParser#url}.
	 * @param ctx the parse tree
	 */
	void enterUrl(urlParser.UrlContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#url}.
	 * @param ctx the parse tree
	 */
	void exitUrl(urlParser.UrlContext ctx);
	/**
	 * Enter a parse tree produced by {@link urlParser#body}.
	 * @param ctx the parse tree
	 */
	void enterBody(urlParser.BodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#body}.
	 * @param ctx the parse tree
	 */
	void exitBody(urlParser.BodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link urlParser#tld}.
	 * @param ctx the parse tree
	 */
	void enterTld(urlParser.TldContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#tld}.
	 * @param ctx the parse tree
	 */
	void exitTld(urlParser.TldContext ctx);
	/**
	 * Enter a parse tree produced by {@link urlParser#path}.
	 * @param ctx the parse tree
	 */
	void enterPath(urlParser.PathContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#path}.
	 * @param ctx the parse tree
	 */
	void exitPath(urlParser.PathContext ctx);
	/**
	 * Enter a parse tree produced by {@link urlParser#phrase}.
	 * @param ctx the parse tree
	 */
	void enterPhrase(urlParser.PhraseContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#phrase}.
	 * @param ctx the parse tree
	 */
	void exitPhrase(urlParser.PhraseContext ctx);
	/**
	 * Enter a parse tree produced by {@link urlParser#scheme}.
	 * @param ctx the parse tree
	 */
	void enterScheme(urlParser.SchemeContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#scheme}.
	 * @param ctx the parse tree
	 */
	void exitScheme(urlParser.SchemeContext ctx);
	/**
	 * Enter a parse tree produced by {@link urlParser#subdomain}.
	 * @param ctx the parse tree
	 */
	void enterSubdomain(urlParser.SubdomainContext ctx);
	/**
	 * Exit a parse tree produced by {@link urlParser#subdomain}.
	 * @param ctx the parse tree
	 */
	void exitSubdomain(urlParser.SubdomainContext ctx);
}