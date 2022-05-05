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
	 * Enter a parse tree produced by {@link jsbachParser#bloc}.
	 * @param ctx the parse tree
	 */
	void enterBloc(jsbachParser.BlocContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#bloc}.
	 * @param ctx the parse tree
	 */
	void exitBloc(jsbachParser.BlocContext ctx);
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
	 * Enter a parse tree produced by {@link jsbachParser#definir_procediment}.
	 * @param ctx the parse tree
	 */
	void enterDefinir_procediment(jsbachParser.Definir_procedimentContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#definir_procediment}.
	 * @param ctx the parse tree
	 */
	void exitDefinir_procediment(jsbachParser.Definir_procedimentContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsbachParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(jsbachParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(jsbachParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsbachParser#if}.
	 * @param ctx the parse tree
	 */
	void enterIf(jsbachParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#if}.
	 * @param ctx the parse tree
	 */
	void exitIf(jsbachParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsbachParser#else_condition}.
	 * @param ctx the parse tree
	 */
	void enterElse_condition(jsbachParser.Else_conditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#else_condition}.
	 * @param ctx the parse tree
	 */
	void exitElse_condition(jsbachParser.Else_conditionContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsbachParser#while}.
	 * @param ctx the parse tree
	 */
	void enterWhile(jsbachParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#while}.
	 * @param ctx the parse tree
	 */
	void exitWhile(jsbachParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link jsbachParser#condicio}.
	 * @param ctx the parse tree
	 */
	void enterCondicio(jsbachParser.CondicioContext ctx);
	/**
	 * Exit a parse tree produced by {@link jsbachParser#condicio}.
	 * @param ctx the parse tree
	 */
	void exitCondicio(jsbachParser.CondicioContext ctx);
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