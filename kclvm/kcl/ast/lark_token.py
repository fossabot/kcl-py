# Copyright 2020 The KCL Authors. All rights reserved.

# Auto generated by {gen_lark_token.go & kcl.lark}; DO NOT EDIT!!!


class LarkToken:

    # kcl.lark rules and tokens (len=186)
    L_start = "start"  # start: (NEWLINE | statement)* ...
    L_statement = "statement"  # statement: simple_stmt | compound_stmt ...
    L_simple_stmt = "simple_stmt"  # simple_stmt: (assign_stmt | unification_stmt | expr_stmt | assert_stmt | import_stmt | type_alias_stmt) NEWLINE ...
    L_compound_stmt = "compound_stmt"  # compound_stmt: if_stmt | schema_stmt | rule_stmt ...
    L_import_stmt = "import_stmt"  # import_stmt: IMPORT dot_name (AS NAME)? ...
    L_dot_name = "dot_name"  # dot_name: (leading_dots identifier) | identifier ...
    L_leading_dots = "leading_dots"  # leading_dots: DOT+ ...
    L_assert_stmt = "assert_stmt"  # assert_stmt: ASSERT simple_expr (IF simple_expr)? (COMMA test)? ...
    L_if_stmt = "if_stmt"  # if_stmt: IF test COLON execution_block (ELIF test COLON execution_block)* (ELSE COLON execution_block)? ...
    L_execution_block = "execution_block"  # execution_block: if_simple_stmt | NEWLINE _INDENT schema_init_stmt+ _DEDENT ...
    L_if_simple_stmt = "if_simple_stmt"  # if_simple_stmt: (simple_assign_stmt | unification_stmt | expr_stmt | assert_stmt) NEWLINE ...
    L_assign_stmt = "assign_stmt"  # assign_stmt: identifier [COLON type] (ASSIGN identifier)* ASSIGN test ...
    L_simple_assign_stmt = "simple_assign_stmt"  # simple_assign_stmt: identifier ASSIGN test ...
    L_unification_stmt = "unification_stmt"  # unification_stmt: identifier COLON schema_expr ...
    L_schema_stmt = "schema_stmt"  # schema_stmt: [decorators] (SCHEMA|MIXIN|PROTOCOL) NAME [LEFT_BRACKETS [schema_arguments] RIGHT_BRACKETS] [LEFT_PARENTHESES identifier (COMMA identifier)* RIGHT_PARENTHESES] [for_host] COLON NEWLINE [schema_body] ...
    L_schema_arguments = "schema_arguments"  # schema_arguments: schema_argument (COMMA schema_argument)* ...
    L_schema_argument = "schema_argument"  # schema_argument: NAME [COLON type] [ASSIGN test] ...
    L_schema_body = "schema_body"  # schema_body: _INDENT (string NEWLINE)* [mixin_stmt] (schema_attribute_stmt|schema_init_stmt|schema_index_signature)* [check_block] _DEDENT ...
    L_schema_attribute_stmt = "schema_attribute_stmt"  # schema_attribute_stmt: attribute_stmt NEWLINE ...
    L_attribute_stmt = "attribute_stmt"  # attribute_stmt: [decorators] identifier [QUESTION] COLON type [(ASSIGN|COMP_OR) test] ...
    L_schema_init_stmt = "schema_init_stmt"  # schema_init_stmt: if_simple_stmt | if_stmt ...
    L_schema_index_signature = "schema_index_signature"  # schema_index_signature: LEFT_BRACKETS [NAME COLON] [ELLIPSIS] basic_type RIGHT_BRACKETS COLON type [ASSIGN test] NEWLINE ...
    L_rule_stmt = "rule_stmt"  # rule_stmt: [decorators] RULE NAME [LEFT_BRACKETS [schema_arguments] RIGHT_BRACKETS] [LEFT_PARENTHESES identifier (COMMA identifier)* RIGHT_PARENTHESES] [for_host] COLON NEWLINE [rule_body] ...
    L_rule_body = "rule_body"  # rule_body: _INDENT (string NEWLINE)* check_expr+ _DEDENT ...
    L_for_host = "for_host"  # for_host: FOR identifier ...
    L_decorators = "decorators"  # decorators: (AT decorator_expr NEWLINE)+ ...
    L_decorator_expr = "decorator_expr"  # decorator_expr: identifier [call_suffix] ...
    L_type = "type"  # @type: type_element (OR type_element)* ...
    L_type_element = "type_element"  # type_element: schema_type | basic_type | compound_type | literal_type ...
    L_schema_type = "schema_type"  # schema_type: identifier ...
    L_basic_type = "basic_type"  # basic_type: STRING_TYPE | INT_TYPE | FLOAT_TYPE | BOOL_TYPE | ANY_TYPE ...
    L_compound_type = "compound_type"  # compound_type: list_type | dict_type ...
    L_list_type = "list_type"  # list_type: LEFT_BRACKETS (type)? RIGHT_BRACKETS ...
    L_dict_type = "dict_type"  # dict_type: LEFT_BRACE (type)? COLON (type)? RIGHT_BRACE ...
    L_literal_type = "literal_type"  # literal_type: string | number | TRUE | FALSE | NONE ...
    L_type_alias_stmt = "type_alias_stmt"  # type_alias_stmt: TYPE NAME ASSIGN type ...
    L_check_block = "check_block"  # check_block: CHECK COLON NEWLINE _INDENT check_expr+ _DEDENT ...
    L_check_expr = "check_expr"  # check_expr: simple_expr [IF simple_expr] [COMMA primary_expr] NEWLINE ...
    L_mixin_stmt = "mixin_stmt"  # mixin_stmt: MIXIN LEFT_BRACKETS [mixins | multiline_mixins] RIGHT_BRACKETS NEWLINE ...
    L_multiline_mixins = "multiline_mixins"  # multiline_mixins: NEWLINE _INDENT mixins NEWLINE _DEDENT ...
    L_mixins = "mixins"  # mixins: identifier (COMMA (NEWLINE mixins | identifier))* ...
    L_expr_stmt = "expr_stmt"  # expr_stmt: testlist_expr ...
    L_testlist_expr = "testlist_expr"  # testlist_expr: test (COMMA test)* ...
    L_test = "test"  # test: if_expr | simple_expr ...
    L_if_expr = "if_expr"  # if_expr: simple_expr IF simple_expr ELSE test ...
    L_simple_expr = "simple_expr"  # simple_expr: unary_expr | binary_expr | primary_expr ...
    L_unary_expr = "unary_expr"  # unary_expr: un_op simple_expr ...
    L_binary_expr = "binary_expr"  # binary_expr: simple_expr bin_op simple_expr ...
    L_bin_op = "bin_op"  # bin_op: L_OR | L_AND ...
    L_un_op = "un_op"  # un_op: L_NOT | PLUS | MINUS | NOT ...
    L_primary_expr = "primary_expr"  # primary_expr: identifier call_suffix | operand | primary_expr select_suffix | primary_expr call_suffix | primary_expr slice_suffix ...
    L_operand = "operand"  # operand: identifier | number | string | constant | quant_expr | list_expr | list_comp | config_expr | dict_comp | schema_expr | lambda_expr | LEFT_PARENTHESES test RIGHT_PARENTHESES ...
    L_select_suffix = "select_suffix"  # select_suffix: [QUESTION] DOT NAME ...
    L_call_suffix = "call_suffix"  # call_suffix: LEFT_PARENTHESES [arguments [COMMA]] RIGHT_PARENTHESES ...
    L_slice_suffix = "slice_suffix"  # slice_suffix: [QUESTION] LEFT_BRACKETS (test | [test] COLON [test] [COLON [test]]) RIGHT_BRACKETS ...
    L_arguments = "arguments"  # arguments: argument (COMMA argument)* ...
    L_argument = "argument"  # argument: test | NAME ASSIGN test | MULTIPLY test | DOUBLE_STAR test ...
    L_identifier = "identifier"  # identifier: NAME (DOT NAME)* ...
    L_quant_expr = "quant_expr"  # quant_expr: quant_op [ identifier COMMA ] identifier IN quant_target LEFT_BRACE (simple_expr [IF simple_expr] | NEWLINE _INDENT simple_expr [IF simple_expr] NEWLINE _DEDENT)? RIGHT_BRACE ...
    L_quant_target = "quant_target"  # quant_target: string | identifier | list_expr | list_comp | config_expr | dict_comp ...
    L_quant_op = "quant_op"  # quant_op: ALL | ANY | FILTER | MAP ...
    L_list_expr = "list_expr"  # list_expr: LEFT_BRACKETS [list_items | NEWLINE [_INDENT list_items _DEDENT]] RIGHT_BRACKETS ...
    L_list_items = "list_items"  # list_items: list_item ((COMMA [NEWLINE] | [NEWLINE]) list_item)* [COMMA] [NEWLINE] ...
    L_list_item = "list_item"  # list_item: test | star_expr | if_item ...
    L_list_comp = "list_comp"  # list_comp: LEFT_BRACKETS (list_item comp_clause+ | NEWLINE _INDENT list_item comp_clause+ _DEDENT) RIGHT_BRACKETS ...
    L_dict_comp = "dict_comp"  # dict_comp: LEFT_BRACE (entry comp_clause+ | NEWLINE _INDENT entry comp_clause+ _DEDENT) RIGHT_BRACE ...
    L_entry = "entry"  # entry: test (COLON | ASSIGN | COMP_PLUS) test ...
    L_comp_clause = "comp_clause"  # comp_clause: FOR loop_variables [COMMA] IN simple_expr [NEWLINE] [IF test [NEWLINE]] ...
    L_if_entry = "if_entry"  # if_entry: IF test COLON if_entry_exec_block (ELIF test COLON if_entry_exec_block)* (ELSE COLON if_entry_exec_block)? ...
    L_if_entry_exec_block = "if_entry_exec_block"  # if_entry_exec_block: (test (COLON | ASSIGN | COMP_PLUS) test | double_star_expr | if_entry) [NEWLINE] | NEWLINE _INDENT (test (COLON | ASSIGN | COMP_PLUS) test | double_star_expr | if_entry) ((COMMA [NEWLINE] | [NEWLINE]) (test (COLON | ASSIGN | COMP_PLUS) test | double_star_expr | if_entry))* [COMMA] [NEWLINE] _DEDENT ...
    L_if_item = "if_item"  # if_item: IF test COLON if_item_exec_block (ELIF test COLON if_item_exec_block)* (ELSE COLON if_item_exec_block)? ...
    L_if_item_exec_block = "if_item_exec_block"  # if_item_exec_block: list_item [NEWLINE] | NEWLINE _INDENT list_item ((COMMA [NEWLINE] | NEWLINE) list_item)* [COMMA] [NEWLINE] _DEDENT ...
    L_star_expr = "star_expr"  # star_expr: MULTIPLY primary_expr ...
    L_double_star_expr = "double_star_expr"  # double_star_expr: DOUBLE_STAR primary_expr ...
    L_loop_variables = "loop_variables"  # loop_variables: primary_expr (COMMA primary_expr)* ...
    L_schema_expr = "schema_expr"  # schema_expr: identifier (LEFT_PARENTHESES [arguments] RIGHT_PARENTHESES)? config_expr ...
    L_config_expr = "config_expr"  # config_expr: LEFT_BRACE [config_entries | NEWLINE [_INDENT config_entries _DEDENT]] RIGHT_BRACE ...
    L_config_entries = "config_entries"  # config_entries: config_entry ((COMMA [NEWLINE] | [NEWLINE]) config_entry)* [COMMA] [NEWLINE] ...
    L_config_entry = "config_entry"  # config_entry: test (COLON | ASSIGN | COMP_PLUS) test | double_star_expr | if_entry ...
    L_lambda_expr = "lambda_expr"  # lambda_expr: LAMBDA [schema_arguments] [RIGHT_ARROW type] LEFT_BRACE [expr_stmt | NEWLINE _INDENT schema_init_stmt+ _DEDENT] RIGHT_BRACE ...
    L_number = "number"  # number: DEC_NUMBER [multiplier] | HEX_NUMBER | BIN_NUMBER | OCT_NUMBER | FLOAT_NUMBER ...
    L_multiplier = "multiplier"  # multiplier: SI_N_L | SI_U_L | SI_M_L | SI_K_L | SI_K | SI_M | SI_G | SI_T | SI_P  ...
    L_string = "string"  # string: STRING | LONG_STRING ...
    L_ASSIGN = "ASSIGN"  # ASSIGN: "=" ...
    L_COLON = "COLON"  # COLON: ":" ...
    L_SEMI_COLON = "SEMI_COLON"  # SEMI_COLON: ";" ...
    L_COMMA = "COMMA"  # COMMA: "," ...
    L_QUESTION = "QUESTION"  # QUESTION: "?" ...
    L_ELLIPSIS = "ELLIPSIS"  # ELLIPSIS: "..." ...
    L_RIGHT_ARROW = "RIGHT_ARROW"  # RIGHT_ARROW: "->" ...
    L_LEFT_PARENTHESES = "LEFT_PARENTHESES"  # LEFT_PARENTHESES: "(" ...
    L_RIGHT_PARENTHESES = "RIGHT_PARENTHESES"  # RIGHT_PARENTHESES: ")" ...
    L_LEFT_BRACKETS = "LEFT_BRACKETS"  # LEFT_BRACKETS: "[" ...
    L_RIGHT_BRACKETS = "RIGHT_BRACKETS"  # RIGHT_BRACKETS: "]" ...
    L_LEFT_BRACE = "LEFT_BRACE"  # LEFT_BRACE: "{" ...
    L_RIGHT_BRACE = "RIGHT_BRACE"  # RIGHT_BRACE: "}" ...
    L_PLUS = "PLUS"  # PLUS: "+" ...
    L_MINUS = "MINUS"  # MINUS: "-" ...
    L_MULTIPLY = "MULTIPLY"  # MULTIPLY: "*" ...
    L_DIVIDE = "DIVIDE"  # DIVIDE: "/" ...
    L_MOD = "MOD"  # MOD: "%" ...
    L_DOT = "DOT"  # DOT: "." ...
    L_AND = "AND"  # AND: "&" ...
    L_OR = "OR"  # OR: "|" ...
    L_XOR = "XOR"  # XOR: "^" ...
    L_NOT = "NOT"  # NOT: "~" ...
    L_LESS_THAN = "LESS_THAN"  # LESS_THAN: "<" ...
    L_GREATER_THAN = "GREATER_THAN"  # GREATER_THAN: ">" ...
    L_EQUAL_TO = "EQUAL_TO"  # EQUAL_TO: "==" ...
    L_NOT_EQUAL_TO = "NOT_EQUAL_TO"  # NOT_EQUAL_TO: "!=" ...
    L_GREATER_THAN_OR_EQUAL_TO = "GREATER_THAN_OR_EQUAL_TO"  # GREATER_THAN_OR_EQUAL_TO: ">=" ...
    L_LESS_THAN_OR_EQUAL_TO = "LESS_THAN_OR_EQUAL_TO"  # LESS_THAN_OR_EQUAL_TO: "<=" ...
    L_DOUBLE_STAR = "DOUBLE_STAR"  # DOUBLE_STAR: "**" ...
    L_DOUBLE_DIVIDE = "DOUBLE_DIVIDE"  # DOUBLE_DIVIDE: "//" ...
    L_SHIFT_LEFT = "SHIFT_LEFT"  # SHIFT_LEFT: "<<" ...
    L_SHIFT_RIGHT = "SHIFT_RIGHT"  # SHIFT_RIGHT: ">>" ...
    L_AT = "AT"  # AT: "@" ...
    L_COMP_PLUS = "COMP_PLUS"  # COMP_PLUS: "+=" ...
    L_COMP_MINUS = "COMP_MINUS"  # COMP_MINUS: "-=" ...
    L_COMP_MULTIPLY = "COMP_MULTIPLY"  # COMP_MULTIPLY: "*=" ...
    L_COMP_DIVIDE = "COMP_DIVIDE"  # COMP_DIVIDE: "/=" ...
    L_COMP_MOD = "COMP_MOD"  # COMP_MOD: "%=" ...
    L_COMP_AND = "COMP_AND"  # COMP_AND: "&=" ...
    L_COMP_OR = "COMP_OR"  # COMP_OR: "|=" ...
    L_COMP_XOR = "COMP_XOR"  # COMP_XOR: "^=" ...
    L_COMP_DOUBLE_STAR = "COMP_DOUBLE_STAR"  # COMP_DOUBLE_STAR: "**=" ...
    L_COMP_DOUBLE_DIVIDE = "COMP_DOUBLE_DIVIDE"  # COMP_DOUBLE_DIVIDE: "//=" ...
    L_COMP_SHIFT_LEFT = "COMP_SHIFT_LEFT"  # COMP_SHIFT_LEFT: "<<=" ...
    L_COMP_SHIFT_RIGHT = "COMP_SHIFT_RIGHT"  # COMP_SHIFT_RIGHT: ">>=" ...
    L_IMPORT = "IMPORT"  # IMPORT: "import" ...
    L_AS = "AS"  # AS: "as" ...
    L_RULE = "RULE"  # RULE: "rule" ...
    L_SCHEMA = "SCHEMA"  # SCHEMA: "schema" ...
    L_MIXIN = "MIXIN"  # MIXIN: "mixin" ...
    L_PROTOCOL = "PROTOCOL"  # PROTOCOL: "protocol" ...
    L_CHECK = "CHECK"  # CHECK: "check" ...
    L_FOR = "FOR"  # FOR: "for" ...
    L_ASSERT = "ASSERT"  # ASSERT: "assert" ...
    L_IF = "IF"  # IF: "if" ...
    L_ELIF = "ELIF"  # ELIF: "elif" ...
    L_ELSE = "ELSE"  # ELSE: "else" ...
    L_L_OR = "L_OR"  # L_OR: "or" ...
    L_L_AND = "L_AND"  # L_AND: "and" ...
    L_L_NOT = "L_NOT"  # L_NOT: "not" ...
    L_IN = "IN"  # IN: "in" ...
    L_IS = "IS"  # IS: "is" ...
    L_LAMBDA = "LAMBDA"  # LAMBDA: "lambda" ...
    L_ALL = "ALL"  # ALL: "all" ...
    L_ANY = "ANY"  # ANY: "any" ...
    L_FILTER = "FILTER"  # FILTER: "filter" ...
    L_MAP = "MAP"  # MAP: "map" ...
    L_TYPE = "TYPE"  # TYPE: "type" ...
    L_ANY_TYPE = "ANY_TYPE"  # ANY_TYPE: "any" ...
    L_STRING_TYPE = "STRING_TYPE"  # STRING_TYPE: "str" ...
    L_INT_TYPE = "INT_TYPE"  # INT_TYPE: "int" ...
    L_FLOAT_TYPE = "FLOAT_TYPE"  # FLOAT_TYPE: "float" ...
    L_BOOL_TYPE = "BOOL_TYPE"  # BOOL_TYPE: "bool" ...
    L_TRUE = "TRUE"  # TRUE: "True" ...
    L_FALSE = "FALSE"  # FALSE: "False" ...
    L_NONE = "NONE"  # NONE: "None" ...
    L_UNDEFINED = "UNDEFINED"  # UNDEFINED: "Undefined" ...
    L_SI_N_L = "SI_N_L"  # SI_N_L: "n" ...
    L_SI_U_L = "SI_U_L"  # SI_U_L: "u" ...
    L_SI_M_L = "SI_M_L"  # SI_M_L: "m" ...
    L_SI_K_L = "SI_K_L"  # SI_K_L: "k" ...
    L_SI_K = "SI_K"  # SI_K: "K" ...
    L_SI_M = "SI_M"  # SI_M: "M" ...
    L_SI_G = "SI_G"  # SI_G: "G" ...
    L_SI_T = "SI_T"  # SI_T: "T" ...
    L_SI_P = "SI_P"  # SI_P: "P" ...
    L_SI_K_IEC = "SI_K_IEC"  # SI_K_IEC: "Ki" ...
    L_SI_M_IEC = "SI_M_IEC"  # SI_M_IEC: "Mi" ...
    L_SI_G_IEC = "SI_G_IEC"  # SI_G_IEC: "Gi" ...
    L_SI_T_IEC = "SI_T_IEC"  # SI_T_IEC: "Ti" ...
    L_SI_P_IEC = "SI_P_IEC"  # SI_P_IEC: "Pi" ...
    L_IEC = "IEC"  # IEC: "i" ...
    L_NAME = "NAME"  # NAME: /\$?[a-zA-Z_]\w*/ ...
    L_COMMENT = "COMMENT"  # COMMENT: /#[^\n]*/ ...
    L_NEWLINE = "NEWLINE"  # NEWLINE: ( /\r?\n[\t ]*/ | COMMENT )+ ...
    L_STRING = "STRING"  # STRING: /r?("(?!"").*?(?<!\\)(\\\\)*?"|'(?!'').*?(?<!\\)(\\\\)*?')/i ...
    L_LONG_STRING = "LONG_STRING"  # LONG_STRING: /r?(""".*?(?<!\\)(\\\\)*?"""|'''.*?(?<!\\)(\\\\)*?''')/is ...
    L_DEC_NUMBER = "DEC_NUMBER"  # DEC_NUMBER: /\-?0|\-?[1-9]\d*/i ...
    L_HEX_NUMBER = "HEX_NUMBER"  # HEX_NUMBER.2: /\-?0[xX][0-9a-fA-F]+/i ...
    L_OCT_NUMBER = "OCT_NUMBER"  # OCT_NUMBER.2: /\-?0[oO]?[0-7]+/i ...
    L_BIN_NUMBER = "BIN_NUMBER"  # BIN_NUMBER.2 : /\-?0[bB][0-1]+/i ...
    L_FLOAT_NUMBER = "FLOAT_NUMBER"  # FLOAT_NUMBER.2: /(([-+]?\d+\.\d*|\.\d+)(e[-+]?\d+)?|\d+(e[-+]?\d+))/i ...

    # kcl.lark tokens list (len=103)
    LL_token_list = [
        L_ASSIGN,
        L_COLON,
        L_SEMI_COLON,
        L_COMMA,
        L_QUESTION,
        L_ELLIPSIS,
        L_RIGHT_ARROW,
        L_LEFT_PARENTHESES,
        L_RIGHT_PARENTHESES,
        L_LEFT_BRACKETS,
        L_RIGHT_BRACKETS,
        L_LEFT_BRACE,
        L_RIGHT_BRACE,
        L_PLUS,
        L_MINUS,
        L_MULTIPLY,
        L_DIVIDE,
        L_MOD,
        L_DOT,
        L_AND,
        L_OR,
        L_XOR,
        L_NOT,
        L_LESS_THAN,
        L_GREATER_THAN,
        L_EQUAL_TO,
        L_NOT_EQUAL_TO,
        L_GREATER_THAN_OR_EQUAL_TO,
        L_LESS_THAN_OR_EQUAL_TO,
        L_DOUBLE_STAR,
        L_DOUBLE_DIVIDE,
        L_SHIFT_LEFT,
        L_SHIFT_RIGHT,
        L_AT,
        L_COMP_PLUS,
        L_COMP_MINUS,
        L_COMP_MULTIPLY,
        L_COMP_DIVIDE,
        L_COMP_MOD,
        L_COMP_AND,
        L_COMP_OR,
        L_COMP_XOR,
        L_COMP_DOUBLE_STAR,
        L_COMP_DOUBLE_DIVIDE,
        L_COMP_SHIFT_LEFT,
        L_COMP_SHIFT_RIGHT,
        L_IMPORT,
        L_AS,
        L_RULE,
        L_SCHEMA,
        L_MIXIN,
        L_PROTOCOL,
        L_CHECK,
        L_FOR,
        L_ASSERT,
        L_IF,
        L_ELIF,
        L_ELSE,
        L_L_OR,
        L_L_AND,
        L_L_NOT,
        L_IN,
        L_IS,
        L_LAMBDA,
        L_ALL,
        L_ANY,
        L_FILTER,
        L_MAP,
        L_TYPE,
        L_ANY_TYPE,
        L_STRING_TYPE,
        L_INT_TYPE,
        L_FLOAT_TYPE,
        L_BOOL_TYPE,
        L_TRUE,
        L_FALSE,
        L_NONE,
        L_UNDEFINED,
        L_SI_N_L,
        L_SI_U_L,
        L_SI_M_L,
        L_SI_K_L,
        L_SI_K,
        L_SI_M,
        L_SI_G,
        L_SI_T,
        L_SI_P,
        L_SI_K_IEC,
        L_SI_M_IEC,
        L_SI_G_IEC,
        L_SI_T_IEC,
        L_SI_P_IEC,
        L_IEC,
        L_NAME,
        L_COMMENT,
        L_NEWLINE,
        L_STRING,
        L_LONG_STRING,
        L_DEC_NUMBER,
        L_HEX_NUMBER,
        L_OCT_NUMBER,
        L_BIN_NUMBER,
        L_FLOAT_NUMBER,
    ]

    # kcl.lark rules list (len=83)
    LL_rule_list = [
        L_start,
        L_statement,
        L_simple_stmt,
        L_compound_stmt,
        L_import_stmt,
        L_dot_name,
        L_leading_dots,
        L_assert_stmt,
        L_if_stmt,
        L_execution_block,
        L_if_simple_stmt,
        L_assign_stmt,
        L_simple_assign_stmt,
        L_unification_stmt,
        L_schema_stmt,
        L_schema_arguments,
        L_schema_argument,
        L_schema_body,
        L_schema_attribute_stmt,
        L_attribute_stmt,
        L_schema_init_stmt,
        L_schema_index_signature,
        L_rule_stmt,
        L_rule_body,
        L_for_host,
        L_decorators,
        L_decorator_expr,
        L_type,
        L_type_element,
        L_schema_type,
        L_basic_type,
        L_compound_type,
        L_list_type,
        L_dict_type,
        L_literal_type,
        L_type_alias_stmt,
        L_check_block,
        L_check_expr,
        L_mixin_stmt,
        L_multiline_mixins,
        L_mixins,
        L_expr_stmt,
        L_testlist_expr,
        L_test,
        L_if_expr,
        L_simple_expr,
        L_unary_expr,
        L_binary_expr,
        L_bin_op,
        L_un_op,
        L_primary_expr,
        L_operand,
        L_select_suffix,
        L_call_suffix,
        L_slice_suffix,
        L_arguments,
        L_argument,
        L_identifier,
        L_quant_expr,
        L_quant_target,
        L_quant_op,
        L_list_expr,
        L_list_items,
        L_list_item,
        L_list_comp,
        L_dict_comp,
        L_entry,
        L_comp_clause,
        L_if_entry,
        L_if_entry_exec_block,
        L_if_item,
        L_if_item_exec_block,
        L_star_expr,
        L_double_star_expr,
        L_loop_variables,
        L_schema_expr,
        L_config_expr,
        L_config_entries,
        L_config_entry,
        L_lambda_expr,
        L_number,
        L_multiplier,
        L_string,
    ]

    # kcl.lark tokens string value map
    LL_token_str_value_map = {
        L_ASSIGN: "=",
        L_COLON: ":",
        L_SEMI_COLON: ";",
        L_COMMA: ",",
        L_QUESTION: "?",
        L_ELLIPSIS: "...",
        L_RIGHT_ARROW: "->",
        L_LEFT_PARENTHESES: "(",
        L_RIGHT_PARENTHESES: ")",
        L_LEFT_BRACKETS: "[",
        L_RIGHT_BRACKETS: "]",
        L_LEFT_BRACE: "{",
        L_RIGHT_BRACE: "}",
        L_PLUS: "+",
        L_MINUS: "-",
        L_MULTIPLY: "*",
        L_DIVIDE: "/",
        L_MOD: "%",
        L_DOT: ".",
        L_AND: "&",
        L_OR: "|",
        L_XOR: "^",
        L_NOT: "~",
        L_LESS_THAN: "<",
        L_GREATER_THAN: ">",
        L_EQUAL_TO: "==",
        L_NOT_EQUAL_TO: "!=",
        L_GREATER_THAN_OR_EQUAL_TO: ">=",
        L_LESS_THAN_OR_EQUAL_TO: "<=",
        L_DOUBLE_STAR: "**",
        L_DOUBLE_DIVIDE: "//",
        L_SHIFT_LEFT: "<<",
        L_SHIFT_RIGHT: ">>",
        L_AT: "@",
        L_COMP_PLUS: "+=",
        L_COMP_MINUS: "-=",
        L_COMP_MULTIPLY: "*=",
        L_COMP_DIVIDE: "/=",
        L_COMP_MOD: "%=",
        L_COMP_AND: "&=",
        L_COMP_OR: "|=",
        L_COMP_XOR: "^=",
        L_COMP_DOUBLE_STAR: "**=",
        L_COMP_DOUBLE_DIVIDE: "//=",
        L_COMP_SHIFT_LEFT: "<<=",
        L_COMP_SHIFT_RIGHT: ">>=",
        L_IMPORT: "import",
        L_AS: "as",
        L_RULE: "rule",
        L_SCHEMA: "schema",
        L_MIXIN: "mixin",
        L_PROTOCOL: "protocol",
        L_CHECK: "check",
        L_FOR: "for",
        L_ASSERT: "assert",
        L_IF: "if",
        L_ELIF: "elif",
        L_ELSE: "else",
        L_L_OR: "or",
        L_L_AND: "and",
        L_L_NOT: "not",
        L_IN: "in",
        L_IS: "is",
        L_LAMBDA: "lambda",
        L_ALL: "all",
        L_ANY: "any",
        L_FILTER: "filter",
        L_MAP: "map",
        L_TYPE: "type",
        L_ANY_TYPE: "any",
        L_STRING_TYPE: "str",
        L_INT_TYPE: "int",
        L_FLOAT_TYPE: "float",
        L_BOOL_TYPE: "bool",
        L_TRUE: "True",
        L_FALSE: "False",
        L_NONE: "None",
        L_UNDEFINED: "Undefined",
        L_SI_N_L: "n",
        L_SI_U_L: "u",
        L_SI_M_L: "m",
        L_SI_K_L: "k",
        L_SI_K: "K",
        L_SI_M: "M",
        L_SI_G: "G",
        L_SI_T: "T",
        L_SI_P: "P",
        L_SI_K_IEC: "Ki",
        L_SI_M_IEC: "Mi",
        L_SI_G_IEC: "Gi",
        L_SI_T_IEC: "Ti",
        L_SI_P_IEC: "Pi",
        L_IEC: "i",
    }


