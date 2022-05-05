using System.Text;

namespace SyntaxMethod {
    public class G<T> where T : Terminal {

        private Vn vn;
        private Vt vt;
        private P<T> p;
        private Token s;

        public G(string tFile, string ntFile, List<Operator<T>> operators) {

            vt = Vt.FromFile(tFile);

            vn = new();

            s = vn.GetOrCreate("S");

            p = P<T>.FromFile(ntFile, vn, vt, operators);
        }

        public override string ToString() {
            StringBuilder stringBuilder = new StringBuilder();

            foreach (var klp in p.productions) {
                foreach (var kvp in klp.Value) {
                    stringBuilder.AppendLine(kvp.ToString());
                }
            }

            return stringBuilder.ToString();
        }

        public bool Verify(T[] terminals) {

            bool[] used = new bool[terminals.Length];

            var combinations = FindNonterminal(s, terminals, used, (_, _) => true);

            foreach (var combination in combinations) {
                if (combination.Count == terminals.Length) {
                    return true;
                }
            }

            return false;
        }

        private List<List<int>> FindTerminalOrNonterminal(Token target, T[] terminals, bool[] used, Func<List<int>, bool, bool> parentConstraint) {

            if (target.IsTerminal) {
                return FindTerminal(target, terminals, used, parentConstraint);
            }
            else {
                return FindNonterminal(target, terminals, used, parentConstraint);
            }
        }

        private List<List<int>> FindNonterminal(Token target, T[] terminals, bool[] used, Func<List<int>, bool, bool> parentConstraint) {

            List<List<int>> possibleCombinations = new();

            var targetProductions = p.productions[target];

            foreach(var production in targetProductions) {

                List<List<int>> aCombinations = FindTerminalOrNonterminal(production.a, terminals, used, parentConstraint);

                if (production.op == null) {

                    possibleCombinations.AddRange(aCombinations);

                }
                else {

                    foreach (var aCombination in aCombinations) {

                        SetUsed(used, aCombination, true);

                        List<List<int>> bCombinations = FindTerminalOrNonterminal(production.b, terminals, used, (bCombination, isFull) => {
                            return production.op.func(terminals, aCombination, bCombination, isFull);
                        });

                        foreach (var bCombination in bCombinations) {

                            List<int> combination = new(aCombination);
                            combination.AddRange(bCombination);

                            if (parentConstraint(combination, true)) {
                                possibleCombinations.Add(combination);
                            }
                        }

                        SetUsed(used, aCombination, false);
                    }
                }
            }

            return possibleCombinations;
        }

        private List<List<int>> FindTerminal(Token target, T[] terminals, bool[] used, Func<List<int>, bool, bool> parentConstraint) {
            List<List<int>> possibleCombinations = new();

            for (int i = 0; i < terminals.Length; i++) {

                if ((!used[i]) && (terminals[i].GetValue() == target.Value)) {

                    var terminal = new List<int>() { i };

                    if (parentConstraint(terminal, false)) {
                        possibleCombinations.Add(terminal);
                    }
                }
            }

            return possibleCombinations;        
        }

        private void SetUsed(bool[] used, List<int> indexes, bool state) {
            for (int i = 0; i < indexes.Count; i++) {
                used[indexes[i]] = state;
            }
        }

        public List<Token> GetTerminals() {
           return vt.Terminals.ToList();
        }
    }
}
