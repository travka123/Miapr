namespace SyntaxMethod {
    public class Token {

        public static Token EmptyToken { get; } = new Token(String.Empty, false, 0);

        public string Name { get; }
        public bool IsTerminal { get; }
        public int Value { get; }
        
        public Token(string name, bool isTerminal, int value) {
            Name = name;
            IsTerminal = isTerminal;
            Value = value;
        }

        public override string ToString() {
            return $"{Name}({(IsTerminal ? $"terminal, val: {Value:X}" : $"nonterminal, id: {Value}")})";
        }
    }
}
