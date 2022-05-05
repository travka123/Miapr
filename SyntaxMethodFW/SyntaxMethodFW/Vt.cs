using System.Text.RegularExpressions;

namespace SyntaxMethod {
    public class Vt {

        public List<Token> Terminals { get; } = new();

        public void Define(string name, int value) {

            if (Terminals.Find(t => (t.Name == name || t.Value == value)) != null) {
                throw new InvalidOperationException();
            }

            Terminals.Add(new Token(name, true, value));
        }

        public Token Get(string name) => Terminals.Find(t => t.Name == name) ?? throw new Exception();

        public bool IsTerminal(string name) => Terminals.Find(t => t.Name == name) != null;

        public static Vt FromFile(string file) {
            Vt vt = new Vt();

            foreach (var line in File.ReadLines(file)) {
                if (line.Trim().Length > 0) {

                    var match = Regex.Match(line, @"^\s*(\w+)\s*[=]\s*(\w+)\s*$");

                    if (!match.Success) {
                        throw new InvalidDataException();
                    }

                    string name = match.Groups[1].Value;
                    int value = Convert.ToInt32(match.Groups[2].Value, 16);

                    vt.Define(name, value);
                }
            }

            return vt;
        }
    }
}