class TokenValue:
    ASSIGN = "="
    COLON = ":"
    SEMI_COLON = ";"
    COMMA = ","
    QUESTION = "?"
    ELLIPSIS = "..."
    RIGHT_ARROW = "->"
    LEFT_PARENTHESES = "("
    RIGHT_PARENTHESES = ")"
    LEFT_BRACKETS = "["
    RIGHT_BRACKETS = "]"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    PLUS = "+"
    MINUS = "-"
    MULTIPLY = "*"
    DIVIDE = "/"
    MOD = "%"
    DOT = "."
    AND = "&"
    OR = "|"
    XOR = "^"
    NOT = "~"
    LESS_THAN = "<"
    GREATER_THAN = ">"
    EQUAL_TO = "=="
    NOT_EQUAL_TO = "!="
    GREATER_THAN_OR_EQUAL_TO = ">="
    LESS_THAN_OR_EQUAL_TO = "<="
    DOUBLE_STAR = "**"
    DOUBLE_DIVIDE = "//"
    SHIFT_LEFT = "<<"
    SHIFT_RIGHT = ">>"
    AT = "@"
    COMP_PLUS = "+="
    COMP_MINUS = "-="
    COMP_MULTIPLY = "*="
    COMP_DIVIDE = "/="
    COMP_MOD = "%="
    COMP_AND = "&="
    COMP_OR = "|="
    COMP_XOR = "^="
    COMP_DOUBLE_STAR = "**="
    COMP_DOUBLE_DIVIDE = "//="
    COMP_SHIFT_LEFT = "<<="
    COMP_SHIFT_RIGHT = ">>="
    IMPORT = "import"
    AS = "as"
    RULE = "rule"
    SCHEMA = "schema"
    MIXIN = "mixin"
    PROTOCOL = "protocol"
    CHECK = "check"
    FOR = "for"
    ASSERT = "assert"
    IF = "if"
    ELIF = "elif"
    ELSE = "else"
    L_OR = "or"
    L_AND = "and"
    L_NOT = "not"
    IN = "in"
    IS = "is"
    LAMBDA = "lambda"
    ALL = "all"
    ANY = "any"
    FILTER = "filter"
    MAP = "map"
    TYPE = "type"
    ANY_TYPE = "any"
    STRING_TYPE = "str"
    INT_TYPE = "int"
    FLOAT_TYPE = "float"
    BOOL_TYPE = "bool"
    TRUE = "True"
    FALSE = "False"
    NONE = "None"
    UNDEFINED = "Undefined"
    SI_N_L = "n"
    SI_U_L = "u"
    SI_M_L = "m"
    SI_K_L = "k"
    SI_K = "K"
    SI_M = "M"
    SI_G = "G"
    SI_T = "T"
    SI_P = "P"
    SI_K_IEC = "Ki"
    SI_M_IEC = "Mi"
    SI_G_IEC = "Gi"
    SI_T_IEC = "Ti"
    SI_P_IEC = "Pi"
    IEC = "i"
