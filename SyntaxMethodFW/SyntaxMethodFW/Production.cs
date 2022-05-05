namespace SyntaxMethod {
    public record Production<T>(Token result, Token a, Token b, Operator<T>? op) where T : Terminal {

        public override string ToString() {

            if (op == null) {
                return $"{result} -> {a}";
            }

            return $"{result} -> {a} {op} {b}";
        }
    }
}
