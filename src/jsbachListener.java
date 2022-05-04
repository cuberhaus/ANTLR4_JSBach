// Generated from jsbach.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link jsbachParser}.
 */
public interface jsbachListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link jsbachParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(jsbachParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(jsbachParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsbachParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(jsbachParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(jsbachParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by the {@code pot}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPot(jsbachParser.PotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code pot}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPot(jsbachParser.PotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code div_mult_mod}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDiv_mult_mod(jsbachParser.Div_mult_modContext ctx);
	/**
	 * Exit a parse tree produced by the {@code div_mult_mod}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDiv_mult_mod(jsbachParser.Div_mult_modContext ctx);
	/**
	 * Enter a parse tree produced by the {@code num}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNum(jsbachParser.NumContext ctx);
	/**
	 * Exit a parse tree produced by the {@code num}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNum(jsbachParser.NumContext ctx);
	/**
	 * Enter a parse tree produced by the {@code mes_minus}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMes_minus(jsbachParser.Mes_minusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code mes_minus}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMes_minus(jsbachParser.Mes_minusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code id}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterId(jsbachParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code id}
	 * labeled alternative in {@link jsbachParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitId(jsbachParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsbachParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(jsbachParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(jsbachParser.AssignContext ctx);
}