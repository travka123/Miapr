namespace SyntaxMethod {
    public class Vn {
        List<Token> nonterminals = new();

        public Token GetOrCreate(string name) {
            Token? token = nonterminals.Find(t => t.Name == name);

            if (token == null) {
                token = new Token(name, false, nonterminals.Count);
                nonterminals.Add(token);
            }
            
            return token;
        }
    }
}
