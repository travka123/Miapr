using System.Text.RegularExpressions;

namespace SyntaxMethod {
    public class P<T> where T : Terminal {

        public Dictionary<Token, List<Production<T>>> productions { get; } = new();

        public void AddRule(Production<T> production) {

            if (productions.ContainsKey(production.result)) {
                productions[production.result].Add(production);
            }
            else {
                productions.Add(production.result, new List<Production<T>>() { production });
            }
        }

        public static Token FindToken(string name, Vn vn, Vt vt) {
            if (vt.IsTerminal(name)) {
                return vt.Get(name);
            } else {
                return vn.GetOrCreate(name);
            }
        }

        public static P<T> FromFile(string file, Vn vn, Vt vt, List<Operator<T>> operators) {
            P<T> result = new P<T>();

            foreach (var line in File.ReadLines(file)) {
                if (line.Trim().Length > 0) {

                    var match = Regex.Match(line, @$"^\s*(\w+)\s*->\s*(\w+)\s*({String.Join('|', operators.Select(o => o.name))})\s*(\w+)\s*$");

                    if (match.Success) {

                        Token rt = vn.GetOrCreate(match.Groups[1].Value);
                        Token at = FindToken(match.Groups[2].Value, vn, vt);
                        Operator<T> op = operators.Find(op => op.name == match.Groups[3].Value) ?? throw new InvalidDataException();
                        Token bt = FindToken(match.Groups[4].Value, vn, vt);

                        result.AddRule(new Production<T>(rt, at, bt, op));

                    }
                    else if((match = Regex.Match(line, @"^\s*(\w+)\s*->\s*(\w+)\s*$")).Success) {

                        Token rt = vn.GetOrCreate(match.Groups[1].Value);
                        Token at = FindToken(match.Groups[2].Value, vn, vt);

                        result.AddRule(new Production<T>(rt, at, Token.EmptyToken, null));
                    }
                    else {

                        throw new InvalidDataException();
                    }  
                }
            }

            return result;
        } 
    }
}
